""" Quizzical Version: 1.0
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.06.11-0841 """


import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


random.shuffle(question_bank)


g_show = QuizBrain(question_bank)

while g_show.still_questions():
    g_show.next_question()

print(f"Congrats you got all 12 questions right!!")
