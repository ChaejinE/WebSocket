# What is WebSocket ?
- 웹 브라우저에서 javascript로 TCP 동기 통신을 위한 통신 프로토콜이다.
  - C#에서는 signalR, Java에서는 표준 Websocket으 사용한다.
  - signalR은 웹소켓을 사용하지 않는 것은 아니고 MVC FrameWork에 맞게 표준 websocket에서 여러 기능을 추가한 것이다.

> Python에서 왜 WebSocket을 사용할까 ?
    > - PHP에서는 웹소켓을 구현하기가 어렵다.
    > - 여러 이유가 있는데 그 중 한가지는 PHP에서 직접적으로 Thread 관리가 어렵기 때문이라고한다.
    > - 실제로 HTTP 프로토콜로 tcp socket 접속해서 헤더의 handshake를 통해 http 접속을 비동기식, Request & Reponse 처리를 하고 접속을 끊는 행위가 ***아니라 동기식으로 접속을 유지한다.***
    > - 접속을 관리해아하는 멀티 스레드를 만들어야하고, 관리하는 풀과 제어가 만들어져야하는데 그 점이 PHP에서는 관리하기가 어렵다.
    > - PHP는 단순히 한번의 Request와 Response에 대한 스크립트로 표현되어 있어 한계가 있다.
- PHP에 대한 웹 소켓 대안으로는 socket.io(node.js), pytho websocket이 있다.
  - socket.io는 정확히 웹소켓 기술이 아니라 AJAX Long Polling 기술이다.
    - http 프로토콜에서 Request & Response 후 접속을 바로 끊는게 아니라 약간 갭을 주는 것이다. 그러므로 데이터가 바뀌면 브라우저로 다시 재요청을하는데, 유저가 느끼기에 Http Poling으로 접속이 연결을 유지하는 듯한 효과를 내는 방법이다.
    - 결국, TCP로 동기적으로 묶여있지 않아 여러버그가 발생할 수 있다. 대표적으로 반응이 느린것.

- WebSocket은 HTTP와 같은 약속이다.
- Transport protocol의 일종으로 서버와 클라이언트 간 효율적 양방향 통신을 구현하기 위한 구조다.
- 웹소켓을 이용하면 하나의 HTTP 접속으로 양방향 메시지를 자윫게 주고 받을 수 있다.
  - 기존에는 클라이언트의 요청이 없다면 서버로부터 응답을 받을 수 없는 구조였다.
  - 웹소켓은 이러한 문제를 해결할 수 있는 새로운 약속이었으며 양방향 통신이 가능함에따라 브라우저는 서버가 직접 보내는 데이터를 받아들여 사용자가 다른 웹사이트로 이동하지 않아도 최신 데이터가 적용된 웹을 볼 수 있게 해준다. (새로고침 등 노필요)

# 2. 작동원리
- Server - Client 간 웹소켓 연결을 HTTP 프로토콜을 통해 이뤄진다.
- 연결이 정상적으로 이뤄진다면, Server와 Client 간 웹소켓 즉, TCP/IP기반의 연결이 이뤄지고 일정 시간이 지나면 HTTP 연결은 자동으로 끊어진다.

# 3. 문제점
- 프로그램 구현에 보다 많은 복잡성 초래
  - HTTP와 달리 웹소켓은 Stateful protocol 이므로 서버와 클라이언트 간 연결을 항상 유지해야한다.
  - 비정상적으로 연결이 끊어졌을 때 적절하게 대응해야된다.
  - 기존 HTTP 사용과 비교헀을 때, 코딩 복잡성을 가중 시키는 요인이 될 수 있다.
- Server - Client 간 Socket 연결 유지 자체가 비용
  - 트래픽 양이 많은 서버같은 경우 CPU에 큰 부담이된다.
- 오래된 웹 브라우저의 경우 지원하지 않는다.

# 4. 사용 예시
- SNS APP (FaceBook)
- Multiplayer Game (LOL)
- 위치기반 APP
- 증권 거래 정보 Site App
- 화상 채팅 APP
- 구글 Docs 같은 동시 접속 수정 Tools