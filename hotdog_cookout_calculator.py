# Michael Perez
# 11/23/2022
# COP1047C
# Project 2

# 8. Hot Dog Cookout Calculator
# 
# Assume hot dogs come in packages of 10, and hot dog 
# buns come in packages of 8. Write a program that 
# calculates the number of packages of hot dogs and 
# the number of packages of hot dog buns needed for a 
# cookout, with the minimum amount of leftovers. The 
# program should ask the user for the number of people 
# attending the cookout and the number of hot dogs each 
# person will be given. The program should display the 
# following details:
# 
# • The minimum number of packages of hot dogs required
# • The minimum number of packages of hot dog buns required
# • The number of hot dogs that will be left over
# • The number of hot dog buns that will be left over
############

people = int(input("Enter number of people: "))
number_of_hotdogs_per_person = int(input("Enter number of hot dogs: "))

hotdogs_per_package = 10
buns_per_package = 8

total_hotdogs = people * number_of_hotdogs_per_person

number_of_hotdog_packages_needed = total_hotdogs // hotdogs_per_package
number_of_hotdog_bun_packages_needed = total_hotdogs // buns_per_package

if (total_hotdogs % buns_per_package):
    number_of_hotdog_bun_packages_needed += 1
    
if (total_hotdogs % hotdogs_per_package):
    number_of_hotdog_packages_needed += 1

total_buns = number_of_hotdog_bun_packages_needed * buns_per_package

hotdogs_leftover = total_hotdogs % hotdogs_per_package
buns_leftover = total_buns - total_hotdogs

print("Minimum number of packages of hot dogs required =", number_of_hotdog_packages_needed)
print("Minimum number of packages of hot dog buns required =", number_of_hotdog_bun_packages_needed)
print("Number of hot dogs left over =", hotdogs_leftover)
print("Number of hot dogs buns left over =", buns_leftover)