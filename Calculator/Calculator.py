import tkinter as tk

fenster = tk.Tk()
fenster.title("Calculator")

eingabe = tk.Entry(fenster, width=20, font=("Arial", 24), borderwidth=5, justify="right")
eingabe.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_klick(wert):
    eingabe.insert(tk.END, str(wert))

def berechnen():
    try:
        ergebnis = eval(eingabe.get())
        eingabe.delete(0, tk.END)
        eingabe.insert(0, str(ergebnis))
    except:
        eingabe.delete(0, tk.END)
        eingabe.insert(0, "Fehler")

def loeschen():
    eingabe.delete(0, tk.END)

def loesche_letztes_zeichen():    
    aktueller_text = eingabe.get()
    neuer_text = aktueller_text[:-1]
    eingabe.delete(0, tk.END)
    eingabe.insert(0, neuer_text)
    
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("Del", 5, 1),
]

for (text, row, col) in buttons:
    if text == "=":
        cmd = berechnen
    elif text == "C":
        cmd = loeschen
    elif text == "Del":
        cmd = loesche_letztes_zeichen
    else:
        cmd = lambda x=text: button_klick(x)

    tk.Button(fenster, text=text, width=5, height=2, font=("Arial", 18),
              command=cmd).grid(row=row, column=col, padx=5, pady=5)

fenster.mainloop()