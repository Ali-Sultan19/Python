INFO = "My name is {0}, I am from {1}, My age is {2}"
name='Ali'
country='Pakistan'
age='22'
print(INFO.format(name,country,age))
print(f"My name is {name}, I am from {country}, My age is {age}")


price = 1000
product = 'Iphone 16'
txt = f"The price of this {product} is {price:.2f} dollars!"
print(txt)
print(txt.format())
print(f"The price of this product is : {price}")