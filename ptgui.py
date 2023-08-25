from tkinter import *

# Class representation for Property Tax Gui
class PropTaxGUI:
    # Create the initializer 
    def __init__(self):
        # Create window and set title
        self.mainWindow = Tk()
        self.mainWindow.title('Property Tax Calculator')
        self.mainWindow.geometry('500x440')

        # Create label and text box for actual property value
        self.actValLabel = Label(self.mainWindow, text='Enter the value of your property: ')
        self.textBoxPropVal = Entry(self.mainWindow, width=10)

        # Place widgets in window using grid layout
        self.actValLabel.grid(row=0, column=0)
        self.textBoxPropVal.grid(row=0, column=1)

        # Create labels for assessed value and assessed value label
        self.assessedValLabel = Label(self.mainWindow, text='Assessed Value of Property: ')
        self.calcAssessValLabel = Label(self.mainWindow, text='')

        # Place widgets for assessed value labels
        self.assessedValLabel.grid(row=1, column=0)
        self.calcAssessValLabel.grid(row=1, column=1)

        # Create labels for property tax owed and property tax owed label
        self.propTaxLabel = Label(self.mainWindow, text='Property Tax Owed: ')
        self.calcPropTaxLabel = Label(self.mainWindow, text='')

        # Place widgets for property tax owed labels
        self.propTaxLabel.grid(row=2, column=0)
        self.calcPropTaxLabel.grid(row=2, column=1)

        # Create button for calculate button
        self.calcButton = Button(self.mainWindow, text='Calculate Property Tax Owed', command=self.calcButton_click)

        # Create button for exit button
        self.exitButton = Button(self.mainWindow, text='Exit', command=self.mainWindow.destroy)

        # Place widgets in window
        self.calcButton.grid(row=3, column=0)
        self.exitButton.grid(row=3, column=1)

        # Enter the main window loop
        self.mainWindow.mainloop()

    # Event handling method for calculate property tax button
    def calcButton_click(self):
        # Get actual value of property
        actValue = float(self.textBoxPropVal.get())
        # Calculate assessed value
        assessed_value = float(actValue * .60)
        propTaxOwed = float((assessed_value * .64) / 100)
        # Display assessed value and property tax owed
        self.calcAssessValLabel.configure(text=format(assessed_value, '.2f'))
        self.calcPropTaxLabel.configure(text=format(propTaxOwed, '.2f'))


# Main module to call the class
def main():
    mypropTaxGUI = PropTaxGUI()

main()