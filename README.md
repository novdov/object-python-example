# object-python-example

[오브젝트: 코드로 이해하는 객체지향 설계](https://wikibook.co.kr/object/)(조영호, 위키북스, 2019)의 예제 코드를 파이썬으로 실습한 내용을 정리합니다.

- 원 예제 코드 (in Java): [GitHub 저장소](https://github.com/eternity-oop/object)

## 실습 환경
```bash
python == 3.8
```


## 컨벤션
- Python
    - (Java 의) `private` 클래스 인스턴스 변수는 언더스코어(`_`)로 변수명을 시작합니다.
    - `typing` 모듈을 사용해 메서드 인자와 리턴 값의 타입을 표시합니다.
- Git
    - 커밋 메시지에는 `etc)`, `ch01)` 등과 같이 커밋 종류를 명시합니다.


## 코드 스타일 & 타입 체크
- 코드 스타일: [`black`](https://github.com/psf/black)/[`isort`](https://github.com/timothycrosley/isort) 를 사용합니다.
- 정적 타입 체크: [`pyright`](https://github.com/microsoft/pyright) 를 사용합니다.


## 함께 읽으면 좋을 책
- [클린 아키텍처](https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=202322454)(로버트 C. 마틴 저, 송준이 역, 2인사이트, 2019)
