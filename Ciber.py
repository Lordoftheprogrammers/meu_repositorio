# Funções Lambda

ineq= lambda a, b, c: a*b*c
print(ineq(2,3,4))

outra = lambda a=2: print(a)
outra()

ainda_mais_uma = lambda a:print(a)
ainda_mais_uma("jldkjfldskj")

# Variáveis globais

x=300
def fx():
    global x
print(x)

# Tratamento de excepções

try:
    num=12
    num2=num/0
except ZeroDivisionError:
    print("errado")
    pass    

# Exceptions explained by ChatGPT

""" The try statement in Python is typically followed by one or more of the following clauses:

except: This clause specifies the exception(s) that the try block can handle. If an exception occurs within the try block, Python checks if it matches any of the specified exceptions in the except clause. If a match is found, the code inside the except block is executed. The except clause is used for handling exceptions and providing alternative code paths when an exception occurs.

else: This clause is optional and comes after the except clause(s). The code inside the else block is executed if no exceptions occur in the try block. It is typically used to specify code that should run when the try block completes successfully without any exceptions. The else clause is useful for separating the normal code flow from the exception handling code.

finally: This clause is optional and comes after the except and else clauses. The code inside the finally block is always executed, regardless of whether an exception occurred or not. It is commonly used to define cleanup code that must be executed, such as closing files or releasing resources. The finally clause ensures that this cleanup code is executed, even if an exception is raised and not caught. """

try:
    # Code that may raise an exception
    result = 10 / 0  # Division by zero to raise an exception
except ZeroDivisionError:
    # Exception handling code for ZeroDivisionError
    print("Error: Division by zero")
else:
    # Code to run if no exceptions occur
    print("No exceptions occurred")
finally:
    # Cleanup code that always runs
    print("Cleanup code")

# Como fazer um GET no Python

import requests
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x.text)