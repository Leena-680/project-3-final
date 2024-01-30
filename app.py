from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import pandas as pd
import sqlite3


app = Flask(__name__)
CORS(app)

# Function to get DataFrame from SQLite DB
def get_dataframe():
    with sqlite3.connect('student_data.db') as conn:
        df = pd.read_sql_query("SELECT * FROM students", conn)
    return df

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/map_2")
def map_2():
    return render_template("iso_map.html")

@app.route("/visualisation_1")
def visualisation_1():
    return render_template("visualisation_1.html")

@app.route("/visualisation_2")
def visualisation_2():
    return render_template("visualisation_2.html")

@app.route("/About")
def about():
    return render_template("about.html")

@app.route('/data', methods=['GET'])
def get_data():
    df = get_dataframe()

    # Calculatations for each grade
    grade_categories = ['A', 'B', 'C', 'D']
    total_students = len(df)
    result = []

    for grade in grade_categories:
        grade_df = df[df['final_grade'] == grade]
        female_df = grade_df[grade_df['sex'] == 'F']
        male_df = grade_df[grade_df['sex'] == 'M']

        # Calculate 'Yes'/'No' percentages for higher education
        yes_count = grade_df['higher_ed'].value_counts().get('yes', 0)
        no_count = grade_df['higher_ed'].value_counts().get('no', 0)
        total = yes_count + no_count

        stats = {
            'finalGrade': grade,
            'totalStudent': total_students,
            'studentNo': len(grade_df),
            'females': len(female_df),
            'males': len(male_df),
            'avgStudyTime': grade_df['study_time'].mean(),
            'avgTravelTime': grade_df['travel_time'].mean(),
            'sumClassFailures': int(grade_df['class_failures'].sum()),
            'higher_ed_YesPct': (yes_count / total) * 100 if total > 0 else 0,
            'higher_ed_NoPct': (no_count / total) * 100 if total > 0 else 0,
            'higher_ed_Yes_girls': sum(female_df['higher_ed'] == 'yes'),
            'higher_ed_Yes_boys': sum(male_df['higher_ed'] == 'yes'),
        }

        result.append(stats)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)