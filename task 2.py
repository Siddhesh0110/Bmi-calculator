# Function to calculate BMI
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

# Function to determine BMI category
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Main program
def main():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        # Determine BMI category
        category = bmi_category(bmi)
        
        # Display the results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are in the '{category}' category.")
    
    except ValueError:
        print("Please enter valid numbers for weight and height.")

# Run the main program
if __name__ == "__main__":
    main()
