from dataclasses import dataclass
import pyinputplus as pyip
from tabulate import tabulate
from typing import List

@dataclass
class Exercise:
    name: str
    category: str


def create_exercise():
    """Allows user to input data for a new exercise"""
    print("New Exercise Entry\n")
    name = pyip.inputStr("Exercise Name: ")
    category = pyip.inputMenu(numbered=True, choices=['Full Body','Arms','Legs','Shoulders','Chest','Back'])

    e = Exercise(name, category)
    return e

def list_exercises(exercise_list:List[Exercise])-> None:
    print(tabulate(exercise_list, headers=['Exercise Name','Category']))


if __name__ == "__main__":
    exercise_list = []
    loop_count = 0
    while True:
        if loop_count ==0:
            create_new_exercise = pyip.inputYesNo("Create an exercise?: ") 
        else: 
            create_new_exercise = pyip.inputYesNo("Add another exercise?: ")
        if create_new_exercise == "yes":
            e = create_exercise()
            exercise_list.append(e)
            list_exercises(exercise_list)
            loop_count += 1
        else:
            print("Exiting...")
            break
