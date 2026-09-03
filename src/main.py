from utils import square, is_even, celsius_to_fahrenheit

# Get input from user
num = float(input("Enter a number: "))

# Calculate results
sq = square(num)
even = is_even(num)
fah = celsius_to_fahrenheit(num)

# Display results
print(f"Square: {sq}")
print(f"Is even? {even}")
print(f"Fahrenheit equivalent: {fah:.2f}°F")
