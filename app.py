#docstring- Asyraf airb-plane database application
#imports
import sqlite3

#constants and variables
DATABASE = "fighter.db"


#functions
def print_all_aircraft():
    '''Print all the aircraft niceley'''
    db = sqlite3.connect("fighter.db")
    cursor = db.cursor()
    sql = "SELECT * from fighter;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop all through resulrs
    print("name                       speed  max_g  climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finishes here
    db.close()


def print_all_aircraft_speed():
    '''Print all the aircraft niceley'''
    db = sqlite3.connect("fighter.db")
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY speed DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #loop all through resulrs
    print("name                       speed  max_g  climb range payload")
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    #loop finishes here
    db.close()


def print_all_aircraft_climb():
    '''Print all the aircraft nicely sorted by climb'''
    db = sqlite3.connect("fighter.db")
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY climb DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop all through the results
    print("name                       speed  max_g  climb range payload")
    # Print each fighter's details
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    db.close()


def print_all_aircraft_range():
    '''Print all the aircraft nicely sorted by range'''
    db = sqlite3.connect("fighter.db")
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY range DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop all through the results
    print("name                       speed  max_g  climb range payload")
    # Print each fighter's details
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    db.close()


def print_all_aircraft_payload():
    '''Print all the aircraft nicely sorted by payload'''
    db = sqlite3.connect("fighter.db")
    cursor = db.cursor()
    sql = "SELECT * from fighter ORDER BY payload DESC;"
    cursor.execute(sql)
    results = cursor.fetchall()
    #Loop all through the results
    print("name                       speed  max_g  climb range payload")
    # Print each fighter's details
    for fighter in results:
        print(f"{fighter[1]:<30}{fighter[2]:<8}{fighter[3]:<6}{fighter[4]:<6}{fighter[5]:<6}{fighter[6]:<6}")
    db.close()

       




#maincode
while True:
    user_input = input("What would you like to do. \n1. Print all aircraft.\n2. Print by speed.\n3. Print by climb.\n4. Print by range.\n5. Print by payload.\n6. Exit.")
    if user_input == "1":
        print_all_aircraft()
    elif user_input == "2":
        print_all_aircraft_speed()
    elif user_input == "3":
        print_all_aircraft_climb() 
    elif user_input == "4":
        print_all_aircraft_range() 
    elif user_input == "5":
        print_all_aircraft_payload()  
    elif user_input == "6":
        break
    else:
        print("That was not an option\n")
