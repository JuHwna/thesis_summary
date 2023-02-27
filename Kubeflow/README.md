1. https://sidepunch.tistory.com/entry/Kubeflow-%EC%84%A4%EC%B9%98-Ubuntu-2104-minikube
2. https://learning-sarah.tistory.com/entry/Kubeflow-13-%EC%84%A4%EC%B9%98
3. https://jmholly.tistory.com/entry/Minikube-Exiting-due-to-GUESTMISSINGCONNTRACK-Sorry-Kubernetes-1202-requires-conntrack-to-be-installed-in-roots-path
4. https://yangoos57.github.io/blog/mlops/kubeflow/installation_guide/


- https://hub.docker.com/r/nvidia/cuda
- https://mintpsyco.tistory.com/m/32
- https://velog.io/@moey920/Kubeflow-%EB%85%B8%ED%8A%B8%EB%B6%81-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0




## Minikube로 설치하는 방법
1. https://mintpsyco.tistory.com/m/32 or https://sidepunch.tistory.com/entry/Kubeflow-%EC%84%A4%EC%B9%98-Ubuntu-2104-minikube

2. https://github.com/kubeflow/manifests 나온 순서대로 차례대로 설치
- while ! kustomize build example | kubectl apply -f -; do echo "Retrying to apply resources"; sleep 10; done 이거로 설치 시 뭔가 오류 발생

3. 설치 과정 속 Custom Resource Definition Install Error 발생 시
- https://gain-yoo.github.io/trouble%20shooting/custom-resource-error/

4. 노트북 생성 시 오류 발생하면
- https://otzslayer.github.io/kubeflow/2022/06/11/could-not-find-csrf-cookie-xsrf-token-in-the-request.html 해당 사이트 처럼 수정
- https://velog.io/@seokbin/Kubeflow-V1.4-%EC%84%A4%EC%B9%98-%EB%B0%8F-%EC%B4%88%EA%B8%B0-%EC%84%A4%EC%A0%95User-%EC%B6%94%EA%B0%80-CORS


