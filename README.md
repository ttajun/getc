# python 비동기

1개 이상의 URL을 인자로 받아 각각 Get 요청을 보내서   
받은 응답 데이터들의 길이 평균, 표준편차 구하기

## Usage
```bash
usage: get.py [-h] [-t TIMEOUT] [-k] URL [URL ...]
```

## Example
```bash
$ python get.py http://www.xnsystems.com/product/ https://www.github.com/ https://www.kakao.com/
평균: 90244.33333333333
표준편차: 86904.14313227854
```
