n = int(input())

def sum_from_one_to_N(N):
    sum = N*(1+N)/2
    result = int(sum/10)
    return result

final = sum_from_one_to_N(n)

print(final)