import tkinter as tk             
from tkinter import ttk         
from tkinter import messagebox  
import sqlite3 as sql       

# defining an empty list  
tasks = []
completed_tasks = []

def add_task():    
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:   
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks (title, completed) values (?, ?)', (task_string, False))
        list_update()  
        task_field.delete(0, 'end')


def list_update():  
    clear_list()  
    for task in tasks:
        if task in completed_tasks:
            task_listbox.insert('end', task)
            task_listbox.itemconfig('end', {'fg': 'gray'})
        else:
            task_listbox.insert('end', task)


def delete_task():  
    try:   
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks: 
            tasks.remove(the_value)
            if the_value in completed_tasks:
                completed_tasks.remove(the_value)
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

 
def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box == True:  
        while(len(tasks) != 0): 
            tasks.pop()
        completed_tasks.clear()
        the_cursor.execute('delete from tasks')   
        list_update()

def mark_task_done():
    try:
        selected_index = task_listbox.curselection()[0]
        the_value = task_listbox.get(selected_index)
        if the_value in tasks and the_value not in completed_tasks:
            completed_tasks.append(the_value)
            the_cursor.execute('update tasks set completed = ? where title = ?', (True, the_value))
        list_update()
    except IndexError:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Mark as Done.')

        
def clear_list():  
    task_listbox.delete(0, 'end')


def close():   
    print(tasks)   
    guiWindow.destroy()
    the_connection.commit()
    the_cursor.close()

def retrieve_database(): 
    while(len(tasks) != 0):  
        tasks.pop()   
    completed_tasks.clear()
    for row in the_cursor.execute('select title, completed from tasks'):   
        tasks.append(row[0])
        if row[1]:
            completed_tasks.append(row[0])

if __name__ == "__main__": 
    guiWindow = tk.Tk()
    guiWindow.title("To-Do List Manager")
    guiWindow.geometry("650x650+750+250")
    guiWindow.resizable(0, 0) 
    guiWindow.configure(bg = "#00FFFF")


    the_connection = sql.connect('listOfTasks.db')  
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text, completed boolean)')
    the_cursor.execute("PRAGMA table_info(tasks)")
    columns = [column[1] for column in the_cursor.fetchall()]
    if 'completed' not in columns:
        the_cursor.execute('ALTER TABLE tasks ADD COLUMN completed BOOLEAN')
        the_cursor.execute('UPDATE tasks SET completed = FALSE WHERE completed IS NULL')
 
    header_frame = tk.Frame(guiWindow, bg = "#E6E6FA")  
    functions_frame = tk.Frame(guiWindow, bg = "#E6E6FA")  
    listbox_frame = tk.Frame(guiWindow, bg = "#E6E6FA")  
  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")

    # LABELS 
    header_label = ttk.Label(  
        header_frame,  
        text = "The To-Do List",  
        font = ("Algerian", "30"),  
        background = "#E6E6FA",  
        foreground = "#000000"  
    )  
    header_label.pack(padx = 20, pady = 20) 
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("French Script MT", "20"),  
        background = "#E6E6FA",  
        foreground = "#000000"  
    ) 
    task_label.place(x = 30, y = 40)

    # ENTRY FIELD  
    task_field = ttk.Entry(  
        functions_frame,  
        font = ("French Script MT", "15"),  
        width = 21,  
        background = "#FFF8DC",  
        foreground = "#A52A2A"  
    )  
    task_field.place(x = 60, y = 80)

    # BUTTONS 
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add task",  
        width = 24,  
        command = add_task  
    )  
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task",  
        width = 24,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks",  
        width = 24,  
        command = delete_all_tasks  
    )
    mark_done_button = ttk.Button(
            functions_frame,
            text="Mark as Done",
            width=24,
            command=mark_task_done
    )
    exit_button = ttk.Button(  
        functions_frame,  
        text = "Exit",  
        width = 24,  
        command = close  
    ) 
    add_button.place(x = 60, y = 120)  
    del_button.place(x = 60, y = 160)  
    del_all_button.place(x = 60, y = 200)
    mark_done_button.place(x = 60, y = 240)
    exit_button.place(x = 60, y = 280)

    # LIST BOX
    task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 30,  
        height = 15,  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#E0FFFF",  
        selectforeground = "#000000"  
    )   
    task_listbox.place(x = 10, y = 20)

    # CALLING THE FUNCTIONS
    retrieve_database()  
    list_update()  
    guiWindow.mainloop()  
    the_connection.commit()  
    the_cursor.close()  
