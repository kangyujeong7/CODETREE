n = int(input())

if n>=3000:
    print("book")
elif n>=1000: #  3000이상인건 이미 한번거르고 오기 떄문에 쓸필요없다 / 조건 1이 false이면서, 조건2가 True일때 실행할 코드
    print("mask")
else:
    print("no")