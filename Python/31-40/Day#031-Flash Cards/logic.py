""" OOP: Logic for Phrase Cards!
    Coded by TechGYQ
    www.MythosWorks.com
    OC:2022.08.17-1954
    R1:2023.01.22-0123 """

# Imports
import sys
import tkinter.ttk

import googletrans
from random import randint
import pandas as pd
from tkinter import *

# Supported languages for app.
options_dict = {'ja': "https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Japanese2015_10000",
                'es': 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Spanish1000',
                'fr': 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/French_wordlist_opensubtitles_5000',
                'de': 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/German_subtitles_1000',
                'ga': 'https://github.com/michmech/irish-word-frequency/blob/master/frequency.txt',
                'iw': 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Hebrew/00#1-10000'}

# Dictionary of Country flags and color themes for question cards & buttons.
flag_dict = {'ja-background': '#BC002D',
             'ja-text': '#FFFFFF',
             'es-background': '#006341',
             'es-text': '#FFFFFF',
             'fr-background': '#002654',
             'fr-text': '#FFFFFF',
             'de-background': '#FFCC00',
             'de-text': '#000000',
             'ga-background': '#009A44',
             'ga-text': '#FFFFFF',
             'iw-background': '#0038B8',
             'iw-text': '#FFFFFF'}


# Main game logic, creates buttons & and creates items.
class Logic:
    """ Fetches all data for card game and keeps tally """

    def __init__(self):
        self.background_color = '#000000'
        self.url = 'https://en.wiktionary.org/wiki/Wiktionary:Frequency_lists/Japanese2015_10000'
        self.data = pd.read_html(self.url)[0].values.T
        self.language_data = pd.DataFrame(columns=['Word'])
        self.col_num = 2
        self.language_data['Word'] = self.data[self.col_num]
        self.transpose = googletrans.Translator()

        # TK Setup.
        self.display = Tk()
        self.display.title('Phrase Cards')
        self.display.config(padx=30, pady=30, bg=self.background_color)

        # Others.
        self.PBar = tkinter.ttk.Progressbar(orient='horizontal', mode='determinate', length=280)
        self.load_text = Label(text='', bg='black', fg='white')

        # Buttons.
        self.btn_Japan = Button(width=10, text='Japanese', command=lambda: self.lang_packs('ja'),
                                bg=flag_dict['ja-background'], fg=flag_dict['ja-text'])
        self.btn_Spanish = Button(width=10, text='Spanish', command=lambda: self.lang_packs('es'),
                                  bg=flag_dict['es-background'], fg=flag_dict['es-text'])
        self.btn_French = Button(width=10, text='French', command=lambda: self.lang_packs('fr'),
                                 bg=flag_dict['fr-background'], fg=flag_dict['fr-text'])
        self.btn_German = Button(width=10, text='German', command=lambda: self.lang_packs('de'),
                                 bg=flag_dict['de-background'], fg=flag_dict['de-text'])
        self.btn_Irish = Button(width=10, text='Irish', command=lambda: self.lang_packs('ga'),
                                bg=flag_dict['ga-background'], fg=flag_dict['ga-text'])
        self.btn_New = Button(width=10, text="Hebrew", command=lambda: self.lang_packs('iw'),
                              bg=flag_dict['iw-background'], fg=flag_dict['iw-text'])
        self.btn_Continue = Button(width=15, text='Continue', command=self.game_screen, bg='#000000', fg='#FFFFFF')
        self.btn_Language = Button(width=15, text='Swap Language', command=self.start_screen, bg='#000000',
                                   fg='#FFFFFF')
        self.btn_Quit = Button(width=15, text='Quit Playing', command=sys.exit, bg='#000000', fg='#FFFFFF')

        # Start screen.
        self.start_screen()

        # Game screen item load
        self.backdrop = Canvas(width=300, height=300)
        self.logo_img = PhotoImage(file='images/card_back.png')
        self.backdrop.create_image(75, 100, image=self.logo_img)

        # Questions & Answer data
        self.nums = []
        self.questions = []
        self.answers = []
        self.total = 0
        self.guessed = 0

        # Code in game logic must have stats.
    def score(self):
        percentage = round(100 * float(self.guessed) / float(self.total))
        print(f"%s of %s guessed correctly! That's %s%% accurate!" % (self.guessed, self.total, percentage))

# Fetches selected language data & questions
    def fetch(self):
        # TODO update url with selected language pack fix issues with fetching data!!!!!!!!.
        # self.tables = pd.read_html(self.url)
        self.data = pd.read_html(self.url)[0].values.T
        self.language_data = pd.DataFrame(columns=['Word'])
        self.language_data['Word'] = self.data[self.col_num]
        print(self.language_data)
        x = 10
        i = 0

        while x > 0:
            x -= 1
            self.nums.append(randint(0, len(self.data[self.col_num])))

        for item in self.nums:
            p = 10
            i += 1
            percentage = round(100 * float(i) / float(p))
            self.PBar['value'] = i * 10
            self.PBar.update()
            self.load_text.config(text=f'Picking questions! {percentage}% of 100% loaded')
            word = self.language_data['Word'].iloc[item]
            answer = self.transpose.translate(word, dest='en')
            self.questions.append(word)
            self.answers.append(answer.text)

        self.game_screen()
        print(self.questions, self.answers)

# Fetches new questions and resets lists
    def new_questions(self):
        self.nums.clear()
        self.questions.clear()
        self.answers.clear()
        self.fetch()

# Select Language to learn.
    def lang_packs(self, item):
        # ja, es, fr, de, ga, iw
        if item == 'ja':
            self.url = options_dict['ja']
            self.col_num = 2
            self.load_screen()
            self.new_questions()
        elif item == 'es':
            self.url = options_dict['es']
            self.col_num = 1
            self.load_screen()
            self.new_questions()
        elif item == 'fr':
            self.url = options_dict['fr']
            self.col_num = 1
            self.load_screen()
            self.new_questions()
        elif item == 'de':
            self.url = options_dict['de']
            self.col_num = 1
            self.load_screen()
            self.new_questions()
        elif item == 'ga':
            self.url = options_dict['ga']
            self.col_num = 1
            self.load_screen()
            self.new_questions()
        elif item == 'iw':
            self.url = options_dict['iw']
            self.col_num = 0
            self.load_screen()
            self.new_questions()
        else:
            print('We got a problem scotty!')

# Clears all items from game screen. Used to switch views or start new set of questions
    def clear_screen(self):
        self.btn_Japan.grid_forget()
        self.btn_Spanish.grid_forget()
        self.btn_French.grid_forget()
        self.btn_German.grid_forget()
        self.btn_Irish.grid_forget()
        self.btn_New.grid_forget()
        self.btn_Continue.grid_forget()
        self.btn_Language.grid_forget()
        self.PBar.grid_forget()
        self.load_text.grid_forget()
        self.btn_Quit.grid_forget()

    def load_screen(self):
        self.clear_screen()
        self.PBar.grid(row=0, column=0)
        self.load_text.grid(row=2, column=0)

# Starting screen to select language to learn.
    def start_screen(self):
        self.clear_screen()
        self.btn_Japan.grid(row=0, column=0)
        self.btn_Spanish.grid(row=0, column=1)
        self.btn_French.grid(row=1, column=0)
        self.btn_German.grid(row=1, column=1)
        # self.btn_Irish.grid(row=2, column=0)
        # self.btn_New.grid(row=2, column=1)

# Game screen holds question, answer and 2 false answers also keeps score.
    # TODO Implement game screen with 3 possible answers and have card flip after answer
    def game_screen(self):
        self.clear_screen()
        self.backdrop.grid(column=1, row=0)

# TODO implement messagebox to change language or try again!
    def menu_screen(self):
        self.clear_screen()
        self.background_color = '#000000'
        self.btn_Continue.grid(row=0, column=0)
        self.btn_Language.grid(row=0, column=2)
        self.btn_Quit.grid(row=1, column=1)
