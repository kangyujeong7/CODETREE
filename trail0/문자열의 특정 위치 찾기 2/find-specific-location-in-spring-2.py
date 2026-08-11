N = input()
elements = [ 'apple','banana','grape','blueberry','orange']
count=0

for i in elements:
    temp = i
    if N == temp[2]:
        print(i)
        count+=1
    if N == temp[3]:
        print(i)
        count+=1
print(count)