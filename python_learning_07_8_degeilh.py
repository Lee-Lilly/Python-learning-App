# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 10:52:37 2020

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


# Print key, value pairs nested in the food bank list by looping through dictionary
def print_foodbank():
    print("\n The Food Bank List:\n")
    for food in food_bank:
        for k, v in food.items():
            print(k + ": " + str(v))
        print("\n") 
  


# Sorting food_bank with comparator such as energy, fat. etc.
def print_menu():
    print_choice = input("Print sorted: 'n' for name, 'cat' for category, 'en' for energy, 'fat' for fat, 'pro' for protein, 'car' for carbonhydrate, 's' for salt, 'b' for main menu. ")
    while print_choice != 'b':
        if print_choice == 'n':
            food_bank.sort(key= itemgetter('name'))
            print("\n Alphabetic order")
            for food in food_bank: 
                print('name: '+ food.get('name')) #accessing certain value using get()
        elif print_choice == 'cat':
            food_bank.sort(key= itemgetter('category'))
            print("\n Alphabetic order")
            for food in food_bank:
                print(('name: '+ food.get('name'), 'category: ' + food.get('category'))) # print out as tuples
        elif print_choice == 'en':
            food_bank.sort(key= itemgetter('Energy(kcal)'), reverse = True)
            print("\n Higher engergy first")
            for food in food_bank:
                print(('name: '+ food.get('name'), 'Energy(kcal): ' + str(food.get('Energy(kcal)'))))
        elif print_choice == 'fat':
            food_bank.sort(key= itemgetter('Fat(g)'))
            print("\n Less fat first")
            for food in food_bank:
                print(('name: '+ food.get('name'), 'Fat(g): ' + str(food.get('Fat(g)'))))
        elif print_choice == 'car':
            food_bank.sort(key= itemgetter('Carbonhydrate(g)'), reverse = True)
            print("\n Higer carbonhydrate first")
            for food in food_bank:
               print(('name: '+ food.get('name'), 'Carbonhydrate(g): ' + str(food.get('Carbonhydrate(g)'))))
        elif print_choice == 'pro':
            food_bank.sort(key= itemgetter('Protein(g)'), reverse = True)
            print("\n Higher protein first")
            for food in food_bank:
                print(('name: '+ food.get('name'), 'Protein(g): ' + str(food.get('Protein(g)'))))
        elif print_choice == 's':
            food_bank.sort(key= itemgetter('Salt(mg)'))
            print("\n Less salt first")
            for food in food_bank:
                print(('name: '+ food.get('name'), 'Salt(mg): ' + str(food.get('Salt(mg)'))))
        print_choice = input("Print in sorted: 'n' for name, 'cat' for category, 'en' for energy, 'fat' for fat, 'pro' for protein, 'car' for carbonhydrate, 's' for salt, 'b' for main menu. ") 

# User can add food items to the food_bank, print out or quit 
def main_menu():    
    user_choice = input("Enter 'a' to add food item; 'p' to print food info; 'ps' to print sorted nutrition info; 'q' to quit. ")
    while user_choice != 'q':
    
        if user_choice == 'a':
            food_item = input_data() # get food item from user input
            food_bank.append(food_item) # add food itme to list
            # Inform the user
            print('\nThanks! ' + food_item['name'] + ' is registered!')
        
        elif user_choice == 'p':
            print_foodbank()   
            
        # User can print out trailored info
        elif user_choice == 'ps':
            print_menu() 
        
        #back to main menu
        user_choice = input("Enter 'a' to add food item; 'p' to print food info; 'ps' to print sorted nutrition info; 'q' to quit. ")
  

# Call entry of program
main_menu()
        

