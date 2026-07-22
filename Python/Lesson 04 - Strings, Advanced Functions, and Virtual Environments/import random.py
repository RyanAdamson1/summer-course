import random 
with open('input.txt', 'w') as file:
    for i in range(100):
        num = random.randint(50,100)
        file.write(str(num)+ "\n")

text_to_write = [
    "This is a new line of text.\n",
    "Here is another line.\n",
    "And yet another line.\n"
]
with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()
    #lines_stripped=[line.strip for line in lines]
    count = 0
    min = 1000
    max = 0
    sum = 0
    for line in lines:
        amount= int(line)
        sum += amount
        count += 1

        if amount > max:
             max = amount

        if amount < min:
             min = amount
    average = sum/ count

print(f"\n Max:{max}, Min {min}, Average:{average}\n")
        