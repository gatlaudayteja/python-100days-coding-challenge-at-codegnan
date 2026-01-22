def evenorodd(n):
    if n % 2:
        return"odd"
    else:
        return"even"
print(evenorodd(13))

#positional arguments
#sub of two numbers using func

def sub(n1, n2):
    res = n1 -n2
    return res
a = int(input())
b = int(input())
print(sub(a, b))
print(sub(b,a))

def sub(n1, n2):
    res = n1 -n2
    return res
a, b = 10, 5
print(sub(a, b))
print(sub(b, a))

#sum of two num using func
#sum of 3 numb using func
#sum of 4 numb using func

#list properties
lst = [10,2,4,4.534,'hi','hello']
print(lst[2])
print(lst[-3])
print(lst[2:])

 #example

lst = [1,2,3,40,'hi', 'hello']
lst[0] = 100
print(lst)

#string is immutable
#s = 'srinu'
#s[0] = '2'
#Sprint(s)

#nested elements
lst = [1,2,3,[10,5,20],4,6]
print(lst[3])
print(lst[2])
print(lst[3][4])

#reading list of integer elements from user
#map func
l = list(map(int,input().split()))
print(type(1), 1)

#read list of number and if numbers is even odd 
lst = [1,2,3,4,5]
res = [2,2.5,4,4.5,6]
for i in range(0, len(lst)):
    if lst[i] % 2:
        lst[i] = lst[i] + 1
    else:
        lst[i] += 0.5
print(lst)
         
