#importing math library
import math

#constant calc definition
calc = True

#function to get number one
def x ():
    while True:
        x = input ("x is? Leave empty if not relevant")
        if x == "":
            break
        else:
            try:
                x = int(x)
            except:
                print ("Not a number!")
            else:
                return x
                break

#function to get numbertwo
def y ():
    while True:
        y = input ("Y is? Leave empty if not relevant")
        if y == "":
            break
        else:
            try:
                y = int(y)
            except:
                print ("Not a number!")
            else:
                return y
                break

#function to get operator
def operator ():            
    while True:
        operator = input ("+ for x+y,- for x-y,* for x*y,/ for x/y,/2 for square root,\n1/ for 1/x,*2 for x*x,% for x/100,*3 for x*x*x,/3 for cubic_root,\n** for power,// for root,10* for 10 power x,2* for 2 power x,p for pi,\n| for absolute,! for factorial,10 for logx10,le for logex,l for logxy,\ne for e,e* for e power x,m for mod,s for sinus x,c for cosinus x,\nt for tangens x,r for rds to dgr,d for dgr to rds\n")
        if operator [0] in ("+","-","*","/","/2","1/","*2","%","*3","/3","**","//","10*","2*","p","|","!","10","le","l","e","e*","m","s","c","t","r","d"):
            return operator
        else:
            print ("Wrong operator!")
        
#continueance function
def reply_if_continue ():
    while True:
        reply = input ("Do you want to continue? Y/N")
        if reply.lower() [0] == "y":
            reply = input ("Do you want to use previous result? Y/N")
            if reply.lower() [0] == "y":
                return "yy"
            else:
                return "yn"
        elif reply.lower() [0] == "n":
            break
        else:
            print ("Wrong input!")
        
#function to trigger math function
def calculation (a,b,c):
    if c == "+":
        d = Calculator(a,b)
        e = d.plus ()
        return e
    elif c == "-":
        d = Calculator(a,b)
        e = d.minus ()
        return e
    elif c == "*":
        d = Calculator(a,b)
        e = d.multiply ()
        return e
    elif c == "/":
        d = Calculator(a,b)
        e = d.divide ()
        return e
    elif c == "/2":
        d = Calculator(a,b)
        e = d.square_root ()
        return e
    elif c == "1/":
        d = Calculator(a,b)
        e = d.inverte ()
        return e
    elif c == "*2":
        d = Calculator(a,b)
        e = d.square ()
        return e
    elif c == "%":
        d = Calculator(a,b)
        e = d.percentage ()
        return e
    elif c == "*3":
        d = Calculator(a,b)
        e = d.cube ()
        return e
    elif c == "/3":
        d = Calculator(a,b)
        e = d.cube_root ()
        return e
    elif c == "**":
        d = Calculator(a,b)
        e = d.power ()
        return e
    elif c == "//":
        d = Calculator(a,b)
        e = d.root ()
        return e
    elif c == "10*":
        d = Calculator(a,b)
        e = d.ten_on ()
        return e
    elif c == "2*":
        d = Calculator(a,b)
        e = d.two_on ()
        return e
    elif c == "p":
        d = Calculator(a,b)
        e = d.pi ()
        return e
    elif c == "|":
        d = Calculator(a,b)
        e = d.absolute_value ()
        return e
    elif c == "!":
        d = Calculator(a,b)
        e = d.factorial ()
        return e
    elif c == "10":
        d = Calculator(a,b)
        e = d.declogarithm  ()
        return e
    elif c == "le":
        d = Calculator(a,b)
        e = d.natural_logarithm ()
        return e
    elif c == "l":
        d = Calculator(a,b)
        e = d.logarithm ()
        return e
    elif c == "e":
        d = Calculator(a,b)
        e = d.e ()
        return e
    elif c == "e*":
        d = Calculator(a,b)
        e = d.esquare ()
        return e
    elif c == "m":
        d = Calculator(a,b)
        e = d.mod ()
        return e
    elif c == "s":
        d = Calculator(a,b)
        e = d.sinus ()
        return e
    elif c == "c":
        d = Calculator(a,b)
        e = d.cosinus ()
        return e
    elif c == "t":
        d = Calculator(a,b)
        e = d.tangent  ()
        return e
    elif c == "r":
        d = Calculator(a,b)
        e = d.radians_to_degrees ()
        return e
    elif c == "d":
        d = Calculator(a,b)
        e = d.degress_to_radians ()
        return e
    
#class for calculator functions
class Calculator ():
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    
    def plus (self):
        z = self.x + self.y
        return z
    
    def minus (self):
        z = self.x - self.y
        return z
    
    def multiply (self):
        z = self.x * self.y
        return z
    
    def divide (self):
        if self.y == 0:
            z = "DIV0 error!"
        else:
            z = self.x / self.y
        return z
    
    def square_root (self):
        z = self.x**(1/2)
        return z
    
    def inverte (self):
        if self.x == 0:
            z = "DIV0 error!"
        else:
            z = 1 / self.x
        return z
    
    def square (self):
        z = self.x**2
        return z
        
    def percentage (self):
        z = self.x/100
        return z  
    
    def cube (self):
        z = self.x**3
        return z 
    
    def cube_root (self):
        z = self.x**(1/3)
        return z 
    
    def power (self):
        z = self.x**self.y
        return z
    
    def root (self):
        if self.y == 0:
            z = "DIV0 error!"
        else:
            z = self.x**(1/self.y)
        return z
    
    def ten_on (self):
        z = 10**self.x
        return z
    
    def two_on (self):
        z = 2**self.x
        return z
    
    def pi (self):
        z = math.pi
        return z
            
    def absolute_value (self):
        if self.x > -1:
            z = self.x
        else:
            z = self.x * -1
        return z
    
    def factorial (self):
        i = 0
        z = 1
        for i in range(1,self.x+1):
            z = i*z
            i = i+1
        return z
    
    def declogarithm (self):
        z = math.log10 (self.x)
        return z
    
    def natural_logarithm (self):
        z = math.log(self.x)
        return z
    
    def logarithm (self):
        z = math.log(self.x,self.y)
        return z
    
    def e (self):
        z = math.e
        return z
    
    def esquare (self):
        z = math.exp (self.x)
        return z
    
    def mod (self):
        z = math.modf (self.x)
        return z
    
    def sinus (self):
        z = math.sin (self.x)
        return z
    
    def cosinus (self):
        z = math.cos (self.x)
        return z
    
    def tangent (self):
        z = math.tan (self.x)
        return z
    
    def radians_to_degrees (self):
        z = math.degrees (self.x)
        return z
    
    def degress_to_radians (self):
        z = math.radians (self.x)
        return z

while True:

    try:
        number1 = old_result
    except:
        number1 = x ()
        
    operation = operator ()
    
    if operation in ("/2","1/","*2","%","*3","/3","10*","2*","p","|","!","10","le","e","e*","m","s","c","t","r","d"):
        number2 = ""
    else:
        number2 = y ()
    
    result = calculation (number1,number2,operation)
    
    print (result)
    
    continuance = reply_if_continue ()
    
    if continuance == "yy":
        old_result = result
        continue
    elif continuance == "yn":
        del old_result
        continue
    else:
        try:
            del old_result
            break
        except:
            break