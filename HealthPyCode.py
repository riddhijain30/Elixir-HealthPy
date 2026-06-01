import mysql.connector
from clrprint import *
#To create new user database
def new_user(): 
    name = input("What's your name? ").lower()
    age = int(input("Age: "))
    weight = float(input("Weight (in kg): "))
    height = float(input("Height (in cm): "))
    gender = input("Enter gender (M/F): ").upper()
    Daily=input("This will be used for daily input of your activity. Type 0 to get started: ")
    print(display_bmi(weight, height))
    cur.execute(f"CREATE DATABASE IF NOT EXISTS {name};")
    cur.execute(f"USE {name};")        
    chosen = input("Choose your goal: \na. Physical Health\nb. Mental Health\nc. Lifestyle and Routine\nWhich area should your focus be inclined to? (a, b, c): ").lower()
    if chosen == 'a':
        goal = physical_health()
        focus = "Physical Health"
    elif chosen == 'b':
        goal = mental_health()
        focus = "Mental Health"
    elif chosen == 'c':
        goal = lifestyle_and_routine()
        focus = "Lifestyle and Routine"
    else:
        print("Invalid choice. Please select a valid option.")
    user_data = (age, weight, height, gender, focus, goal, Daily)
    create_table_query = """CREATE TABLE IF NOT EXISTS users (
                                Age VARCHAR(100),
                                Weight VARCHAR(100),
                                Height VARCHAR(100),
                                Gender VARCHAR(1),
                                Focus VARCHAR(100),
                                Goal VARCHAR(100),
                                Daily VARCHAR (100)
                            ); """
                            
    cur.execute(create_table_query)
    insert_query = """INSERT INTO users (Age, Weight, Height, Gender, Focus, Goal, Daily)
                        VALUES (%s, %s, %s, %s, %s, %s, %s);"""

    cur.execute(insert_query, user_data)
    con.commit()
    clrprint("Your response has been successfully recorded. Now you can use the existing user section.",clr="r")
    existing_user()    
