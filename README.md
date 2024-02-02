# divformulagenerator
This script generates a formula to verify if an integer of n decimal digits is divisible by x

# Examples:

$ python3 divtestformula.py 10 3

A number n with 10 decimal digits of the form n=abcdefghij is divisible by 3 if 

a+b+c+d+e+f+g+h+i+j

is divisible by 3

$ python3 divtestformula.py 7 13

A number n with 7 decimal digits of the form n=abcdefg is divisible by 13 if 

a+4b+3c-d-4e-3f+g

is divisible by 13

$ python3 divtestformula.py 10 100

A number n with 10 decimal digits of the form n=abcdefghij is divisible by 100 if 

10i+j

is divisible by 100

$ python3 divtestformula.py 10 19

A number n with 10 decimal digits of the form n=abcdefghij is divisible by 19 if 

-a-2b-4c-8d+3e+6f-7g+5h-9i+j

is divisible by 19

