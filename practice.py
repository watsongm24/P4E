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

x = addtwo(3, 9)  # Call addtwo() function with arguments 3 and 9 and assign the return value to x
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
    
# Initialize a variable to keep track of the largest number found so far.
largest_so_far = -1
print('Before:', largest_so_far)
# Iterate through each number in the list [3, 6, 91, 36, 78, 99].
for the_num in [3, 6, 91, 36, 78, 99]:
    # Check if the current number is greater than the largest number found so far.
    if the_num > largest_so_far:
        # If the current number is greater, update the largest_so_far to the current num
        largest_so_far = the_num
    
    # Print the current largest number and the current number being compared.
    print(largest_so_far, the_num)

# After the loop, print the final largest number found.
print('After:', largest_so_far)


smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
#####################################################
#Summing in a loop
zork = 0
print('Before ', zork)
for things in [2,34,67,24,23,99]:
    zork = zork + 1
    print(zork, things)
print('After, zork')