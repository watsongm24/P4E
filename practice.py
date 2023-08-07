# First function example without arguments
def test():
    print("Hello")
    print("Watson")

print("This is a Zip")
test()  # Call the test() function to print "Hello" and "Watson"

###############################################################################

x = 7
print("I am going to use a function \n")

# Second function example
def print_lyrics():
    print("I am a lumberjack, and I am Okay")
    print("I sleep all night and I work all day")

print("This is a test print")
print_lyrics()  # Call the print_lyrics() function to print the lumberjack song
x = x + 8
print(x)
print_lyrics()  # Call the print_lyrics() function again

####################################################################

# Third function example using parameters and arguments
def greet(lang):
    if lang == 'es':
        print("Hola")
    elif lang == 'fr':
        print("Bonjour")
    else:
        print("Hello")

greet('es')  # Call greet() function with argument 'es' to print "Hola"
greet('fr')  # Call greet() function with argument 'fr' to print "Bonjour"
greet("ENG")  # Call greet() function with argument "ENG" to print "Hello"

#####################################################################

# Fourth function example using return value
def greets(langua):
    if langua == 'es':
        return 'Hola'
    elif langua == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greets('en'), 'Watson')  # Print the return value 'Hello' and 'Watson'
print(greets('es'), 'Goodman')  # Print the return value 'Hola' and 'Goodman'
print(greets('fr'), 'Beve')  # Print the return value 'Bonjour' and 'Beve'

#####################################################################

# Fifth function example using multiple arguments and parameters
def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 9)  # Call addtwo() function with arguments 3 and 9 and assign the return 
print(x)  # Print the value of x, which is 12

#####################################################################
#A definite loop with strings
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends:
    print('I am happy to see you ', friend)
print('Bye')
#####################################################################
#Finding the largest value
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [3,6,91,36,78,99]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)

#####################################################
#Summing in a loop
zork = 0
print('Before ', zork)
for things in [2,34,67,24,23,99]:
    zork = zork + 1
    print(zork, things)
print('After, zork')

####################################################
#Summary in a loop
zork = 0
print('Before', zork)
for i in [34, 57, 92, 2, 7, 283]:
    zork = zork + i
    print(zork)
print('After', zork)

######################################################
#Finding the average in a loop
count = 0
sum = 0
print('Before', count, sum)
for i in [34, 57, 92, 2, 7, 283]:
    count = count + 1
    sum = sum + i
    print(count, sum, i)
print('after', count, sum, sum/count)

################################################
# Filtering in a loop
print('Before')
for value in [23, 53, 66, 348, 34802, 234]:
    if value > 30:
        print('Large Number', value)
print('After')

#################################################
#Search using a Boolean Variable
found = False
print('Before', found)
for value in [54,7, 6, 79, 3, 100]:
    if value == 3:
        found = True
    print(found, value)
print('After', found)

##################################################
#Find the smallest value
smallest = None
print('Before', smallest)
for value in [34, 5, 1, 7, 18, 53]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('after', smallest) 

##################################################
#Looping Through Strings
fruit = 'mango'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1
print(index)
##################################################
print('This is a new loop')
#Loopiong and Counting
word = 'mangooo'
counts = 0
for i in word:
    if i == 'o':
        counts = count + 1
print('The number of "o" is ', counts)
################################################################
