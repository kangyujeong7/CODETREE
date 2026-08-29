a, b = map(int, input().split())

# Please write your code here.



def a_to_the_power_of_b(n,m):
    sum = 1

    for i in range(m):
        sum*=n
    
    return sum
        
print(a_to_the_power_of_b(a,b))