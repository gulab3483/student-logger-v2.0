import tkinter as tk


#Set up grid
root = tk.Tk()
root.wm_title("Student Logger")
#root.grid_rowconfigure(row=1)

my_dict = {'4723' : {'name' : 'Bob', 'Courses' : []},
           '5329' : {'name' : 'Jeff', 'Courses' : []},
           '1627' : {'name' : 'Diana', 'Courses' : []}}


def addStudent(studentID, name, courses):
    my_dict[studentID] = {'name' : name, 'Courses' : courses}

def printStudents():
	w = tk.Label(OutputFrame, text ="")
	for i in my_dict.keys():
		text = w.cget("text") + "Student Name: {}\tStudent ID: {}\tStudent Courses: {}\n".format(my_dict[i]['name'], i, my_dict[i]['Courses'])
		w.configure(text=text)
	w.grid(column=3, row=0)

#OutputFrame():
OutputFrame = tk.Frame(root, width = 500, height = 300)
OutputFrame.grid(column=3)

#Text pane:
textPane = tk.Frame(root, width=500, height = 150)
textPane.grid(column=3)

#Button pane:
buttonFrame = tk.Frame(root, width=200, height=200)
buttonFrame.grid(row=0, column=0)

psButton = tk.Button(buttonFrame, text="Print Students", command=printStudents)
psButton.grid(row=0, column=0)

# my_dict['4723']['Courses'].append('Economics')
# addStudent('9537', 'Tom',['math', 'science', 'doingstuff'])

root.mainloop()
