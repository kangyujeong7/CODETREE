N = int(input())

Boolean = str(((N%2==1)and(N%3==0) )or ((N%2==0)and(N%5==0)))
result = Boolean[0].lower()+ Boolean[1:]
print(result)