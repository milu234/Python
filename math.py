import math

print("The absolute value of -8 is {0}".format(abs(-8)))	#gives the positive disance from zero

print("The exponential value  of 4 is {0}".format(math.exp(4))); #exponential value
print("The factorial of 8 is {0}".format(math.factorial(8))); #gives back factorial
print("The sign will get changed of 8 : {0}".format(math.copysign(-8,7))); #returns x with the sign of y
print("The absolute value of -89 is {0}".format(math.fabs(-89))); #retturns absolute value
print("The largest integer of the value 8.9 is {0}".format(math.floor(8.9))); #returns the largest intger less than equal to x
print("The remainder when 46 is divide by 6 is {0}".format(math.fmod(45,6))); #returns the remainder
print("The mantissa and exponent of the number 45 is {0}".format(math.frexp(45))); #returns the mantissa and exponent of x as pair of(m,e)
#print(math.fsum(7)); #returns an accurate floating point
print("The number is not infinity is {0}".format(math.isfinite(7))); #returns true if the x isneither a infinity nor a number
print("The value of the given even number is : {0}".format(math.ldexp(2,2))); #returns x*(2**i)
print("The fractional and integer part of the given number is {0}".format(math.modf(12.36))) #return fractional anf integer part of x
print("The truncated value of the 12 is {0}".format(math.trunc(12))); #returns the truncated value
print("The value of e raise to 3 is {0}",format(math.exp(3))); #returns e**x
#print(math.log(10[ 2])) #returns the logarithmic value of x
print("The value of log 10 to base 2 is {0}".format(math.log2(10))); #returns the logarithmic value of x
print("The logarithmic value of the log 10 to the base 10 is {0}".format(math.log10(10)));  #returns the logarithmic value of x
print("The value of the 2 raise 4 is {0}".format(math.pow(2,4))); #Returns x raised to the power y
print("The squre root of 81 is {0}".format(math.sqrt(81))); #Returns the square root of x
print("The value of cos 1 is {0}".format(math.acos(1))); #Returns the arc cosine of x
print("The value of sin 1 is {0}".format(math.asin(1))); #Returns the arc sine of x
print("The value of tan 1 is {0}".format(math.atan(1))); #Returns the arc tan of x
print("The Cosine of 1 is {0}".format(math.cos(1)));
print("The Sine of 1 is {0}".format(math.sin(1)));
print("The Tan of 1 is {0}".format(math.tan(1)));
print("The  hyperbolic Cosine of 1 is {0}".format(math.cosh(1)));
print("The  hyperbolic sine of 1 is {0}".format(math.sinh(1)));
print("The hyperbolic tan of 1 is {0}".format(math.tanh(1)));
print("The error function  of 1 is {0}".format(math.erf(1)));
print("The degree of 10 is {0}".format(math.degrees(10)));
print("The hypotaneous of 3 and 4 is is {0}".format(math.hypot(3,4)));
print("The value  of pi is {0}".format(math.pi));
print("The value  of mathematical constant e is  {0}".format(math.e));




