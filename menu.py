from tkinter import *
import circle

class Menu:
    def __init__(self):
        self.bg_color = "white"
        self.text_color = "black"

        self.screen_size = (900,900)
        self.first_x = self.screen_size[0]//2
        self.y = self.screen_size[1]//2
        self.text_size = self.screen_size[0]//10
        self.offcice_size_text = 10

        self.screen = Tk(className='Circle beauty')
        self.screen.geometry("{}x{}".format(self.screen_size[0], self.screen_size[1]))
        self.screen.configure(bg=self.bg_color)

        self.menu = Label(bg=self.bg_color, text="Circle beauty", font=(None, self.text_size))
        self.menu.place(x=self.first_x, y=self.y, anchor="center")

        self.cb = Label(bg=self.bg_color, 
        text="pick color palette: \n(0 - black bg, white circle) \n(1 - white bg, black circle) \n(2 - from black bg to white bg)",
        font=(None, self.offcice_size_text))

        self.cb.place(x=self.first_x-100, y=self.y+(self.text_size//3)*3, anchor="center")

        self.choose_cb = Entry(self.screen, width=5, )
        self.choose_cb.place(x=self.first_x+100, y=self.y+(self.text_size//3)*3, anchor="center")

        self.circ = Label(bg=self.bg_color, 
        text="how much to increase \nthe value each time?\n(2 to the power of 'x')\nI suggest from 0 to -10",
        font=(None, self.offcice_size_text))

        self.circ.place(x=self.first_x-100, y=self.y+(self.text_size//3)*6, anchor="center")

        self.choose_circ = Entry(self.screen, width=5)
        self.choose_circ.place(x=self.first_x+100, y=self.y+(self.text_size//3)*6, anchor="center")

        self.ps = Label(bg=self.bg_color, 
        text="there is nothing like data validation, \nso you are responsible for incorrect input \nand subsequent errors",
        font=(None, self.offcice_size_text))

        self.ps.place(x=self.first_x, y=self.y+(self.text_size//3)*12, anchor="center")

        self.submit = Button(self.screen, width=20, height=2, text="Submit", command = lambda : self.start(self.screen_size, int(self.choose_circ.get()), int(self.choose_cb.get())))
        self.submit.place(x=self.first_x, y=self.y+(self.text_size//3)*13, anchor="center")

        self.screen.mainloop() 
    
    def start(self, size, var, bg):
            self.screen.destroy()
            cir = circle.Circle(size, var, bg)
            cir.run() 

if __name__=="__main__":
    menu = Menu()
  