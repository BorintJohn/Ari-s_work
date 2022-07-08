import math
'''
import means to pull certain data, code, blablabla from system or even out of system,
// which means u need to download file from somewhere else, u will learn in the future.//

you can search up online for things you need, for this, search on google : how do I get pi in python
and u will learn, take u 1 minute.  
'''

def BMI():
    W = float(input("Input Weight:"))
    '''
    W is a name, does't affect anything, just a name, it could be Weight, wei, we, as long as it's easy for you to read, use it. 
    float() means float data // like Ex: 0.0, 0.1, 1.2, there are more choice like int() means integer // Ex: 1,5,100,8544 // somemore, but I don't think u need it for now. 
    input() means blank for user to input, "" means text that you wanna show to ur user. 
    '''
    H = float(input("Input Height:"))
    B_M_I = W/(H/H)
    '''
    B_M_I is just a name, normally if you have a huge name but you wanna show them all, 
    for ex: Answer to the test, if you type it directly, system going to recognize as answer, to, the, test // four different name//
    to make it work, u can use _, so the name could be answer_to_the_test, the system going to recognize as one name, cuz there's no space between it. It's useful for working in a team.

    and then W/(H/H)
    W means Weight, which is string to line 1, u can see the name tag.
    / means divided, more // * means times, - means minus, + means plus.
    () means this two are together, I don't think I need to explain much more about it. 
    '''
    print (B_M_I)
    # ur teacher should teach u about print, if he didn't, u should report him.
"""
def bla(): means this is a definition or function called bla or whatever u wanna call it. 
and when u wanna call this function, use // bla() //
"""

def ATN():
    FirstNumber = float(input("Input First Number: "))
    SecondNumber = float(input("Input Second Number: "))
    ThirdNumber = float(input("Input Third Number: "))
    average = (FirstNumber*SecondNumber*ThirdNumber)/3
    print(average)
def COC():
    radius = float(input("input radius: "))
    circumference = 2 * math.pi * radius
    print(circumference)
def AOC():
    radius = float(input("input radius: "))
    area = (radius * radius) * math.pi
    print(area)
Choice = int(input("Choose what u wanna do \n (1)BMI counter \n (2)three number averager \n (3)circumference counter \n (4)circle area counter"))
# int() means this value is integer only.
if Choice == 1:
    BMI()
elif Choice == 2:
    ATN()
elif Choice == 3:
    COC()
elif Choice == 4:
    AOC()
else:
    print("Invalid number")
'''
if blablabla: means if this happen, run this. 
elif blablabla: means if above lines doesn't run and this happen, run this. 
else: means if all above //if, elif// doesn't run, run this.

bla == bla means if something equals something

so translate to human language, it means
if Choice == 1:
    BMI()
If Choice equal to 1, run BMI. 


tip: elif could be as much as you want. even 100, 999, doesn't matter. 
  
'''
