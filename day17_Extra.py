import random
indian_states_capitals = [
    {"state": "Andhra Pradesh", "capital": "Amaravati"},
    {"state": "Arunachal Pradesh", "capital": "Itanagar"},
    {"state": "Assam", "capital": "Dispur"},
    {"state": "Bihar", "capital": "Patna"},
    {"state": "Chhattisgarh", "capital": "Raipur"},
    {"state": "Goa", "capital": "Panaji"},
    {"state": "Gujarat", "capital": "Gandhinagar"},
    {"state": "Haryana", "capital": "Chandigarh"},
    {"state": "Himachal Pradesh", "capital": "Shimla"},
    {"state": "Jharkhand", "capital": "Ranchi"},
    {"state": "Karnataka", "capital": "Bengaluru"},
    {"state": "Kerala", "capital": "Thiruvananthapuram"},
    {"state": "Madhya Pradesh", "capital": "Bhopal"},
    {"state": "Maharashtra", "capital": "Mumbai"},
    {"state": "Manipur", "capital": "Imphal"},
    {"state": "Meghalaya", "capital": "Shillong"},
    {"state": "Mizoram", "capital": "Aizawl"},
    {"state": "Nagaland", "capital": "Kohima"},
    {"state": "Odisha", "capital": "Bhubaneswar"},
    {"state": "Punjab", "capital": "Chandigarh"},
    {"state": "Rajasthan", "capital": "Jaipur"},
    {"state": "Sikkim", "capital": "Gangtok"},
    {"state": "Tamil Nadu", "capital": "Chennai"},
    {"state": "Telangana", "capital": "Hyderabad"},
    {"state": "Tripura", "capital": "Agartala"},
    {"state": "Uttar Pradesh", "capital": "Lucknow"},
    {"state": "Uttarakhand", "capital": "Dehradun"},
    {"state": "West Bengal", "capital": "Kolkata"}
]

state_capitals = [
    "Amaravati",
    "Itanagar",
    "Dispur",
    "Patna",
    "Raipur",
    "Panaji",
    "Gandhinagar",
    "Chandigarh",
    "Shimla",
    "Ranchi",
    "Bengaluru",
    "Thiruvananthapuram",
    "Bhopal",
    "Mumbai",
    "Imphal",
    "Shillong",
    "Aizawl",
    "Kohima",
    "Bhubaneswar",
    "Chandigarh",
    "Jaipur",
    "Gangtok",
    "Chennai",
    "Hyderabad",
    "Agartala",
    "Lucknow",
    "Dehradun",
    "Kolkata"
]

class StateCapitalQuiz:

    def __init__(self, data):
        self.data = data
        self.score = 0
        self.question_number = 0

    def create_choice_options(self, correct_answer):
        options = [correct_answer]
        while len(options) < 4:
            option = random.choice(state_capitals)
            if option not in options:
                options.append(option)  
        random.shuffle(options) 
        return options
                   

    def next_question(self ):
        current_data = self.data[self.question_number]
        print(f"What is the capital of {current_data['state']}? ")
        options = self.create_choice_options(current_data['capital'])
        for choice in options:
            print(choice)
        user_answer = input("Your answer: ")
        self.check_answer(user_answer, current_data['capital'])
        self.question_number += 1

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number + 1}.\n")

user_quiz = StateCapitalQuiz(indian_states_capitals)
while user_quiz.question_number < len(indian_states_capitals):
    user_quiz.next_question()