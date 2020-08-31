# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 17:29:07 2020

@author: chang
"""

# Title
title = "Nutrition App"
print(title)

# List of food categories
categories =["Fruit", "Diary", "Vegetable", "Meat", "Fish", "Egg", "Fat-Oil", "Beverage"]

# Add more category to the list
categories.append('Cereals')
categories.append('Sugar&Confectionary')
categories.append('Potatoes')
categories.append('Alcohol')

# Initialize an empty food bank list
food_bank =[] 

# Declare class Food contructed with named parameters
class Food:
    def __init__(self, name, category, nutrition):
        self.name = name
        self.category = category
        self.nutrition = nutrition
        
    # Define toString() printing format
    def __repr__(self):
        return "\nname: {},\ncategory: {},\nnutrition:\n{}".format(self.name, self.category, self.nutrition)

# Define a food item of "Food" class
food_item = Food('Whole egg', 'Egg', 
                     {
                        'Energy(kcal)': 118,
                        'Fat(g)': 8.1,
                        'Carbonhydrate(g)': 0.3,        
                        'Protein(g)': 11.1 ,
                        'Salt(mg)': 247.6,
                    })
# Add the food_item to food_bank
food_bank.append(food_item)

# Print food_bank list
print("\nFood Bank List: ")
print(food_bank)

# Function to get food data from user input         
def input_data():
    name = input("Enter a new food name: ")
    print("\nFollow the category list:")
    
    print(sorted(categories))
    category = input("Choose a category: ")
    
    nutrition = {}
    print("\nFollow the steps to complete nutrition details, if no value put 0")
    
    key = 'Energy(kcal)'
    value = float(input("Enter energy(kcal/100g): "))
    nutrition.update({key: value})
    
    key = 'Fat(g)'
    value = float(input("Enter fat(g/100g): "))
    nutrition.update({key: value})
    
    key = 'Carbonhydrate(g)'
    value = float(input("Enter carbonhydrate(g/100g): "))
    nutrition.update({key: value})
    
    key = 'Protein(g)'
    value = float(input("Enter protein(g/100g): "))
    nutrition.update({key: value})
    
    
    key = 'Salt(mg)'
    value = float(input("Enter salt(g/100g): "))
    nutrition.update({key: value})
    
    # Call "Food" constructor with user input as parameters  
    food_data = Food(name, category, nutrition)
    
    return food_data

# Add the user input food item to the food bank
food_item = input_data()
food_bank.append(food_item)

# Inform the user
print('\nThanks! ' + food_item.name + ' is registered!\n')

# Print items in the food bank list in the format of Class Food
print("Food Bank List:")
for food in food_bank:
    print(food)
    

# fat_index = []
# energy_index =[]
    
# Loop through "food_bank to extract nutrition values to generate value lists
# for food in food_bank:
#     fat_index.append(food.nutrition['Fat(g)'])
#     energy_index.append(food.nutrition['Energy(kcal)'])

# List comprehension to generate value lists 
fat_index = [food.nutrition['Fat(g)'] for food in food_bank]
energy_index = [food.nutrition['Energy(kcal)'] for food in food_bank] 
 
# Simple Statistic  
least_fat = min(fat_index) 
most_energy = max(energy_index)
print("\nThe Least fat: " + str(least_fat))
print("\nThe Most energy: " + str(most_energy))


total_fat = sum(fat_index) 
total_energy = sum(energy_index)
print("\nThe Total fat: " + str(total_fat))
print("\nThe Total energy: " + str(total_energy))