# 프로젝트 소개
백엔드 경험이 거의 없기에, URL Shortener를 만들어 보며 python, django, mysql에 익숙해지기 위해 진행한 프로젝트입니다.

# 개발 기간
- 2022/12/01일 ~ 2022/12/23일

# 기술 스택
- ```Python 3.9```
- IDE : Pycharm Community Edition(2022.3)
- Framework : Django(4.1.4)
- Database : MySQL(8.0)

# 주요 기능
- Origin URL 주소를 입력하면 Shortening URL을 반환. 이 때, 잘못된 형식의 Origin URL를 입력하면 에러 메세지를 출력
- Copy 버튼을 누를 시, Shortening URL 을 클립보드에 복사
- Shortening URL을 브라우저 주소창에 입력하면 그에 대응하는 Origin URL로 Redirect
- 최상단의 메뉴바에서 홈 버튼을 누르면 URL Shortener 초기 화면으로 이동하고, 데이터베이스 조회 버튼을 누르면 현재까지 변환된 URL 정보들을 확인할 수 있음
- 일정 시간이 지나면 변환된 URL 정보들을 초기화 (5분으로 설정함)

# 코드 중 확인받고 싶은 부분
### 1. 이벤트 처리 관련

urlResult.html :
```
<form action="{% url 'index'%}" method="POST">
    {% csrf_token %}
    <div style="display:inline;" class="res">Result : </div>
    <input type="text" name="shortURL" value="{{shortURL}}" class="shortURL" readonly/>
    <button type="submit" name="copyBtn" value="copyBtn" class="copyBtn">copy</button>
</form>
```

views.py :
```
def display(request):
    if request.POST.get("copyBtn"):
        fetchResult = request.POST['shortURL']
        clipboard.copy(str(fetchResult))
    return render(request, 'myApp/index.html')
```

- 현재 copy 버튼을 통해 서버에 POST 정보를 전달하고 있습니다. 이러한 방식 이외에 JS의 button onclick 와 같은 POST 방식 없이 이벤트를 처리할 수 있는 방법이 있나요?
- copy 버튼을 눌렀을 때 클립보드에 Shortening URL만 복사되고 web 정보는 바뀌지 않았으면 합니다. 하지만 POST 방식으로 Client 정보를 Server에 넘기면 템플릿을 새로 render 하면서 이전 정보가 모두 사라지는 문제가 있어, copy 버튼을 누르면 클립보드에 Shortening URL을 복사 후 초기 화면으로 돌아가도록 구현했습니다. 이러한 상황을 해결할 방법이 있을까요?

### 2. Domain 주소 관련

views.py :
```
def urlResult(request):
    urlConvert = True
    originURL = request.POST['originURL']
    if not originURL.startswith('http'):
        return render(request, 'myApp/urlResult.html', {"urlConvert": urlConvert, "shortURL": "실패"})
    shortURL = "http://127.0.0.1:8000/" + shortener(originURL)
    ...
```

- Origin URL -> Shortening URL로 변환 후 Client에게 Shortening URL을 반환할 때, ```http://127.0.0.1:8000/``` 를 shortener 결과 값 앞에 덧붙였습니다. 이 때 ```127.0.0.1:8000```와 같은 Loopback ip address를 domain 주소로 나타낼 방법이 있을까요?

# 개발 과정에서 궁금했던 부분
- 이번 프로젝트에서 Client와 Server 간 POST / GET 통신 방법 중 POST만 사용했습니다. 이러한 점이 성능에 영향을 끼칠 수 있을까요?
- crsf_token을 처음 사용해봤는데, 해당 토큰은 Server가 Client에게 새로운 Web 페이지를 할당할 때 마다 랜덤한 값으로 주어진다고 알고 있습니다. 그렇다면 해당 token값을 Client측에서 저장하고 있어야 한다고 생각하는데, 이를 위한 사용자 세션을 따로 구현할 필요는 없는 건가요?
- 일반적으로 HTML / CSS 작업을 할 때, 상대/절대 경로만 적절히 설정하면 HTML에서 CSS 파일을 불러올 수 있었습니다. 그런데 Django에서는 static 디렉토리를 개별적으로 만들고 HTML에서 ```{% load static %}```와 같은 template 언어를 사용해야 HTML / CSS가 제대로 연동되는 이유가 궁금합니다.
- Database에서 Original URL 크기를 ```VARCHAR(2048)```로 설정했는데, 이처럼 DB의 record가 각각 매우 큰 크기를 가질 경우 성능 하락의 원인이 될 것이라 생각합니다. 그렇다면 Original URL을 효과적으로 저장할 수 있는 다른 방법이 있을지 궁금합니다.
- DB 탐색에서 성능 향상을 위해 mysql의 index 기능을 사용했습니다. 하지만 Original URL은 크기가 너무 크고, Origin Hash는 탐색에서 사용하지 않아 Shortening URL 속성에만 index 기능을 추가해 놓은 상태입니다. index 기능은 update가 적고, 정수형 자료일 경우에 효과적이라고 알고 있는데, 이러한 점에서 update는 없지만, ```VARCHAR(30)```으로 선언된 Shortening URL 속성이 index를 사용한다고 해서 성능 향상을 기대할 수 있을지 궁금합니다.
