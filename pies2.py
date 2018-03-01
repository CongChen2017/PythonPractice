# part 1

print("Welcome to the House of Pies! Here are our pies:")
print("--------------------------------------------------")

pielist = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]
for index, pie in enumerate(pielist):
	print(index+1, pie)

pieorder = []

y = "y"

while y == "y":
	select = input("please choose pie you'd like to order via number ")
	print("Great! We'll have that " + pielist[int(select)-1] + " right out for you.")
	y = input("would you like to make another order? (y)es or (n)o ")
	pieorder.append(pielist[int(select)-1])

print("--------------------------------------------------")
print("you have ordered " + str(len(pieorder)) + " pies!")

#part 2

piedic = {"Pecan": 0, "Apple Crisp": 0, "Bean": 0, "Banoffee": 0, "Black Bun": 0, "Blueberry": 0, "Buko": 0, "Burek": 0, "Tamale": 0, "Steak": 0}


from collections import Counter

c = Counter(pieorder)


for pp in c:
	piedic[pp] = c[pp]

print("--------------------------------------------------")
print("your purchased:")
for pie in piedic:
    print(piedic[pie], pie)
