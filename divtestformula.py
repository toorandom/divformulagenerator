# This is just an easy generator of formulas that help you test if a number of n digits is divisible by a number x
# Eduardo Duarte
# toorandom@gmail.com
#

import sys

# We just analyze each coefficient in the decimal powers expansion modulo the "number" we want to know it is divisible
# by getting the congruence to that "number" and picking the smallest between the negative and the positive congruence (absolute value)
def get_coefficients_divtest(digits,number):
	seq1=[x % number for x in  [ 10**(n) for n in range(0,digits)] ][::-1]
	seq2=[(x % number)-number for x in  [ 10**(n) for n in range(0,digits)] ][::-1]
	easy_seq = [min(a, b, key=abs) for a, b in zip(seq1, seq2)]
	return easy_seq



### main


if(len(sys.argv) < 3):
	print("arg1 must be the number of digits, arg2 the integer we want to generate the formula")
	print("example: $ python thisfile.py 4 13")
	print("Eduardo Duarte, toorandom@gmail.com")
	exit (1)

digits = int(sys.argv[1])
number = int(sys.argv[2]) 

formula_coefs = get_coefficients_divtest(digits,number)

### Just beautify the coefficients for nice formula display

#put the sign before  the number in the array
formula_coefs_friendly = [f"+{x}" if x >= 0 else f"{x}" for x in formula_coefs]

#the for the '1' coefficients we delete the one and only leave the sign
for x in range(len(formula_coefs_friendly)):
	if(abs(int(formula_coefs_friendly[x])) == 1):
		formula_coefs_friendly[x] = formula_coefs_friendly[x][0]
		
#if the first element of the list is just a '+' replace it by empty char
if(formula_coefs_friendly[0] == '+' ):
	formula_coefs_friendly[0] = ''
#if the first element of the list is '+x', replace it by 'x'
if(len(formula_coefs_friendly[0])>1):
	if(formula_coefs_friendly[0][0] == '+'):
		formula_coefs_friendly[0] = str(int(formula_coefs_friendly[0]))


#we define the digit names in this order, i.e. 123 is a=1, b=2, c=3
constants = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') 

#if we ran out of constants we add the new digit names d_k, for k>len(constants)
if (digits > len(constants)): 
	extra_constants = [ 'd_' + str(x) for x in list(range(len(constants),digits+1)) ] 
	constants = constants + extra_constants

#we print the human message explaining what we did

print('A number n with ' + str(digits)  + ' decimal digits of the form n=' + ''.join(constants[:digits]) + " is divisible by " + str(number) + " if \n")

j=0
for x in zip(formula_coefs_friendly,constants):
	if(formula_coefs[j] != 0):
		print(x[0]+x[1], end='') 
	j=j+1

print('\n\nis divisible by '+ str(number))


	
		

