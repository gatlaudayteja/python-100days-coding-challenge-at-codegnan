def add(a,b):
    return a+b
print(add(10,20))

#sum of three numbers

def add(a,b,c):
    return a+B+C
print(add(10,20,30))

#sum of four numbers

def add(a,b,c,d):
    return a+b+c+d
print(add(10,20,30,40))

#using both 2,3,4 numbers

def add(a,b,c=0,d=0):
    return a+b+c+d
print(add(1,2,3,4))
print(add(1,2,3))
print(add(1,2))

#variable length of positional arguments

def add(a,b,c=1,d=2):
    return a*b*c*d
print(add(1,2))
print(add(1,2,3))
print(add(1,2,4))

#variable length of prositional args
def add(a, *args):
    print(a)
    print(args)
add(1,2,3,4,5,6,7,8,9)

#we sum of the numbers

def add(a, *args):
    print(a)
    print(args)
    s = 0
    for num in args:
        s+= num
    return s
print(add(1,2,3,4,5))

#list operations:
# 1.concatination
#  2.repeat


#repeat
#11 = [1,2,3]
#print(11 * 2)


#empty list of representation
l1 = []
l2 = list()
print(type(11))
print(type(12))
print(len(11),len(12))

 #list functions
# 1.append
# 2.extend
# 3.insert
# 4.remove

#append

lst = [1,2,3,4]
lst.append([10,30,40])
print(lst)

#extend

lst = [1,2,3,4]
lst.extend([10,20,30])
print(lst)

#insert

lst = [1,2,3,4]
lst.insert(2,100)
lst.insert(2,200)
print(lst)
lst.insert(100, 1000)
print(lst)

#

lst = [1,2,3,4]
print(lst.pop())
print(lst.pop(3))

 #remove

lst = [1,2,3,4,5,6,7]
lst.remove(2)
lst.remove(3)
print(lst)

#count

lst = [1,2,3,3,5,6,7,7,9]
print(lst.count(3))
print(lst.count(8))

#index

lst = [1,2,3,4,5,6,7,8,9]
print(lst.index(3))
print(lst.index(8))

#sort
lst = [1,2,3,3,4,3,4,2,5]
lst.sort()
print(lst)

# reverse

lst = [1,2,3,3,4,3,4,2,5]
lst.sort(reverse = True)
print(lst)


##convert list of number into even list and odd list

lst=list(map(int,input("Enter list of numbers").split()))
even_list=[]
odd_list=[]
for num in lst:
    if num%2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("Even list: ",even_list)
print("Odd list: ",odd_list)


#marks analyser
#pass marks=35(+)
#fail marks=35(-)
marks=list(map(int,input("Enter marks: ").split()))
def marks_analyser(marks):
    avg = sum(marks) / len(marks)
    if avg>= 35:
        return "Pass"
    else:
        return "Fail"
print(marks_analyser(marks))


