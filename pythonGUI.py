#################################################
#################################################
##                                             ##
##  Final Project Database                     ##
##                                             ##
##  Due 5/14/21                                ##
##                                             ##
#################################################
#################################################
from tkinter import*
from tkinter import ttk
import tkinter.messagebox
import pymysql

class ConnectorDB:

    def __init__(self, root):
        self.root = root
        titlespace = " "
        self.root.title(102 * titlespace + "MySQL Database")
        self.root.geometry("776x700+300+0")
        self.root.resizable(width =False, height=False)

        #Main Frame
        MainFrame = Frame(self.root, bd=10, width=770, height=700, relief=RIDGE, bg='steel blue')
        MainFrame.grid()

        #Title Frame
        TitleFrame = Frame(MainFrame, bd=7, width=770, height=500, relief=RIDGE)
        TitleFrame.grid(row = 0, column = 0)
        TopFrame = Frame(MainFrame, bd=5, width=770, height=400, padx=2, relief=RIDGE, bg='steel blue')
        TopFrame.grid(row=1, column=0)

        #Left Frame
        LeftFrame = Frame(TopFrame, bd=5, width=770, height=400, padx=2, relief=RIDGE, bg='steel blue')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width=600, height=180, relief=RIDGE, padx=2, pady=4, bg='steel blue')
        LeftFrame1.pack(side=TOP, padx=0, pady=0)

        #Right Frame
        RightFrame = Frame(TopFrame, bd=5, width=100, height=400, padx=2, relief=RIDGE, bg='steel blue')
        RightFrame.pack(side=RIGHT)
        RightFrame1 = Frame(RightFrame, bd=5, width=90, height=300, padx=2, pady=2, relief=RIDGE)
        RightFrame1.pack(side=TOP)
        #===========================================================================================#
        student_id =IntVar()
        first_name =StringVar()
        last_name =StringVar()
        phone =StringVar()
        email =StringVar()
        #===========================================================================================#
        #functions 
        def iExit():
            '''
            Function to exit the GUI
            '''
            iExit = tkinter.messagebox.askyesno("MySQL Connection", "Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def Reset():
            '''
            Function that resets input
            in the text boxes
            '''
            self.entstudent_id.delete(0,END)
            self.entFirst.delete(0,END)
            self.entLast.delete(0,END)
            self.entphone.delete(0,END)
            self.entemail.delete(0,END)

        def addData():
            '''
            Function to add
            data to the database
            '''
          #  if student_id.get() =="" or first_name.get() =="" or last_name.get() =="":
             #   tkinter.messagebox.showerror("Mysql Connnection", "Enter Correct Details")
          #  else:
            sqlCon = pymysql.connect(host ="you_wish,user="admin",password="hunter2",database="school_management_system")
            cur =sqlCon.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s)",(

            student_id.get(),
            first_name.get(),
            last_name.get(),
            phone.get(),
            email.get(),
            ))
            sqlCon.commit()
            sqlCon.close()
            tkinter.messagebox.showinfo("MySql Connection", "Record Entered Successfully")

        def DisplayData():
            '''
            Function to display
            the data from the table
            to the GUI
            '''
            sqlCon = pymysql.connect(host ="cs-470.cnojrtaqodew.us-east-2.rds.amazonaws.com",user="admin",password="wpVTRX5Aa",database="school_management_system")
            cur =sqlCon.cursor()
            cur.execute("select * from student")
            result= cur.fetchall()
            if len(result) != 0:
                self.student_records.delete(*self.student_records.get_children())
                for row in result:
                    self.student_records.insert('',END,values =row)
            sqlCon.commit()
            sqlCon.close()
            
        def TableInfo(ev):
            '''
            Function to display the row
            selected by the user to the
            '''
            viewInfo = self.student_records.focus()
            learnerData = self.student_records.item(viewInfo)
            row = learnerData['values']
            student_id.set(row[0])
            first_name.set(row[1]),
            last_name.set(row[2]),
            phone.set(row[3]),
            email.set(row[4]),

        def update():
            '''
            Updates the data in table to
            user specified contraints
            '''
            
            sqlCon = pymysql.connect(host ="cs-470.cnojrtaqodew.us-east-2.rds.amazonaws.com",user="admin",password="wpVTRX5Aa",database="school_management_system")
            cur =sqlCon.cursor()
            cur.execute("update student set first_name=%s, last_name=%s, phone=%s, email=%s where student_id=%s",(

            student_id.get(),
            first_name.get(),
            last_name.get(),
            phone.get(),
            email.get(),
            ))
            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Updated Successfully")


        def deleteDB():
            '''
            deletes selected data
            from the table
            '''
            sqlCon = pymysql.connect(host ="cs-470.cnojrtaqodew.us-east-2.rds.amazonaws.com",user="admin",password="wpVTRX5Aa",database="school_management_system")
            cur =sqlCon.cursor()
            cur.execute("delete from student where student_id=%s",student_id.get())

            sqlCon.commit()
            DisplayData()
            sqlCon.close()
            tkinter.messagebox.showinfo("Data Entry Form", "Record Successfully Deleted")
            Reset()

        def searchDB():
            '''
            searches the table for a
            certain student ID number
            and returns the results to the
            screen
            '''
            try:
                sqlCon = pymysql.connect(host ="cs-470.cnojrtaqodew.us-east-2.rds.amazonaws.com",user="admin",password="wpVTRX5Aa",database="school_management_system")
                cur =sqlCon.cursor()
                cur.execute("Select * from student where student_id=%s",student_id.get())
                row = cur.fetchone()

                student_id.set(row[0])
                first_name.set(row[1]),
                last_name.set(row[2]),
                phone.set(row[3]),
                email.set(row[4]),

                sqlCon.commit()
            except:
                tkinter.messagebox.showinfo("Data Entry Form", "No Such Record Found")
                Reset()
            sqlCon.close()
        
        #lbls
