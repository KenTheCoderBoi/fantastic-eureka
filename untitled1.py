from tkinter import *

root = Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background="snow")

entry_word = Entry(root)
entry_word.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label = Label(root,text="",bg="gold",fg="black")
label2 = Label(root,text="",bg="gold",fg="black")
def asciiconvert():
    label_word = entry_word.get()
    encrypted = []
    for letters in label_word:
        letter= str(ord(letters))
        label["text"] += letter + " "
        encrypted = (letter)
        label2["text"] += chr(int(encrypted)-17) + ""
button = Button(root, text = "generate", command=asciiconvert)
button.place(relx=0.5,rely = 0.5, anchor = CENTER)
label.place(relx=0.5,rely = 0.6, anchor = CENTER)
label2.place(relx=0.5,rely = 0.7, anchor = CENTER)

root.mainloop()