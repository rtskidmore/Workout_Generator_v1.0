from flask import Flask, render_template, redirect, url_for, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import random

# data = pd.read_csv('exercises/exercises.txt')
# data.to_csv('exercises/exercises.csv')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///exercise-generator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class ExerciseList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equipment = db.Column(db.String(250), nullable=False)
    exercise = db.Column(db.String(250), nullable=False)


# db.create_all()
# data = pd.read_csv('exercises/exercises.csv')
# for index, row in data.iterrows():
#     new_item = ExerciseList(id=index, equipment=row['equipment'], exercise=row['exercise'])
#     db.session.add(new_item)
#     db.session.commit()

# exercise_data = db.session.query(ExerciseList).all()
# print(type(exercise_data[0]))
# equipment = input("Please select your equip: ")
# all_possible_exercises = ExerciseList.query.filter_by(equipment=equipment).all()
# exercise_list = []
# for i in all_possible_exercises:
#     exercise_list.append(i.exercise)
# print(exercise_list)

@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/workout', methods=["GET", "POST"])
def workout_page():
    if request.method == "POST":
        all_exercises = []
        equipment_list = request.form.getlist('mycheckbox')
        for item in equipment_list:
            possible_exercises = ExerciseList.query.filter_by(equipment=item).all()
            for i in possible_exercises:
                all_exercises.append(f"{i.equipment} {i.exercise}")
        new_workout = random.sample(all_exercises, 12)
        return render_template('workout.html', workout=new_workout)



if __name__ == "__main__":
    app.run(debug=True)
