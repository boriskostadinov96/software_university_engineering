number_of_lines = int(input())
counter = 0
for brackets in range(number_of_lines):
    current_command = input()
    if "(" in current_command:
        counter += 1
    elif ")" in current_command:
        counter -= 1

    if counter != 0 and counter != 1:
        print("UNBALANCED")
        break
else:
    print("BALANCED")