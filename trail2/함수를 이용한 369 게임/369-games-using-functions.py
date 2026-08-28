a, b = map(int, input().split())

# Please write your code here.

def checking_3_6_9(k):
    string_number = str(k)
    list_number = list(map(int,string_number))
    if 3  in list_number or 6  in list_number or 9  in list_number:
        return k



def is_magic_number(n):
    return checking_3_6_9(n) or n%3 ==0




cnt = 0
for i in range(a,b+1):
    if is_magic_number(i):
        cnt+=1

print(cnt)