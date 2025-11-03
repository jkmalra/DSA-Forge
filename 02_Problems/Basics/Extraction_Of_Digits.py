# The problem is to extract & print each digit of a given integer number starting from the last digit.
# The digits should be printed without spaces or any separators.

    # For example, given the input 1234, the output should be 4321.

num = 5873

n = num
while n > 0:
    last_digit = n % 10
    print(last_digit, end='')
    n = n // 10




#  The last digit is obtained using the modulus operation (n % 10)
#  print the last_digit
#  Remove the last digit from the number by using integer division (n // 10)
#  
# like: 5873 % 10 = 3      --this will be printed
#        5873 // 10 = 587
#        587 % 10 = 7       --this will be printed
#        587 // 10 = 58