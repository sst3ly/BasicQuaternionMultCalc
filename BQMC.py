#BASIC QUATERNION (EXPRESSION(coming soon)) CALCULATOR

#note: Q stands for quaternion(s) in this file

def calcQm(a, b):#calculates the Q. Just a ton of if statements
    if(a == "1"):
        if(b == "1"):return "1"
        if(b == "i"):return "i"
        if(b == "j"):return "j"
        if(b == "k"):return "k"
    if(a == "i"):
        if(b == "1"):return "i"
        if(b == "i"):return "-1"
        if(b == "j"):return "-k"
        if(b == "k"):return "j"
    if(a == "j"):
        if(b == "1"):return "j"
        if(b == "i"):return "k"
        if(b == "j"):return "-1"
        if(b == "k"):return "-i"
    if(a == "k"):
        if(b == "1"):return "k"
        if(b == "i"):return "-j"
        if(b == "j"):return "i"
        if(b == "k"):return "-1"

inptd = input("Please enter two basic quaternions seperated by a comma: ")#input
firstUnit = ""#the first thing to multiply
secondUnit = ""#the second thing to multiply
fsuSwitch = False#used to toggle which unit is being made(line 41-42)
for c in inptd:
    if(c != " " and c != "i" and c != "j" and c != "k" and c != "," and c !="1" and c != "-"):#checks to see if the current char isn't a Q
        raise KeyboardInterrupt(f"The statement has {c}, which is not a basic quaternion.")#if so, returns an error
    else:#otherwise it will continue
        if(c == " "): pass#doesn't care about spaces
        if(c == "i" or c == "j" or c == "k" or c == "-"):#if its anything that can be used for the Q calc, then
            if(fsuSwitch == False):#add it to the 1st/2nd unit depending on the fsuSwitch
                firstUnit += c
            elif(fsuSwitch == True):
                secondUnit += c
        if(c == ","):#if its a comma, then change the fsuSwitch to True instead of False
            fsuSwitch = True      

print(calcQm(firstUnit, secondUnit))#print out the calc's answer to multiplying the two units


