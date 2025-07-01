#functions

def greet(name):
    print(f"Hello,{name}")
greet('Nox')    

def add(a,b):
    return a + b
result = add(7,3)
print(result)
    
def greet(name , greeting='hello'):
    print(f"{greeting}", name)  
greet('Nox','Good Evening')