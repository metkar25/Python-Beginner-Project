from tkinter.messagebox import QUESTION
from question_model import QuestionModel
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = QuestionModel(question_text , question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("-------------------------------------------------------------------------------------------------")
print(f"You have completed the quiz, Your final score was {quiz.score}/{quiz.question_number} ")
print("-------------------------------------------------------------------------------------------------")