#===========================================================================================#
        #Title
        self.lbltitle=Label(TitleFrame, font=('arial',40,'bold'), text="School Database", bd=7)
        self.lbltitle.grid(row=0,column=0, padx=132)
#===========================================================================================#
        #Student ID
        self.lblstudent_id=Label(LeftFrame1, font=('arial',12,'bold'), text="Student ID", bd=7, justify='left')                          
        self.lblstudent_id.grid(row=1, column=0, sticky=W, padx=5)
        self.entstudent_id=Entry(LeftFrame1, font=('arial',12,'bold'), text="Student ID", bd=7, justify='left', width=44,
                                 textvariable=student_id)
        self.entstudent_id.grid(row=1, column=1, stick=W, padx=5)

        #First Name
        self.lblFirst=Label(LeftFrame1, font=('arial',12,'bold'), text="First Name", bd=7, justify='left')                        
        self.lblFirst.grid(row=2, column=0, sticky=W, padx=5)
        self.entFirst=Entry(LeftFrame1, font=('arial',12,'bold'), bd=7, justify='left', width=44,
                            textvariable=first_name)
        self.entFirst.grid(row=2, column=1, stick=W, padx=5)

        #Last Name
        self.lblLast=Label(LeftFrame1, font=('arial',12,'bold'), text="Last Name", bd=7, justify='left')                 
        self.lblLast.grid(row=3, column=0, sticky=W, padx=5)
        self.entLast=Entry(LeftFrame1, font=('arial',12,'bold'), bd=7, justify='left', width=44,
                           textvariable=last_name)
        self.entLast.grid(row=3, column=1, stick=W, padx=5)

        #phone
        self.lblphone=Label(LeftFrame1, font=('arial',12,'bold'), text="phone", bd=7, justify='left')
        self.lblphone.grid(row=4, column=0, sticky=W, padx=5)
        self.entphone=Entry(LeftFrame1, font=('arial',12,'bold'), bd=7, justify='left', width=44,
                            textvariable=phone)
        self.entphone.grid(row=4, column=1, stick=W, padx=5)

        #Email
        self.lblemail=Label(LeftFrame1, font=('arial',12,'bold'), text="email", bd=7, justify='left')                     
        self.lblemail.grid(row=5, column=0, sticky=W, padx=5)
        self.entemail=Entry(LeftFrame1, font=('arial',12,'bold'), bd=7, justify='left', width=44,
                            textvariable=email)
        self.entemail.grid(row=5, column=1, stick=W, padx=5)

        #Table======================================================================================#
        scroll_y = Scrollbar(LeftFrame, orient = VERTICAL)
        self.student_records=ttk.Treeview(LeftFrame, height=12, columns=("stdid", "first_name", "last_name", "phone","email"),
                                          yscrollcommand=scroll_y.set)
        
        scroll_y.pack(side = RIGHT, fill=Y)

        self.student_records.heading("stdid", text="Student ID")
        self.student_records.heading("first_name", text="First Name")
        self.student_records.heading("last_name", text="Last Name")
        self.student_records.heading("phone", text="Phone")
        self.student_records.heading("email", text="Email")

        self.student_records['show']='headings'

        self.student_records.column("stdid", width=70)
        self.student_records.column("first_name", width=100)
        self.student_records.column("last_name", width=100)
        self.student_records.column("phone", width=70)
        self.student_records.column("email", width=70)

        self.student_records.pack(fill=BOTH, expand=1)
        self.student_records.bind("<ButtonRelease-1>",TableInfo)
        #DisplayData()

        #Buttons====================================================================================#
        
        self.buttonAddNew=Button(RightFrame1, font=('arial',16, 'bold'), text="Add New", bd =4, pady=1, padx=24,
                             width = 8, height=2, command=addData).grid(row=0,column=0, padx=1)

        self.buttonDisplay=Button(RightFrame1, font=('arial',16, 'bold'), text="Display", bd =4, pady=1, padx=24,
                             width = 8, height=2, command=DisplayData).grid(row=1,column=0, padx=1)

        self.buttonUpdate=Button(RightFrame1, font=('arial',16, 'bold'), text="Update", bd =4, pady=1, padx=24,
                             width = 8, height=2, command=update).grid(row=2,column=0, padx=1)

        self.buttonDelete=Button(RightFrame1, font=('arial',16, 'bold'), text="Delete", bd =4, pady=1, padx=24,
                             width = 8, height=2, command=deleteDB).grid(row=3,column=0, padx=1)

        self.buttonSearch=Button(RightFrame1, font=('arial',16, 'bold'), text="Search", bd =4, pady=1, padx=24,
                             width = 8, height=2, command=searchDB).grid(row=4,column=0, padx=1)

        self.buttonReset=Button(RightFrame1, font=('arial',16, 'bold'), text="Reset", bd =4, pady=1, padx=24,
                             width = 8, height=2, command=Reset).grid(row=5,column=0, padx=1)

        self.buttonExit=Button(RightFrame1, font=('arial',16, 'bold'), text="Exit", bd =4, pady=1, padx=24,
                             width = 8, height=2, command=iExit).grid(row=6,column=0, padx=1)



if __name__=='__main__':
    root = Tk()
    application = ConnectorDB(root)
    root.mainloop()

























          #
                          #   
         #                  #
         #
 #                               
 #                #      #
   #             #            #

        ##                
         # #           # #         
       #  #  #          #  #    ###
    #  #   #  #          # #  #  # 
  #   #    #   #    #   #   #    #
#    #   ##    #     # #        #
#     ###     #       #        #  # 
 #              #     #       #   ##
  #        #     #  #         #  # #
   #      # #  ### #           ##  #   
   #   ##    #    ##    #         #
  #    # #     ## #    # # #     #  
##    # #     #     #   #     # # #
