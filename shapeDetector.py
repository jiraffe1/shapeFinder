#one of my early python programs from 2019
#which detects 3x3 shapes in a 400 "pixel" grid. 

import tkinter
from random import randint

#GUI setup
window = tkinter.Tk()
window.geometry('800x550')
window.title('Image finder 3x3')

#variables and lists setup
grid = []
colours = ['black','white']
target = []#list representing target
current_score = 0
scores = []


#generates the image randomly
def generate_list():
    for count in range(9):
        target.append(randint(0,1))
    for count in range(600):
        grid.append(randint(0,1))
    #at the beginning, all scores are set to 0.
    for count in range(400):
        scores.append(0)

def doScan():#filter
    for h in range(400):
        current_score = 0
        if grid[h] == target[4]:
            current_score += 1
        else:
            current_score -= 1
        if grid[h-21] == target[0]:
            current_score += 1
        if grid[h-20] == target[1]:
            current_score += 1
        if grid[h-19] == target[2]:
            current_score += 1
        if grid[h-1] == target[3]:
            current_score += 1
        if grid[h+1] == target[5]:
            current_score += 1
        if grid[h+19] == target[6]:
            current_score += 1
        if grid[h+20] == target[7]:
            current_score += 1
        if grid[h+21] == target[8]:
            current_score += 1
            #allows for different targets
        scores[h] = (current_score/5)
    
    GUI_with_filter()
def GUI_no_filter():   #I felt that there needed to be 2 separate GUI "settings"
            # one for before filters are applied and one for after.
    for i in range(20): #I also did this because i don't know any other ways around it 
        for j in range(20): #and this seemed like the simplest.
  
            btn = tkinter.Button(window,text=scores[(i*20)+j],background=colours[grid[(i*20)+j]], foreground='Blue')
            btn.grid(column=i,row=j)

    for k in range(3):
        for l in range(3):
            btn = tkinter.Button(window,text='    ',command=None,background=colours[target[k*3+l]])
            btn.grid(column=24+k,row=l)

    lbl = tkinter.Label(window,text='target ==>')
    lbl.grid(column=22,row=1)


    btn69 = tkinter.Button(window,text='Scan grid',command=doScan)
    btn69.grid(column=22,row=10)

        
def GUI_with_filter():
    #print(scores)
    for i in range(20):
        for j in range(20):
            if scores[(i*20)+j] == max(scores):
                btn = tkinter.Button(window,text=scores[(i*20)+j],background='Red',foreground='Black')
            elif scores[(i*20)+j] == min(scores):
                btn = tkinter.Button(window,text=scores[(i*20)+j],background='Blue',foreground='White')
            else:
                btn = tkinter.Button(window,text=scores[(i*20)+j],background=colours[grid[(i*20)+j]], foreground='Blue')
            btn.grid(column=i,row=j)

    for k in range(3):
        for l in range(3):
            btn = tkinter.Button(window,text='    ',command=None,background=colours[target[k*3+l]])
            btn.grid(column=24+k,row=l)

    lbl = tkinter.Label(window,text='target ==>')
    lbl.grid(column=22,row=1)
    lbl2 = tkinter.Label(window,text='most alike')
    lbl2.grid(column=22,row=3)
    lbl3 = tkinter.Label(window,text=(str(round(max(scores)/1.8)*100))+'%')
    lbl3.grid(column=22,row=4)
    lbl5 = tkinter.Label(window,text='least alike')
    lbl5.grid(column=22,row=5)
    lbl6 = tkinter.Label(window,text=(str(round(min(scores)/1.8)*100))+'%')
    lbl6.grid(column=22,row=6)
    if max(scores) == 1.8:
        lbl4 = tkinter.Label(window,text='Match detected!')
    else:
        lbl4 = tkinter.Label(window,text='No complete matches!')
        
    lbl4.grid(column=22,row=7)
    
    if min(scores) == -0.2:
        lbl4 = tkinter.Label(window,text='full anti-Target detected!')
    else:
        lbl4 = tkinter.Label(window,text='No anti-Targets!')
        
    lbl4.grid(column=22,row=8)

    btn6 = tkinter.Button(window,text='Do filter',command=doFilter)
    btn6.grid(column=22,row=10)

generate_list()
#print(grid)
GUI_no_filter()


