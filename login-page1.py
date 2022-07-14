from tkinter import *
from tkinter import ttk

root = Tk()
root.configure(bg='purple')
root.title('STUDENT REGISTRATION FORM')
#root.attributes('-fullscreen', True)
root.geometry('1500x1500')


label1_line1 = Label(root,text='FIRST NAME',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row = 0,column = 0)
entry1_line1 = Entry(root,width=30).grid(row = 0,column = 3)
label2_line1 = Label(root,text='(max 30 characters a-z and A-Z)',bg='purple',fg='white',width=30,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=0,column = 4)

label1_line2 = Label(root,text='LAST NAME',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row = 2,column = 0)
entry1_line2 = Entry(root,width=30).grid(row = 2,column = 3)
label2_line2 = Label(root,text='(max 30 characters a-z and A-Z)',bg='purple',fg='white',width=30,anchor=W, font=('Montserat',10,'bold')).grid(row = 2,column = 4)

label1_line3 = Label(root,text='DATE OF BIRTH',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row = 4,column = 0)

day = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']
year = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
#use labda function in YEAR


day_menu = ttk.Combobox(root,values=day,width=27).grid(row =4 , column = 3)
label2_line3 = Label(root,text='Day',bg='white').grid(row=4,column=3)

#day_menu.current(0)
month_menu = ttk.Combobox(root,values=months,width=27).grid(row =4 , column = 4)
label3_line3 = Label(root,text='Month',bg='white').grid(row=4,column=4)


year_menu = ttk.Combobox(root,values=year,width=27).grid(row =4 , column = 5)
label4_line3 = Label(root,text='Year',bg='white').grid(row=4,column=5)


label1_line4 = Label(root,text='EMAIL ID',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=5,column=0)
entry1_line4 = Entry(root,width=30).grid(row=5,column=3)

label1_line5 = Label(root,text='Mobile Number',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=6,column=0)
entry1_line5 = Entry(root,width=30).grid(row=6,column=3)
label2_line5 = Label(root,text='(10 digit number)',bg='purple',fg='white',width=30,anchor=W, font=('Montserat',10,'bold')).grid(row=6,column=4)

label1_line6 = Label(root,text='GENDER',bg='purple',fg='white',width=15,anchor=W, font=('Montserat',10,'bold')).grid(row=7,column=0)
v=IntVar()
radio_button1_line6 = Radiobutton(root,text='Male',bg='purple',fg='white',height=2,anchor=W).grid(row=7,column=3)
radio_button2_line6 = Radiobutton(root,text='Female',bg='purple',fg='white',height=2,anchor=W).grid(row=7,column=4)

label1_line7 = Label(root,text='ADDRESS',bg='purple',fg='white',width=10 ,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=8,column=0)
entry1_line7 = Text(root,width=30,height=4,fg='black').grid(row=8,column=3)


label1_line8 = Label(root,text='CITY',bg='purple',fg='white',width=15,height=3,anchor=W, font=('Montserat',10,'bold')).grid(row=12,column=0)
entry1_line8 = Entry(root,width=30,fg='black').grid(row=12,column=3)

label1_line9 = Label(root,text='PINCODE',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=13,column=0)
entry1_line9 = Entry(root,width=30,fg='black').grid(row=13,column=3)
label2_line9 = Label(root,text='(6 digit number)',bg='purple',fg='white',width=30,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=13,column=4)

label1_line10 = Label(root,text='STATE',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=13,column=0)
entry1_line10 = Entry(root,width=30,fg='black').grid(row=13,column=3)
label2_line10 = Label(root,text='(max 30 characters a-z and A-Z)',bg='purple',fg='white',width=30,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=13,column=4)

label1_line11 = Label(root,text='COUNTRY',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=14,column=0)
entry1_line11 = Entry(root,width=30,fg='black').grid(row=14,column=3)
label2_line11 = Label(root,text='INDIA',fg='black',anchor=W).grid(row=14,column=3	)

