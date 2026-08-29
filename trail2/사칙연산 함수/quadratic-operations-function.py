a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here

#   print(f"{a} {o} {c} = {aoc}")


def plus(A,B):
    return A+B
def minus(A,B):
    return A-B
def multiple(A,B):
    return A*B
def divide(A,B):
    return A//B

if o == "+":
  print(f"{a} {o} {c} = {plus(a,c)}")

elif o == "-":
      print(f"{a} {o} {c} = {minus(a,c)}")
elif o == "*":
      print(f"{a} {o} {c} = {multiple(a,c)}")
elif o == "/":
      print(f"{a} {o} {c} = {divide(a,c)}")
else:
    print("False")





