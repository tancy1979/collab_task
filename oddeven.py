# Write a function to determine if a positive integer is odd or even


def oddeven(n):
  if n % 2 == 0: # even 
    print("This positive integer is even")
  else: # odd
    print("This positive integer is odd")
    
#main
oddeven(5)
oddeven(6)

# boolean version
''' Returns True if positive integer is odd, False if positive integer is even
'''
def is_odd(n):
  if n % 2 == 1: # odd
    return True
  else: # even
    return False

#main
print(is_odd(5))
print(is_odd(6))
