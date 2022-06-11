import random


class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        guess = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text}. "
                      f"((T)rue/(F)alse)?: ")
        if guess.startswith('T') or guess.startswith('t'):
            guess = "True"
            self.check_answer(guess, self.question_list[self.question_number].answer)

        elif guess.startswith('F') or guess.startswith('f'):
            guess = "False"
            self.check_answer(guess, self.question_list[self.question_number].answer)

        else:
            print("That's not a valid answer!\n")
            self.next_question()

    def check_answer(self, guess, answer):
        if guess == answer:
            self.question_number += 1
            print()
            if self.still_questions():
                self.next_question()
            else:
                pass

        elif guess != answer:
            print(f"Well ain't that cute....BUT IT'S WRONG!! You got {self.question_number} questions right\n")
            self.question_number = 0
            random.shuffle(self.question_list)