label1_line12 = Label(root,text='HOBBIES',bg='purple',fg='white',width=15,height=2,anchor=W, font=('Montserat',10,'bold')).grid(row=15,column=0)
Checkbutton_1 = Checkbutton(root,text='Drawing',width=15,background='purple',fg='white', font=('Montserat',10,'bold')).grid(row=15,column=3)
Checkbutton_2 = Checkbutton(root,text='Singing',width=15,background='purple',fg='white', font=('Montserat',10,'bold')).grid(row=15,column=4)
Checkbutton_3 = Checkbutton(root,text='Dancing',width=15,background='purple',fg='white', font=('Montserat',10,'bold')).grid(row=15,column=5)
Checkbutton_4 = Checkbutton(root,text='Sketching',width=15,background='purple',fg='white', font=('Montserat',10,'bold')).grid(row=15,column=6)
Checkbutton_5 = Checkbutton(root,text='Singing',width=15,background='purple',fg='white', font=('Montserat',10,'bold')).grid(row=15,column=7)




root.mainloop()


# from tkinter import *
# from tkinter import ttk
# window=Tk()
# window.title("STUDENT REGISTRATION FORM")
# window.geometry('1500x1500')
# window.configure(background="purple");
# a074 = Label(window ,text = "First Name ",background="purple").grid(row = 0,column = 0)
# b074 = Label(window ,text = "Last Name ",background="purple").grid(row = 2,column = 0)
# c074 = Label(window ,text = "Date Of Birth ",background="purple").grid(row = 3,column = 0)
# d074 = Label(window ,text = "Email Id ",background="purple").grid(row = 3,column = 0)
# e074 = Label(window ,text = "Mobile Number ",background="purple").grid(row = 4,column = 0)
# f074 = Label(window ,text = "Gender",background="purple").grid(row = 5,column = 0)
# g074 = Label(window ,text = "Address ",background="purple").grid(row = 6,column = 0)
# h074 = Label(window ,text = "City ",background="purple").grid(row = 9,column = 0)
# i074 = Label(window ,text = "Pincode ",background="purple").grid(row = 10,column = 0)
# j074 = Label(window ,text = "State ",background="purple").grid(row = 11,column = 0)
# k074 = Label(window ,text = "Country ",background="purple").grid(row = 12,column = 0)
# l074 = Label(window ,text = "Hobbies ",background="purple").grid(row = 13,column = 0)
# m074 = Label(window ,text = "Qualifications ",background="purple").grid(row = 15,column = 0)
# n074 = Label(window ,text = "Courses Applied For ",background="purple").grid(row = 23,column = 0)

# e1_074=Entry(window,fg="purple",bg="light grey").grid(row = 0,column = 10)
# ttk.Label(window,text="Max 30 character A-Z and a-z",font=("Helvetica",7),background="purple").grid(row=0,column=11)

# e2_074=Entry(window,fg="purple",bg="light grey").grid(row = 2,column = 10)
# ttk.Label(window,text="Max 30 character A-Z and a-z",font=("Helvetica",7),background="purple").grid(row=1,column=11)

# day=StringVar()
# day = ttk.Combobox(window,width=4,textvariable=day)
# day.grid(row=3,column=10)
# ttk.Label(window, text = "Day",state='readonly',background="white").grid(row=2,column=10)
# day['values'] = ('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')

# month=StringVar()
# month=ttk.Combobox(window,width=6,textvariable=month)
# month.grid(row=3,column=11)
# ttk.Label(window,text="Month",state='readonly',background="white").grid(row=2,column=11)
# month['values']=('January','February','March','April','May','June','July','August','September','October','November','December')

# year=IntVar()
# year=ttk.Combobox(window,width=5,textvariable=year)
# year.grid(row=3,column=12)
# ttk.Label(window,text="Year",state='readonly',background="white").grid(row=2,column=12)
# year['values']=(2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021)

