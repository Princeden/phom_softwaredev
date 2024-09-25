import csv    # Import required libraries
import random
from flask import Flask
jobs = ' '
all_occupations = [] #Creates list of dictionaries for all occupations
def select_occupation():
    with open("occupations.csv", mode = "r") as file:  # Opens CSV File
        csvFile = csv.reader(file)   # Reads CSV File
        pSum = 0  #Creates pSum variable which will be used as divider
        for line in csvFile:   #Loops through CSV object
            if not(line[0] == "Job Class" or line[0] == "Total"):   #Takes out first and last row
                pSum += float(line[1])*10   #Calculates pSum value
                all_occupations.append({"Job Class": line[0], "Percentage": float(line[1]), "pSum": pSum})  #Creates dictionary and adds to list
            
    job = random.randint(0, 998)   #Random Integer
    selected_job = ''
    for i in all_occupations:  #Loops through list
        if job < i["pSum"]:   #Finds range the random integer is in
            selected_job = i #Prints the selected occupation
            break   #Breaks out of loop as range was found
    return selected_job['Job Class']
app = Flask(__name__)           #create instance of class Flask


@app.route("/")                 #assign fxn to route
def hello_world():
#    print("test")
    print("the __name__ of this module is... ")
    job = select_occupation()
    jobs = ''
    for i in all_occupations:
        if i['Job Class'] not in jobs:
            jobs += i['Job Class'] + '<br>'
    print(job)
    print(__name__)
    return 'Team VAP (Aditya, Princedon, Vedant) 5 <br>'  + jobs + '<br>' + job

if __name__ == "__main__":      # true if this file NOT imported 
#if the file is imported what does the name become?
    app.debug = True            # enable auto-reload upon code change
    app.run()    