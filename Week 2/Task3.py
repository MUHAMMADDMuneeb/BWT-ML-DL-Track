def convert_temperature(temp, scale):
    if scale.upper() == "C":
        converted_temp = (temp * 9/5) + 32
        print(f"{temp} degrees Celsius is equal to {converted_temp:.2f} degrees Fahrenheit.")
    elif scale.upper() == "F":
        converted_temp = (temp - 32) * 5/9
        print(f"{temp} degrees Fahrenheit is equal to {converted_temp:.2f} degrees Celsius.")
    else:
        print("Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit.")

    return converted_temp

# Example usage:
temperature = float(input("Enter the temperature: "))
scale = input("Enter the scale (C for Celsius, F for Fahrenheit): ")

converted_temperature = convert_temperature(temperature, scale)
