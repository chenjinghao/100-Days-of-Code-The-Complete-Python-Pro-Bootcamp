from tkinter import *
from tkinter import ttk
from random import randint
import time

global content_entered
global test_content
global test_startTime
global test_endTime

root = Tk()
root.title('Typing Speed Test -Adam CHEN JINGHAO')

mainframe = ttk.Frame(root, padding ='5')
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0,weight=1)

content = [
    "Believe in your potential",
    "Chase your dreams fearlessly",
    "Never give up on yourself",
    "Hard work always pays off",
    "Stay true to your vision"
]

def start():
    global content_entered, test_content, test_startTime
    test_startTime = time.time()
    random_pick = randint(0,4)
    test_content = content[random_pick]
    ttk.Label(mainframe, text=' ').grid(column=1,row=7)
    ttk.Label(mainframe, text=test_content).grid(column=1,row=8)
    content_entered = StringVar()
    ttk.Entry(mainframe,textvariable=content_entered).grid(column=1,row=9)
    ttk.Button(mainframe, text='FINISH', command=finish).grid(column=1,row=10)

    return content_entered,test_content, test_startTime

def finish():
    global content_entered,test_content, test_endTime, test_startTime
    test_endTime = time.time()
    content_entered = content_entered.get()
    content_entered_splited = content_entered.split()
    test_content_splited = test_content.split()
    
    test_word_count = 0
    for word in test_content_splited:
        test_word_count += 1

    num_corrected = 0
    for word_entered in content_entered_splited:
        for word_test in test_content_splited:
            if word_entered == word_test:
                num_corrected += 1
    


    ttk.Label(mainframe,text=f'You type: {content_entered}').grid(column=1,row=11)
    ttk.Label(mainframe,text=f'You get {num_corrected} correct out of {test_word_count}').grid(column=1,row=12)
    time_taken = test_endTime - test_startTime
    time_taken = round(time_taken,2)
    ttk.Label(mainframe,text=f'Total time taken is {time_taken} sec!').grid(column=1,row=13)

    if num_corrected == test_word_count:
        ttk.Label(mainframe,text='Good JOB!').grid(column=1,row=14)
    else:
        ttk.Label(mainframe,text='Try Harder!').grid(column=1,row=14)
    


ttk.Label(mainframe, text='Welcome',font=("36")).grid(column=1,row=0)
ttk.Label(mainframe, text='my Typing Speed Tester', font=('24')).grid(column=1,row=1)
ttk.Label(mainframe, text='-Adam CHEN JINGHAO',font=('12')).grid(column=1,row=2, sticky=(E))
ttk.Label(mainframe, text=' ').grid(column=1,row=3)
tester_rule = 'Click the START button below and the time to start calculate until you finish typing and click the FINISH when you finish.'
ttk.Label(mainframe, text=tester_rule).grid(column=1, row=4, rowspan=2)

test = ttk.Button(mainframe, text='START',command=start).grid(column=1,row=6)



root.mainloop()