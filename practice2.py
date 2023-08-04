''' This loop keeps taking input from the user until the user enters 'done',
 then it breaks out of the loop.'''
while True:
    line = input('> ')  # Takes user input and stores it in the 'line' variable.
    if line == 'done':  # If the user enters 'done', the loop is terminated 
      print(line)  # Otherwise, the input is printed, and the loop continues
print('Done!')  # After the loop, it prints 'Done!' to indicate the loop has finished.


''' This loop keeps taking input from the user until the user enters 'done', 
but it skips the loop iteration if the user enters '#'.'''
while True:
    line = input('> ')  # Takes user input and stores it in the 'line' variable.
    if line == '#':  # If the user enters '#', the current iteration is skipped
        continue
    if line == 'done':  # If the user enters 'done', the loop is terminated
        break
    print(line)  # Otherwise, the input is printed, and the loop continues to the next
print('Done!')  # After the loop, it prints 'Done!' to indicate the loop has finished.
