from random import choice


class BandGenerator():
    a_list = open('adjectives.txt', 'r').readlines()
    b_list = open('nouns.txt', 'r').readlines()

    def name(self):
        band = choice(self.a_list).title().strip() + ' ' + choice(self.b_list).title().strip()
        name = f"Rock on {band}!!"
        print(name)

