class Currency(object):
    def _init_(self, country, value):
        self.country = country
        self.value = float(value)
def from_som(self, soms):

    return self.value * int(soms)

def to_som(self, soms):

    return int(soms) / self.value
again = True

while again:
    country = input('What country are you going to? ')
    value = float(input('How many soms are equal to 1 currency from their country?  '))

    foreign_country = Currency(country, value)

    convert = input('What would you like to convert? 1. To SOM 2. To %s money' % country)
    soms = input('How many soms would you like to convert?n')

    if( convert == '1' ):
        print (soms + ' ' + country + ' money are worth ' + str(foreign_country.to_som(soms)) + ' Kyrgyz soms')
    elif( convert == '2' ):
    	print (soms + ' soms are worth ' + str(foreign_country.from_som(soms)) + soms + ' ' + country)

    again = input('Want to go again? (Y/N)')

    if( again == 'y' or again == 'Y' ):
        again = True
    elif( again == 'n' or again == 'N' ):
        again = False
        
        
def bubbleSort(mon):
    
  for i in range(len(mon)):

    for j in range(0, len(mon) - i - 1):

      if mon[j] > mon[j + 1]:

        temp = mon[j]
        mon[j] = mon[j+1]
        mon[j+1] = temp


cur = [1, 84, 96, 94, 2]

bubbleSort(cur)

print('Currencies in ascending order compared to som:')
print(cur)

euro = 94.3
dollar = 84.4
ruble = 1.1
som = 1

get_min = lambda euro, dollar : min(eurp, dollar) 
print(get_min()) 

get_max = lambda ruble, som : max(ruble,som) 
print(get_max()) 

class India():
	def capital(self):
		print("New Delhi")

	def language(self):
		print("Hindi and English")

class USA():
	def capital(self):
		print("Washington, D.C.")

	def language(self):
		print("English")


obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
country.capital()
country.language()