# e3_074=Entry(window,fg="purple",bg="light grey").grid(row=3,column=10)

# e4_074=Entry(window,fg="purple",bg="light grey").grid(row=4,column=10)
# ttk.Label(window,text="10 digit number",font=("Helvetica",7),background="purple").grid(row=4,column=11)

# R1_074=Radiobutton(window,bg="purple",text="Male").grid(row=5,column=10)
# R2_074=Radiobutton(window,bg="purple",text="Female").grid(row=5,column=11)

# e3_074=Entry(window,fg="purple",bg="light grey").grid(row=6,column=10)

# e4_074=Entry(window,fg="purple",bg="light grey").grid(row=9,column=10)

# e5_074=Entry(window,fg="purple",bg="light grey").grid(row=10,column=10)

# e6_074=Entry(window,fg="purple",bg="light grey").grid(row=11,column=10)

# e7_074=Entry(window,fg="purple",bg="light grey").grid(row=12,column=10)

# C1_074=Checkbutton(window,text = "Drawing",background="purple").grid(row=13,column=10)
# C2_074=Checkbutton(window,text="Singing",background="purple").grid(row=13,column=11)
# C3_074=Checkbutton(window,text="Dancing",background="purple").grid(row=13,column=12)
# C4_074=Checkbutton(window,text="Sketching",background="purple").grid(row=13,column=13)
# C5_074=Checkbutton(window,text="Others",background="purple").grid(row=14,column=10)
# e8_074=Entry(window,fg="purple",bg="light grey").grid(row=14,column=11)

# ttk.Label(window,text="SI.No.Examination",background="purple").grid(row=15,column=10)
# ttk.Label(window,text="Board",background="purple").grid(row=15,column=11)
# ttk.Label(window,text="Percentage",background="purple").grid(row=15,column=12)
# ttk.Label(window,text="Year Of Passing",background="purple").grid(row=15,column=13)
# ttk.Label(window,text="1. Class X",background="purple").grid(row=16,column=10)
# ttk.Label(window,text="2. Class XII",background="purple").grid(row=17,column=10)
# ttk.Label(window,text="3. Graduation",background="purple").grid(row=18,column=10)
# ttk.Label(window,text="4. Masters",background="purple").grid(row=19,column=10)
# e9_074=Entry(window,fg="purple",bg="light grey").grid(row=16,column=11)
# e10_074=Entry(window,fg="purple",bg="light grey").grid(row=16,column=12)
# e11_074=Entry(window,fg="purple",bg="light grey").grid(row=16,column=13)
# e12_074=Entry(window,fg="purple",bg="light grey").grid(row=17,column=11)
# e13_074=Entry(window,fg="purple",bg="light grey").grid(row=17,column=12)
# e14_074=Entry(window,fg="purple",bg="light grey").grid(row=17,column=13)
# e15_074=Entry(window,fg="purple",bg="light grey").grid(row=18,column=11)
# e16_074=Entry(window,fg="purple",bg="light grey").grid(row=18,column=12)
# e17_074=Entry(window,fg="purple",bg="light grey").grid(row=18,column=13)
# e18_074=Entry(window,fg="purple",bg="light grey").grid(row=19,column=11)
# e19_074=Entry(window,fg="purple",bg="light grey").grid(row=19,column=12)
# e20_074=Entry(window,fg="purple",bg="light grey").grid(row=19,column=13)

# R3_074=Radiobutton(window,bg="purple",text="BCA").grid(row=23,column=10)
# R4_074=Radiobutton(window,bg="purple",text="B.Com").grid(row=23,column=11)
# R5_074=Radiobutton(window,bg="purple",text="B.Sc").grid(row=23,column=12)
# R6_074=Radiobutton(window,bg="purple",text="B.A.").grid(row=23,column=13)


# B1_074=Button(window,text="SUBMIT").grid(row=24,column=11)
# B2_074=Button(window,text="RESET").grid(row=24,column=13)
# window.mainloop()
