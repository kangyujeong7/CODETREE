A,B = map(int,input().split())

for i in range(B,A-1,-1): # A+1을 하나로 봐야한다, 그러면 기본개념 설명에 stop:두번째 인자로 전달된 값까지, 하지만 해당 값은 포함되지 않습니다 -> 니깐 A+1은 포함되지 않는다.
    print(i,end=" ") # for i in range(B,A+1,-1)이건 틀린답