""" OOP: Logic for Phrase Cards!
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.08.17-1954 """

# Imports
import googletrans
from random import randint, choice
import pandas as pd
from tkinter import *
from tkinter import messagebox

options_dict = {'jp': "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Japanese2015_10000", 'es': '',
                'fr': ''}


class Logic:
    """ Fetches all data for card game and keeps tally """

    def __init__(self):
        self.background_color = '#B1DDC6'
        self.url = 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Japanese2015_10000'
        # self.tables = pd.read_html(self.url)
        self.data = pd.read_html(self.url)[0].values.T
        self.language_data = pd.DataFrame(columns=['Word'])
        self.language_data['Word'] = self.data[2]
        self.transpose = googletrans.Translator()
        self.display = Tk()
        self.display.title('Phrase Cards')
        self.display.config(padx=30, pady=30, bg=self.background_color)
        self.backdrop = Canvas(width=300, height=300)
        self.logo_img = PhotoImage(file='images/card_front.png')
        self.backdrop.create_image(75, 100, image=self.logo_img)
        self.backdrop.grid(column=1, row=0)
        self.nums = []
        self.questions = []
        self.answers = []
        self.total = 0
        self.guessed = 0

# Fetches selected language data & questions
    def fetch(self):
        x = 10
        i = 0

        while x > 0:
            x -= 1
            self.nums.append(randint(0, len(self.data[2])))

        for item in self.nums:
            p = 10
            i += 1
            percentage = round(100 * float(i) / float(p))
            print(f'{percentage}% of 100%')
            word = self.language_data['Word'].iloc[item]
            answer = self.transpose.translate(word)
            self.questions.append(word)
            self.answers.append(answer.text)

        print(self.questions, self.answers)

# Fetches new questions and resets lists
    def new_questions(self):
        self.nums.clear()
        self.questions.clear()
        self.answers.clear()
        self.fetch()

# TODO Implement starting screen to pick language

# TODO Implement game screen with 3 possible answers and have card flip after answer

# TODO implement messagebox to change language or try again!
