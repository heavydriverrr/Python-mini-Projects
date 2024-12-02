bill = int(input("Enter bill amount : $"))
tip_per = int(input("enter the percentage of tip you wanna give (0, 5, 10, 20), %"))

total_bill = int(bill * (tip_per/100)) + bill
divd_bill = int(input("In how many people you want to split BILL : "))

final_pay = total_bill/divd_bill
print(f"Each person have to pay(total {divd_bill} persons) : ${final_pay}")
