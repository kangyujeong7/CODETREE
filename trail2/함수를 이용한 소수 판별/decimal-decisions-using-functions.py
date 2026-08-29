a, b = map(int, input().split())


# Please write your code here.
#소수 고르는 것
#소수의 정의:소수(素數, Prime Number)의 정의는 "1보다 큰 자연수 중에서, 1과 자기 자신만을 약수로 가지는 수"
def checking_prime(k):
    for i in range(2,k):
        if k % i == 0:
            return False
            break 
    return k



sum = 0 
for i in range(a,b+1):
    sum += checking_prime(i)

print(sum)