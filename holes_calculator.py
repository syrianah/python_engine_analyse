from tkinter import Tk, IntVar, Label, Entry, Button


def calculate():
    Az = data_Az.get()
    n = data_n.get()
    t = data_t.get()
    Rm = 215
    Pmax = 15.7
    Fz = Az * Pmax
    az = round((Fz / n) / (Rm * 0.75 * t), 2)
    data_az.set(az)


root = Tk()
root.title('Tyrakowy kalkulator')
root.geometry("450x150")

data_Az = IntVar()
data_n = IntVar()
data_t = IntVar()
data_az = IntVar()

Label(root, text='Powierzchnia zatyczki').grid(row=0)
Label(root, text='Ilość otworów').grid(row=1)
Label(root, text='Grubość scianki').grid(row=2)
Label(root, text='Odległość otworów od krawędzi rurki').grid(row=3)
Label(root, textvariable=data_az).grid(row=3, column=1)

Entry(root, textvariable=data_Az).grid(row=0, column=1)
Entry(root, textvariable=data_n).grid(row=1, column=1)
Entry(root, textvariable=data_t).grid(row=2, column=1)

Button(root, text="Oblicz", command=calculate).grid(row=4, column=1)


root.mainloop()
