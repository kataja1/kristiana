import random

computer_number = random.randint(1, 100)

attempts = 0

print("Uzmini skaitli no 1 līdz 100")


while True:
    user_guess = int(input("Tavs minējums: "))
    attempts += 1

    if user_guess < computer_number:
        print("Lielāks")
    elif user_guess > computer_number:
        print("Mazāks")
    else:
        print("Uzminēts! Skaitlis bija .")
        print("Minēšanas reižu skaits")
        break
    

