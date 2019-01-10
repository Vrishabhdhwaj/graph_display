from tkinter import *

root=Tk()

frame=Frame(root,width=500)
frame.grid(row=0,column=0,columnspan=2,rowspan=4)

#main info labels

Lmain=Label(root,text="Student Details",font="Times 15 bold underline")
L1=Label(root,text="Name of the Candidate:")
E1=Entry(root)
L2=Label(root,text="Father's Name:")
E2=Entry(root)
v=IntVar()
L3=Label(root,text="Gender:")
R1=Radiobutton(root,text="Male",variable=v,value=1)
R2=Radiobutton(root,text="Female",variable=v,value=2)
L1.grid(row=1,column=0)
L2.grid(row=2,column=0)
L3.grid(row=3,column=0)
E1.grid(row=1,column=1)
E2.grid(row=2,column=1,pady=20)
R1.grid(row=3,column=1,sticky=W)
R2.grid(row=4,column=1,sticky=W)
Lmain.grid(row=0,column=0,columnspan=2)

#subject labels ,entries ,radiobutton and subject info

Lsub=Label(root,text="Please enter your subject marks",font="Calibri 12 bold underline")
Lsub.grid(row=5,column=0,columnspan=2)
Ls1=Label(root,text="Physics")
Ls2=Label(root,text="Maths")
Ls3=Label(root,text="Chemistry")
Es1=Entry(root)
Es2=Entry(root)
Es3=Entry(root)
Ls1.grid(row=6,column=0)
Ls2.grid(row=7,column=0)
Ls3.grid(row=8,column=0)
Es1.grid(row=6,column=1)
Es2.grid(row=7,column=1)
Es3.grid(row=8,column=1)
phy=Es1.get()
mat=Es2.get()
che=Es3.get()

#this is the outline of the bar graph

can=Canvas(root,bg="white",height=400,width=400)
can.grid(row=9,column=0,rowspan=6,columnspan=2)
lineY=can.create_line(50,50,50,350)
lineX=can.create_line(50,350,350,350)
line1=can.create_line(45,300,55,300)
line2=can.create_line(45,250,55,250)
line3=can.create_line(45,200,55,200)
line4=can.create_line(45,150,55,150)
line5=can.create_line(45,100,55,100)
label1=can.create_text(35,300,text="20")
label2=can.create_text(35,250,text="40")
label3=can.create_text(35,200,text="60")
label4=can.create_text(35,150,text="80")
label5=can.create_text(35,100,text="100")
label6=can.create_text(105,360,text="Physics")
label7=can.create_text(205,360,text="Maths")
label8=can.create_text(305,360,text="Chemistry")

#function that shows the graph

def Bar_Graph():
	total=int(Es1.get())+int(Es2.get())+int(Es3.get())
	percentage=round(total/3.0, 2)
	ph=350-(int(Es1.get())*25)/10
	ma=350-(int(Es2.get())*25)/10
	ch=350-(int(Es3.get())*25)/10
	polyphy=can.create_polygon(80,350,130,350,130,ph,80,ph,fill="red")
	polypmat=can.create_polygon(180,350,230,350,230,ma,180,ma,fill="blue")
	polyche=can.create_polygon(280,350,330,350,330,ch,280,ch,fill="green")
	label9=can.create_text(150,30,text="Your Total Score is:" + str(total))
	labe20=can.create_text(300,30,text="Your Percentage is:" + str(percentage))

#Buttons go here
button1=Button(root,text="Submit",command=Bar_Graph)
button1.grid(row=16,column=0)

button2=Button(root,text="Quit",command=root.destroy)
button2.grid(row=16,column=1)

root.mainloop()
