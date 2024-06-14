"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""

def display_title(title):
    print(f"{title}\n{'=' * len(title)}")

def main_menu():
    print("[A] View Data")
    print("[B] Visualize Data")
    print("[X] Exit")
    return input("Please enter your choice: ").strip().upper()

def view_data_menu():
    print("View Data Menu:")
    print("[A] View Reviews by Park")
    print("[B] Number of Reviews by Park and Location")
    print("[C] Average Score by Year")
    print("[D] Average Score by Park and Location")
    print("[X] Return to Main Menu")
    return input("Please enter your choice: ").strip().upper()

def visualize_data_menu():
    print("Visualize Data Menu:")
    print("[A] Most Reviewed Parks")
    print("[B] Average Scores")
    print("[C] Park Ranking by Nationality")
    print("[D] Most Popular Month by Park")
    print("[X] Return to Main Menu")
    return input("Please enter your choice: ").strip().upper()

def get_input(prompt):
    return input(prompt).strip()