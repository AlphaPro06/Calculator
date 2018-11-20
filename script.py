Cal_1 = raw_input("Please input first value")
Cal_2 = raw_input("Please input second value")

Cal_Function = raw_input("Do what to = 1. Multiply 2. Divide 3. Add 4. Subtract ?")

if Cal_Function == 1:
    Multi = Multiply(Cal_1, Cal_2)
    print Multi
if Cal_Function == 2:
    Div = Divide(Cal_1, Cal_2)
    print Div
if Cal_Function == 3:
    Ad = Add(Cal_1, Cal_2)
    print Ad
if Cal_Function == 4:
    Sub = Subtract(Cal_1, Cal_2)
    print Sub

def Multiply (Cal_1, Cal_2):
    Ans = Cal_1 * Cal_2
    return Ans
def Divide (Cal_1, Cal_2):
    Ans = Cal_1 / Cal_2
    return Ans
def Add (Cal_1, Cal_2):
    Ans = Cal_1 + Cal_2
    return Ans
def Subtract (Cal_1, Cal_2):
    Ans = Cal_1 - Cal_2
    return Ans

