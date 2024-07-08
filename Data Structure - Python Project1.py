A = "SACHIN".lower()
print(A)

U = "sachin".upper()
print(U)

l = "SHALINI".lower()
print(l)

R = "SHALINI".replace('I','K')
print(R)

msg = "  end  "
msg.strip(' ')
print(msg)

msg = "Cat in a hat"
msg1= msg.find('a',8)
print(msg1)

print(msg.index('a'))

print(msg.replace('a', 'k'))

#Numbers:

num1 = 10 + 25 + 3.0
print(type(num1))

X = abs(-10)
print(X)

var = [3, 'Data', 8.7, 'P']
print(type(var))

mylist = ["Europe", "Asia", "North America", "South America", "Africa", "Australia", 2009, 2140, 12.5, 6.25]
print(len(mylist))

var = [52, 14, 87, 15, 10, 158, 6]
print(max(var))

var = [52, 14, 87, 15, 10, 158,]
var.append(74)
print(var)

mylist = ["Europr", "Asia", "North America", "South America", "Africa", "Australia", 2009, 2140, 12.5, 6.25]
mylist.append(['B', 'T', 'C'])
print(mylist)

var = [4, 2, 1, 6]
var.append(['B', 'C', 'T'])
print(var)

var1 = [8,9,10]
var2 = [8,9,10]
var2==var1
var2 is var1
print(var1)
print(var2)
var1.remove(9)
print(var1)

# Set
var1= {26,100}
print(var1)

list1= [4,8,9]
set1= set(list1)
print(type(set1))

print(set1)

var= {4,8,9}
print(type(var))

var = {4, 8, 9, 7, 1, 8, 1}
print(var)

list1 = ["Hello", "Hi", "Greetings", "Cheers", "Hi", "Hello", "Greetings!"]
var = set(list1)
print(var)

set1 = {26, 200, 2001, 92, 550, 2001, 338, 92, 11}
length= (len(set1))
print(length)

set1 = {26, 200, 2001, 92, 550, 2001, 338, 92.0, 11}
length = (len(set1))
set1.add(550)
print(set1)



set1 = {26, 200, 2001, 92, 550, 2001, 338, 92.0, 11}
set1.remove(550)
print(set1)

# Tuple
var1 = (50)
print(type(var1))

mytuple = (100, 250, 300, 450, 500, "Python", "Java", "C++")
print(mytuple[0:3])

mytuple = (100, 250, 300, 450, 500, "Python," "Java", "C++")
print(mytuple[7:])

mytuple = (100, 250, 300, 450, 500, "Python", "Java", "C++")
print(mytuple[-5:-2])

print(mytuple[7:])

print(mytuple[-2:-5])

mytuple = (100, 250, 300, 450, 500)
(a, b, c, d, e) = mytuple
print(d%10)
print(d//10)

print(d/10)

mytuple = (100, 250, 300, 450, 500)
print(min(mytuple))

mytuple = (100, 250, 300, 450, 500, "python", "Java", "C++")
(mytuple+ (410, 430, 450, 205*2, 900//2, 445)).count(450)

print(mytuple)

(mytuple+ (410, 430, 300, 450, 205*2, 900//2, 445))

mytuple = (100, 250, 300, 450, 500, 650, 700, 850, 900)
print(mytuple[1::3])

mytuple = (100, 250, 300, 250, 500, 650, 700, 250, 900)
print(mytuple.index(250))

mytuple = (67, 8, 58, 94, 90, 54, 67)
(a, b, c, d, e, f, g) = mytuple


# Range
myrange = range(11)
print(list(myrange))

myrange = range(3, 15, 2)
print(list(myrange))

myrange = range(10, 19, 3)
print(list(myrange)[2])

myrange = range(10, 16, 2)[::2]
print(list(myrange))

myrange = range(5, 15, 4)[::-1]





















