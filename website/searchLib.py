import pandas as pd
import numpy as np
import os
from fuzzywuzzy import fuzz, process
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = "newTable.csv"
df = pd.read_csv(DATA_FILE)
classes = df['Course Block #'].tolist()
lowerClasses = {x: x.lower().strip().replace(' ','') for x in classes}


def search(string): 
    string = string.lower().strip().replace(' ','')
    if string.startswith('cs') and string.count('cs') == 1:
        string = string.replace('cs', 'compsci')
    
    filtered_courses = {}
    sorted_courses = process.extract(string, classes, limit=10)
    output_courses = [] 
    for course in sorted_courses:
        output_courses.append(course[0])

    ########################################
    # print("Which course would you like to see?")
    # for i in range(len(sorted_courses)):
    #     print(str(i + 1) + ") " + sorted_courses[i])
    # print("-----------------------------------------------")
    # choice = input()
    # return sorted_courses[int(choice) - 1]
    return output_courses
    ########################################

def printCourseList(courses): 
    string = ""
    for course in courses:
        string += "<div class=\"class\"><button>" + course + "</button></div>"
    return string
        

def printCourse(course):
    
    # print all the info
    string = df[df['Course Block #'] == course].values[0]
    output = "" 
    output += "<h1>" + string[0] + ": " + string[1] + "</h1>"
    output += "<h2>Description</h2>"
    output += "<p>" + string[2] + "</p>"
    output += "<p>-------------------------------------------------</p>"
    output += "<h2>Prerequisites</h2>"
    print(string[4])
    output += "<p>" + string[4] + "</p>"
    output += "<p>-------------------------------------------------</p>"
    output += "<p><b>Course Credits: </b>" + str(string[3]) + "</p>"
    output += "<p><b>Repeatable for Credit: </b>" + string[5] + "</p>"
    output += "<p><b>Last Taught: </b>" + string[6] + "</p>"
    output += "<p><b>Course Level: </b>" + string[7] + "</p>"
    output += "<p><b>Course Breadth: </b>" + string[8] + "</p>"
    output += "<p><b>Graduate Requirement: </b>" + string[9] + "</p>"
    output += "<p><b>L&S Credit: </b>" + string[10] + "</p>"
    output += "<p><b>Ethnic Studies: </b>" + string[11] + "</p>"
    output += "<p><b>Honors: </b>" + string[12] + "</p>"
    output += "<p><b>General Education: </b>" + string[13] + "</p>"
    output += "<p><b>Workplace Experience: </b>" + string[14] + "</p>"
    output += "<p><b>Foreign Language: </b>" + string[15] + "</p>"
    
    return output
        


if __name__ ==  "__main__": 
    print("Which class would you like to search for?")
    className = input()
    printCourse(search(className))