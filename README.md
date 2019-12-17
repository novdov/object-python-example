# object-python-example

[오브젝트: 코드로 이해하는 객체지향 설계](https://wikibook.co.kr/object/)(조영호, 위키북스, 2019)의 예제 코드를 파이썬으로 실습한 내용을 정리합니다.

- 원 예제 코드 (in Java): [GitHub 저장소](https://github.com/eternity-oop/object)

## 실습 환경
```bash
python == 3.7
```


## 컨벤션
- (Java 의) `private` 클래스 인스턴스 변수는 변수명 접두어로 언더스코어를 붙여 선언합니다.
- `typing` 모듈을 사용해 메서드 인자와 리턴 값의 타입을 표시합니다.


## 코드 스타일 & 타입 체크
- 코드 스타일: [`black`](https://github.com/psf/black)/[`isort`](https://github.com/timothycrosley/isort) 를 사용합니다.
- 정적 타입 체크: [`pyright`](https://github.com/microsoft/pyright) 를 사용합니다.
s