# MAGIC 8-BALL (25pts)
# Create a tkinter app which acts as a "Magic 8-ball" fortune teller
# The user asks a yes/no question that they want an answer to.
# Then the user clicks a button, and your program displays
# the "magic" random answer to their question.
# Your program will have the following properties:
# - Use an App class to create the tkinter app
# - Add a proper title (appears in the window tab)
# - Add a Label widget at the top to give the user instructions/intro.
# - Add an Entry widget so the user can enter their question.
# - Add a Button widget which will trigger the answer.
# - Add a Label widget to display the answer (set to a initial value of "Your Fortune Here" or "--" or similar)
# - Get your random answer message from a list of at least 10 possible strings. (e.g. ["Yes", "No", "Most Likely", "Definitely", etc...])
# - Add THREE or more other style modifications to make your app unique (font family, font size, color, padding, image, borders, justification, whatever you can find in tkinter library etc.)  Make a comment at the top or bottom of your code to tell me your 3 things you did. (Just to help me out in checking your assignment)

#fbot.com to look up
#tkinter 8.5 reference

##############Modified the format of the title, fonts, and color


from tkinter import *
from tkinter.font import *
import random

class App():
    def __init__(self, master):

        #Title Font
        self.title_font = Font(family='Comic Sans MS', size=30)
        self.other_font = Font(family = 'Curlz MT', size = 20)

        #Variables
        self.entry_question = DoubleVar()
        self.entry_question.set('')

        self.fortune_text = DoubleVar()
        self.fortune_text.set("Get Your Fortune Here!")

        self.fortunes = ['Yes.', 'No.', 'Maybe So.', 'Lol! You wish.', 'Ask again.', 'Hard to tell at the moment.', 'For sure.', 'No chance.', 'It is certain.', 'Do not feel like answering right now.']

        #Title

        self.title = Label(master, text = 'Magic 8 Ball', font= self.title_font, bg = 'red', fg = 'gold', relief = 'raised', borderwidth = 5)
        self.title.grid(row=1, column = 1, columnspan = 2, sticky = 'w' + 'e', padx = 15, ipadx = 10, pady = 10)

        #Instructions
        self.instructions = Label(master, text = 'Please enter a yes or no question.', font = self.other_font)
        self.instructions.grid(row = 2, column = 1, columnspan = 2, sticky = 'e' + 'w')

        #Entry Widget
        self.ask = Label(master, text = 'Ask your question here.', font = self.other_font)
        self.ask.grid(row = 3, column = 1)

        self.ask_entry = Entry(master, textvariable = self.entry_question)
        self.ask_entry.grid(row = 3, column = 2)

        #Answer
        self.fortune = Label(master, textvariable = self.fortune_text, font = self.other_font)
        self.fortune.grid( row = 4, column = 2)

        #Button
        self.button = Button(master, text = "Get Fortune.", command = lambda: self.fortune_text.set(self.fortunes[random.randrange(len(self.fortunes))]))
        self.button.grid(row = 4, column = 1)




if '__main__' == __name__:
    root = Tk()
    root.title('Magic 8 Ball')
    my_app = App(root)
    root.mainloop()
