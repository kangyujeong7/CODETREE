n = int(input())

def is_magic_number(N):
    string_number = str(N)
    number_list = list(map(int,string_number ))
    sum = 0
    for i in number_list:
        sum+=i
    if N %2 ==0 and sum % 5 ==0:
        return "Yes"
    else:
        return "No"

# Please write your code here.\

print(is_magic_number(n))