import tkinter as tk
from tkinter import messagebox
flashcards=[
    {"q":"capital of india","a":"new delhi"},
    {"q":"2+2","a":"4"},
    {"q":"python keyword for function","a":"def"}]
index= 0
showing_answer= False
def update_card():
    global showing_answer
    question_label.config(text=flashcards[index]["q"])
    answer_label.config(text="")
    showing_answer=False

def show_answer():
    global showing_answer
    if not showing_answer:
        answer_label.config(text=flashcards[index]["a"])
        showing_answer= True

def next_card():
    global index
    if index<len(flashcards)-1:
        index+=1
        update_card()

def prev_card():
     global index
     if index> 0:
        index-=1
        update_card()

def add_card():
    q=question_entry.get()
    a=answer_entry.get()
    if q and a:
        flashcards.append({"q":q,"a":a})
        question_entry.delete(0,tk.END)
        answer_entry.delete(0,tk.END)
        messagebox.showinfo("success","flashcard added!")
    else:
        messagebox.showwarning("error","please enter both question and answer")

def edit_card():
    flashcards[index]["q"]=question_entry.get()
    flashcards[index]["a"]=answer_entry.get()
    update_card()
    messagebox.showinfo("updated","flashcard updated")

def delete_card():
    global index
    if flashcards:
        flashcards.pop(index)
        if index>=len(flashcards):
            index=len(flashcards)-1
        if flashcards:
            update_card()
        else:
            question_label.config(text="no flashcards available")
            answer_label.config(text="")
            messagebox.showinfo("deleted","flashcard deleted")

root=tk.Tk()
root.title("flashcard quiz app")
root.geometry("400x450")

question_label=tk.Label(root,text="",font=("Arial", 16),wraplength=350)
question_label.pack(pady=20)

answer_label=tk.Label(root,text="",font=("Arial", 14),fg="green")
answer_label.pack(pady=10)

tk.Button(root,text="show answer",command=show_answer).pack(pady=5)
nav_frame=tk.Frame(root)
nav_frame.pack(pady=10)

tk.Button(nav_frame,text="previous",command=prev_card).grid(row=0,column=0,padx=10)
tk.Button(nav_frame,text="next",command=next_card).grid(row=0,column=1,padx=10)


tk.Label(root,text="add/edit flashcard").pack(pady=10)

question_entry=tk.Entry(root,width=40)
question_entry.pack(pady=5)
question_entry.insert(0,"question")



answer_entry=tk.Entry(root,width=40)
answer_entry.pack(pady=5)
answer_entry.insert(0,"answer")

tk.Button(root,text="add",command=add_card).pack(pady=3)
tk.Button(root,text="edit",command=edit_card).pack(pady=3)
tk.Button(root,text="delete",command=delete_card).pack(pady=3)

update_card()
root.mainloop()










    

    
