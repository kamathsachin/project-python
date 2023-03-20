import tkinter


def convert_miles_kms():
    km = int(mile_entry.get()) * 1.60934
    calc_label.config(text=km)


window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

mile_entry = tkinter.Entry()
mile_entry.grid(column=1, row=0)

mile_label = tkinter.Label(text="Miles")
mile_label.grid(column=2, row=0)

equal_label = tkinter.Label(text="is equal to")
equal_label.grid(column=0, row=1)

calc_label = tkinter.Label(text="0")
calc_label.grid(column=1, row=1)

km_label = tkinter.Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = tkinter.Button(text="Calculate", command=convert_miles_kms)
calc_button.grid(column=1, row=3)

window.mainloop()
