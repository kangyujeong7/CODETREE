N = int(input())
temp = 0
#만약 N이상이 되면 contineu로 멈추고 i를 출력시켜라

for i in range(1,N+1):
    temp+=i
    if temp >= N:
        break
print(i)
    