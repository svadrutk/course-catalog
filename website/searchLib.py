import pandas as pd
import os
import re
import requests
from fuzzywuzzy import process
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = "newTable.csv"
df = pd.read_csv(DATA_FILE)
classes = df['Course Block #'].tolist()
lowerClasses = {x: x.lower().strip().replace(' ','') for x in classes}


def search(string): 
    string = string.lower().strip().replace(' ','')
    if string.startswith('cs') and string.count('cs') == 1 and not string.startswith('cs&d'):
        string = string.replace('cs', 'compsci')
    
    sorted_courses = process.extract(string, classes, limit=20)
    output_courses = [] 
    for course in sorted_courses:
        courseData = df[df['Course Block #'] == course[0]].values[0]
        output_courses.append("<b>" + courseData[1] + "</b>" + "<br><br>" + courseData[0])
    print(output_courses)
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
    course = re.search(r".*<br>([^<]*)$", course).group(1)
    # print all the info
    string = df[df['Course Block #'] == course].values[0]
    output = "" 
    output += "<br>"
    output += "<h1 style=\"text-align: center; font-size: 3rem;\">" + string[0] + ": " + string[1] + "</h1>"
    output += "<div class=\"info-container\">"
    output += "<div class=\"info-box\">"

    output += "<div class=\"info-subbox\">"
    output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\">" + string[2] + "</h2>"
    output += "</div>"

    output += "<div class=\"info-subbox\">"
    output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\"><b>Prerequisites: </b>" + string[4] + "</h2>"
    output += "</div>"

    output += "<div class=\"info-subbox\">"
    output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\"><h2 style=\"color: #c5050c; display: inline; font-style: normal;\">" + str(string[3]) + "</h2> Course Credits</h2>"
    if string[5] != 'No': 
        output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\">This course is repeatable for credit.</h2>"
    if string[7] != 'This course does NOT have a level.':
        output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\"> Course Level: " + string[7] + "</h2>"
    if string[8] != 'This course does NOT have a breadth.':
        output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\">Course Breadth: " + string[8] + "</h2>"
    if string[9] != 'This course does NOT count towards the 50% graduate coursework requirement.':
        output += "<p><b>Graduate Requirement: </b>" + string[9] + "</p>"
    if string[10] != 'This course does NOT count as L&S credit.':
        output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\">" + string[10] + "</h2>"
    if string[11] != 'This course does NOT count towards Ethnic Studies.':
        output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\">" + string[11] + "</h2>"
    if string[12] != 'This course is NOT an honors course.':
        output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\">" + string[12] + "</h2>"
    if string[13] != 'This course does NOT have a General Education designation.':
        output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\"> This course has a Gen Ed designation. </h2>"
    if string[14] != 'This course is NOT a Workplace Experience course.':
        output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\">" + string[14] + "</h2>"
    if string[15] != 'This course does NOT have a Foreign Language designation.':
        output += "<p><b>Foreign Language: </b>" + string[15] + "</p>"
    output += "<h2 style=\"font-style: normal; font-weight: 400; font-size: 1.5rem;\">Last taught in " + string[6] + ".</h2>"
    output += "</div>"
    output += "</div>"
    

    
    
    return output
        
def getGradeDistribution(course): 
    course = re.search(r".*<br>([^<]*)$", course).group(1)
    string = df[df['Course Block #'] == course].values[0]
    # use madgrades API 
    url = "https://api.madgrades.com/v1/courses"
    token = "192214970a684cd68488a22e5fa80a34"
    headers = { "Authorization": f"Token token={token}"}
    queryResponse = requests.get(url, headers=headers, params={"query": string[0]})
    if queryResponse.status_code == 200: 
        queryResponse = queryResponse.json() 
        uuid = queryResponse['results'][0]['uuid']
    ###############################
    classURL = url + "/" + uuid + "/grades"
    classResponse = requests.get(classURL, headers=headers)
    if classResponse.status_code == 200: 
        classGrades = classResponse.json() 
    classGrades = classGrades['cumulative']
    grades = {'category': ['A', 'AB', 'B', 'BC', 'C', 'D', 'F'], 'values': [classGrades['aCount'], classGrades['abCount'], classGrades['bCount'], classGrades['bcCount'], classGrades['cCount'], classGrades['dCount'], classGrades['fCount']]}
    gradeDF = pd.DataFrame(grades)
    return gradeDF

    
    



    


    
    
    

if __name__ ==  "__main__": 
    getGradeDistribution('ANTHRO 105')