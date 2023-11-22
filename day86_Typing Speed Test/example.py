Home
100 Days of Code: The Complete Python Pro Bootcamp for 2023
Instructions
Submission
Instructor example
Give feedback
How did you do?
Compare the instructor's example to your own
Instructor example

Dr. Angela Yu
Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

This is your developer diary. There is no right or wrong, only learnings.

Your submission
C
CHEN JINGHAO
Posted A few seconds ago
Reflection Time:

This is a place to journal your experience of completing this project. This will help you figure out how to improve as a developer.

Write down how you approached the project. What was hard, what was easy. How might you improve for the next project? What was your biggest learning from today? What would you do differently if you were to tackle this project again?

https://replit.com/@chenjinghao/day86Typing-Speed-Test



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
How did you do on this exercise?

Take a moment to reflect on what you learned from this exercise

C
Add feedback...
I learned...
Course content
Start
Assignment 5: Typing Speed Test
Master Python by building 100 projects in 100 days. Learn data science, automation, build websites, games and apps!
Rating: 4.7 out of 5
4.7
241,476 ratings
1,041,321
Students
58 hours
Total
Last updated October 2023
English
English, Arabic [Auto]
, 
What you'll learn
You will master the Python programming language by building 100 unique projects over 100 days.
You will learn automation, game, app and web development, data science and machine learning all using Python.
You will be able to program in Python professionally
You will learn Selenium, Beautiful Soup, Request, Flask, Pandas, NumPy, Scikit Learn, Plotly, and Matplotlib.
Create a portfolio of 100 Python projects to apply for developer jobs
Be able to build fully fledged websites and web apps with Python
Be able to use Python for data science and machine learning
Build games like Blackjack, Pong and Snake using Python
Build GUIs and Desktop applications with Python
Description
Welcome to the 100 Days of Code - The Complete Python Pro Bootcamp, the only course you need to learn to code with Python. With over 500,000 5 STAR reviews and a 4.8 average, my courses are some of the HIGHEST RATED courses in the history of Udemy!  

100 days, 1 hour per day, learn to build 1 project per day, this is how you master Python.

At 60+ hours, this Python course is without a doubt the most comprehensive Python course available anywhere online. Even if you have zero programming experience, this course will take you from beginner to professional. Here's why:

The course is taught by the lead instructor at the App Brewery, London's best in-person programming Bootcamp.

The course has been updated to be 2023 ready and you'll be learning the latest tools and technologies used at large companies such as Apple, Google and Netflix.

This course doesn't cut any corners, there are beautiful animated explanation videos and tens of real-world projects which you will get to build. e.g. Tinder auto swiper, Snake game, Blog Website, LinkedIn Auto Submit Job Application

The curriculum was developed over a period of 2 years, with comprehensive student testing and feedback.

We've taught over 600,000 students how to code and many have gone on to change their lives by becoming professional developers or starting their own tech startup.

You'll save yourself over $12,000 by enrolling, and still get access to the same teaching materials and learn from the same instructor and curriculum as our in-person programming Bootcamp.

The course is constantly updated with new content, with new projects and modules determined by students - that's you!



We'll take you step-by-step through engaging video tutorials and teach you everything you need to know to succeed as a Python developer.

The course includes over 65 hours of HD video tutorials and builds your programming knowledge while making real-world Python projects.



Throughout this comprehensive course, we cover a massive amount of tools and technologies, including:

Python 3 - the latest version of Python

PyCharm, Jupyter Notebook, Google Colab

Python Scripting and Automation

Python Game Development

Web Scraping

Beautiful Soup

Selenium Web Driver

Request

WTForms

Data Science

Pandas

NumPy

Matplotlib

Plotly

Scikit learn

Seaborn

Turtle

Python GUI Desktop App Development

Tkinter

Front-End Web Development

HTML 5

CSS 3

Bootstrap 4

Bash Command Line

Git, GitHub and Version Control

Backend Web Development

Flask

REST

APIs

Databases

SQL

SQLite

PostgreSQL

Authentication

Web Design

Deployment with GitHub Pages, Heroku and GUnicorn

and much much more!

By the end of this course, you will be fluently programming in Python and you'll be so good at Python that you can get a job or use the language professionally.

You'll also build a portfolio of 100 projects that you can show off to any potential employer. Including:

