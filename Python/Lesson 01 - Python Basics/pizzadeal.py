user_pizza1 = float(input ("what pizza diameter do you want for the first pizza? (use numbers) "))
user_price1 = float(input ("What price is the first pizza? "))

user_pizza2 = float(input ("what pizza diameter do you want for the second pizza? (use numbers) "))
user_price2 = float(input ("What price is the first pizza? "))


calc_pizza_area1 = (3.14159 * (user_pizza1 /2) ** 2)
calc_pizza_area2 = (3.14159 * (user_pizza2 /2) ** 2)

print (f"calculated price per area for pizza 1 is ${calc_pizza_area1 / user_price1: .02f} per sq in")
print (f"calculated price per area for pizza 2 is ${calc_pizza_area2 / user_price2: .02f} per sq in")
 
if calc_pizza_area2 / user_price2 > calc_pizza_area1 / user_price1 :
    print("Pizza 2 is a better deal than pizza 1")
if calc_pizza_area2 / user_price2 < calc_pizza_area1 / user_price1 :
    print("Pizza 1 is a better deal than pizza 2")
if calc_pizza_area2 / user_price2 == calc_pizza_area1 / user_price1 :
    print("both pizzas are the same value")