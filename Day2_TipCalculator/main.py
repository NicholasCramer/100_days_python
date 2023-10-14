

print("Welcome to the tip calculator. ")
total = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

def calculate_tip(total, percentage, num_people):
    percentage_float = int(percentage) / 100
    tip_total = percentage_float * total
    total_bill = total + tip_total
    total_per_person = round(total_bill / num_people, 2)
    final_total_per_person = "{:.2f}".format(total_per_person)

    return final_total_per_person


amount = calculate_tip(total, percentage, num_people)
print(f"Each person should pay: ${amount}")

