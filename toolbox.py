def greet(person):
    if person == "":
        print("You did not enter a name.")
    elif person == "Tim":
        print("Welcome back, Tim!")   
    elif person == "Anja":
        print("Welcome back, Anja!")
    else:
        print(f"Hello, {person}! Welcome to the DevOps Toolkit!")

def get_name():
   while True:
        name = input("Please enter your name: ")

        if name != "":
            return name
        
        print("Please enter a name.")
        

def welcome():
    print("Welcome to the DevOps Toolkit!")

def main():
    welcome()
    greet(get_name())

if __name__ == "__main__":
    main()