
# def make_square(p):
#     count = 1
#     for _ in range(n):
#         for _ in range(n):
#             print(count,end=" ")
#             count+=1
#             if count == 10 :
#                 count = 1
#         print()
        
# n = int(input())
# make_square(n)


# # Please write your code here.

N = int(input())
a = 1

#======================
#오답코드
# def make_square(n):
#     for _ in range(N):
#         for _ in range(N):
#             print(a, end=" ")
#             a+=1
#         print()

# make_square(N)

# 1. 🔍 원인 (Cause)
# 함수 바깥에서 a = 1을 선언했더라도, 함수 내부에서 a += 1처럼 변수의 값을 변경하거나 대입하는 코드가 있으면, 파이썬은 이 a를 함수 내부의 지역 변수(Local Variable)로 인식합니다.

# 이때, print(a)를 실행하는 시점에 함수 안에는 아직 a라는 변수가 생성되지 않았기 때문에 UnboundLocalError(할당되지 않은 변수를 참조함) 에러가 발생합니다.



def make_square(n):
    a =1 
    for _ in range(N):
        for _ in range(N):
            if a > 9:
                a =1 
            print(a, end=" ")
            a+=1
        print()

make_square(N)
