text = input("Your text: ")
# pay attention > f (format string)
print(f"You typed: {text}")
print("You typed: {text}")

# order counts > cough()


def cough():
    print("Cough")


for i in range(3):
    cough()

# say no to write anything after the ?s
# named argument > end
# then use print() to write a new line
for i in range(4):
    print("?", end="")
print()
# same with different syntax
print("?" * 4)

for i in [0, 1, 2]:
    print('!')

for i in range(3):
    print("*")

print("#\n" * 3, end="")

number = int(input("Type a number: "))
if number > 4:
    print("Greater than 4")
elif number < 4:
    print("Smaller than 4")
else:
    print("Equal to 4")

# while True:
#   print("True is true...")

i = 0
while i < 4:
    # print("Lol" + "and I=" + str(i))
    print("Lol", "and I=", i)
    i += 1

# list
listOfNums = [0, 1, 2, 3, 4]
print(listOfNums[:1])
print(listOfNums[:2])
print(listOfNums[2:4])
