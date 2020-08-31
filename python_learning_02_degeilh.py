# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 08:43:54 2020

@author: chang
"""


# Title
title = "Nutrition App"
print(title)

# List of food categories
categories =["Fruit", "Diary", "Vegetable", "Meat", "Fish", "Egg", "Fat-Oil", "Beverage"]

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
# Print food_item in the format of "Food" presentation
print(food_item)
       
# Function to get food data from user input         
def input_data():
    name = input("Enter a food name: ")
    print("\nFollow the category list:")
    
    print(categories)
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

food_item = input_data();

print('\n' + food_item.name + ' is registered!')
print(food_item)