W = float(input("Input Weight:"))
'''
W is a name, does't affect anything, just a name, it could be Weight, wei, we, as long as it's easy for you to read, use it. 
float() means float data // like Ex: 0.0, 0.1, 1.2, there are more choice like int() means integer // Ex: 1,5,100,8544 // somemore, but I don't think u need it for now. 
input() means blank for user to input, "" means text that you wanna show to ur user. 
'''
H = float(input("Input Height:"))
# same as line 1
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
print(B_M_I)
# ur teacher should teach u about print, if he didn't, u should report him.