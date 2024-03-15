# Chosun_Edu_ChatGPT
OpenAI사의 GPT 모델을 활용한 챗봇 개발하기

## VSCode를 사용한 Python 개발환경 구축
1. vscode 설치
2. python 설치(python.org) + 환경변수(PATH) 체크!
3. vscode Extentions(python, python Extention Pack, gitlens, gitgraph) 추가
4. vscode에서 github 계정으로 로그인(연동)
5. github에서 Repository(프로젝트) 생성
6. vscode에서 "git clone repository"로 5번에서 생성한 프로젝트 내려받기
7. 가상환경 생성(venv) : 가상환경 구축 참조
8. vscode에서 python interpreter 설정(ctrl+shift+P) -> venv

### 7.가상환경 구축
 python -m venv ./venv (가상환경 생성)
 .\venv\Scripts\activate (가상환경 접속)
 pip install openai (가상환경 라이브러리)

### 라이브러리 관리
   1.VENV - 프로젝트 하나 관리
   2.Anaconda - 여러가지 프로젝트

### OpenAI API 사용하기
   platform.openai.com
   1.API-KET 발급
   2.카드 등록(VISA, MASTER) + 5.5달러(보유)

### 챗봇 만들기
   - ChatGPT: 서비스 이름(ex: 카카오톡)
    > 인공지능 모델: GPT
    > 무료 : 3.5
    > 유료 : 4.0

###   OpenAI 회사에서 GPT관련 API 제공
   - https://openai.com/blog/openai-api

### LangChain 설치
    pip install langchain