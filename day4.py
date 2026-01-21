# type verification:

n=10
print(type(n))

num= input()
10
print(type(num),num)

# 1.if number is zero print like " Entered number is zero"

m=int(input())
if m==0:
    print(" Entered nuumber is zero")
print("program is done")


# 2. check if number is zero or not
# Approach 1:

num=int(input(" Enter a number:"))
if num==0:
    print(" Number is zero")
else:
    print(" Number is not zero")

#Approach 2:

num=int(input(" Enter a number:"))
if num!=0:
    print(" Number is not zero")
else:
    print(" Number is zero")
    

# 3. check if the num is even or odd
num=int(input(" Enter a number:"))
if num%2==0:
    print(num, " Number is even")
else:
    print(num, "Number is odd")
print("program is successfuly executed")


num=int(input(" Enter a number:"))
n=10
if num>=0 and n%2==0:
    print(num, "Number is positive even")
elif n>=0 and n%2!=0:
    print(num, "Number is positive odd")
elif n<0 and n%2==0:
    print(num, "Number is negitive even")
else:
    print(num, "Number is negitive odd")
