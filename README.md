# Python-GUI-API-Quiz-App-Day-34

### What I learned:

Fetching API data, working with object instances and methods of classes, organizing code into separate files. Wrapping everything in a UI. This got me confused couple of times, but I managed to work my way through this ✔

<!-- ![grab-landing-page](https://github.com/skaftisveins/Python-Tkinter-Password-Manager-Day-29/blob/master/demo.gif) -->

![ScreenShot](https://github.com/skaftisveins/Python-GUI-API-Quiz-App-Day-34/blob/master/demo.gif)

### Files and what they do

### data.py: 
import data from opentdb.com with paramaters. Convert to json

### question_model.py: 
class Question with q_text and q_answer instance attributes

### quiz_brain.py:
import html to use unescape on fx. quote characters in a string

class QuizBrain with q_list instance attribute and the following instance methods:
still_has_questions()
next_question()
check_answer()

### ui.py:
from tkinter import *
import QuizBrain

class QuizInterface with quiz_brain instance attribute and the following instance methods:
get_next_question()
true_pressed()
false_pressed()
give_feedback()

