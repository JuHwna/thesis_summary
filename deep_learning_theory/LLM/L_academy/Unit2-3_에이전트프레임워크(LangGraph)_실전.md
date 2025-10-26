# LangGraph를 활용한 이메일 분류
- LangGraph를 사용하여 완전한 이메일 처리 워크플로우를 구축

<img width="866" height="434" alt="image" src="https://github.com/user-attachments/assets/b88af34a-a9fb-45e1-8c69-b9384cf772b3" />

### 패키지 설치

~~~
!pip install langgraph langchain_openai langchai_huggingface
~~~

## 환경설정
- 필요한 모든 라이브러리를 가져오기
- LangGraph는 그래프 구조를 제공하고 LangChain은 LLM과 작업할 수 있는 편리한 인터페이스를 제공함

~~~
import os
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

# Set your OpenAI API key here
os.environ["OPENAI_API_KEY"] = "sk-xxxx"    # Replace with your actual API key

# Initialize our LLM
model = ChatOpenAI(model="gpt-4o", temperature=0)
~~~

## 1단계 상태 정의하기
- LangGraph에서 상태(state)는 매우 중요한 개념
- 상태 : 워크플로우를 통해 전달되는 모든 정보를 나타냄
- 알프레드의 이메일 처리 시스템에서는 다음을 추적해야 함
  - 처리 중인 이메일
  - 스팸 여부
  - 정당한 이메일에 대한 초안 응답
  - LLM과의 대화 기록

~~~
class EmailState(TypedDict):
    email: Dict[str, Any]
    is_spam: Optional[bool]
    spam_reason: Optional[str]
    email_category: Optional[str]
    draft_response: Optional[str]
    messages: List[Dict[str, Any]]
~~~

## 2단계 : 노드 정의하기
- 노드를 형성할 처리 함수 정의
- 각 노드는 이메일 처리 작업의 특정 단계를 수행함

~~~
import os
from typing import TypedDict, List, Dict, Any, Optional
from langgraph.graph import StateGraph, START, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint


# Initialize LLM
model = ChatOpenAI(model="gpt-4o", temperature=0)

# Create the graph
email_graph = StateGraph(EmailState)
~~~

