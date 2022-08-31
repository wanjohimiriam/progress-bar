from tkinter import *
from tkinter.ttk import *

def start():
    import time
    for i in range(1, 100, 1):
        progress['value']= i
        root.update_idletasks()
        label1.config(text=str(i)+'%')
        time.sleep(0.02)
    progress['value']=100
    root.destroy()

root= Tk()

label1= Label(root, font=('arial', 20, 'bold'))
label1.pack(padx=100, pady=5)

s=Style()
s.configure("TProgressbar", foreground="red", background="red", thickness=40)

progress= Progressbar(root, style='TProgressbar', length=400, mode="determinate")
progress.pack(padx=10, pady=10)

button= Button(root, text="Start", command=start)
button.pack(padx=10, pady=10)

root.title("Progressbar")
root.mainloop()


