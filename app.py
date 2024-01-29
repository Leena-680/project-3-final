from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pandas as pd
import sqlite3


app = Flask(__name__)
CORS(app)

# Function to get DataFrame from SQLite DB
def get_dataframe():
    with sqlite3.connect('../group-2-project_UPDATED/student_data.db') as conn:
        df = pd.read_sql_query("SELECT * FROM students", conn)
    return df

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/map_2")
def map_2():
    return render_template("map_2.html")

@app.route("/visualisation_1")
def visualisation_1():
    return render_template("visualisation_1.html")

@app.route('/returnjson', methods = ['GET']) 
def ReturnJSON(): 
    if(request.method == 'GET'): 

        jsonData = [
          {
            "totalStudent": 384,        # Total no of students in dataset
            "studentNo": 40,            # no of students with grade A
            "females": 16,              # no of girls with grade A
            "males": 24,                # no of boys with grade A
            "higher_ed_NoPct": 0,       # no of students with higher ed goal = N
            "higher_ed_YesPct": 100,    # no of students with higher ed goal = Y
            "higher_ed_Yes_girls": 16,  # no of girls with higher ed goal = Y
            "higher_ed_Yes_boys": 24,   # no of boys with higher ed goal = Y
            "finalGrade": "A"
          },
          {
            "totalStudent": 384,
            "studentNo": 169,   
            "females": 87,   
            "males": 82,     
            "higher_ed_NoPct": 2.4,
            "higher_ed_YesPct": 97.6,
            "higher_ed_Yes_girls": 86,   
            "higher_ed_Yes_boys": 79,     
            "finalGrade": "B"
          },
          {
            "totalStudent": 384,
            "studentNo": 140,   
            "females": 78,   
            "males": 62,     
            "higher_ed_NoPct": 7.2,
            "higher_ed_YesPct": 92.8,
            "higher_ed_Yes_girls": 76,   
            "higher_ed_Yes_boys": 54,    
            "finalGrade": "C"
          },
          {
            "totalStudent": 384,
            "studentNo": 46,   
            "females": 27,   
            "males": 19,     
            "higher_ed_NoPct": 13.1,
            "higher_ed_YesPct": 86.9,
            "higher_ed_Yes_girls": 26,   
            "higher_ed_Yes_boys": 14,    
            "finalGrade": "D"
          }
        ];
  
        return jsonify(jsonData) 
    

@app.route("/visualisation_2")
def visualisation_2():
    return render_template("visualisation_2.html")

@app.route("/About")
def about():
    return render_template("about.html")

@app.route('/data', methods=['GET'])
def get_data():
    df = get_dataframe()

    # Define the columns for which to calculate 'Yes'/'No' percentages
    yes_no_columns = ['higher_ed', 'internet_access', 'romantic_relationship']

    # Calculate statistics for each grade
    grade_categories = ['A', 'B', 'C', 'D']
    result = []

    for grade in grade_categories:
        grade_df = df[df['final_grade'] == grade]

        stats = {
            'finalGrade': grade,
            'studentNo': len(grade_df),
            'avgStudyTime': grade_df['study_time'].mean(),
            'avgTravelTime': grade_df['travel_time'].mean(),
            'sumClassFailures':int(grade_df['class_failures'].sum()),
            'avgAbsence': grade_df['absences'].mean(),
            'avgHealth': grade_df['health'].mean(),
            'avgFreeTime': grade_df['free_time'].mean(),
            'avgSocial': grade_df['social'].mean(),
            'avgWeekdayAlcohol': grade_df['weekday_alcohol'].mean(),
            'avgWeekendAlcohol': grade_df['weekend_alcohol'].mean()
        }

        # Calculate 'Yes'/'No' percentages for specified columns
        for col in yes_no_columns:
            yes_count = grade_df[col].value_counts().get('yes', 0)
            no_count = grade_df[col].value_counts().get('no', 0)
            total = yes_count + no_count
            stats[f'{col}_YesPct'] = (yes_count / total) * 100 if total > 0 else 0
            stats[f'{col}_NoPct'] = (no_count / total) * 100 if total > 0 else 0
                    
        result.append(stats)

    return jsonify(result)

@app.route('/data-by-gender', methods=['GET'])
def get_data_by_gender():
    df = get_dataframe()

    # Define the columns for 'Yes'/'No' percentages
    yes_no_columns = ['higher_ed', 'internet_access', 'romantic_relationship']
    genders = df['sex'].unique()

    # Calculate statistics for each gender
    result = []

    for gender in genders:
        gender_df = df[df['sex'] == gender]

        stats = {
            'sex': gender,
            'studentNo': len(gender_df),
            'avgStudyTime': gender_df['study_time'].mean(),
            'avgTravelTime': gender_df['travel_time'].mean(),
            'avgAbsence': gender_df['absences'].mean(),
            'avgHealth': gender_df['health'].mean(),
            'avgFreeTime': gender_df['free_time'].mean(),
            'avgSocial': gender_df['social'].mean(),
            'avgWeekdayAlcohol': gender_df['weekday_alcohol'].mean(),
            'avgWeekendAlcohol': gender_df['weekend_alcohol'].mean()
        }

        # Calculate 'Yes'/'No' percentages for specified columns
        for col in yes_no_columns:
            yes_count = gender_df[col].value_counts().get('yes', 0)
            no_count = gender_df[col].value_counts().get('no', 0)
            total = yes_count + no_count
            stats[f'{col}_YesPct'] = (yes_count / total) * 100 if total > 0 else 0
            stats[f'{col}_NoPct'] = (no_count / total) * 100 if total > 0 else 0

        result.append(stats)

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)