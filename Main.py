import random
from tkinter import * 
from tkinter import messagebox   
import tkinter as tk

root = Tk()
root.title('Japanese Letter Game')
root.config(bg="skyblue")

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

inputValue = ''
score = 0
mistakes = 0
randomNumber = random.randrange(len(eLetter)-1)
randomLetter = jLetters[randomNumber]
counter = 0

def getInput():
    global randomLetter
    global entry
    global randomNumber
    global mistakes
    global score
    global counter

    inputValue = entry.get()
    if(inputValue == eLetter[randomNumber]):
        score+=1
    else:
        mistakes+=1

    randomNumber = random.randrange(len(eLetter)-1)
    randomLetter = jLetters[randomNumber]
    letterFrame['text'] = randomLetter
    statusFrame['text'] = 'score: ' + str(score) + '\n mistakes: ' + str(mistakes)
    entry.delete(0, END)

    counter+=1
    
    if counter==15:
        if score>=12:
            messagebox.showinfo(title="Excellent", message="You can now go to Japan !!")
            clearData()
        elif score>8 and score<12:
            messagebox.showinfo(title="Not bad", message="You have passed the test.")
            clearData()
        else:
            messagebox.showinfo(title="Failed", message="Better luck next time mwehehe")
            clearData()

def clearData():
    global randomLetter
    global entry
    global randomNumber
    global mistakes
    global score
    global mistakes
    global counter

    entry.delete(0, END)
    mistakes = 0
    score = 0
    counter = 0
    statusFrame['text'] = 'score: ' + str(score) + '\n mistakes: ' + str(mistakes)
    randomNumber = random.randrange(len(eLetter)-1)
    randomLetter = jLetters[randomNumber]
    letterFrame['text'] = randomLetter


    



  
statusFrame = Label(root, width=18, height=3, font=("Arial", 15), text='score: 0 \n mistakes: 0', bg='cyan4', fg='yellow2')
resetButton = Button(root, width=10, height=1, font=("Arial", 15), text="reset", bg='firebrick3', fg='gray12', borderwidth=0, command=clearData)
letterFrame = Label(root, width=2, height=0, font=("Arial", 100), bg='white', text=randomLetter, fg='dark orchid')
entry = Entry(root, width=10, font=("Arial", 20))
enterButton = Button(root, width=5, height=0, font=("Arial", 14), text='Enter', bg='green3', fg='white',
                     command=getInput)

resetButton.grid(row=0, column=0, sticky='SW', padx='25', pady='30')
statusFrame.grid(row=0,  column=0, padx=25, pady=30)
letterFrame.grid(row=0, column=1, padx=40, pady=40)
entry.grid(row=1, column=1, padx=5, pady=10, sticky='W')
enterButton.grid(row=1, column=1, padx=10, sticky='E', pady=10)



root.mainloop()