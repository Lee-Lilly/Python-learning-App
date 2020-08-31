# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 08:10:02 2020

@author: chang
"""
from operator import itemgetter

# Title
title = "Nutrition App"
print(title)

# List of food categories
categories =["Fruit", "Diary", "Vegetable", "Meat", "Fish", 
             "Egg", "Fat-Oil", "Beverage", "Cereals", "Sweets",
             "Potatoes", "Alcohol"]

# Initialize an empty food bank list
food_bank =[] 
      
# Intit a food_item as dictionary
food_item = {'name': 'Whole egg', 
             'category': 'Egg',                      
            'Energy(kcal)': 118,
            'Fat(g)': 8.1,
            'Carbonhydrate(g)': 0.3,        
            'Protein(g)': 11.1 ,
            'Salt(mg)': 247.6,
            }
# Add the food_item to food_bank
food_bank.append(food_item)

# Function to construct "Food" from user input data       
def input_data():
    #init a dictionary
    food_data ={} 
    
    food_data['name'] = input("Enter a new food name: ")
    
    print("\nFollow the category list:")    
    print(sorted(categories))
    
    food_data['category'] = input("Choose a category: ")
    
    print("\nFollow the steps to complete nutrition details, if no value put 0.")
    
    food_data['Energy(kcal)'] = float(input("Enter energy(kcal/100g): "))
    
    food_data['Fat(g)'] = float(input("Enter fat(g/100g): "))
    
    food_data['Carbonhydrate(g)'] = float(input("Enter carbonhydrate(g/100g): "))
    
    food_data['Protein(g)'] = float(input("Enter protein(g/100g): "))
    
    food_data['Salt(mg)'] = float(input("Enter salt(mg/100g): "))   
    
    return food_data

# Add the user input food item to the food bank
food_item = input_data()
food_bank.append(food_item)

# Inform the user
print('\nThanks! ' + food_item['name'] + ' is registered!')

# Print key, value pairs nested in the food bank list by looping through dictionary
def print_foodlist():
    print("\n The Food Bank List:\n")
    for food in food_bank:
        for k, v in food.items():
            print(k + ": " + str(v))
        print("\n") 
  
print_foodlist()      

# Sort the list by comparators, such as 'name', 'energy', etc.
print("Sort Food bank by comparators, such as 'name', 'energy', etc.")

# Sort list of dictionary using itemgetter from operator module
print("\nSorted by name")
food_bank.sort(key= itemgetter('name'))
for food in food_bank: 
    print('name: '+ food.get('name')) #accessing certain value using get()

print("\n Sorted by category")
food_bank.sort(key= itemgetter('category'))
for food in food_bank:
    print(('name: '+ food.get('name'), 'category: ' + food.get('category'))) # print out as tuples
    
print("\n Sorted by energy - decending")
food_bank.sort(key= itemgetter('Energy(kcal)'),  reverse = True)
for food in food_bank:
    print(('name: '+ food.get('name'), 'Energy(kcal): ' + str(food.get('Energy(kcal)'))))
    
print("\n Sorted by fat - accending")
food_bank.sort(key= itemgetter('Fat(g)'))
for food in food_bank:
    print(('name: '+ food.get('name'), 'Fat(g): ' + str(food.get('Fat(g)'))))

print("\n Sorted by carbonhydrate - decending")
food_bank.sort(key= itemgetter('Carbonhydrate(g)'), reverse = True)
for food in food_bank:
    print(('name: '+ food.get('name'), 'Carbonhydrate(g): ' + str(food.get('Carbonhydrate(g)'))))


print("\n Sorted by protein - decending")
food_bank.sort(key= itemgetter('Protein(g)'), reverse = True)
for food in food_bank:
    print(('name: '+ food.get('name'), 'Protein(g): ' + str(food.get('Protein(g)'))))

print("\n Sorted by salt - accending")
food_bank.sort(key= itemgetter('Salt(mg)'))
for food in food_bank:
    print(('name: '+ food.get('name'), 'Salt(mg): ' + str(food.get('Salt(mg)'))))


# List comprehension to generate value lists 
fat_index = [food['Fat(g)'] for food in food_bank]
energy_index = [food['Energy(kcal)'] for food in food_bank] 
 
# Simple Statistic  
print("\n Some simple Statistics")

least_fat = min(fat_index) 
most_energy = max(energy_index)
print("\nMinimum fat(g/100g): " + str(least_fat) + "; " + "Maxmum energy(kcal/100g): " + str(most_energy) )

total_fat = sum(fat_index) 
total_energy = sum(energy_index)
print("\nTotal fat(g/100g) " + str(total_fat) + "; " + "Total energy(kcal/100g): " + str(total_energy))
