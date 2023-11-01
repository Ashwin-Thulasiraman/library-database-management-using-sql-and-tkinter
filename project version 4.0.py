import mysql.connector as s
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk

mc=s.connect(host="localhost",user="root",passwd="")
cr=mc.cursor()

cr.execute('create database if not exists library')
cr.execute('use library')
cr.execute('drop table if exists library_data')
cr.execute('create table if not exists orders(Book_Name varchar(90),Date_of_Order date)')
cr.execute("create table if not exists library_data(ID int primary key,Book varchar(45),Author varchar(45),Genre varchar(45),DateOfPublication date,price float(10,2),Held_by varchar(45));")
cr.execute('''insert into library_data values (001,'Da Vinci Code,The','Brown,Dan','Crime
Thriller','19901230',2000,'Vishnu'),
(002,'Harry Potter and The Deadly Hallows','J.K.Rowling','Child fiction','19870305',3500,'Mayur'),
(003,'Fifty Shades Of Grey','James.E.L','Romance & Sagas','19890406',2700,'Rama'),
(004,'Angels and Demons','Brown,Dan','Crime Thriller','19950304',2400,'Library'),
(005,'Twilight','Meyer,Stephenie','Young Adult Fiction','19990417',1500,'Shrinivas'),
(006,'New Moon','Meyer,Stephenie','Young Adult Fiction','19910724',1700,'Ramakrishna'),
(007,'One Day','Nicholls,David','General Literary Fiction','19930927',1400,'Kishan'),
(008,'Atonement','McEwan,Ian','General Literary Fiction','19960409',1800,'Deepak'),
(009,'Thousand Splendid Suns','Hosseni,Khaled','General Literary Fiction','19951130',3000,'Library'),
(010,'Life of Pi','Mattel,Yann','General Literary Fiction','19920114',2900,'Apoorva'),
(011,'A lost Boy','Pelzer,Dave','biography','19930212',1700,'Library'),
(012,'Hunger Games','Collins','Young Adult Fiction','18870312',2100,'Library'),
(013,'Nights of Rani and Stars','Binchy','Literary Fiction','19910424',2700,'Library'),
(014,'My booky Wook','Brand','Autobiography','19960606',2400,'library'),
(015,'About a Boy','Hornby','Literary fiction','19970715',1800,'Shrinivas'),
(016,'Room on The Broom','Donaldson','Picture books','19950830',1600,'Deepak'),
(017,'Brick Lane','Ali,Monica','Literary fiction','19990621',3200,'library'),
(018,'Small Island','Levy,Andrea','Literary fiction','20010717',3600,'Library'),
(019,'Down Under','Bryson','Travelogue','20010719',2700,'Shrinivas'),
(020,'lord of The Rings','Tolkien.J.R.R','Science Fiction','20000709',3100,'Vishnu'),
(021,'Hannibal','Harris,Thomas','Crime Thriller','19990804',1900,'Library'),
(022,'Dear Fatty','French,Dawn','Autobiography','19900708',1800,'Kishan'),
(023,'To Kill a Mockingbird','Lee,Harper','Literary Fiction','19980905',2199,'Library'),
(024,'Broker','Grisham,John','Crime thriller','19890909',3400,'Mayur'),
(025,'Man and Boy','Parsons,Tony','Literary Fiction','19930425',4500,'Rama'),
(026,'Birdsong','Faulks,Sebastian','Literary Fiction','19940919',1200,'Library'),
(027,'Labyrinth','Mosse,Kate','Literary Fiction','19970807',1600,'Apoorva'),
(028,"Angelas Ashes",'McCourt','Autobiography','19970409',1700,'Library'),
(029,'Billy Connolly','Stephenson','Biography','19950809',1400,'Library'),
(030,'Sound of Laughter','Kay,Peter','Autobiography','19930927',1900,'Ramakrishna'),
(031,"Time Travellers Wife",'Audrey','Literary Fiction','19930927',2100,'Vishnu'),
(032,'One Day','Nicholls','Literary fiction','19990927',2300,'Ashwin'),
(033,'Digital Fortress','Brown,Dan','Crime Thriller','19930917',2500,'Vishva'),
(034,'Lovely Bones','Alice','Literary Fiction','19961007',3200,'Library'),
(035,'Deception Point','Brown,Dan','Adventure','19960721',3000,'Avesh'),
(036,'Lost Symbol','Brown,Dan','Crime Thriller','19940807',2000,'Moshin'),
(037,'Fifty Shades Freed','James','Romance','19920229',2700,'Kuldeep'),
(038,'Shadow Of The Wind','Zafon','Literary fiction','19910126',2560,'Vijay'),
(039,'Harry Potter And The Half Blood Prince','J.K.Rowling','Science fiction','19980506',3400,'Rohit'),
(040,'Very hungry Caterpillar','Eric','Picture Books','19951221',3700,'Rohan'),
(041,'White Teeth','Smith,Zadie','Literary Fiction','19930530',3400,'Library'),
(042,'Madame Bovary','Gustave Flavbert','French Novel','19870605',2700,'Library'),
(043,'In Search Of Lost Time','Marcel Proust','Science Fiction','19960516',2900,'Parag'),
(044,'The Stranger','Albert Camus','Crime Thriller','19940908',3200,'Kajal'),
(045,'The Red And The Black','Stendhal','French Novel','19860516',3400,'Lilly'),
(046,'The Charterhouse By Parama','Stendhal','French Novel','19830715',3600,'Library'),
(047,'Cousin Bette','Honoure de Balzac','Crime Thriller','19920409',3200,'Charlie'),
(048,'Candide','Volatire','Romance and Sagas','19930715',2600,'Sundar'),
(049,'Germinal','Emile Zolta','Literary Fiction','19840819',3700,'Library'),
(050,'The Lover','Margurite Duras','Literary Fiction','19821230',3200,'Mark');
''')
HEIGHT=500
WIDTH=600

