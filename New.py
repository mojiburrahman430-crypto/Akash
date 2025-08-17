def simple_calculator():
    print("Welcome to Simple Calculator!")
    
    while True:
        # Input numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Input operation
        print("Select operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        
        operation = input("Enter choice (1/2/3/4): ")
        
        # Perform calculation
        if operation == '1':
            result = num1 + num2
            op_symbol = '+'
        elif operation == '2':
            result = num1 - num2
            op_symbol = '-'
        elif operation == '3':
            result = num1 * num2
            op_symbol = '*'
        elif operation == '4':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            result = num1 / num2
            op_symbol = '/'
        else:
            print("Invalid operation choice. Please try again.")
            continue
        
        # Show result
        print(f"{num1} {op_symbol} {num2} = {result}")
        
        # Ask if want to calculate again
        again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thank you for using Simple Calculator. Goodbye!")
            break

if __name__ == "__main__":
    simple_calculator()