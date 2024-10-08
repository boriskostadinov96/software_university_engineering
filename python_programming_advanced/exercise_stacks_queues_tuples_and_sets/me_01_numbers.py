first_set = set([int(x) for x in input().split()])
second_set = set([int(x) for x in input().split()])
n = int(input())

for _ in range(n):
    first_command, second_command, *data = input().split()
    current_command = first_command + " " + second_command

    if current_command == "Add First":
        [first_set.add(int(el)) for el in data]

    elif current_command == "Add Second":
        [second_set.add(int(el)) for el in data]

    elif current_command == "Remove First":
        [first_set.discard(int(el)) for el in data]

    elif current_command == "Remove Second":
        [second_set.discard(int(el)) for el in data]

    else:
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")

# solution 2
# first_set = set(int(x) for x in input().split())
# second_set = set(int(x) for x in input().split())
#
# functions = {
#     "Add First": lambda x: [first_set.add(int(el)) for el in x],  # first_set.update(second_set)
#     "Add Second": lambda x: [second_set.add(int(el)) for el in x],
#     "Remove First": lambda x: [first_set.discard(int(el)) for el in x],
#     "Remove Second": lambda x: [second_set.discard(int(el)) for el in x],
#     "Check Subset": lambda x: print(first_set.issubset(second_set) or second_set.issubset(first_set)),
# }
#
# for _ in range(int(input())):
#     first_command, second_command, *data = input().split()
#
#     command = first_command + " " + second_command
#
#     functions[command](data)
#
# print(*sorted(first_set), sep=", ")
# print(*sorted(second_set), sep=", ")