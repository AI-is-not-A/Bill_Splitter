import random

num_people = int(input("Enter the number of friends joining (including you):"))
if num_people <= 0:
    print("No one is joining for the party")
    exit()

people = {}
for _ in range(0, num_people):
    people[input()] = 0

total_bill = int(input("Enter the total bill value:"))
answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:')

if answer == "Yes":
    winner = random.choice(list(people.keys()))
    people[winner] = 0
    split_value = total_bill / (num_people - 1)
    if split_value % 1 == 0:
        split_value = int(split_value)
    for key in people.keys():
        if key != winner:
            people[key] = split_value
    print(f"{winner} is the lucky one!")
    print(people)
elif answer == "No":
    print("No one is going to be lucky")
    split_value = round(total_bill / num_people, 2)
    for key in people.keys():
        people[key] = split_value
    print(people)
else:
    print("Please, write Yes or No:")