#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator.\n")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
split_by = int(input("How many people to split the bill?"))
tip_percent = tip / 100
total_tip = tip_percent * bill
total_bill = bill + total_tip
bill_per_person = total_bill / split_by
final = round(bill_per_person,2)
final = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final}")
