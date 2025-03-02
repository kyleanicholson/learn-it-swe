from dataclasses import dataclass
import pyinputplus as pyip
from tabulate import tabulate
from typing import List
import pickle


@dataclass
class Exercise:
    name: str
    category: str


def create_exercise():
    """Creates an exercise based on user's inputs"""
    print("New Exercise Data Entry\n")
    name = pyip.inputStr("Exercise Name: ")
    category = pyip.inputMenu(
        numbered=True,
        choices=["Full Body", "Arms", "Legs", "Shoulders", "Chest", "Back"],
    )

    e = Exercise(name, category)

    return e


def add_exercise_to_list(exercise: Exercise, exercise_list: List) -> List[Exercise]:
    """Adds an exercise to an existing list and returns the updated list"""
    updated_list = exercise_list
    updated_list.append(e)
    return updated_list


def tabulate_exercise_list(exercise_list: List[Exercise]) -> None:
    """Prints the current list of exercises that have been added by the user"""
    print(
        tabulate(
            [(e.name, e.category) for e in exercise_list],
            headers=["Exercise Name", "Category"],
        )
    )


def save_exercise_list_to_file(
    exercise_list: List[Exercise], file_path: str = None
) -> None:
    """Saves the list to a .pkl file"""

    if file_path is None:
        file_path = pyip.inputFilepath("Enter file path: ")
    with open(file_path, "wb") as file:
        pickle.dump(exercise_list, file)


def load_exercise_list_from_file(file_path: str = None) -> List[Exercise]:
    """Loads an stored exercise list from a .pkl file"""
    if file_path is None:
        file_path = pyip.inputFilepath("Enter file path: ")
    with open(file_path, "rb") as file:
        exercise_list = pickle.load(file)

    return exercise_list


if __name__ == "__main__":
    load_existing_exercise_list = pyip.inputYesNo("Load exercise list from file? ")
    if load_existing_exercise_list == "yes":
        exercise_list = load_exercise_list_from_file()
        if exercise_list:
            print("Existing exercise list loaded successfully!")
            tabulate_exercise_list(exercise_list)
        else:
            print("Error loading exercise list: starting from blank list")
    else:
        exercise_list = []
    loop_count = 0
    while True:
        if loop_count == 0:
            create_new_exercise = pyip.inputYesNo("Create an exercise?: ")
        else:
            create_new_exercise = pyip.inputYesNo("Add another exercise?: ")
        if create_new_exercise == "yes":
            e = create_exercise()
            exercise_list = add_exercise_to_list(e, exercise_list)
            tabulate_exercise_list(exercise_list)
            loop_count += 1
        else:
            save_exercise_list = pyip.inputYesNo("Save exercise list to file?: ")
            if save_exercise_list == "yes":
                save_exercise_list_to_file(exercise_list)
            print("Exiting...")
            break
