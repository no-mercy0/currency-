#CURRENCY CONVENTER
currencies = {
    "SOM":"(Kyrgyz Som)",
    "RUB":"(Russian Ruble)",
    "USD":"(US Dollar)",
    "EUR":"(Euro)",
    "GBP":"(Great Britain Pound)"
}

def som_to_dollar():
    value = input("How many do you want to convert? ")
    ammount = float(value)
    conv = ammount * 0.012
    print(conv)
    
def dollar_to_som():
    value = input("How many do you want to convert? ")
    ammount = float(value)
    conv = ammount * 84.78
    print(conv)

def som_to_euro():
    value = input("How many do you want to convert? ")
    ammount = float(value)
    conv = ammount * 0.010
    print(conv)

def euro_to_som():
    value = input("How many do you want to convert? ")
    ammount = float(value)
    conv = ammount * 97.05
    print(conv)

def som_to_rub():
    value = input("How many do you want to convert? ")
    ammount = float(value)
    conv = ammount * 0.86
    print(conv)

def rub_to_som():
    value = input("How many do you want to convert? ")
    ammount = float(value)
    conv = ammount * 1.17
    print(conv)

def som_to_pound():
    value = input("How many do you want to convert? ")
    ammount = float(value)
    conv = ammount * 0.0085
    print(conv)

def pound_to_som():
    value = input("How many do you want to convert? ")
    ammount = float(value)
    conv = ammount * 114.11
    print(conv)

print("WELCOME TO THE CURRENCY CONVERTER!")
print("Please choose your currency: ")
for x in currencies:
    print(x + " " + currencies[x])
con = input("Convert: ")
to = input("To: ")

if con == "SOM" and to == "USD":
    lambda x: som_to_dollar(x)
    som_to_dollar()
    print("Thanks for using our program! See you later")
elif con == "USD" and to == "SOM":
    lambda x:dollar_to_som(x)
    dollar_to_som()
    print("Thanks for using our program! See you later")
elif con == "SOM" and to == "EUR":
    lambda x:som_to_euro(x)
    som_to_euro()
    print("Thanks for using our program! See you later")
elif con == "EUR" and to == "SOM":
    lambda x:euro_to_som(x)
    euro_to_som()
    print("Thanks for using our program! See you later")
elif con == "SOM" and to == "RUB":
    lambda x:som_to_rub(x)
    som_to_rub()
    print("Thanks for using our program! See you later")
elif con == "RUB" and to == "SOM":
    lambda x:rub_to_som(x)
    rub_to_som()
    print("Thanks for using our program! See you later")
elif con == "SOM" and to == "GBP":
    lambda x:som_to_pound(x)
    som_to_pound()
    print("Thanks for using our program! See you later")
elif con == "GBP" and to == "SOM":
    lambda x:pound_to_som(x)
    pound_to_som()
    print("Thanks for using our program! See you later")
else:
    print("Not found.")
SOM = 1
RUB = SOM * 1.17
USD = SOM * 84.78
EUR = SOM * 97.05
GBP = SOM * 114.11