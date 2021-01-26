import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter.font import Font

path = r'F:\Rhishikesh\Programming\GitHub\Contact-Book\Contact-Book' # Enter the path where you would like to save
file_name = r'\Contacts.csv'

try:
    df = pd.read_csv(path + file_name)
except FileNotFoundError:
    Contacts = pd.DataFrame(columns = ['First Name', 'Last Name', 'Mobile No.', 'E-mail ID'])
    Contacts.to_csv(path + file_name, index = False)
    df = pd.read_csv(path + file_name)

win = tk.Tk()

msg_font = Font(win, family = 'Arial', size = 10)

tab = ttk.Notebook(win)
tab1 = ttk.Frame(tab, width = 300, height = 200)
tab2 = ttk.Frame(tab, width = 300, height = 200)
tab.add(tab1, text = 'Contact List')
tab.add(tab2, text = 'New Contact')
tab.pack(expand = True, fill='both')

def display(event):
    i = contact_list.curselection()
    
    f_name.delete(0, tk.END)
    f_name.insert(0, df.iloc[i]['First Name'])
    
    l_name.delete(0, tk.END)
    l_name.insert(0, df.iloc[i]['Last Name'])
    
    mob.delete(0, tk.END)
    mob.insert(0, df.iloc[i]['Mobile No.'])
    
    e_mail.delete(0, tk.END)
    e_mail.insert(0, df.iloc[i]['E-mail ID'])

contact_lbl = tk.Label(tab1, text = 'Contacts')
contact_lbl.place(x = 20, y = 10)

contact_list = tk.Listbox(tab1, selectmode = 'extended')
for (i, j) in zip(df['First Name'], df['Last Name']):
    contact_list.insert(tk.END, str(i) + ' ' + str(j))
contact_list.place(x = 20, y = 30)
contact_list.bind('<<ListboxSelect>>', display)

f_lbl = tk.Label(tab1, text = 'First Name')
f_lbl.place(x = 150, y = 30)

f_name = tk.Entry(tab1)
f_name.place(x = 150, y = 50)

l_lbl = tk.Label(tab1, text = 'Last Name')
l_lbl.place(x = 150, y = 70)

l_name = tk.Entry(tab1)
l_name.place(x = 150, y = 90)

m_lbl = tk.Label(tab1, text = 'Mobile No.')
m_lbl.place(x = 150, y = 110)

mob = tk.Entry(tab1)
mob.place(x = 150, y = 130)

e_lbl = tk.Label(tab1, text = 'E-mail ID')
e_lbl.place(x = 150, y = 150)

e_mail = tk.Entry(tab1)
e_mail.place(x = 150, y = 170)

fname_lbl = tk.Label(tab2, text = 'First Name')
fname_lbl.place(x = 40, y = 30)

fname_ent = tk.Entry(tab2)
fname_ent.place(x = 150, y = 30)

lname_lbl = tk.Label(tab2, text = 'Last Name')
lname_lbl.place(x = 40, y = 60)

lname_ent = tk.Entry(tab2)
lname_ent.place(x = 150, y = 60)

mob_lbl = tk.Label(tab2, text = 'Mobile No.')
mob_lbl.place(x = 40, y = 90)

mob_ent = tk.Entry(tab2)
mob_ent.place(x = 150, y = 90)

email_lbl = tk.Label(tab2, text = 'Email ID')
email_lbl.place(x = 40, y = 120)

email_ent = tk.Entry(tab2)
email_ent.place(x = 150, y = 120)

def save():
    fname = fname_ent.get()
    lname = lname_ent.get()
    mob = mob_ent.get()
    email = email_ent.get()
    try:
        int(mob)
    except ValueError:
        inval_lbl = tk.Label(tab2, font = msg_font, text = 'Invalid Number!!!')
        inval_lbl.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        inval_lbl.after(2000, lambda: inval_lbl.destroy())
        return
    if len(mob) < 10:
        inval_lbl = tk.Label(tab2, font = msg_font, text = 'Please enter a valid number of atleast 10 digit!')
        inval_lbl.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
        inval_lbl.after(2000, lambda: inval_lbl.destroy())
        return
    dict = {'First Name' : fname, 'Last Name' : lname, 'Mobile No.' : mob, 'E-mail ID' : email}
    global df
    df = df.append(dict, ignore_index = True)
    global path
    df.to_csv(path + file_name, index = False)
    saved_lbl = tk.Label(tab2, font = msg_font, text = 'Saved Successfully!')
    saved_lbl.place(relx = 0.5, rely = 0.5, anchor = tk.CENTER)
    saved_lbl.after(2000, lambda: saved_lbl.destroy())
    fname_ent.delete(0, tk.END)
    lname_ent.delete(0, tk.END)
    mob_ent.delete(0, tk.END)
    email_ent.delete(0, tk.END)

save_btn = tk.Button(tab2, command = save, text = 'Save to Contacts')
save_btn.place(x = 150, y = 170, anchor = tk.CENTER)

win.mainloop()