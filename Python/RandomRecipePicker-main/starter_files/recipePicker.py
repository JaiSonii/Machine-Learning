import tkinter as tk

# initiallize app
root = tk.Tk()
root.title("New App")
root.eval("tk::PlaceWindow . center")
frame1= tk.Frame(root, width=500,height=600, bg="#3d6466")
frame1.grid(row=0,column=0)
# run app
root.mainloop()