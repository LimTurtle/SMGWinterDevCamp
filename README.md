# URL Shortener 프로젝트 개요

1. 해당 주제를 선택한 이유
---
백엔드를 처음부터 구현한 경험이 없기에 선택

2. 주요 기능
---
2-1) Origin URL 주소를 입력하면 Shortening URL을 반환. 이 때, 잘못된 형식의 Origin URL를 입력하면 에러 메세지를 출력
2-2) Copy 버튼을 누를 시, Shortening URL 을 클립보드에 복사
2-3) Shortening URL을 브라우저 주소창에 입력하면 그에 대응하는 Origin URL로 Redirect
2-4) 최상단의 메뉴바에서 홈 버튼을 누르면 URL Shortener 초기 화면으로 이동하고, 데이터베이스 조회 버튼을 누르면 현재까지 변환된 URL 정보들을 확인할 수 있음
2-5) 일정 시간이 지나면 변환된 URL 정보들을 초기화 (5분으로 설정함)
