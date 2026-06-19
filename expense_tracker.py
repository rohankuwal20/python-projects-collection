income = float(input("enter your income :"))
expense = float(input("enter your expense :"))
remaining_balance = income - expense
print(f"your income is : {income}rs")
print(f"your expense is : {expense}rs")
print(f"your remaining Balance is : {remaining_balance}rs")
if remaining_balance < 0 :
    print("Warning: you are in debt !")
else :
    savings = remaining_balance*0.2
    print(f"suggested savings : {savings}rs")