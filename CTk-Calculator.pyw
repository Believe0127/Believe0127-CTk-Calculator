import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.title("おしゃれなGui App")
app.geometry("400x280")
app.iconbitmap(default="calculator.ico")

#足し算
def plus():
    value1 = int(write_box1.get())
    value2 = int(write_box2.get())
    answer = value1 + value2
    answerbox.delete(0, customtkinter.END)
    answerbox.insert(0, answer)
#引き算
def minus():
    value1 = int(write_box1.get())
    value2 = int(write_box2.get())
    answer = value1 - value2
    answerbox.delete(0, customtkinter.END)
    answerbox.insert(0, answer)
#掛け算
def kake():
    value1 = int(write_box1.get())
    value2 = int(write_box2.get())
    answer = value1 * value2
    answerbox.delete(0, customtkinter.END)
    answerbox.insert(0, answer)
#割り算
def wari():
    value1 = int(write_box1.get())
    value2 = int(write_box2.get())
    answer = value1 / value2
    answerbox.delete(0, customtkinter.END)
    answerbox.insert(0, answer)
    

# write
write1 = customtkinter.CTkLabel(master=app, text="数値1")
write2 = customtkinter.CTkLabel(master=app, text="数値2")
write1.pack()
write2.pack()
write1.place(x=75, y=15)
write2.place(x=245, y=15)

# writebox
write_box1 = customtkinter.CTkEntry(master=app)
write_box2 = customtkinter.CTkEntry(master=app)
write_box1.pack()
write_box2.pack()
write_box1.place(x=35, y=45)
write_box2.place(x=195, y=45)


#plus
plus_btn = customtkinter.CTkButton(master=app, text="足し算", command=plus)
plus_btn.pack()
plus_btn.place(x=25, y=130)

#minus
minus_btn = customtkinter.CTkButton(master=app, text="引き算", command=minus)
minus_btn.pack()
minus_btn.place(x=25, y=165)

#kake
kake_btn = customtkinter.CTkButton(master=app, text="掛け算", command=kake)
kake_btn.pack()
kake_btn.place(x=25, y=200)

#wari
wari_btn = customtkinter.CTkButton(master=app, text="割り算", command=wari)
wari_btn.pack()
wari_btn.place(x=25, y=235)

#AnswerBox
answerbox = customtkinter.CTkEntry(master=app)
answerbox.pack()
answerbox.place(x=195, y=90)
answer_moji = customtkinter.CTkLabel(master=app, text="答え: ")
answer_moji.pack()
answer_moji.place(x=160, y=90)

app.mainloop()