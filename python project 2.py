import tkinter as tk

tasks = []

def update_task_list():
  task_list.delete(0, tk.END)  
  for i, task in enumerate(tasks, start=1):
    task_list.insert(tk.END, f"{i}. {task}")

def remove_all_tasks():
  tasks.clear()                                                                                                                                                                                      
  update_task_list()  

def add_task():
  task_info = entry_task.get()
  if task_info:
    tasks.append(task_info)
    update_task_list()
    entry_task.delete(0, tk.END)  
    print("Task added successfully!")
  else:
    print("Please enter a task description!")

def remove_task():
  if not tasks:
    print("No tasks found!")
  else:
    try:
      selected_index = task_list.curselection()[0]
      del tasks[selected_index]
      update_task_list()
      print("Task removed successfully!")
    except (IndexError, ValueError):
      print("Invalid task selection!")

#gui (window,frame,label,litsbox,frame,buttons 3,description frame,label,entry)

window = tk.Tk()
window.title("To-Do List")
window.configure(bg="#874F41")

task_list_frame = tk.Frame(window,bg="#874F41")
task_list_frame.pack(padx=10, pady=10)

task_list_label = tk.Label(task_list_frame, text="Tasks:",bg="#874F41",foreground="BEIGE",font=('helvetica',13,"bold"))
task_list_label.pack()

task_list = tk.Listbox(task_list_frame, width=50,bg="BEIGE",selectbackground="#ac8968")
task_list.pack()

button_frame = tk.Frame(window,bg="#874F41")
button_frame.pack(padx=10, pady=10)

add_task_button = tk.Button(button_frame, text="Add Task", command=add_task, bg="BEIGE")
add_task_button.pack(side=tk.LEFT, padx=5)

remove_task_button = tk.Button(button_frame, text="Remove Task", command=remove_task,bg="BEIGE")
remove_task_button.pack(side=tk.LEFT, padx=5)

show_tasks_button = tk.Button(button_frame, text="Remove All Tasks", command=remove_all_tasks,bg="BEIGE")
show_tasks_button.pack(side=tk.LEFT, padx=5)

entry_frame = tk.Frame(window,bg="#874f41")
entry_frame.pack(padx=10, pady=10)

entry_label = tk.Label(entry_frame, text="Task Description:",bg="#874F41",foreground="BEIGE",font=('helvetica',13,"bold"))
entry_label.pack()

entry_task = tk.Entry(entry_frame, width=50,bg="BEIGE")
entry_task.pack()

window.mainloop()

