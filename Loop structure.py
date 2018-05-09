#Syntax for if/elif/else
a=40
if a < 4:
    print('Value is less than 4')
elif a < 7:
    print ('Value is less than 7')
elif a < 10:
    print ('Value is less than 10')
else:
    print ('Value is 10 or more')

#Sum of all numbers stored in list
har = [1,2,3,4,5,6,7,8,9,10]
total = sum(har)
print(total)

#For loop - Execute block of code several number of times
fl = [0,1,2,3,4,5,6,7,8,9,10,11]
sum=0
for elem in fl:
    sum=sum+elem
    print(sum)

#For loop with else - Executed when items in the for loop exhausts
flelse = ['H','a','r','s','h','a']
for elem in flelse:
    print(elem)
else:
    print('My name is displayed outside the list')

#While loop - test expression (condition) is true

#Sum of all even numbers till 'n'
n=int(input("Enter n:"))
#Declare variable for sum of even number
Evensum=0
#Declare counter for increment
i=0
while i<=n:
    Evensum=Evensum+i
    i=i+2
print('The sum of the even number is', Evensum)

#Sum of all odd numbers till 'n'
n=int(input("Enter n:"))
#Declare variable for sum of even number
oddsum=0
#Declare counter to satify the condition
i=1
while i<=n:
    oddsum=oddsum+i
    i=i+2
print('The sum of the odd number is', oddsum)






