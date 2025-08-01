# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FREEZING_POINT_DIFFERENCE = 32

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit temperature to Celsius"""
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FREEZING_POINT_DIFFERENCE
    celsius = (fahrenheit - FREEZING_POINT_DIFFERENCE) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius temperature to Fahrenheit"""
    global CELSIUS_TO_FAHRENHEIT_FACTOR, FREEZING_POINT_DIFFERENCE
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_DIFFERENCE
    return fahrenheit

def main():
    print("Temperature Conversion Tool")
    print("--------------------------")
    
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        temperature = float(temp_input)
        
        # Get unit input
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        while unit not in ['C', 'F']:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp}°C")
        elif unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
            
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()