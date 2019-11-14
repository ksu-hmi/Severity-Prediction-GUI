import tkinter as tk
from tkinter import messagebox
from functools import partial
r= tk.Tk()
r.title("Medical_Prediction")
terms = ''
sev_level = 0
#phy_g = 0
#pat_g = 0

#Add widgets in this area

#Making the box with an input field for user
tk.Label(r, text="Enter A Medical Term: ").grid(row=0)
e1 = tk.Entry(r)
e1.grid(row=0, column=1)

def show_entry_fields():
    global terms
    temp_terms = e1.get()
    print("Term: ", temp_terms)
    terms = terms + " " + temp_terms
    print("New Term string:  ", terms)
    e1.delete(0,tk.END)

def call_back():
    print("You added a term.")

# test call model.  actual model includes PHI data so will not be on GitHub.  
# For testing test model output sets sev_level = 5 or to random int 1-9
def call_model(string):
    print("function called")
    global terms
    global sev_level
    if type(string) == str:
        temp = ''
        temp = string[0:10]
        print("test passed, input was a string that started with: ", temp)
        sev_level = 5 #randint(1,9)
        return sev_level
    else:
        print("test failed, input was not a string")

def clicked():
  #when gender variables added, this is where the global variables will be pulled from GUI, converted to 0/1 before calling model
  sev_level = call_model(terms)
  messagebox.showinfo('Calculating Severity Score', ('Severity Level = ', sev_level))
 
#Making 2 buttons one for quit and one to show
tk.Button(r,text= "Quit", command= r.quit).grid(row=3, column=0, sticky=tk.W, pady=4)
tk.Button(r,text="Input", command= show_entry_fields).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(r, text= "Predict", width= 25,command= clicked).grid(row=4, column = 0, sticky=tk.W, pady=4)

#button.pack()



# This needs to be at the end
r.mainloop()
