import pandas as pd
import numpy as np
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DATA_FILE = "classes.csv"
def cleanup_data(): 
    print(os.access(DATA_FILE, os.R_OK))
    df = pd.read_csv(DATA_FILE)
    courseDesignationList = df['Course Designation'].tolist()
    
    levelList = [] 
    breadthList = []
    gradList = [] 
    lsList = []
    ethnicList = []
    honorsList = []
    genEdList = []
    workList = []
    foreignLangList = []

    counter = 0
    for course in courseDesignationList:
        if isinstance(course, str):
            if 'Level - Advanced' in course:
                levelList.append('Advanced')
            elif 'Level - Intermediate' in course:
                levelList.append('Intermediate')
            elif 'Level - Elementary' in course:
                levelList.append('Elementary')
            else: 
                levelList.append('This course does NOT have a level.')


            if 'Breadth - Literature' in course:
                breadthList.append('Literature')
            elif 'Breadth - Humanities' in course:
                breadthList.append('Humanities')
            elif 'Breadth - Social Science' in course:
                breadthList.append('Social Science')
            elif 'Breadth - Biological Sci.' in course:   
                breadthList.append('Biological Science')
            elif 'Breadth - Physical Sci.' in course:
                breadthList.append('Physical Science')
            elif 'Breadth - Natural Science' in course:
                breadthList.append('Natural Science')
            elif 'Breadth - Either Humanities or Social Science' in course:
                breadthList.append('Humanities/Social Science')
            elif 'Breadth - Either Biological Science or Social Science' in course:
                breadthList.append('Biological Science/Social Science')
            elif 'Breadth - Either Social Science or Natural Science' in course:
                breadthList.append('Social Science/Natural Science')
            elif 'Breadth - Either Humanities or Natural Science' in course:
                breadthList.append('Humanities/Natural Science')
            else: 
                breadthList.append('This course does NOT have a breadth.') 
            

            if 'Grad 50% - Counts toward 50% graduate coursework requirement' in course:
                gradList.append('This course counts towards the 50% graduate coursework requirement.')
            else: 
                gradList.append('This course does NOT count towards the 50% graduate coursework requirement.')
            
            if 'L&S Credit - Counts as Liberal Arts and Science credit in L&S' in course:
                lsList.append('This course counts as L&S credit.')
            else: 
                lsList.append('This course does NOT count as L&S credit.')

            if 'Ethnic St - Counts toward Ethnic Studies requirement' in course: 
                ethnicList.append('Ethnic Studies')
            else: 
                ethnicList.append('This course does NOT count towards Ethnic Studies.')
            
            if 'Honors - Honors Only Courses (H)' in course: 
                honorsList.append('Honors')
            elif 'Honors - Accelerated Honors (!)' in course:
                honorsList.append('Accelerated Honors')
            elif 'Honors - Honors Optional (%)' in course:
                honorsList.append('Honors Optional')
            else: 
                honorsList.append('This course is NOT an honors course.')

            if 'Gen Ed - Communication Part A' in course: 
                genEdList.append('Communication A')
            elif 'Gen Ed - Communication Part B' in course:
                genEdList.append('Communication B')
            elif 'Gen Ed - Quantitative Reasoning Part A' in course:
                genEdList.append('Quantitative Reasoning A')
            elif 'Gen Ed - Quantitative Reasoning Part B' in course:
                genEdList.append('Quantitative Reasoning B')
            else: 
                genEdList.append('This course does have a General Education designation.')
            
            if 'Workplace - Workplace Experience Course' in course:
                workList.append('This course is a Workplace Experience course.')
            else: 
                workList.append('This course is NOT a Workplace Experience course.')

            if 'Frgn Lang - 1st semester language course' in course:
                foreignLangList.append('1st Semester Language Course')
            elif 'Frgn Lang - 2nd semester language course' in course:
                foreignLangList.append('2nd Semester Language Course')
            elif 'Frgn Lang - 3rd semester language course' in course:
                foreignLangList.append('3rd Semester Language Course')
            elif 'Frgn Lang - 4th semester language course' in course:
                foreignLangList.append('4th Semester Language Course')
            elif 'Frgn Lang - 5th + semester language course' in course:
                foreignLangList.append('5th+ Semester Language Course')
            else: 
                foreignLangList.append('This course does NOT have a Foreign Language designation.')
        else: 
            levelList.append('This course does NOT have a level.')
            breadthList.append('This course does NOT have a breadth.')
            gradList.append('This course does NOT count towards the 50% graduate coursework requirement.')
            lsList.append('This course does NOT count as L&S credit.')
            ethnicList.append('This course does NOT count towards Ethnic Studies')
            honorsList.append('This course is NOT an honors course.')
            genEdList.append('This course does NOT have a General Education designation.')
            workList.append('This course is NOT a Workplace Experience course.')
            foreignLangList.append('This course does NOT have a Foreign Language designation.') 
        counter += 1

    df['Repeatable'] = df['Repeatable'].str.replace('Yes, unlimited number of completions', 'Unlimited')
    df['Repeatable'] = df['Repeatable'].str.replace('Yes, for 2 number of completions', '2')
    df['Repeatable'] = df['Repeatable'].str.replace('Yes, for 3 number of completions', '3')
    df['Repeatable'] = df['Repeatable'].str.replace('Yes, for 4 number of completions', '4')
    df['Repeatable'] = df['Repeatable'].str.replace('Yes, for 5 number of completions', '5')
    df['Repeatable'] = df['Repeatable'].str.replace('Yes, for 6 number of completions', '6')

    df['Course Level'] = levelList
    df['Course Breadth'] = breadthList
    df['Grad Req'] = gradList
    df['L&S Credit'] = lsList
    df['Ethnic Studies'] = ethnicList
    df['Honors'] = honorsList
    df['Gen Ed'] = genEdList
    df['Workplace'] = workList
    df['Foreign Language'] = foreignLangList

    df['Course Designation'] = df['Course Designation'].str.replace('Level - Advanced', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Level - Intermediate', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Level - Elementary', '')

    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Literature. Counts toward the Humanities req', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Humanities', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Social Science', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Biological Sci. Counts toward the Natural Sci req', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Physical Sci. Counts toward the Natural Sci req', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Either Humanities or Social Science', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Either Biological Science or Social Science', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Either Social Science or Natural Science', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Either Humanities or Natural Science', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Breadth - Natural Science', '')

    df['Course Designation'] = df['Course Designation'].str.replace('Grad 50% - Counts toward 50% graduate coursework requirement', '')

    df['Course Designation'] = df['Course Designation'].str.replace('L&S Credit - Counts as Liberal Arts and Science credit in L&S', '')

    df['Course Designation'] = df['Course Designation'].str.replace('Ethnic St - Counts toward Ethnic Studies requirement', '')

    df['Course Designation'] = df['Course Designation'].str.replace('Honors - Honors Only Courses (H)', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Honors - Accelerated Honors (!)', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Honors - Honors Optional (%)', '')
    
    df['Course Designation'] = df['Course Designation'].str.replace('Gen Ed - Communication Part A', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Gen Ed - Communication Part B', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Gen Ed - Quantitative Reasoning Part A', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Gen Ed - Quantitative Reasoning Part B', '')

    df['Course Designation'] = df['Course Designation'].str.replace('Workplace - Workplace Experience Course', '')
    
    df['Course Designation'] = df['Course Designation'].str.replace('Frgn Lang - 1st semester language course', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Frgn Lang - 2nd semester language course', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Frgn Lang - 3rd semester language course', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Frgn Lang - 4th semester language course', '')
    df['Course Designation'] = df['Course Designation'].str.replace('Frgn Lang - 5th + semester language course', '')

    # delete course designation column
    del df['Course Designation']

    df['Requisites'].fillna('No prerequisites.', inplace=True)
    df.to_csv("newTable.csv", index=False)  


cleanup_data()

