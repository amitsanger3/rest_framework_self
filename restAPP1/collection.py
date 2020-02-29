from .models import *
import pandas as pd


def enter_data():
    data = pd.read_csv('data.csv')
    print(data.head())
    for i in range(data.shape[0]):
        student = data.iloc[i]
        new_student = Student(
            first_name=student['First Name'],
            last_name=student['Last Name'],
            gender=student['Gender'],
            age=int(student['Age']),
            email=student['Email']
        )
        new_student.save()
    return None
