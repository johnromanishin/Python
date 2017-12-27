from Tkinter import *
class App:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.button = Button(frame, 
                         text="QUIT", fg="red",
                         command=frame.quit)
    self.button.pack(side=LEFT)

    self.slogan = Button(frame,
                         text="RED",
                         command=self.write_RED)
    self.slogan.pack(side=LEFT)

    self.blue = Button(frame,
                         text="BLUE",
                         command=self.write_BLUE)
    self.blue.pack(side=LEFT)

  def write_slogan(self):
    print "Tkinter is RED"


  def write_blue(self):
    print "Tkinter is BLUE"
root = Tk()
app = App(root)
root.mainloop()
