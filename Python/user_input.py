'''
Name: Bianca Jimenez
github link: https://github.com/bjimenez52/Python/tree/main/Python
'''

total_budget =input("How much is your total budget? $") # (total budget is $7000)
total_budget =float(total_budget)
print(f"total_budget", "$", total_budget)

mortgage = input("How much is your your mortgage? $") # (total mortgage is $1250.50)
mortgage = float(mortgage)
print(f"mortgage", "$", mortgage)

utilities = input("How much are your utilities? $") # (total utilities is $300)
utilities = float(utilities)
print(f"utilities", "$", utilities)

groceries =input("How much are your groceries? $") # (total groceries is $250)
groceries = float(groceries)
print(f"groceries", "$", groceries)

transportation = input("How much is your transportation? $") # (total transportation is $100)
transportation = float(transportation)
print(f"transportation", "$", transportation)

health_care =input("How much is your health care? $") # (total health_care is $60.50)
health_care =float(health_care)
print(f"health_care", "$", health_care)

personal_care = input("How much for your personal care? $") # (total personal_care is $60)
personal_care = float(personal_care)
print(f"person_care", "$", personal_care)

clothing = input("How much for your clothing? $") # (total clothing is $40)
clothing = float(clothing)
print(f"clothing", "$", clothing)

debt =input("How more is your debt? $") # (total debt is $3680)
debt =float(debt)
print(f"debt", "$", debt)

sum = (mortgage + utilities + groceries + transportation + health_care + personal_care +clothing + debt)
print(f"Total amount spent", "$", sum)

percentage = (sum / total_budget) * 100
print(f"{percentage:2.0f} %")