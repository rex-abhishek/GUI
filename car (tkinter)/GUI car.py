from tkinter import*

ak=Tk()

c=Canvas(ak,height=650,width=800)
c.create_line(80,250,120,350)
c.create_line(120,350,170,350)
c.create_line(80,250,150,250)
c.create_line(150,250,220,150)
c.create_line(220,150,500,150)
c.create_line(500,150,600,250)
c.create_line(600,250,720,250)
c.create_line(720,250,720,350)
c.create_line(720,350,620,350)
c.create_oval(170,300,260,400, fill="black")
c.create_oval(530,300,620,400, fill="black")
c.create_line(260,350,530,350)

c.create_rectangle(220,250,350,170)
c.create_rectangle(400,250,500,170)

# road 
c.create_rectangle(0,300,850,500)
c.create_line(0,420,50,420)
c.create_line(80,420,120,420)
c.create_line(150,420,220,420)
c.create_line(250,420,320,420)
c.create_line(350,420,400,420)
c.create_line(400,420,450,420)
c.create_line(480,420,530,420)
c.create_line(550,420,600,420)
c.create_line(620,420,670,420)
c.create_line(690,420,760,420)

c.pack()
ak.mainloop()

