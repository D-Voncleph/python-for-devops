#! python3
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random
import os
import shutil
import time

# Set the time limit in seconds (e.g., 1 hour = 3600 seconds)
TIME_LIMIT = 3600

# The quiz data. Keys are states and values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 
'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Create a folder to store the quizzes
quiz_folder = "capitals_quizzes"

# Check if the quiz folder exists and if it's older than the time limit
if os.path.exists(quiz_folder):
    folder_creation_time = os.path.getmtime(quiz_folder)
    if (time.time() - folder_creation_time) > TIME_LIMIT:
        print(f"'{quiz_folder}' is older than {TIME_LIMIT} seconds. Deleting it.")
        shutil.rmtree(quiz_folder)
        print("Directory deleted.")

# This will create the folder if it doesn't already exist
os.makedirs(quiz_folder, exist_ok=True)

# Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quiz_filename = os.path.join(quiz_folder, f'capitalsquiz{quizNum + 1}.txt')
    answerkey_filename = os.path.join(quiz_folder, f'capitalsquiz_answers{quizNum + 1}.txt')
    
    with open(quiz_filename, 'w') as quizFile, open(answerkey_filename, 'w') as answerKeyFile:
        # Write out the header for the quiz.
        quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
        quizFile.write(f"{' ' * 20}State Capitals Quiz (Form {quizNum + 1})\n\n")

        # Shuffle the order of the states.
        states = list(capitals.keys())
        random.shuffle(states)
        
        all_capitals = list(capitals.values())

        # Loop through all 50 states, making a question for each one.
        for questionNum in range(50):
            # Get right and wrong answers.
            correctAnswer = capitals[states[questionNum]]
            
            # Get a list of all capitals except the correct one.
            wrong_capitals = [c for c in all_capitals if c != correctAnswer]
            wrongAnswers = random.sample(wrong_capitals, 3)
            
            answerOptions = wrongAnswers + [correctAnswer]
            random.shuffle(answerOptions)

            # Write the question and answer options to the quiz file.
            quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
            for i in range(4):
                quizFile.write(f" {'ABCD'[i]}. {answerOptions[i]}\n")
            quizFile.write('\n')
            
            # Write the answer key to a file.
            answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")