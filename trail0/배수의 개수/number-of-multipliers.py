cnt_3= 0
cnt_5 = 0
for _ in range(10):
    N = int(input())
    if N % 3 == 0 and N%5==0:
        cnt_3+=1
        cnt_5+=1
    elif N %3 ==0:
        cnt_3+=1
    elif N%5 ==0:
        cnt_5+=1
    
print(cnt_3,end=" ")
print(cnt_5)

# 3의 배수인데 그중 5의 배수인것