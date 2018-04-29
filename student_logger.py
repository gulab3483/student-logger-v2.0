import tkinter as tk


#Set up grid
root = tk.Tk()
root.wm_title("Student Logger")
#root.grid_rowconfigure(row=1)

my_dict = {'4723' : {'name' : 'Bob', 'Courses' : []},
           '5329' : {'name' : 'Jeff', 'Courses' : []},
           '1627' : {'name' : 'Diana', 'Courses' : []}}

def getInput(a,b,c):
	my_dict[b.get()] = {'name' : a.get(), 'Courses' : c.get()}


def addStudent():
    tk.Label(textPane,text="Student Name:").grid(row=0, column=0)
    input1 = tk.Entry(textPane)
    input1.grid(row=0, column=1)
    tk.Label(textPane,text="Student ID:  ").grid(row=1, column=0)
    input2 = tk.Entry(textPane)
    input2.grid(row=1, column=1)
    tk.Label(textPane,text="Student Courses:").grid(row=2, column=0)
    input3 = tk.Entry(textPane)
    input3.grid(row=2, column=1)
    getInputB = tk.Button(textPane, text="Submit", command=getInput(input1,input2,input3))
    getInputB.grid(row=1, column=2)


def printStudents():
	w = tk.Label(OutputFrame, text ="")
	for i in my_dict.keys():
		text = w.cget("text") + "Student Name: {}\tStudent ID: {}\tStudent Courses: {}\n".format(my_dict[i]['name'], i, my_dict[i]['Courses'])
		w.configure(text=text)
	w.grid(column=3, row=0)

#OutputFrame():
OutputFrame = tk.Frame(root, width = 500, height = 300)
OutputFrame.grid(column=2)

#Text pane:
textPane = tk.Frame(root, width=500, height = 150)
textPane.grid(column=2)

#Button pane:
buttonFrame = tk.Frame(root, width=200, height=200)
buttonFrame.grid(row=0, column=0)

psButton = tk.Button(buttonFrame, text="Print Students", command=printStudents)
psButton.grid(column=0)
asButton = tk.Button(buttonFrame, text="Add Student", command=addStudent)
asButton.grid(column=0)

OutputFrame.grid_propagate(False)
textPane.grid_propagate(False)
buttonFrame.grid_propagate(False)
root.mainloop()
