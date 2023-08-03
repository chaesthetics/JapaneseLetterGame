import random
from tkinter import * 
from tkinter import messagebox   
import tkinter as tk

root = Tk()
root.title('Japanese Letter Game')
root.config(bg="skyblue")

statusFrame = Label(root, width=18, height=3, font=("Arial", 15), text='score: 0 \n mistakes: 0', bg='cyan4', fg='yellow2')
resetButton = Button(root, width=10, height=1, font=("Arial", 15), text="reset", bg='firebrick3', fg='gray12', borderwidth=0)
letterFrame = Label(root, width=2, height=0, font=("Arial", 100), bg='white', text='ほ', fg='dark orchid')
entry = Entry(root, width=10, font=("Arial", 20))
enterButton = Button(root, width=5, height=0, font=("Arial", 14), text='Enter', bg='green3', fg='white')

resetButton.grid(row=0, column=0, sticky='SW', padx='25', pady='30')
statusFrame.grid(row=0,  column=0, padx=25, pady=30)
letterFrame.grid(row=0, column=1, padx=40, pady=40)
entry.grid(row=1, column=1, padx=5, pady=10, sticky='W')
enterButton.grid(row=1, column=1, padx=10, sticky='E', pady=10)


jLetters = ['あ','い','う','え','お','は','ひ','ふ','へ','ほ',
            'か','き','く','け','こ','ま','み','む','め','も',
            'さ','し','す','せ','そ','や','ゆ','よ','た','ち',
            'つ','て','と','ら','り','る','れ','ろ','な','に',
            'ぬ','ね','の','わ','ゐ','ん','ゑ','を']

eLetter = ['a','i','oo','e','o','ha','hi','fu','he','ho',
           'kka','ki','ko','ke','ko','ma','mi','mu','mi','mo',
           'sa','shi','su','se','so','ya','yu','yo','ta','chi',
           'tsu','te','to','ra','ri','ru','re','ro','na','ni',
           'nu','ne','no','wa','wi','n','we','wo']


score = 0
mistake = 0

i = 0
while i < 10:
  
  randomNumber = (random.randint(0,47))
  value = input(jLetters[randomNumber])

  if(value == eLetter[randomNumber]):
    score+=1
  else:
    mistake+=1

  Score = "score: "
  Mistake = "mistake: "
  print(Score+str(score))
  print(Mistake+str(mistake))

  i += 1



  root.mainloop()