Blackjack

Snake Game

Pong Game

Auto Swipe on Tinder

Auto Job Applications on LinkedIn

Automate Birthday Emails/SMS

Fully Fledged Blog Website

Build Your Own Public API

Data Science with Google Trends

Analysing Lego Datasets

Google App Store Analysis

and much much more!

Sign up today, and look forward to:

Video Lectures

Code Challenges and Exercises

Fully Fledged Projects

Quizzes

Programming Resources and Cheatsheets

Downloads

Our best selling 12 Rules to Learn to Code eBook

$12,000+ Python Pro Bootcamp course materials and curriculum



Don't just take my word for it, check out what existing students have to say about my courses:

"Angela is just incredible, awesome and just fantastic in this course. I've never had such an instructor; detailed in every aspect of the course, gives precise explanations, gives you the anxiety to learn etc. She's got that ability to make fun while explaining things for better understanding. I really love this course." - Ekeu MonkamUlrich

"Angela is very thorough without ever being boring. I've taken MANY online courses in my life including my Bachelors and Masters degrees. She is by far the best instructor I've ever had. This course is packed with thousands of dollars worth of great instruction, and paced well enough for anyone to pick coding up and run with it- Thank you!" - J Carlucci

"Love the way Angela explains things. Easy to follow and full of logic. I can say she must spend a lot of energy creating this great course. Thank you and I recommend it to all who's interested in coding!" - Yiqing Zheng

"So far (on my third day) this course has taught me more than I was able to learn in multiple other programming courses. This course is clearly outlined and builds upon itself gradually in an easy to understand way." - Normal Ramsey

"It's a different approach to teaching Web Development. I like that you are given everything possible to succeed from the onset." - Ronick Thomas

The tutor is simply AMAZING, by far the best tutor I have ever had. I would give her 10 stars out of 5. She is not just punching the code and talking to herself, but she is actually explaining things. She keeps on giving really useful hints and she will give you a great load of other references. I always knew what I was doing and why I was doing it. All the extra challenges have just made me remember and understand things better. - Peter Dlugos





REMEMBER… I'm so confident that you'll love this course that we're offering a FULL money-back guarantee for 30 days! So it's a complete no-brainer, sign up today with ZERO risk and EVERYTHING to gain.

So what are you waiting for? Click the buy now button and join the world's highest-rated development course.

Who this course is for:
If you want to learn to code from scratch through building fun and useful projects, then take this course.
If you want to start your own startup by building your own websites and web apps.
If you are a complete beginner then this course will be everything you need to become a Python professional
If you are a seasoned programmer wanting to switch to Python then this is the quickest way. Learn through coding projects.
If you are an intermediate Python programmer then you know 100 days of code challenges will help you level up.
Instructor
Dr. Angela Yu
Developer and Lead Instructor
I'm Angela, I'm a developer with a passion for teaching. I'm the lead instructor at the London App Brewery, London's leading Programming Bootcamp. I've helped hundreds of thousands of students learn to code and change their lives by becoming a developer. I've been invited by companies such as Twitter, Facebook and Google to teach their employees.

My first foray into programming was when I was just 12 years old, wanting to build my own Space Invader game. Since then, I've made hundred of websites, apps and games. But most importantly, I realised that my greatest passion is teaching.

I spend most of my time researching how to make learning to code fun and make hard concepts easy to understand. I apply everything I discover into my bootcamp courses. In my courses, you'll find lots of geeky humour but also lots of explanations and animations to make sure everything is easy to understand.

I'll be there for you every step of the way.

Featured review
David K.
49 courses
35 reviews
Rating: 5.0 out of 5
2 years ago
Angela is a great teacher and I have taken some other courses of hers. This one seems to be of the same great quality. If you want a simple code-along, this is not for you. Angela will Challenge you to actually use what she teaches you many times along the way. You WILL know how to program Python when you finish this course!
Was this review helpful?

Requirements
No programming experience needed - I'll teach you everything you need to know
A Mac or PC computer with access to the internet
No paid software required - I'll teach you how to use PyCharm, Jupyter Notebooks and Google Colab
I'll walk you through, step-by-step how to get all the software installed and set up
Get the app
About us
Help and Support
Terms
Privacy policy
Sitemap
Accessibility statement
© 2023 Udemy, Inc.

