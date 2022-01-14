# 동기 호출, 비동기 호출
- Python에서 어떻게 웹소켓 기술을 사용할 수 있을까?
  - websockets:python module
  - asyncio라는 표준 모듈로 개발되어있다.
  - 따라서 먼저 비동기 모듈을 공부해야된다.

# What is asyncio ?
```python
def func1():
    print("hi")
    
def func2():
    print("bye")
    
func1()
func2()
```

![image](https://user-images.githubusercontent.com/69780812/149479696-1b0cc86b-8cb9-484e-b2e2-8fbbcdfcebb9.png)
- 맨 위의 코드는 func1() 호출이 끝나고 func2() 호출이 될 것이다.
- 이러한 전통적인 함수 처리 방식을 Synchronous(동기) 호출 방식이라고 한다.
  - 어떤 요청 및 작업에 대해 완전히 끝낸 후 다음 요청 및 작업을 처리하는 방식이다.
- Asynchronous(비동기) 방식의 일처리는 예를들어 점원이 주문을 받고, 기계의 버튼을 눌러 1분간 기다리지 않고, 기계가 일을 처리하는 동안 다른 주문을 받는 것을 말한다.
  - 점원의 역할은 CPU로 볼 수 있으며 어떤 작업(함수)를 처리하는 데 필요한 데이터를 웹이나 파일로부터 읽는데 대기 시간이 소요되면 아무 일도 진행하지 않은채로 기다리기보다 다른 함수를 차러하는 것이 시스템 성능을 향상시킬 수 있다.
  - 특정 함수가 파일이나 서버로부터 데이터 요청 대기가 필요한 경우 적당한 스케줄링 방식을 기반으로 요청받은 다른 작업을 먼저 처리하고있다가 데이터가 준비될 때 다시 기존에 요청받은 함수를 처리하는 방식을 비동기 처리라고한다.

![image](https://user-images.githubusercontent.com/69780812/149482875-06edd0fd-2b84-4620-82cd-ec79f66c318e.png)
- 동기 방식과 비동기 방식의 차이를 나타내는 그림이다.
- 비동기를 보면, task A에서 데이터 요청을 하는 경우, 기다리지 않고 task A가 끝나지 않은 상태에서 다른 task B를 수행한다. 데이터가 준비되면 task A의 남은 부분을 처리하게 된다.
- 비동기 방식의 전체 태스크 처리시간이 더 짧은 것을 알 수 있다.
- 하지만, 항상 비동기처리 방식이 좋은 것만은 아니다. 수행할 작업이 단순 연산 중심이 아니라 중간 마다 쉴 수 있는 형태의 작업이어야 한다. 
  - 대표적으로 데이터 등 인터넷에 다운로드 받고 이를 처리하는 함수들은 먼저 데이터를 다운 받는 데 시간이 소요되는데, 이런 작업은 비동기처리 방식을 사용하는 것이 좋다.
- 이미지 데이터는 준비되어 있고, 단순히 데이터에 대한 단순 연산으로 구성된 경우라면 비동기처리 방식으로 이를 처리한다고 해도 얻을 수 있는 이점이 없다.
  - 또한, task를 잘 처리하려면 스케줄러가 필요하다는 점도 고려해야된다.

# Coroutine
- Pyton에서는 함수앞에 async라는 키워드를 붙이면 **Coroutine(코루틴)**이라고 부른다.
- 일반 함수 처럼 코루틴을 호출하면 에러가 발생한다. 코루틴은 **스케줄러가 필요하다** 이를 ***이벤트 루프***라고 부른다.
  - 코루틴을 처리하기 전에 이벤트 루프를 만들고, 처리가 끝난 후에는 이벤트 루프를 닫아주면 되는데, 이런 역할을 간단히 처리해주는 것이 asyncio 모듈의 run 함수이다.

```python
import asyncio

async def func1():
    print("hi")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(func1())
loop.close()
```
- 이벤트 루프 동작 등을 세부적으로 제어할 필요가 있을 때, run()과 같은 고수준 함수를 사용하지 않고, 직접 이벤트 루프를 얻고, 루프를 통해 코루틴을 처리한 후 이벤트 루프를 닫을 수 있다.
  - 위 코드는 이벤트 루프를 가져오고 > 코루틴 객체가 완료될 때까지 실행하고 > 이벤트 루프를 닫는다.

```python
import asyncio

async def make_americano():
    print("Ame Start")
    await asyncio.sleep(3)
    print("Ame End")
    
async def make_latte():
    print("Latte start")
    await asyncio.sleep(5)
    print("Latte end")
    
async def main():
    a = make_americano()
    b = make_latte()
    
    await asyncio.gather(a, b)
    
print("Main Start")
asyncio.run(main())
print("Main End")
```

```shell
Main Start
Ame Start
Latte start
Ame End
Latte end
Main End
```
- time.sleep(3) 함수가 CPU를 점유하면서 기다리는 것과 달리 asyncio.sleep() 함수는 CPU가 다른 코루틴을 처리할 수 있도록 CPU 점유를 해제한 상태로 기다린다.
  - 어떤 코루틴이 asyncio.sleep() 함수를 실행하는 순간 이벤트 루프는 다른 코루틴을 실행시킨다.
  - asyncio.slee() 역시 코루틴이다. 코루틴 내 다른 코루틴을 호출할 때에는 await을 사용한다.
- Start는 거의 동시에 출력되는데, 이는 아메리카노를 만드는 코루틴이 Sleep을 호출하는 순간 바로 이벤트 루프가 커피 라테를 만드는 코루틴을 실행시키기 때문이다.

```python
import asyncio

async def make_americano():
    print("Ame Start")
    await asyncio.sleep(3)
    print("Ame End")
    return "Americano"
    
async def make_latte():
    print("Latte start")
    await asyncio.sleep(5)
    print("Latte end")
    return "Latee"
    
async def main():
    a = make_americano()
    b = make_latte()
    
    result = await asyncio.gather(a, b)
    
    print(result)
    
print("Main Start")
asyncio.run(main())
print("Main End")
```
- 값을 return하는 코루틴이다.
- asyncio.gather를 통해 여러 코루틴을 동시에 실행하는 경우 모든 코루틴이 실행이 종료될 때 각 코루틴의 리턴 값이 파이썬 리스트에 담겨서 전달된다.