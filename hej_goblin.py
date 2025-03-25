def say_hi():
    print("Good to meet ya!")

def main():
    user_input = input("Hi!\nReply: ")
    if user_input.lower() == 'hi':
        say_hi()
    else:
        print("You didn't type 'hi'.")

if __name__ == "__main__":
    main()
