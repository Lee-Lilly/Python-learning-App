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
    def __init__(self, name, category, nutrition_panel):
        self.name = name
        self.category = category
        self.nutrition_panel = nutrition_panel
        
    # The format of presentation
    def __repr__(self):
        return "\nname: {},\ncategory: {},\nnutrition:\n{}".format(self.name, self.category, self.nutrition_panel)

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
    
    nutrition_panel = {}
    print("\nFollow the steps to complete nutrition details, if no value put 0")
    
    key = 'Energy'
    value = float(input("Enter energy(kcal/100g): "))
    nutrition_panel.update({key: value})
    
    key = 'Fat'
    value = float(input("Enter fat(g/100g): "))
    nutrition_panel.update({key: value})
    
    key = 'Carbonhydrate'
    value = float(input("Enter carbonhydrate(g/100g): "))
    nutrition_panel.update({key: value})
    
    key = 'Protein'
    value = float(input("Enter protein(g/100g): "))
    nutrition_panel.update({key: value})
    
    
    key = 'Salt'
    value = float(input("Enter salt(g/100g): "))
    nutrition_panel.update({key: value})
    
    food_data = Food(name, category, nutrition_panel)
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