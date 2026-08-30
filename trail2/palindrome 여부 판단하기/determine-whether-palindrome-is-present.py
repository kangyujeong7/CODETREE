A = input()

# Please write your code here.



def palindrome(x):
    if x[0:] == x[::-1]:
        return True
    else:
        return False







if palindrome(A):
    print("Yes")
else:
    print("No")