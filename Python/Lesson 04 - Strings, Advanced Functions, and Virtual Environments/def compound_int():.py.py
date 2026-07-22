# def compound_int(P:float, r:float, t:int, n:int = 1) ->float: 
#     P = float(input("what is your principal: "))
#     r = float(input("what is annual interest rate: "))
#     n = float(input('What is the compound rate (times per year): '))
#     t = int(input("what is the total years borrowed?: "))
#     A = (P * (1+ r / n) ** (n * t), 2 )
#     return A

# result = compound_int()
# print (f"final amount is {result}")

def compound_int(P:float, r:float, t:int, n:int = 1) ->float:
    P = float(input("What is your principal: "))
    r = float(input("What is annual interest rate: "))
    n = float(input("What is the compound rate (times per year): "))
    t = int(input("What is the total years borrowed?: "))
    A = round(P * (1 + r / n) ** (n * t), 2)
    return A

result = compound_int()
print(f"Final amount: {result}")