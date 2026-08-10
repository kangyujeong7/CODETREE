N = input().split()
# R = N.reverse() #반환값은 None이 나옴
# N.reverse() # 이건 뒤집힌 결과가 나옴
R = list(reversed(N)) #새로운 변수에 뒤집힌 결과를 담고 싶다.
print("".join(R))

#리스트.reverse( ) :리스트 자체를 직접수정
#reversed() :뒤집은 반복 가능한 객체 반환

