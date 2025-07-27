# temp_conversion_tool.py

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

if __name__ == "__main__":
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        

        if unit == 'F':
            convert_to_celsius = (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
            print(f"{temp}°F is {convert_to_celsius}°C")
        elif unit == 'C':
            convert_to_fahrenheit = (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
            print(f"{temp}°C is {convert_to_fahrenheit}°F")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")
