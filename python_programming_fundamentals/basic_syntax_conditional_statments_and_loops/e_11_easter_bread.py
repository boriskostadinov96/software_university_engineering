budget = float(input())
flour_price = float(input())
number_of_loaves = 0
colored_eggs = 0

eggs_price = flour_price * 0.75
milk_price = flour_price * 1.25 / 4

loaves = flour_price + eggs_price + milk_price

while budget >= loaves:

    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

    budget -= loaves

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")

