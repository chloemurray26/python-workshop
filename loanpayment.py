#details of loan

moneyowed = input("How much money do you get with this loan? ")
percentrate = input("What percentage of the do you owe?")
paymentmade = input("How much do you owe now?")
month = input("How long do you have to pay this loan?")

monthlyrate = percentrate/100/12

for i in range(month):

#calculate interest
    interestpay = moneyowed + monthlyrate
    moneyowed = interestpay + moneyowed
if moneyowed - paymentmade < 0:
    print(moneyowed)