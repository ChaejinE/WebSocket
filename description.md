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