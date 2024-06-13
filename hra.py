import tkinter as tk


def vypis_ahoj():
    text_output.insert(tk.END, 'Ahoj')

def vypis_cau():
    text_output.insert(tk.END, 'Čau')

def vypis_ ():
    text_output.insert(tk.END, ' ')

def kontrola():
    if text_output.get("1.0", tk.END).strip() == 'Ahoj Čau':
        new_window = tk.Toplevel(root)
        new_window.title("odpoved")
        tk.Label(new_window, text="Dobre", font=("Arial", 12)).pack()


root = tk.Tk()
root.title("Hra")

text_fixed = tk.Text(root, height=1, width=20,font=("Arial", 12))
text_fixed.insert(tk.END, 'Poskladaj vetu') 
text_fixed.pack()
text_fixed.config(state='disabled')  

text_output = tk.Text(root)
text_output.pack()

tlačidlo_ahoj = tk.Button(root, text="Ahoj", command=vypis_ahoj)
tlačidlo_ahoj.pack()

tlačidlo_cau = tk.Button(root, text="Čau", command=vypis_cau)
tlačidlo_cau.pack()

tlačidlo_  = tk.Button(root, text="medzera", command=vypis_ )
tlačidlo_ .pack()

tlačidlo_kontrola = tk.Button(root, text="Kontrola", command=kontrola)
tlačidlo_kontrola.pack()



root.mainloop()



