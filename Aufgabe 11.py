# Writing a program that asks the user for a number of years and calculates how many hours are in that many years. 
# Use 365.25 days per year to account for leap years.

years = int(input("Enter the number of years: ")) 

hours = years * 365.25 * 24

print(f"There are {hours} hours in {years} years.")

