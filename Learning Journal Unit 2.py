
#PART 1

#calculating volume of a sphere
#using the value of "pi" given in Section 2.1 of Think Python 2e

pi = 3.141592653589793 #the value of "pi" so that I avoid using the whole value in the code

def print_volume (r):
	return (4/3) * pi * r**3 # I have divided 4 by 3, multiplied by "pi" and raised to the power 3

#to use a radius of 30	
print ('volume of the sphere with radius of 30 is', print_volume(30))
#----------------------------------------------------------------------------------------------
#to use radius of 35
print ('volume of the sphere with radius of 35 is', print_volume (35))
#----------------------------------------------------------------------------------------------
#to use radius of 40
print ('volume of the sphere with radius of 40 is', print_volume (40))
#----------------------------------------------------------------------------------------------

#PART 2

#Body Mass Index Calculator(BMI)
#To calculate the BMI we divide weight in kilograms by height in metres squared
# BMI = kg/m2


def body_mass_index ():
	return (kg/m**2)

#The weight and height of Rudo
kg = 100
m = 1.6
print('The BMI for Rudo is', body_mass_index())
#-----------------------------------------------------------------------------------------------

#The weight and height of Romeo
kg = 120
m = 1.7
print ('The BMI for Romeo is', body_mass_index())
#-----------------------------------------------------------------------------------------------

#The weight and height of Elon
kg = 60
m = 1.8
print ('The BMI for Elon is', body_mass_index())
#-----------------------------------------------------------------------------------------------








