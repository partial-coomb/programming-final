# Weight Conversion Program

# Class representing the weight converter
class WeightConverter:
    def __init__(self):
        self.conversions = []  # List to store conversions
        self.measurements = ["ounces", "grams", "pounds", "tons"]  # Valid measurements

    def get_input(self):
        # User input
        weight_str = input("Enter a weight measurement (ounces, grams, pounds, tons): ")
        while weight_str not in self.measurements:
            print("Invalid measurement. Please try again.")
            weight_str = input("Enter a weight measurement (ounces, grams, pounds, tons): ")

        weight_value = float(input("Enter the weight value: "))

        return weight_str, weight_value

    def convert_weight(self, weight_str, weight_value, conversion_str):
        # Convert weight to the chosen measurement
        if weight_str == conversion_str:
            return weight_value
        elif weight_str == "ounces":
            if conversion_str == "grams":
                return weight_value * 28.3495
            elif conversion_str == "pounds":
                return weight_value * 0.0625
            elif conversion_str == "tons":
                return weight_value * 0.00003125
        elif weight_str == "grams":
            if conversion_str == "ounces":
                return weight_value / 28.3495
            elif conversion_str == "pounds":
                return weight_value * 0.00220462
            elif conversion_str == "tons":
                return weight_value * 0.00000110231
        elif weight_str == "pounds":
            if conversion_str == "ounces":
                return weight_value / 0.0625
            elif conversion_str == "grams":
                return weight_value / 0.00220462
            elif conversion_str == "tons":
                return weight_value * 0.0005
        elif weight_str == "tons":
            if conversion_str == "ounces":
                return weight_value / 0.00003125
            elif conversion_str == "grams":
                return weight_value / 0.00000110231
            elif conversion_str == "pounds":
                return weight_value / 0.0005

    def add_conversion(self, weight_value, weight_str, conversion_value, conversion_str):
        # Add the conversion to the list
        self.conversions.append((weight_value, weight_str, conversion_value, conversion_str))

    def display_conversions(self):
        # Display all the conversions
        for conversion in self.conversions:
            weight_value, weight_str, conversion_value, conversion_str = conversion
            print(f"{weight_value} {weight_str} is equal to {conversion_value} {conversion_str}")

# Main program
def main():
    converter = WeightConverter()

    while True:
        weight_str, weight_value = converter.get_input()

        conversion_str = input("Enter the weight measurement to convert to (ounces, grams, pounds, tons): ")
        while conversion_str not in converter.measurements:
            print("Invalid measurement. Please try again.")
            conversion_str = input("Enter the weight measurement to convert to (ounces, grams, pounds, tons): ")

        conversion_value = converter.convert_weight(weight_str, weight_value, conversion_str)
        converter.add_conversion(weight_value, weight_str, conversion_value, conversion_str)

        # Display the conversion
        print(f"{weight_value} {weight_str} is equal to {conversion_value} {conversion_str}")

        choice = input("Do you want to perform another conversion?(yes/no): ")
        if choice.lower() == "no": break

        converter.display_conversions()

main()