### EmailState 클래스
- 알프레드의 이메일 처리 시스템에서 이메일 처리에 필요한 정보를 저장하는 데 사용함
- email([Dict[str,Any]) : 처리 중인 이메일의 정보(발신자, 주제, 본문 등)
- is_spam(Optional[bool]) : 이메일이 스팸인지 여부(True/False)
- draft_response(Optional[str]) : 스팸이 아닌 이메일에 대한 답장 초안
- messages([List[Dict[str,Any]]) : LLM과의 대화 기록

~~~
class EmailState(TypedDict):
    email: Dict[str, Any]
    is_spam: Optional[bool]
    draft_response: Optional[str]
    messages: List[Dict[str, Any]]
~~~

### read_email 노드
- read_email 노드 : 수신 이메일을 읽고 처리하는 역할
- 이메일의 발신자와 주제를 출력하고 상태를 변경하지 않으며 단순히 이메일을 처리 과정을 기록함

~~~
def read_email(state: EmailState):
    email = state["email"]
    print(
        f"Alfred is processing an email from {email['sender']} with subject: {email['subject']}"
    )
    return {}
~~~

### handle_spam 노드
- handle_spam 노드 : 스팸으로 분류된 이메일을 처리
- 스팸으로 표시되었다는 메시지를 출력하고 이메일이 스팸 폴더로 이동되었다고 알림
- 상태를 변경하지 않으며 단순히 스팸 이메일과 처리 과정을 기록함

~~~
def handle_spam(state: EmailState):
    print(f"Alfred has marked the email as spam.")
    print("The email has been moved to the spam folder.")
    return {}
~~~

### classify_email 노드
- classify_email 노드 : LLM을 사용하여 이메일이 스팸인지 아닌지 판단함
- 이메일의 내용을 분석하는 프롬프트를 작성하고 LLM에 이 프롬프트를 전달하여 응답을 받음
- 이메일이 스팸인지 여부를 판단하여 is_spam 상태를 업데이트하고 대화 기록을 messages에 추가함

~~~
def classify_email(state: EmailState):
    email = state["email"]

    prompt = f"""
As Alfred the butler of Mr wayne and it's SECRET identity Batman, analyze this email and determine if it is spam or legitimate and should be brought to Mr wayne's attention.

Email:
From: {email['sender']}
Subject: {email['subject']}
Body: {email['body']}

First, determine if this email is spam.
answer with SPAM or HAM if it's legitimate. Only reurn the answer
Answer :
    """
    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)

    response_text = response.content.lower()
    print(response_text)
    is_spam = "spam" in response_text and "ham" not in response_text

    if not is_spam:
        new_messages = state.get("messages", []) + [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": response.content},
        ]
    else:
        new_messages = state.get("messages", [])

    return {"is_spam": is_spam, "messages": new_messages}
~~~

### drafting_response 노드
- drafting_response 노드 : 스팸이 아닌 이메일에 대한 답장 초안을 작성함
- 이메일 내용을 분석하여 정중한 답장 초안을 생성하기 위한 프롬프트를 LLM에 전달함
- 답장 초안을 draft_response에 업데이트하고 대화 기록을 messages에 추가

~~~
def drafting_response(state: EmailState):
    email = state["email"]

    prompt = f"""
As Alfred the butler, draft a polite preliminary response to this email.

Email:
From: {email['sender']}
Subject: {email['subject']}
Body: {email['body']}

Draft a brief, professional response that Mr. Wayne can review and personalize before sending.
    """

    messages = [HumanMessage(content=prompt)]
    response = model.invoke(messages)

    new_messages = state.get("messages", []) + [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": response.content},
    ]

    return {"draft_response": response.content, "messages": new_messages}
~~~

### notify_mr_wayne 노드
- notify_mr_wayne 노드 : Mr.Wayne에게 이메일을 알리고 답장 초안을 제시함
- 이메일의 발신자와 주제를 출력하고 준비된 초안을 보여줌
- 상태를 변경하지 않으며 이메일 처리 과정을 마무리함

~~~
def notify_mr_wayne(state: EmailState):
    email = state["email"]

    print("\n" + "=" * 50)
    print(f"Sir, you've received an email from {email['sender']}.")
    print(f"Subject: {email['subject']}")
    print("\nI've prepared a draft response for your review:")
    print("-" * 50)
    print(state["draft_response"])
    print("=" * 50 + "\n")

    return {}
~~~

### route_email 함수
- route_email : 노드 간의 흐름을 결정하는 라우팅 함수
- 이 함수는 이메일이 스팸인지 아닌지를 판단하여 다음에 어떤 단계를 진행할지 결정하는 역할을 함
  - 입력 : EmailState 객체를 받아, 현재 이메일의 스팸 여부를 확인
  - 출력 : 이메일이 스팸이라면 "spam" 문자열을 반환하고 그렇지 않으면 "legitimate" 문자열을 반환

~~~
def route_email(state: EmailState) -> str:
    if state["is_spam"]:
        return "spam"
    else:
        return "legitimate"
~~~

### 그래프 생성
- 위에서 정의한 클래스, 노드, 함수를 사용하여 스팸 이메일을 분류하고 스팸이 아닌 메일에 답장을 작성하기 위한 그래프를 생성함

|역할|변수명|
|----|------|
|클래스|EmailState|
|노드|read_email<br>handle_spam<br>classify_email<br>drafting_response<br>notify_mr_wayne|
|함수|route_email|

~~~
# Create the graph
email_graph = StateGraph(EmailState)

# Add nodes
email_graph.add_node(
    "read_email", read_email
)  # the read_email node executes the read_mail function
email_graph.add_node(
    "classify_email", classify_email
)  # the classify_email node will execute the classify_email function
email_graph.add_node("handle_spam", handle_spam)  # same logic
email_graph.add_node("drafting_response", drafting_response)  # same logic
email_graph.add_node("notify_mr_wayne", notify_mr_wayne)  # same logic
~~~

## 3단계 : 라우팅 논리 정의하기
- 이제 이메일 분류 후 어떤 경로를 선택할지 결정하는 라우팅 논리를 정의
- 이 로직은 이메일이 스팸인지 정당한지에 따라 다음 단계를 결정함

~~~
# Add edges
email_graph.add_edge(
    START, "read_email"
)  # After starting we go to the "read_email" node

email_graph.add_edge("read_email", "classify_email")  # after_reading we classify

# Add conditional edges
email_graph.add_conditional_edges(
    "classify_email",  # after classify, we run the "route_email" function"
    route_email,
    {
        "spam": "handle_spam",  # if it return "Spam", we go the "handle_span" node
        "legitimate": "drafting_response",  # and if it's legitimate, we go to the "drafting response" node
    },
)

# Add final edges
email_graph.add_edge("handle_spam", END)  # after handling spam we always end
email_graph.add_edge("drafting_response", "notify_mr_wayne")
email_graph.add_edge(
    "notify_mr_wayne", END
)  # after notifyinf Me wayne, we can end  too
~~~

## 4단계 : 상태 그래프 생성 및 엣지 정의하기
- 이제 모든 구성 요소를 연결하여 상태 그래프를 생성하고 엣지를 정의
- 이 과정에서 각 노드를 추가하고 노드 간의 흐름을 결정하는 엣지도 설정함

~~~
# Compile the graph
compiled_graph = email_graph.compile()

from IPython.display import Image, display

display(Image(compiled_graph.get_graph().draw_mermaid_png()))

# Example emails for testing
legitimate_email = {
    "sender": "Joker",
    "subject": "Found you Batman ! ",
    "body": "Mr. Wayne,I found your secret identity ! I know you're batman ! Ther's no denying it, I have proof of that and I'm coming to find you soon. I'll get my revenge. JOKER",
}

spam_email = {
    "sender": "Crypto bro",
    "subject": "The best investment of 2025",
    "body": "Mr Wayne, I just launched an ALT coin and want you to buy some !",
}
# Process legitimate email
print("\nProcessing legitimate email...")
legitimate_result = compiled_graph.invoke(
    {"email": legitimate_email, "is_spam": None, "draft_response": None, "messages": []}
)

# Process spam email
print("\nProcessing spam email...")
spam_result = compiled_graph.invoke(
    {"email": spam_email, "is_spam": None, "draft_response": None, "messages": []}
)
~~~