def win2(x):
    
    frame=tk.Frame(x,bg="silver",bd=5)
    frame.place(relx=0.5,rely=0.1,relwidth=0.6,relheight=0.1,anchor="n")

    entry=tk.Entry(frame,bg="blanchedalmond",font=('Calibri 18 bold'))
    entry.place(relwidth=0.39,relheight=1)

    mf=tk.Frame(x,bg="silver",bd=5)
    mf.place(relx=0.5,rely=0.23,relwidth=0.6,relheight=0.1,anchor="n")

    l2=tk.Label(mf,bg="blanchedalmond",font= ('Ariel 15 bold'))
    l2.place(relwidth=1,relheight=1)
    l2["text"]="Please type the name of desired book\nin the search box and press on get book info"

    f=tk.Frame(x)
    f.place(relx=0.14,rely=0.8,relwidth=0.1,relheight=0.1,anchor="n")
    def bth(y):
        y.destroy()
        root.deiconify()
    
    b=tk.Button(f,text="Back to \nHome window",font=40,command=lambda:bth(x))
    b.place(relheight=1,relwidth=1)
    
    lower_frame=tk.Frame(x,bg="silver",bd=10)
    lower_frame.place(relx=0.5,rely=0.35,relwidth=0.6,relheight=0.6,anchor="n")
    
    #start of messy scrollbar

    my_canvas=tk.Canvas(lower_frame)
    my_canvas.place(relx=0.5,rely=0.35,relwidth=0.6,relheight=0.6,anchor="n")
    my_scrollbar = ttk.Scrollbar(lower_frame, orient='vertical', command=my_canvas.yview)
    my_scrollbar.place(relx=0.7,rely=0.7,relwidth=0.6,relheight=0.6,anchor="n")
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind("<Configure>",lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))
    sec_frame=tk.Frame(my_canvas)
    my_canvas.create_window((0,0),window=sec_frame,anchor="nw")
    #end of messy scrollbar
    label=tk.Label(lower_frame,bg="blanchedalmond",font= ('Calibri 17 bold'))
    label.place(relwidth=1,relheight=1)

    def fetch(entry):
            try:
                l=entry.split(" ")
                entry2=l[1]+","+l[0]
            except:
                entry2=entry
            sql1="select * from library_data where book like '%{}%' or book like '{}%' or book like '{}' or Author like '{}%' or Author like '%{}%' or Author like '{}'".format(entry,entry,entry,entry,entry,entry2)
            cr.execute(sql1)
            d=cr.fetchall()
            label["text"]=""
            n=0
            l=["ID","Book","Author","Genre","Date of Publication","Price","Held by"]
            for i in d:
                count=0
                n+=1
                if n>=2:    
                    label["text"]+="\nAlso related to your search\n\n"
                for j in i:
                    a=l[count]
                    b=a+":"+str(j)
                    label["text"]+=b+"\n"
                    count+=1
            if n==0:
                    cr.execute("select book,author from library_data where genre like '%{}' or genre like '{}' or genre like '%{}%'".format(entry,entry,entry))
                    d=cr.fetchall()
                    label["text"]=""
                    n=0
                    l=["Book","Author","Author","Genre","Date of Publication","Price","Held by"]
                    for i in d:
                        count=0
                        n+=1
                        if n==8:
                            break
                        if n>=2:    
                            label["text"]+="\n"
                        for j in i:
                            a=l[count]
                            b=a+":"+str(j)
                            label["text"]+=b+"\n"
                            count+=1
                    if n==0:
                            label["text"]="""Sorry for your inconvience
    Book/genre not available.
    But don't worry you can place your order
    by typing the full name of your book and clicking
    Place order&view option
    to place your order for the book
    """
                            
            return " "

    button=tk.Button(frame,text="Get book info",font=40,command=lambda: fetch(entry.get()))
    button.place(relx=0.4,relheight=1,relwidth=0.3)
    def fetch1(entry):
            sql1="""insert into orders values('{}',(select curdate()));""".format(entry)
            cr.execute(sql1)
            sql2="""select * from orders where book_name='{}' order by book_name desc limit 1""".format(entry)
            cr.execute(sql2)
            a=cr.fetchone()
            label["text"]="""Your Order has been placed
    You can approach your nearest
    branch of our library after 2 months
    of order placement to enquire
    about the availability\n\n"""+"Your order details:\n"+"Book name"+"\t"+"Date of order placement\n"+str(a[0])+"\t\t"+str(a[1])
            return " "


    button=tk.Button(frame,text="Place order",font=40,command=lambda:fetch1(entry.get()))
    button.place(relx=0.7,relheight=1,relwidth=0.3)

