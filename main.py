import tkinter as tk

from First_Page import First_Page


class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Main")
        self.geometry("400x300")
        self.firstPage=First_Page(self)
        self.firstPage.pack(fill=tk.BOTH, expand=True)



if __name__ == "__main__":
    main = Main()
    main.mainloop()
