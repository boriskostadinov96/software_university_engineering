messages = int(input())

for _ in range(messages):
    current_number = int(input())

    if current_number == 88:
        print("Hello")

    elif current_number == 86:
        print("How are you?")

    elif current_number != 88 and current_number != 86 and current_number < 88:
        print("GREAT!")

    elif current_number > 88:
        print("Bye.")