def win3(x):
    frame=tk.Frame(x,bg="silver",bd=5)
    frame.place(relx=0.5,rely=0.1,relwidth=0.6,relheight=0.1,anchor="n")

    entry=tk.Entry(frame,bg="blanchedalmond",font=('Calibri 18 bold'))
    entry.place(relwidth=0.6,relheight=1)

    mf=tk.Frame(x,bg="silver",bd=5)
    mf.place(relx=0.5,rely=0.23,relwidth=0.6,relheight=0.1,anchor="n")

    l2=tk.Label(mf,bg="blanchedalmond",font= ('Ariel 15 bold'))
    l2.place(relwidth=1,relheight=1)
    l2["text"]="To place your order,please type the full name of book\nin the search box and press on place order"

    f=tk.Frame(x)
    f.place(relx=0.14,rely=0.8,relwidth=0.1,relheight=0.1,anchor="n")
    def bth(y):
        y.destroy()
        root.deiconify()
    
    b=tk.Button(f,text="Back to \nHome window",font=40,command=lambda:bth(x))
    b.place(relheight=1,relwidth=1)
    
    lower_frame=tk.Frame(x,bg="silver",bd=10)
    lower_frame.place(relx=0.5,rely=0.35,relwidth=0.6,relheight=0.6,anchor="n")
    
    label=tk.Label(lower_frame,bg="blanchedalmond",font= ('Calibri 17 bold'))
    label.place(relwidth=1,relheight=1)

    def fetch1(entry):
            sql1="""insert into orders values('{}',(select curdate()));""".format(entry)
            cr.execute(sql1)
            sql2="""select * from orders where book_name='{}' order by book_name desc limit 1""".format(entry)
            cr.execute(sql2)
            a=cr.fetchone()
            label["text"]="""Your Order has been placed
    You can approach your nearest
    branch of our library after 2 months
    of order placement to enquire
    about the availability\n\n"""+"Your order details:\n"+"Book name"+"\t"+"Date of order placement\n"+str(a[0])+"\t\t"+str(a[1])
            return " "

    button=tk.Button(frame,text="Place order",font=40,command=lambda:fetch1(entry.get()))
    button.place(relx=0.6,relheight=1,relwidth=0.4)

def new(root,h):
    root.withdraw()
    r2=tk.Tk()
    canvas=tk.Canvas(r2,height=HEIGHT,width=WIDTH)
    canvas.pack()

    im=Image.open(r"C:\Users\ashwi\Downloads\books.png")
    photo = ImageTk.PhotoImage(im,master=r2)

    label = tk.Label(r2, image=photo)
    label.image = photo
    label.place(relwidth=1, relheight=1)
    if h=="w2":
        win2(r2)
    elif h=="w3":
        win3(r2)
    r2.mainloop()


root=tk.Tk()
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

im = Image.open(r"C:\Users\ashwi\Downloads\booksmod.png.jpg")
photo = ImageTk.PhotoImage(im)

label = tk.Label(root, image=photo)
label.image = photo
label.place(relwidth=1, relheight=1)

frame1=tk.Frame(root,bg="silver",bd=5)
frame1.place(relx=0.5,rely=0.03,relwidth=0.6,relheight=0.1,anchor="n")

label1=tk.Label(frame1,bg="paleturquoise",font= ('Helvetica 20 bold'))
label1.place(relwidth=1,relheight=1)
label1["text"]="Welcome to MIST Library Management System"

frame2=tk.Frame(root,bg="silver",bd=5)
frame2.place(relx=0.5,rely=0.25,relwidth=0.5,relheight=0.3,anchor="n")

label2=tk.Label(frame2,bg="lightyellow",font= ('Helvetica 20'))
label2.place(relwidth=1,relheight=1)
label2["text"]="Choose one of the following two options:\nBook details-To search for book by name,author or genre\nOrder placement-To place an order for your book"

frame3=tk.Frame(root,bg="silver",bd=5)
frame3.place(relx=0.5,rely=0.6,relwidth=0.2,relheight=0.2,anchor="n")

button=tk.Button(frame3,text="Book details",font=100,command=lambda:new(root,"w2"))
button.place(relheight=0.5,relwidth=1)

button=tk.Button(frame3,text="Order placement",font=100,command=lambda: new(root,"w3"))
button.place(rely=0.5,relheight=0.5,relwidth=1)




root.mainloop() 

