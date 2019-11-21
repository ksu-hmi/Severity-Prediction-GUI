#importing the Tkinter and Random Lib.#
import tkinter as tk
import random
from tkinter import *
from tkinter import messagebox
from functools import partial

r= tk.Tk()

#Adding a title to the GUI window#
r.title("Medical_Prediction")

# creating the global variables#
terms = ''
sev_level = 0
#phy_g = 0
#pat_g = 0

#Add widgets in this area below:#

#Making the box with an input field for user to input#
tk.Label(r, text="Enter A Medical Term: ").grid(row=0)
e1 = tk.Entry(r, width=40)
e1.grid(row=0, column=1)


#Making a box for current medical terms
#NOTE: this window should grow or have a scroll bar if text is too much to display
tk.Label(r, text="Current Medical Terms: ").grid(row=1)
e2 = tk.Text(r, height=2, width=30, fg='firebrick')
e2.insert(tk.END, '')
e2.config(state=DISABLED)
e2.grid(row=1, column=1)


#Making the box pt gender#
tk.Label(r, text="Enter Patient Gender: ").grid(row=2)
e3 = tk.Entry(r, width=40)
e3.grid(row=0, column=1)


#Making the box phy gender#
tk.Label(r, text="Enter Physician Gender: ").grid(row=3)
e4 = tk.Entry(r, width=40)
e4.grid(row=0, column=1)


#MAY DELETE LATER#
#HELP! Attempt to create male and female on the r frame, it doesnt show up)
#root = tk.Entry(r)
#v = IntVar() 
#Radiobutton(root, text='Male', variable=v, value=0).pack(anchor=W)
#Radiobutton(root, text='Female', variable=v, value=1).pack(anchor=W) 





def show_entry_fields():
    global terms
    temp_terms = e1.get()
    print("Term: ", temp_terms)
    if terms == '':
        terms = temp_terms
    else:
        terms = terms + " " + temp_terms
    e2.config(state=NORMAL)
    e2.delete(0.0, END) 
    e2.insert(tk.END, terms)
    e1.delete(0,tk.END)
    e2.config(state=DISABLED)

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
       # To test severity level we will use the randint function to ensure all 1-9 works#
        # When model is added this will be commented out#
        sev_level = random.randint(1,3)
        return sev_level
        
    else:
        print("test failed, input was not a string")


         
#Reset button
def reset():
    global terms
    terms = ''
    e2.config(state=NORMAL)
    e2.delete(0.0, END) 
    e2.insert(tk.END, terms)
    e1.delete(0,tk.END)
    e2.config(state=DISABLED)
    return
  




#Pop up window for the severity level calculation and text level#
def clicked():
    #when gender variables added, this is where the global variables will be pulled from GUI, converted to 0/1 before calling model
    sev_level = call_model(terms)
    sev_text=""
    if sev_level ==1: 
        sev_text= "Low Risk"
    elif sev_level ==2: 
        sev_text= "Moderate Risk"
    elif sev_level ==3:
        sev_text= "High Risk"
    messagebox.showinfo('Calculated Severity Score', ("The Calculated Severity Level Predicted From the Model Is:  ", sev_text))
 
#Making buttons: Quit, Input, Predict, and Reset #
tk.Button(r,text= "Quit",width= 15, command= r.quit).grid(row=4, column=0, sticky=tk.W, pady=4)
tk.Button(r,text="Input", width= 15, command= show_entry_fields).grid(row=0, column=2, sticky=tk.W, pady=4)
tk.Button(r, text= "Predict", width= 15,command= clicked).grid(row=4, column = 1, sticky=tk.W, pady=4)
tk.Button(r, text= "Reset", width= 15,command= reset).grid(row=4, column = 2, sticky=tk.W, pady=4)




#Button pack may be deleted later#
#button.pack()



# This needs to be at the end
r.mainloop()






##########
#r = tk.Tk()

#v = tk.IntVar()

#tk.Label(r, 
#        text="""Choose the patient gender:""",
#        justify = tk.LEFT,
#        padx = 20).pack()
#tk.Radiobutton(r, 
#              text="Male",
#              padx = 20, 
#              variable=v, 
#              value=1).pack(anchor=tk.W)
#tk.Radiobutton(r, 
#              text="Female",
#              padx = 20, 
#              variable=v, 
#              value=2).pack(anchor=tk.W)
#
#r.mainloop()