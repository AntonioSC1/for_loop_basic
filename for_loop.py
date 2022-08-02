#print all intergers from 0 to 150.
for i in range(0, 150 +1):
    print(i)

#print all the multiples of 5 from 5 to 1,000
for x in range(5,1000 +5 ,5):
    print(x)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for x in range(1,100 +1):
    if x % 5:
        print("Coding")
    elif x % 10:
        print("Coding Dojo")

#Add odd integers from 0 to 500,000, and print the final sum.
minimum = 0
maximum = 500000
Oddtotal = 0

for number in range(minimum, maximum+1):
    if(number % 2 != 0):
        print("{0}".format(number))
        Oddtotal = Oddtotal + number

print("The Sum of Odd Numbers from {0} to {1} = {2}".format(minimum, maximum, Oddtotal))

#Countdown by fours-Print positive numbers starting at 2018, counting down by four.
def count_down_four():
    number = 2018
    while number > 0:
        print (number)
        number = number - 4
        
count_down_four()

#Flexible Counter - Set three variables: lowNum, highNum, mult.
# Starting at lowNum and going through highNum, print only the integers that are a multiple of mult.
# For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
def flex_countdown(low, high, mult):
    for i in range (low, high):
        if i % mult == 0:
            print (i)
            
flex_countdown(2, 9, 3)