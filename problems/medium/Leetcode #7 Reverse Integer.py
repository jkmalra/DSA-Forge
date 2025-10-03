def reverse(x: int):
    is_negative = False

    if x < 0:
        is_negative = True

    num = abs(x)
    answer = 0
    while num >0:
        last_digit = num % 10
        answer = (answer * 10) + last_digit
        num //= 10
    
    if answer < (-(21**31)) or answer > (2**31 - 1):
        return 0
    return -answer if is_negative else answer

#  To reverse the digits of an integer,
#  we can repeatedly extract the last digit and build the reversed number step by step.
#  If the original number is negative, we handle the sign separately.

# Approach:

# Check if the number is negative and store this information
# Convert the number to its absolute value for easier processing
# Initialize a variable to store the reversed number
# Use a loop to extract the last digit of the number and append it to the reversed number
# Ensure the result does not overflow the 32-bit signed integer range
# Restore the sign if the original number was negative
# Return the reversed number or 0 if it overflows


# Overflow Check:
# After the loop, check if the reversed number is within the 32-bit signed integer range. If not, return 0.