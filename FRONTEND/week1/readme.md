JS란?

웹브라우저상에서 쓰이는 언어

서버쪽에서도 사용은 가능

크롬으로 진행해라.

크롬에서 개발자 도구를 키자. f12눌러서 ... 개발자도구 켜서
콘솔켜서 콘솔로그 해보자.. 그럼 결과 나온다.

이번 강의에서는 비쥬얼스튜디오코드를 통해 코드를 수정해보겠따.

자스 이용법

1. html 문서안에서 작성
2. 외부 스크립트 코드 불러오기

...2주차....

1. 숫자

2. 문자열

3. 참/거짓

4. Null/undefined

5. 연산자
   숫자 + 문자 더하기 할 시 숫자가 문자열로 자동변환

자바스크립트에서 == 는...
정답부터 말하자면, '=='와 '===' 연산자의 주된 차이점은, 예를 들어, 숫자를 숫자 리터럴과 비교하면, '=='는 그것을 허용하지만, '===' 두 변수의 형식은 동일하지 않은 경우, 값뿐만 아니라 두 변수의 유형도 확인하므로, 허용하지 않는 것이다. 즉, '==='는 'false'으로 반환하고, '=='는 'true'로 반환다.
즉 == 는 서로다른 유형의 두 변수의 값을 비교

or ||
and &&
not !

.. 3주차 조건문 반복문....

조건문 if else if else zz

while 문

for 문
초기값, 조건식, 증감식 순으로 씀.

멈추려면 break
해당 루프만 종료시키려면 continue

.. 4주차 함수와 객체......

매개변수는 파라미터라고 함.
리턴으로 결과값 반환도 ㄱㄴ

객체란..????
변수하나에 여러 정보를 담을 수 있음
효율적으로 정보 관리 가능.

Event 어떤 사건을 발생시키는 것.

EventTarget.addEventListner('eventType', function, 캡션사용여부)

---

data어트리뷰트 dataset 프로퍼티

이벤트 객체 -> 온클릭같은 이벤트가 발생시 사용자의 정보를 담음.

스크롤 이벤트도있음.
window.addEventListener('scroll',function())