#Function for when the user wants to work in an existing profile
def existing_user():
    name = input("Enter the name of user id you wish to proceed with (name of user) :").lower()
    cur.execute(f"USE {name};")    
    cur.execute(f"SELECT age, weight, height, gender, focus, goal FROM users;")
    user_info = cur.fetchall()  # Fetch all results
    cur.execute(f"SELECT Focus, Goal FROM users LIMIT 1")
    focus_goal_info = cur.fetchone()  # Fetch one result
    if focus_goal_info:
        focus = focus_goal_info[0]
        goal = focus_goal_info[1]
    else:
        print("No user information found.")
        pass  # Skip to the next iteration if no data
    while(True):
        print("\nHow would you like to work on the id and yourself?: ")
        clrprint("\n1. Track the goal and fill up daily inputs", clr="p")
        clrprint("2. Permanently DELETE the ID", clr="p")
        clrprint("3. Updating the information provided for the id", clr="p")
        clrprint("4. Show progress", clr="p")
        clrprint("5. End program", clr="p")
        task = int(input("Enter the number of the task that you wish to perform(1-5) :"))
        # Handle each task option accordingly
        if task == 1:
            #Fetch the focus and goal again to avoid any confusion
            cur.execute(f"SELECT Focus, Goal FROM users LIMIT 1")
            fgi = cur.fetchone()
            if fgi:
                f = fgi[0]
                g = fgi[1]
            else:
                print("No user information found.")
                pass                
            if f=="Physical Health":
                if g=="1":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("Enter your latest weight: "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="2":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("Enter the weight you could lift today: "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="3":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("How many kms did you run today? "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    con.commit()
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="4":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("How much time did you spend doing stretching exercises? "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    con.commit()
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")             
            elif f=="Lifestyle and Routine":
                if g=="1":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("How many hour did you sleep today?: "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="2":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("How many minutes did you meditate today? "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="3":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("How many ounces of water did you drink today? "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="4":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("How did you feel on a scale of 1 to 5 today? (5 being the best) "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
            elif f=="Mental Health":
                if g=="1":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("What would you like to rate your stress level out of 10:"))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="2":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(clrinput("On a level of 1-5 how did you feel today 5 being the best:",clr="r"))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="3":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("How many hours did you give to yourself:"))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
                elif g=="4":
                    clrprint("Good to see you back! And even better to see you working on yourself!",clr="g")
                    daily_input=int(input("How many hours were you able to do something you like? "))
                    hello=[ ("_", "_", "_", "_", "_", "_", daily_input) ]
                    query=("insert into users (Age, Weight, Height, Gender, Focus, Goal, Daily) values (%s, %s, %s, %s, %s, %s, %s)")
                    cur.executemany(query, hello)
                    con.commit()
                    clrprint("I am glad of your progress! Don't forget to come back tomorrow!",clr="y")
            else:
                print("Error")       
        #Delete user profile
        elif task == 2:
            cur.execute(f"drop database {name};")
            print("\n\nYOUR PROFILE HAS BEEN SUCCESSFULLY DELETED!! :( ")
            exit()
        #Update age, weight or height             
        elif task == 3:
            print("")
            print("1. AGE")
            print("2. WEIGHT")
            print("3. HEIGHT")                     
            A=int(input("Enter the number in front of the attribute that you wish to alter from 1-3 :"))
            if A == 1:
                age=int(input("Enter age:"))
                cur.execute("UPDATE users SET Age={}".format(age))
            elif A == 2:
                weight=int(input("Enter weight:"))
                cur.execute("UPDATE users SET Weight={}".format(weight))
            elif A == 3:
                height=int(input("Enter height(cm):"))
                cur.execute("UPDATE users SET Height={}".format(height))
            else:
                print("Invalid")
            print("\nThe age , weight , height , gender , focus , goal of the given user is given in the according order as follows")
            cur.execute(f"USE {name};")
            cur.execute(f"select* from users;")
            con.commit()
            for i in cur:
                print(i)
            print("\nYOUR ATTRIBUTE HAS BEEN SUCCESSFULLY UPDATED!! :)")
            #Show user's progress
        elif task == 4:
            cur.execute("select * from users;")
            for i in cur:
                print(i)           
        elif task == 5:
            print("\n ☃ Bye byeeeee!☃")
            exit()
        else:
            print("Please enter a valid response")           
# Function to display BMI and suggestions
def display_bmi(weight, height):
    bmi = weight / ((height / 100) ** 2)
    if bmi < 18.5:
        category = "Underweight"
        clrprint( category, clr="yellow")
        suggestion = "Consider a weight gain plan."
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
        clrprint( category, clr="green")
        suggestion = "Maintain your current weight and fitness level."
    elif 25 <= bmi < 29.9:
        category = "Overweight."
        clrprint( category, clr="yellow")
        suggestion = "Consider a weight loss plan."
    else:
        category = "Obese"
        clrprint( category, clr="red")
        suggestion = "Consider a weight loss plan and consult a healthcare provider."
    return bmi, suggestion
# Function for Physical Health options
def physical_health():
    print("\nPhysical Health Options:")
    print("1. Weight Control")
    print("2. Strength Training")
    print("3. Cardiovascular Fitness")
    print("4. Flexibility and Mobility")
    goal = input("Choose an option (1-4): ")
    if goal == '1':
        print("\nWeight Control:")
        print("a. Weight Loss Plans: Diet and exercise programs focused on reducing body weight.")
        print("b. Weight Gain Plans: Strategies for gaining muscle or weight.")
        print("c. Maintenance Programs: Guidelines for maintaining a healthy weight.")
    elif goal == '2':
        print("\nStrength Training:")
        print("a. Muscle Building: Workouts and nutrition plans focused on increasing muscle mass.")
        print("b. Endurance Training: Exercises designed to improve muscular endurance.")
        print("c. Functional Strength: Exercises for daily activities and sports performance.")
    elif goal == '3':
        print("\nCardiovascular Fitness:")
        print("a. Aerobic Exercises: Running, cycling, swimming.")
        print("b. HIIT Workouts: High-Intensity Interval Training.")
        print("c. Heart Rate Monitoring: Tools for tracking cardiovascular workouts.")
    elif goal == '4':
        print("\nFlexibility and Mobility:")
        print("a. Stretching Routines: Static and dynamic stretches.")
        print("b. Yoga and Pilates: Programs for flexibility and balance.")
        print("c. Mobility Exercises: Improving joint and muscle function.")
    else:
        print("Invalid choice.")
    return goal
# Function for Mental Health options
def mental_health():
    print("\nMental Health Options:")
    print("1. Stress Management")
    print("2. Emotional Well-being")
    print("3. Self-Care and Recovery")
    print("4. Work-Life Balance")
    goal = input("Choose an option (1-4): ")
    if goal == '1':
        print("\nStress Management:")
        print("a. Mindfulness and Meditation")
        print("b. Breathing Exercises")
        print("c. Progressive Muscle Relaxation")
    elif goal == '2':
        print("\nEmotional Well-being:")
        print("a. Mood Tracking")
        print("b. Journaling Prompts")
        print("c. Cognitive Behavioral Techniques")
    elif goal == '3':
        print("\nSelf-Care and Recovery:")
        print("a. Relaxation Techniques")
        print("b. Self-Care Routines")
        print("c. Recovery Plans")
    elif goal == '4':
        print("\nWork-Life Balance:")
        print("a. Time Management Tips")
        print("b. Setting Boundaries")
        print("c. Stress Reduction Strategies")
    else:
        print("Invalid choice.")
    return goal
# Function for Lifestyle and Routine options
def lifestyle_and_routine():
    print("\nLifestyle and Routine Options:")
    print("1. Sleep Tracking")
    print("2. Meditation")
    print("3. Hydrating Oneself")
    print("4. Daily Activity Tracking")
    goal = input("Choose an option (1-4): ")
    if goal == '1':
        print("\nSleep Tracking:")
        print("Track sleep based on age and daily data.")
    elif goal == '2':
        print("\nMeditation:")
        print("Meditate every day for better health. Set a daily reminder.")
    elif goal == '3':
        print("\nHydrating Oneself:")
        print("Drink adequate water every day.")
    elif goal == '4':
        print("\nDaily Activity Tracking:")
        print("Track daily steps and calories.")
    else:
        print("Invalid choice.")
    return goal
    # Initialize focus and goal with default values
    focus = "Not Specified"
    goal = "Not Specified"
# Connect to MySQL
con = mysql.connector.connect(
    host='localhost',
    user='root',
    password='ahlcon')
cur = con.cursor()
while True:
    clrprint("I'm Elixir 💐ヾ(＾∇＾)ヾ💐 your health companion, here to help you with all your wellness needs. How can I assist you today?",clr="r")
    clrprint("╔┓┏╦━━╦┓╔┓╔━━╗",clr="p")
    clrprint("║┗┛║┗━╣┃║┃║╯╰║",clr="p")    
    clrprint("║┏┓║┏━╣┗╣┗╣╰╯║",clr="p")    
    clrprint("╚┛┗╩━━╩━╩━╩━━╝",clr="p")
    clrprint("1. New user",clr="g")
    clrprint("2. Existing user",clr="g")
    clrprint("3. Exit",clr="g")
    choice = int(input("Enter your choice: ")) #Asking user choice
    # When the user wants to create a new profile
    if choice==1:
        new_user()
    elif choice==2:
        existing_user()
    elif choice==3:
        exit()
    else:
        print("ENTER A VALID RESPONSE.")
new_user()
existing_user()                
cur.close()
con.commit()
con.close()
