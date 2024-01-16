from flask import Flask, render_template, request
import searchLib
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_query = request.form['search_query']
    # Now you can use the 'search_query' variable in your Python code
    # For example, print it:
    courses = searchLib.search(search_query)
    return render_template('results.html', courses=courses, search_query=search_query)

@app.route('/show_info', methods=['POST'])
def show_info():
    selected_result = request.form['grid-item']
    # Assume you have a function that retrieves information based on the selected result
    result_info = searchLib.printCourse(selected_result)
    gradeDF = searchLib.getGradeDistribution(selected_result)  
    gpa = searchLib.getGPA(gradeDF) 
    values = gradeDF['values'].tolist()

    return render_template('info.html', result_info=result_info, values=values, gpa=gpa)

if __name__ == '__main__':
    app.run(debug=True)