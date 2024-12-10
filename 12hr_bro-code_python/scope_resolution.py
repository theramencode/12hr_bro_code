# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

def func1():
    x = 1
    
    def func2():
        print(x)
    func2()

func1()

x = 3

def func3():
        print(x)

from math import e

def func1():
     print(e)

e = 3

func1()
