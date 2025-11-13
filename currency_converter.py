rates={"USD":1, "INR":82,"EUR":0.93}
amt=float(input("enter amount"))
from_currency = input("enter from").upper()
to_currency = input("enter to").upper()
convert=amt/rates[from_currency]*rates[to_currency]
print(convert)