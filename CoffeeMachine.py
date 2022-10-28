import os
Menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "Money":0
}


def coffmach():
    input()
    os.system('clear')
    print("""
                                                                                                                    
                                                                                                                    
                      //  ) ) //  ) )                                                                               
    ___      ___   __//__  __//__  ___      ___          _   __      ___      ___     / __     ( )   __      ___    
  //   ) ) //   ) ) //      //   //___) ) //___) )     // ) )  ) ) //   ) ) //   ) ) //   ) ) / / //   ) ) //___) ) 
 //       //   / / //      //   //       //           // / /  / / //   / / //       //   / / / / //   / / //        
((____   ((___/ / //      //   ((____   ((____       // / /  / / ((___( ( ((____   //   / / / / //   / / ((____     


""")
    print("MENU")
    num=1
    for i in Menu:
        print(f"{num}.{i}     Cost:${Menu[i]['cost']}")
        num+=1
    Order=input("\nWhat would you like to have?Enter 'exit' to Exit.")
    if Order=='exit':
        print("Thank You")
        return
    if Order=='report':
        for i in resources:
            print(f"{i}: {resources[i]}")
        coffmach()
    for i in Menu[Order]["ingredients"]:
        if Menu[Order]["ingredients"][i]>resources[i]:
            print(f"We're sorry, {i} not sufficient.")
            coffmach()
        else:
            resources[i]-=Menu[Order]["ingredients"][i]
            
    Money=0
    Money+=int(input("How many quarters?"))*0.25
    Money+=int(input("How many dimes?"))*0.1
    Money+=int(input("How many nickels?"))*0.05
    Money+=int(input("How many penniess?"))*0.01
    if Money>=Menu[Order]['cost']:
        Bill=Money-Menu[Order]['cost']
        print(f"Here is $%.2f in change\nHere is your {Order}, Enjoy! "%(Bill))
        resources['Money']+=Bill
        coffmach()
    else:
        print("Money not sufficient, Transaction cancelled!")
        coffmach()
coffmach()
