a, b, c = map(int, input().split())

def minimum(A,B,C):
    if A<B:
        if A<C:
            min = A
            return min    

        else:
            min = C
            return min    

    else:
        if B<C:
            min = B
            return min    

        else:
            min = C
            return min    

print(minimum(a,b,c))