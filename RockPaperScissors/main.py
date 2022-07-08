import random
import textwrap
import tkinter as tk
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar


class RockPaperScissors(MDApp):
    def paper(self, args):
        self.y = 1
        return self.y
    def rock(self, args):
        self.y = 2
        return self.y
    def scissors(self, args):
        self.y = 3
        return self.y
    def random1(self, args):
        self.x = random.randrange(1,4)
        if int(self.x) == self.y:
            if self.x == 1:
                self.wyrandomowalo = "paper"
                print("wyrandomowalo: "+ self.wyrandomowalo)
            if self.x == 2:
                self.wyrandomowalo = "rock"
                print("wyrandomowalo: "+ self.wyrandomowalo)
                print("y=1")
            if self.x == 3:
                self.wyrandomowalo = "scissors"
                print("wyrandomowalo: " + self.wyrandomowalo)
                print("y=1")
            print("congrats")
            self.wynik = "You WIN!"
            print(self.y)
            print(self.x)
            self.x = random.randrange(1, 4)

        else:
            if self.x == 1:
                self.wyrandomowalo = "paper"
                print("wyrandomowalo: " + self.wyrandomowalo)
            if self.x == 2:
                self.wyrandomowalo = "rock"
                print("wyrandomowalo: " + self.wyrandomowalo)
            if self.x == 3:
                self.wyrandomowalo = "scissors"
                print("wyrandomowalo: " + self.wyrandomowalo)
            print(self.y)
            print(self.x)
            self.wynik = "You LOSE!"
            print("ups")
            self.x = random.randrange(1, 4)
        self.text.text = "Opponent shows " + self.wyrandomowalo
        self.text2.text = self.wynik


    def build(self):
        self.wynik = ""
        self.wyrandomowalo = "Hi try to play!"
        self.y=0
        screen = MDScreen()
        #Top Toolbar
        self.toolbar = MDToolbar(title="Rock, Paper or Scissors?")
        self.toolbar.pos_hint = {"top": 1}

        screen.add_widget(self.toolbar)


        #"Paper" button
        screen.add_widget(MDFillRoundFlatButton(
            text="Paper",
            font_size= 17,
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            on_press = self.paper
        ))
        # "Rock" button
        screen.add_widget(MDFillRoundFlatButton(
            text="Rock",
            font_size=17,
            pos_hint={"center_x": 0.3, "center_y": 0.35},
            on_press = self.rock
        ))
        # "Scissors" button
        screen.add_widget(MDFillRoundFlatButton(
            text="Scissors",
            font_size=17,
            pos_hint={"center_x": 0.7, "center_y": 0.35},
            on_press = self.scissors
        ))
        #"Fire" button
        screen.add_widget(MDFillRoundFlatButton(
            text="Show your cards!",
            font_size=17,
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            on_press=self.random1
        ))
        self.text = MDLabel(text=self.wyrandomowalo, pos_hint={'center_x': 0.9, 'center_y': 0.55})
        screen.add_widget(self.text)
        self.text2 = MDLabel(text=self.wynik, pos_hint={'center_x': 0.9, 'center_y': 0.7})
        self.text2.font_size = 50


        screen.add_widget(self.text2)

        return screen



if __name__ == '__main__':
    RockPaperScissors().run()