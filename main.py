from timer import Timer
from tkinter import Tk, Entry, Label, StringVar

root = Tk()
root.title("Type faster!")
root.geometry("650x170")

entry_text = StringVar()
entry_text.set("")


timer = Timer(root)


def verify_text(e):
    timer.start_timer()
    if timer.current_time > 5:
        print('a')
        entry_text.set('')
    timer.current_time = 0


text = Label(root, text="Digite o mais rápido possível!")
text.pack()

entry = Entry(root, textvariable=entry_text)
entry.pack(pady=5)

entry.bind("<KeyRelease>", verify_text)

root.mainloop()
