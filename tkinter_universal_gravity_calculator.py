# Universal Gravity Calculator (30pts)
# In physics, the force of gravity between two objects
# can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters

# Make a tkinter app with the following attributes:
# - use an App class
# - Add a title.
# - Make a label and entry widget for m1, m2, and r
# - Make a "Calculate" button widget to trigger a lambda function
# - Add a calculate label widget to display the answer
# - Make exceptions for division by zero and type conversion errors.
# - When "Calculate" is pushed, the result is displayed.  Yay!
# - Add an exception for the possible entry of zero radius (ZeroDivisionError Exception)
# - Make your app unique by changing 3 or more DIFFERENT style attributes or kwargs for your app.  Perhaps consider: fonts, color, padding, widths, etc).  Put a comment in your code to tell me what you changed. If you change the font for all the widgets, that is ONE thing.  If you add padx to all your app widgets, that is ONE thing.  If you change the color of all your blocks, that is ONE thing.


#Padded, changed color, and chose a font

from tkinter import *
from tkinter.font import *

class App():
    def __init__(self, master):

        self.title_font = Font(family='Curlz Mt', size=30)

        #Declare variables
        self.m1 = DoubleVar()
        self.m2 = DoubleVar()
        self.r = DoubleVar()
        self.total = DoubleVar()

        self.total.set(0)

        # Title
        self.title = Label(master, text='Universal Gravity Calculator', font = self.title_font, bg='red', fg='green', relief='raised', borderwidth=5)
        self.title.grid(row=1, column=1, columnspan=2, sticky='w' + 'e', padx=20, ipadx=10, pady=10)

        #m1 Label and Entry Widget
        self.m1_label = Label(master, text = "Mass of Object One (kg)")
        self.m1_label.grid(row=2, column = 1, sticky = 'e')

        self.m1_entry  =Entry(master, textvariable = self.m1, width = 10, justify = CENTER)
        self.m1_entry.grid(row = 2, column = 2, sticky = 'w')

        #m2 Label and Entry Widget
        self.m2_label = Label(master, text = "Mass of Object Two (kg)")
        self.m2_label.grid(row=3, column = 1, sticky = 'e')

        self.m2_entry =Entry(master, textvariable = self.m2, width = 10, justify = CENTER)
        self.m2_entry.grid(row = 3, column = 2, sticky = 'w')

        #radius Label and Entry Widget
        self.r_label = Label(master, text = "Distance From Centers (m)")
        self.r_label.grid(row=4, column = 1, sticky = 'e')

        self.r_entry  =Entry(master, textvariable = self.r, width = 10, justify = CENTER)
        self.r_entry.grid(row = 4, column = 2, sticky = 'w')

        # Add total button and result label
        self.total_button = Button(master, text = "Calculate Gravity", command = lambda: self.pressed_button())
        self.total_button.grid(row = 5, column = 1, sticky = 'e')

        self.total_label = Entry(master, textvariable = self.total, width = 10, justify = CENTER)
        self.total_label.grid(row=5, column = 2, pady = 10, sticky = 'w')

    def pressed_button(self):
        try:
            self.total.set((6.67 * 10 ** -11) * (self.m1.get() * self.m2.get() / self.r.get() ** 2))
        except:
            self.total.set("Error.")

if '__main__' == __name__:
    root = Tk()
    root.title('Add two numbers')
    my_app = App(root)
    root.mainloop()