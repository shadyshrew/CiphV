from tkinter import *
import tkinter.messagebox
a = ["a","b","c","d","e","f","g","h","i","j","k","l",
     "m","n","o","p","q","r","s","t","u","v","w","x","y","z",
     "A","B","C","D","E","F","G","H","I","J","K","L","M","N"
    ,"O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1"
    ,"2","3","4","5","6","7","8","9","`","~","!","@","#","$",
     "%","t^","&","*","_","+","=","(",")","{","}","|","\\",
     "[","]",":",";","\"","'","<",",",">",".","?"," ","/"]
#94 values
b = [range(1,62)]
key = [12,5,8]


def infostuff():
    tkinter.messagebox.showinfo( "Information", "Type your message in the text box and click on Encrypt to generate a code."
                                                "If an encrypted code is given to you ,decrypt it by pasting it in the text"
                                                "box and clicking decrypt.     "
                                                "Shreyas.N")
def encrypt():
    print("haha")
    ban = []
    inp = entry1.get()
    for i in range(len(inp)):
        for j in range(93):
            if a[j] == inp[i]:
                if i%3 == 0:
                    l = (j + 12)%94
                    ban.append(a[l])
                elif i%3 == 1:
                    l = (j + 5)%94
                    ban.append(a[l])
                elif i%3 == 2:
                    l = (j + 8)%94
                    ban.append(a[l])
    str1 = "".join(ban)
    ent = Entry(root, state='readonly', readonlybackground='white', fg='black')
    var = StringVar()
    var.set(str1)
    ent.config(textvariable=var, relief = 'flat')
    ent.pack()
    #str1 has the generated code

def decrypt():
    print("blah")
    ntemp = []
    ans =[]
    ans = entry1.get()
    for i in range(len(ans)):
        for j in range(93):
            if a[j] == ans[i]:
                if i%3 == 0:
                    l = (j - 12)
                    if j < 0:
                        l = 93 + j
                    ntemp.append(a[l])
                elif i%3 == 1:
                    l = (j - 5)
                    if j < 0:
                        l = 93 + j
                    ntemp.append(a[l])
                elif i%3 == 2:
                    l = (j - 8)
                    if j < 0:
                        l = 93 + j
                    ntemp.append(a[l])
    str2 = "".join(ntemp)
    ent = Entry(root, state='readonly', fg='black')
    var = StringVar()
    var.set(str2)
    ent.config(textvariable=var, relief='flat')
    ent.pack()
root = Tk()
root.wm_title("Ciph")
root.configure(background = '#a1dbcd')

#Frame pack and Button
lab1 = Label(root, text="Type/Paste your message.", bg = "#a1dbcd")
lab2 = Label(root, text="Copy this code.")
entry1 = StringVar()
lab1.pack()
Entry(root, textvariable=entry1).pack(ipady = 30, ipadx = 100)

#Encryption and Decryption Buttons
ec = Button(root, fg="black" , bg = "white", text="Encrypt", command = encrypt)
ec.pack(padx = 4, pady = 4)
dc = Button(root, bg = "black", fg = "white", text = "Decrypt", command = decrypt)
dc.pack(padx = 4, pady = 4)

lsum = Label(root, text = 'The code is:', bg = "#a1dbcd" )
lsum.pack(pady = 2)

#Menu options
menu = Menu(root)
root.config(menu=menu)
sub = Menu(menu)
menu.add_cascade(label="Info", menu=sub)
sub.add_command(label="How does it work?",  command = infostuff)
sub.add_command(label="Exit", command = root.quit)

frame = Frame(root, width = 200, height = 20, bg = "#a1dbcd")
frame.pack()
root.mainloop()