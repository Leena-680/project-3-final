# Project 3: High school student performance #

By  Alexander Hodgins, Gayan DSilva, Leena Chauhan, Himali Wijeratne

## Link to presentation ## 

https://docs.google.com/presentation/d/1q5RqmvoCfvH1nc0b4Y7mZE7_xtfL-h_JvRtW5tdHHCw/edit?usp=sharing 

## Introduction ##

This is a collaborative project to develop a full-stack data visualization web application, using Python Flask-powered API, HTML, JavaScript, and SQLite database, which will allow users to explore a dataset interactively.
The result is a tool that allows users to analyse the maths grades of Portuguese high school students from two different schools. Users can view comparisons based on school location, student grades and students' demographic information such as travel time, and study time.


## Purpose ##

This project will explore whether there is any correlation between student demographics and final grades.

The first visualization will display the location of the two schools and students’ travel radius based on travel mode and travel time 

The second visualisation will investigate if there is any correlation between final grade, study time and travel time. 

The third visualisation will investigate if there is any correlation between student’s final grade and their motivation for higher education based on gender.

## Data Processing and Preparation ## 

The initial data is in CSV format. (student_math_clean.csv)

Using Pandas, this data is loaded on to a DataFrame. (students_data.py)

To create a meaningful analysis, certain parameters in the data required to be mapped. The code below shows the mapping criteria used –
![image](https://github.com/Leena-680/project-3-final/assets/144679119/5ff16e02-1056-431b-b094-a9e8e8bec877)

map_final_grade: Converts numeric grades to letter grades (A, B, C, D)

map_study_time: Maps study time to average hours

map_travel_time: Maps travel time to average minutes

The transformed DataFrame is written to an SQLite database (student_data.db) with table name (students).

## Web Application Development ##

The framework used is Flask. The Flask App features an interactive web interface to the front-end application. (app.py)

Calculates different measures used in Visualisation 1 and 2.

Provides RESTful end points for data retrieval.

When you run the app.py file it creates a JSON file with the required output for data visualisations. 
![image](https://github.com/Leena-680/project-3-final/assets/144679119/ca40dca0-2e4d-42dc-99a3-2dacf36a6b45)

## Frontend Implementation ## 

HTML and Javascript are utilized to fetch and manipulate data from the flask backend.

The app.js file fetches the data from the Flask App and portrays it in the front end. (visualisation_1.html - Mathematics Performance Dashboard)

The visualisations are created using MapBox, Plotly and Chart.js.

Charts update on user interaction.
 
## Data Visualization ## 

Our data analysis and visualisation are based on: 

Visualisation 1 - Displays the travel radius based on travel mode and travel time -  ISOCHRONE map using Mapbox and an Isochrone mapping API

Visualisation 2 - Comparing Final Grade to Average Study Time, Travel Time and Class Failures -  With the use of Plotly, created dynamic gauge charts to show the average study time, average travel time and total class failures for each grade.

Visualisation 3 - Comparing Final Grade to higher education goals- With the use of Chart.js, created a responsive pie chart to analyse if there is a co-relation between higher grades and higher education goals.
 
## Home Page ##

The home page is a html file which displays a brief description of what our group goal was in analysing the dataset as well as an image related to the data. Included on our home page is an easy to navigate menu with “a tags” which link to other template html synchronised with the flask app routes.
![visual 2](https://github.com/Leena-680/project-3-final/assets/145959658/5221c239-cf7b-44b1-8e01-e22c0c82dde6)


## Visualisation 1 ##

This visualisation is an ISOCHRONE map using Mapbox and an Isochrone mapping API, this visualisation shows where the schools are situated and the distance the students travel. The Isochrone API then creates layers depicting the distance and route students could possibly take regarding the travel time depending on their mode of travel. The API also takes in consideration local roads, traffic and environment to create an accurate depiction of where, how and how long these students travel.

### How use the visualisation ###
After selecting the visualisation link on the home page, the map will appear in the centre of the page with the two school markers. When the user has selected the mode of transportation and time travelled click on the marker and the isochrone layer will appear with the potential routes to the school and the area that students may live in around the schools.
![visual 1](https://github.com/Leena-680/project-3-final/assets/145959658/c9abec48-a5b0-4620-a372-05990d3b1a71)
![1 jpg](https://github.com/Leena-680/project-3-final/assets/145959658/575ea165-ae15-4911-b69f-eb5f2ab452dd)


## Visualisation 2 ## 

In this visualisation, we have analysed the time management skills of the students. 
Specifically, the correlation between final math grade, study time and travel time.

When we compare A graders to D graders, average travel time goes up from 11.8 minutes to 16.47 minutes but study time goes down from 4.78 hrs to 3.6 hours. The total class failures go up from 1 to 44. 

We can conclude that travel time does not have a strong correlation with final grade. But social and free time habits may have more impact on final grade.

This visualisation has been created using Plotly. 

![visual two](https://github.com/Leena-680/project-3-final/assets/145959658/536de6e9-9c36-4614-ba80-8d5bad4a12ef)


## Visualisation 3 ##

In this visualisation, we’re investigating the correlation between student’s final grade and their motivation for higher education based on gender.

Are students motivated to get good grades if they have a higher education goal?

From the visualisation, we can see that all the students who achieved A grades have higher education goals. When we select a D grade, 86.9% students have higher education goals. 86.9% is still a very high number. So we can conclude that just having a goal does not result in the highest final grade. Even though most of the students have higher education goal, they do not have good study strategies to get higher final grades.

Here I have used Chart.js to generate pie chart.

![visual three](https://github.com/Leena-680/project-3-final/assets/145959658/b545ccf6-3b7c-4d0c-a640-c3f940a4a890)


## Data set ##

This dataset contains student achievement data for a total of 382 students from two Portuguese high schools, Gabriel Pereira High School and  Mousinho da Silveira High School.

It includes student grades, demographics (age, gender, address type), family factors such as (parents’  education and vocation, family size, quality of family life), social factors (romantic relationship, extracurricular activities, alcohol consumption, social time) and school-related features (absences, extra school support, study time) to name a few.
The dataset originally included performance in Mathematics and English. We focused only on mathematics. 

## Data Ethics ##

This data was compiled using questionnaires and student reports. The use of questionnaires suggests the information was voluntarily surrendered. As it has information on minors, we are under the assumption that the data was collected with permission from the students' guardians. 

The data is anonymised and we could not find any information as to when exactly this dataset was collected, however, we do know it was before 2008. This ensures that anonymity is protected as the data is highly specific and sensitive, therefore if the collection year got released it has the potential to negate anonymity and the potential to do harm.  

This dataset is licensed under Creative Commons Attribution 4.0 International, meaning it can be shared (copied and redistributed in any medium or format for any purpose) and adapted (remix, transform and build upon the material for any purpose) as long as credit is given. 

## Dataset credit ##

We sourced the data set from Kaggle shared by Dillion Myrick. 

https://www.kaggle.com/datasets/dillonmyrick/high-school-student-performance-and-demographics/data  

The data’s original author is Paulo Cortez and was originally sourced from https://archive.ics.uci.edu/dataset/320/student+performance 

P. Cortez and A. Silva. Using Data Mining to Predict Secondary School Student Performance. In A. Brito and J. Teixeira Eds., Proceedings of 5th FUture BUsiness TEChnology Conference (FUBUTEC 2008) pp. 5-12, Porto, Portugal, April, 2008, EUROSIS, ISBN 978-9077381-39-7.

