import collections 

def queue():
    print("Welcome to Queue ")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Display")
    print("5. Quit")
    
    while True:
        choice = input("\nEnter choice (1/2/3/4/5) or 'q' to quit: ")
        
        if choice.lower() == 'q':
            print("Exiting queue. Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input. Please select a valid operation.")

if __name__ == "__main__":
    queue()