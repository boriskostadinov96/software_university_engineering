width = int(input())
length = int(input())

total_count_pieces = width * length

no_more_pieces = False
input_line = input()
while input_line != "STOP":
    current_pieces = int(input_line)

    total_count_pieces -= current_pieces

    if total_count_pieces <= 0:
        no_more_pieces = True
        break

    input_line = input()

if no_more_pieces:
    print(f"No more cake left! You need {abs(total_count_pieces)} pieces more.")
else:
    print(f"{total_count_pieces} pieces are left.")


# solution 2
# cake_length = int(input())
# cake_width = int(input())
#
# cake_area = cake_width * cake_length
#
# command = input()
# while command != "STOP":
#     pieces = int(command)
#
#     cake_area -= pieces
#
#     if cake_area <= 0:
#         print(f"No more cake left! You need {abs(cake_area)} pieces more.")
#         break
#
#     command = input()
#
# if cake_area > 0:
#     print(f"{cake_area} pieces are left." )