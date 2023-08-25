import tkinter as tk

# Class representation
class BmiCalculator:
    def __init__(self):
        # Create window and set titles
        self.mainWindow = tk.Tk()
        self.mainWindow.title('BMI Calculator')
        self.mainWindow.geometry('500x400')
        
        # Create label and text box for weight in lbs
        self.actWgtLabel = tk.Label(self.mainWindow, text='Enter weight in pounds: ')
        self.textBoxWgt = tk.Entry(self.mainWindow, width=5)
        
        # Place widgets in window using grid layout
        self.actWgtLabel.grid(row=1, column=2)
        self.textBoxWgt.grid(row=1, column=5)
        
        # Create label and text box for height in inches
        self.actHgtLabel = tk.Label(self.mainWindow, text='Enter height in inches: ')
        self.textBoxHgt = tk.Entry(self.mainWindow, width=5)
        
        # Place widgets in window using grid layout
        self.actHgtLabel.grid(row=2, column=2)
        self.textBoxHgt.grid(row=2, column=5)
        
        # Create label for BMI
        self.BmiLabel = tk.Label(self.mainWindow, text='BMI: ')
        self.calcBmiLabel = tk.Label(self.mainWindow, text='')
        
        # Create button for Calculate BMI and Exit
        self.calcButton = tk.Button(self.mainWindow, text='Calculate BMI', command=self.calcButton_click)
        self.exitButton = tk.Button(self.mainWindow, text='Exit', command=self.mainWindow.destroy)
        
        # Place widgets in window
        self.BmiLabel.grid(row=4, column=2)
        self.calcBmiLabel.grid(row=4, column=3)
        self.calcButton.grid(row=5, column=2)
        self.exitButton.grid(row=5, column=3)
        
        # Enter main window loop
        self.mainWindow.mainloop()
    
    # Event handling method for calculating BMI (weight in lbs/height in inches squared * 703)
    def calcButton_click(self):
        # Get actual weight in lbs
        actWgt = float(self.textBoxWgt.get())
        # Get actual height in inches
        actHgt = float(self.textBoxHgt.get())
        # Calculate BMI
        BMI = float((actWgt / (actHgt ** 2)) * 703)
        # Display BMI
        self.calcBmiLabel.configure(text=format(BMI, '.2f'))
        
# Main module to call the class
def main():
    BmiCalculator()

if __name__ == '__main__':
    main()