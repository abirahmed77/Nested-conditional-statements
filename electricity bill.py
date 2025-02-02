unit = int(input("Enter units of Electricity Consumed : "))

if unit < 50 :
    amount = unit * 2.6
    surcharge = 25

elif unit <= 100 :
    amount = unit * 3.25
    surcharge = 35
    
elif unit <= 200 :
    amount = unit * 5.26
    surcharge = 45
    
else :
    amount = unit * 8.45
    surcharge = 75
    
total = amount + surcharge

print(f"Bill : {amount}")
print(f"Tax : {surcharge}")
print(f"Total : {total}")