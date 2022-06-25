import tkinter
from tkinter import *
import random
import json

# load questions and answer choices from json file
with open('./data.json', encoding="utf8") as f:
    data = json.load(f) 

# convert the dictionary in lists of questions and answers_choice 
questions = [value for value in data[0].values()]
answers_choice = [value for value in data[1].values()]
answers = [0,0,2,0,1,2,2,1,2,1,3,2,3,2] 


user_answer = []
indexes = []
def generateQuestion():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def showresult(score):
    questionLbl.destroy()
    rButton1.destroy()
    rButton2.destroy()
    rButton3.destroy()
    rButton4.destroy()
    
    labelresulttext = Label(
        root,
        font = ("Times",20),
        background = "#ffffff",
    )
    labelresulttext.pack(pady=(150,50))

    
    if score >= 20:
        labelresulttext.configure(text="You are Outstanding !!")
    elif (score >= 10 and score < 20):
        labelresulttext.configure(text="You are Good and can Be Better !!",)
    else:
        labelresulttext.configure(text="You are Poor and Should Work Hard !!")
    labelpoint = Label(
        root,
        text ="Your point is : "+str(score),
        font = ("Times",20),
        )
    labelpoint.pack()

def calculate():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
    showresult(score)


question = 1
def selected():
    global radioVariable,user_answer
    global questionLbl,rButton1,rButton2,rButton3,rButton4
    global question
    x = radioVariable.get()
    user_answer.append(x)
    radioVariable.set(-1)
    if question < 5:
        questionLbl.config(text= questions[indexes[question]])
        rButton1['text'] = answers_choice[indexes[question]][0]
        rButton2['text'] = answers_choice[indexes[question]][1]
        rButton3['text'] = answers_choice[indexes[question]][2]
        rButton4['text'] = answers_choice[indexes[question]][3]
        question += 1
    else:
        calculate()

def startquiz():
    global questionLbl,rButton1,rButton2,rButton3,rButton4
    questionLbl = Label(
        root,
        text = questions[indexes[0]] ,
        font = ( "Times", 16, "bold" ),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    questionLbl.pack(pady=(100,30))

    global radioVariable
    radioVariable = IntVar()
    radioVariable.set(-1)

    rButton1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Verdana", 12),
        value = 0,
        variable = radioVariable,
        command = selected,
        background = "#ffffff",
    )
    rButton1.pack(pady=5)

    rButton2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Verdana", 12),
        value = 1,
        variable = radioVariable,
        command = selected,
        background = "#ffffff",
    )
    rButton2.pack(pady=5)

    rButton3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Verdana", 12),
        value = 2,
        variable = radioVariable,
        command = selected,
        background = "#ffffff",
    )
    rButton3.pack(pady=5)

    rButton4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Verdana", 12),
        value = 3,
        variable = radioVariable,
        command = selected,
        background = "#ffffff",
    )
    rButton4.pack(pady=(5,100))


def startgame():
    labeltext.destroy()
    instructionLbl.destroy()
    startBtn.destroy()
    rulesLbl.destroy()
    generateQuestion()
    startquiz()

    
root = tkinter.Tk()
root.title("Quiz App")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)


labeltext = Label(
    root,
    text = "Welcome to the Quiz App ",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(100,50))


startBtn = Button(
    root,
    text = "Start the game",
    font = ("Times",14,"bold"),
    width = 50,
    height = 3,
    background="#00ffff",
    command = startgame,
)
startBtn.pack()


instructionLbl = Label(
    root,
    text = "Read The Rules:",
    background = "#00ffff",
    font = ("Consolas",16,"bold","underline"),
    justify = "center",
)
instructionLbl.pack(pady=(100,10))

rulesLbl = Label(
    root,
    text = "This quiz contains 5 questions.\nOnce you select a radio button that will be a final choice.\nClick Start Once You Are ready!!!",
    font = ("Times",14)
    
    )
rulesLbl.pack()

root.mainloop()

