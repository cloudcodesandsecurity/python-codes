import random

Name = input("What is your name?: ")

print("#################################################################")
print(Name + " " + "Welcome!" + " " + "to the Business Name Generator.")
print("#################################################################")

print("Instruction:  You are required to provide 3 names and the nature of business")
print("Type any three names of your choice: ")
a = input("first_name = ")
b = input("second_name = ")
c = input("third_name = ")

Name_list = (a, b, c)

print("#################################################################")
print("Type the nature of the business:\n")
d = input("What is the business line?: ")
print("#################################################################")

full_name = random.choice(Name_list) + "-" + d
print(full_name)


