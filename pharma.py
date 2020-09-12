from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import pymysql

def main():
    root = Tk()
    app = Window1(root)
    root.configure(bg = 'powder blue')
    root.mainloop()




#================================MAIN WINDOW =================================================================
class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("PHARMACY APP")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master,bg = 'powder blue')
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame,text = "CHEMIST INVENTORY SYSTEM",font = ('arial',50,'bold'),bd = 20,bg = 'powder blue')
        self.LabelTitle.grid(row = 0,column = 0,columnspan = 2,pady = 20)

        self.LoginFrame1 = Frame(self.frame, width = 1010,height = 300,relief = 'flat',bg = 'powder blue')
        self.LoginFrame1.grid(row = 1, column = 0, pady = 20)

        self.LoginFrame2 = Frame(self.frame, width = 1010,height = 100,bd = 10,relief = 'ridge',bg = 'powder blue')
        self.LoginFrame2.grid(row = 5, column = 0,pady = 20)

        self.LoginFrame3 = Frame(self.frame, width = 1010,height = 200,bd = 10,relief = 'ridge',bg = 'powder blue')
        self.LoginFrame3.grid(row = 9, column = 0)

#============================USERNAME AND PASSWORD ==============================================================================



        self.lblUsername = Label(self.LoginFrame1,text = "Username",font = ('arial',30,'bold'),bd = 22,bg = 'powder blue')
        self.lblUsername.grid(row = 0,column = 0)
        self.txtUsername = Entry(self.LoginFrame1,font = ('arial',30,'bold'),textvariable = self.Username,bd = 22)
        self.txtUsername.grid(row = 0,column = 1,pady = 10)

        self.lblpassword = Label(self.LoginFrame1,text = "Password",font = ('arial',30,'bold'),bd = 22,bg = 'powder blue')
        self.lblpassword.grid(row = 1,column = 0)
        self.txtpassword = Entry(self.LoginFrame1,font = ('arial',30,'bold'),textvariable = self.Password,show = ".",bd = 22)
        self.txtpassword.grid(row = 1,column = 1,padx = 85)



#=======================================BUTTONS ON MAIN WINDOW=============================================================



        self.btnLogin = Button(self.LoginFrame2,text = "Login",width = 17,font = ('arial',20,'bold'),command = self.Login_details)
        self.btnLogin.grid(row = 0, column = 0)

        self.btnReset = Button(self.LoginFrame2,text = "Reset",width = 17,font = ('arial',20,'bold'),command = self.reset)
        self.btnReset.grid(row = 0, column = 1)

        self.btnexit = Button(self.LoginFrame2,text = "Exit",width = 17,font = ('arial',20,'bold'),command = self.iexit)
        self.btnexit.grid(row = 0, column = 2)

        self.btnAdd = Button(self.LoginFrame3,text = "Add new stock",state = DISABLED,width = 15,font = ('arial',20,'bold'),command =self.Adding_product)
        self.btnAdd.grid(row = 0, column = 0)

        self.btnBill = Button(self.LoginFrame3,text = "New bill",state = DISABLED,width = 15,font = ('arial',20,'bold'),command =self.print_bill)
        self.btnBill.grid(row = 0, column = 1)

        self.btnStock = Button(self.LoginFrame3,text = "Check stock",state = DISABLED,width = 15,font = ('arial',20,'bold'),command = self.stock_check)
        self.btnStock.grid(row = 0, column = 2)



#========================================FUNCTIONS OF BUTTONS===========================================================
        
    
    def Login_details(self):
        User = (self.Username.get())
        pas = (self.Password.get())
        if User ==  "gup" and pas == str(9873):
            self.btnAdd.config(state = NORMAL)
            self.btnBill.config(state = NORMAL)
            self.btnStock.config(state = NORMAL)
            

        else:
            tkinter.messagebox.askokcancel("CHEMIST INVENTORY SYSTEM","You have entered the invalid login details")
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()
    
    
    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()
        self.btnAdd.config(state = DISABLED)
        self.btnStock.config(state = DISABLED)
        self.btnBill.config(state = DISABLED)

    
    def iexit(self):
        self.iexit = tkinter.messagebox.askyesno("CHEMIST INVENTORY SYSTEM","Do you really want to exit!")
        if self.iexit > 0:
            self.master.destroy()
            return

    
    def Adding_product(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)
    
    
    def print_bill(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)


    def stock_check(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window5(self.newWindow)



#====================================ADDING PRODUCT WINDOW====================================================================



class Window2:
    def __init__(self,master):
        self.master = master
        self.master.title("Add a product")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'powder blue')
        self.frame = Frame(self.master,bg = 'powder blue')
        self.frame.pack()

        self.Product_id = StringVar()
        self.Product_name = StringVar()
        self.Product_qty = IntVar()
        self.Product_price = IntVar()
    



#====================================LABELS AND ENTRY FIELDS====================================================================



        self.LabelTitle = Label(self.frame,text = " NEW PRODUCT ADDITION ",font = ('arial',50,'bold'),bg = 'powder blue',pady = 20)
        self.LabelTitle.grid(row = 0, column = 0,columnspan = 2)
        self.AddFrame = Frame(self.frame, width = 1010,height = 600,relief = 'ridge',bg = 'powder blue')
        self.AddFrame.grid(row = 1, column = 0)
        
        self.lblid = Label(self.AddFrame,text = "Product ID",font = ('arial',25,'bold'),bd = 22,bg = 'powder blue')
        self.lblid.grid(row = 0,column = 0)
        self.txtid = Entry(self.AddFrame,font = ('arial',25,'bold'),textvariable = self.Product_id,bd = 22)
        self.txtid.grid(row = 0,column = 1)

        self.lblname = Label(self.AddFrame,text = "Product Name",font = ('arial',25,'bold'),bd = 22,bg = 'powder blue')
        self.lblname.grid(row = 1,column = 0)
        self.txtname = Entry(self.AddFrame,font = ('arial',25,'bold'),textvariable = self.Product_name,bd = 22)
        self.txtname.grid(row = 1,column = 1)

        self.lblqty = Label(self.AddFrame,text = "Product Quantity",font = ('arial',25,'bold'),bd = 22,bg = 'powder blue')
        self.lblqty.grid(row = 2,column = 0)
        self.txtqty = Entry(self.AddFrame,font = ('arial',25,'bold'),textvariable = self.Product_qty,bd = 22)
        self.txtqty.grid(row = 2,column = 1)

        self.lblprice = Label(self.AddFrame,text = "Product Price",font = ('arial',25,'bold'),bd = 22,bg = 'powder blue')
        self.lblprice.grid(row = 3,column = 0)
        self.txtprice = Entry(self.AddFrame,font = ('arial',25,'bold'),textvariable = self.Product_price,bd = 22)
        self.txtprice.grid(row = 3,column = 1)



#===================================ADD WINDOW BUTTON==========================================================================



        self.btnADD = Button(self.AddFrame,text = "ADD",width = 15,bd = 10,font = ('arial',20,'bold'),command = self.addbtn)
        self.btnADD.grid(row = 6,column = 3)



#====================================FUNCTION OF ADD BUTTON====================================================================


    
    def addbtn(self):
        ide = (self.Product_id.get())
        name = (self.Product_name.get())
        qty = (self.Product_qty.get())
        price = (self.Product_price.get())
        a = []
        if ide ==  None or name ==  None or qty ==  0 or price ==  0:
            tkinter.messagebox.showerror(" NEW PRODUCT ADDITION ","You haven't entered all the details")
        else:
            query = 'SELECT Product_id from STOCK'
            try:
              
                conn = pymysql.connect(host="localhost",user="root", passwd="deepak@123",database="pharmacy")
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(query)
                        value = cur.fetchall()
                        for i in value:
                            for j in i:
                                a.append(j)

                        if ide not in a:
                            query1 = "INSERT INTO STOCK (Product_id, Product_name, Product_qty, product_price) VALUES('{}','{}',{},'{}')".format(ide,name,qty,price)
                            cur.execute(query1)
                        else:
                            query2 = "SELECT Product_qty from STOCK WHERE Product_id = '{}'".format(ide)
                            cur.execute(query2)
                            ans = cur.fetchone()
                            qty += ans[0]
                            query3 = "UPDATE STOCK SET Product_qty = {} WHERE Product_id = '{}'".format(qty,ide)
                            cur.execute(query3)
            except Exception as e:
                tkinter.messagebox.showerror(" NEW PRODUCT ADDITION ",e)




            
            self.Product_id.set("")
            self.Product_name.set("")
            self.Product_qty.set("")
            self.Product_price.set("")
            self.txtid.focus()



#====================================BILLING WINDOW====================================================================


class Window3:
    def __init__(self,master):
        self.master = master
        self.master.title("Print a bill")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'powder blue')

        self.Product_id = IntVar()
        self.name = StringVar()
        self.phone = IntVar()
        self.doc = StringVar()
        self.docadd = StringVar()
        self.Product_nam = StringVar()
        self.Product_qt = IntVar()
        self.Product_pric = IntVar()


#====================================LABEL AND ENTRY FIELDS====================================================================


        self.LabelTitle = Label(self.master,text = " BILLING ",font = ('arial',30,'bold'),bg = 'powder blue',pady = 10)
        self.LabelTitle.pack(fill = X)
        self.frame2 = LabelFrame(self.master,text = 'CUSTOMER DETAILS',bg = 'powder blue',font = ('arial',15,'bold'))
        self.frame2.place(x = 0, y= 80, relwidth = 1)

        self.framepr = LabelFrame(self.master,text = 'BILL',bg = 'powder blue',font = ('arial',15,'bold'))
        self.framepr.place(x = 5, y= 170,width = 820,height = 500)

        self.framere = LabelFrame(self.master,text = 'BILL DETAILS',bg = 'powder blue',font = ('arial',15,'bold'))
        self.framere.place(x = 850,y = 170,height = 250, width = 460)

        self.pdtlbl = Label(self.framere,text = " PRODUCT ID ",font = ('arial',15,'bold'),bg = 'powder blue')
        self.pdtlbl.grid(row = 0,column = 0,pady = 5,padx = 5)
        self.pdttxt = Entry(self.framere,textvariable = self.Product_id,font = ('arial',10,'bold'),bd = 5,relief = 'ridge')
        self.pdttxt.grid(row = 0,column = 1,pady = 5,padx = 5)

        self.pdtqlbl = Label(self.framere,text = " PRODUCT QTY ",font = ('arial',15,'bold'),bg = 'powder blue')
        self.pdtqlbl.grid(row = 5,column = 0,pady = 5,padx = 5)
        self.pdtqtxt = Entry(self.framere,textvariable = self.Product_qt,font = ('arial',10,'bold'),bd = 5,relief = 'ridge')
        self.pdtqtxt.grid(row = 5,column = 1,pady = 5,padx = 5)

        self.custmerlbl = Label(self.frame2,text = " CUSTOMER NAME ",font = ('arial',10,'bold'),bg = 'powder blue')
        self.custmerlbl.grid(row = 0,column = 0,pady = 5)
        self.custmertxt = Entry(self.frame2,textvariable = self.name,font = ('arial',10,'bold'),bd = 5,relief = 'ridge')
        self.custmertxt.grid(row = 0,column = 1,pady = 5)

        self.custmerphlbl = Label(self.frame2,text = " CUSTOMER PHONE ",font = ('arial',10,'bold'),bg = 'powder blue')
        self.custmerphlbl.grid(row = 0,column = 2,pady = 5)
        self.custmerphtxt = Entry(self.frame2,textvariable = self.phone,font = ('arial',10,'bold'),bd = 5,relief = 'ridge')
        self.custmerphtxt.grid(row = 0,column = 3,pady = 5)

        self.dctlbl = Label(self.frame2,text = " DOCTOR NAME ",font = ('arial',10,'bold'),bg = 'powder blue')
        self.dctlbl.grid(row = 0,column = 4,pady = 5)
        self.dcttxt = Entry(self.frame2,textvariable = self.doc,font = ('arial',10,'bold'),bd = 5,relief = 'ridge')
        self.dcttxt.grid(row = 0,column = 5,pady = 5)

        self.dctaddlbl = Label(self.frame2,text = " DOCTOR ADDRESS ",font = ('arial',10,'bold'),bg = 'powder blue')
        self.dctaddlbl.grid(row = 0,column = 6,pady = 5)
        self.dctaddtxt = Entry(self.frame2,textvariable = self.docadd,font = ('arial',10,'bold'),bd = 5,relief = 'ridge')
        self.dctaddtxt.grid(row = 0,column = 7,pady = 5)



#====================================BILL WINDOW BUTTONS====================================================================



        self.btnADD = Button(self.framere,text = "ADD",width = 7,font = ('arial',10,'bold'),command = self.addbtn2)
        self.btnADD.grid(row = 7,column = 2)
        
        self.btnDEL = Button(self.framere,text = "REMOVE",width = 7,font = ('arial',10,'bold'),command = self.remove_item)
        self.btnDEL.grid(row = 10,column = 2)


#====================================TREEVIEW AND BILL DISPLAY====================================================================


        self.billsTV = ttk.Treeview(self.framepr,height=21, columns=('Rate','Quantity','Cost'))
        
        self.billsTV.grid(row=5, column=0, columnspan=5,padx = 5)

        self.scrollBar = Scrollbar(self.framepr, orient="vertical")
        self.scrollBar.grid(row=5, column=4, sticky="NSE")

        self.billsTV.configure(yscrollcommand=self.scrollBar.set)

        self.billsTV.heading('#0',text="PRODUCT NAME")
        self.billsTV.heading('#1',text="PRICE")
        self.billsTV.heading('#2',text="QUANTITY")
        self.billsTV.heading('#3',text="COST")


#====================================BILL WINDOW FUNCTIONS====================================================================


    def printbill(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window4(self.newWindow)


    def addbtn2(self):
        if self.Product_qt.get() == 0:
            tkinter.messagebox.showerror(" BILL WINDOW ","You haven't entered the quantity")
        else:
            qty = self.Product_qt.get()
            ide = self.Product_id.get()
            query = "SELECT Product_name,Product_price FROM STOCK WHERE Product_id = '{}'".format(ide)
            try:
                conn = pymysql.connect(host = "localhost",user = "root",passwd = "deepak@123",database = "pharmacy")
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(query)
                        value = cur.fetchone()
                self.billsTV.insert("", 'end',text = value[0] , values =( value[1],qty, value[1]*qty))
                self.Product_id.set("")
                self.Product_qt.set("")
                self.pdttxt.focus()

            except Exception as e:
                tkinter.messagebox.showerror(" NEW PRODUCT ADDITION ",e)
            

            

    def remove_item(self):
        selected_items = self.billsTV.selection()        
        for selected_item in selected_items:
            self.billsTV.delete(selected_item)



#====================================STOCK WINDOW====================================================================



class Window5:
    def __init__(self,master):
        self.master = master
        self.master.title("STOCK")
        self.master.geometry('1350x750+0+0')
        self.master.config(bg = 'powder blue')



#====================================LABELS OF STOCK WINDOW====================================================================



        self.LabelTitle = Label(self.master,text = " STOCK ",font = ('arial',30,'bold'),bg = 'powder blue',pady = 10)
        self.LabelTitle.pack(fill = X)

        self.framepr = LabelFrame(self.master,text = 'Stock Details',bg = 'powder blue',font = ('arial',15,'bold'))
        self.framepr.place(x = 290, y= 100,width = 820,height = 500)

        self.stockTV = ttk.Treeview(self.framepr,height=20, columns=('Rate','Quantity','Cost'))
        
        self.stockTV.grid(row=5, column=0, columnspan=5,padx = 5)

        self.scrollBar = Scrollbar(self.framepr, orient="vertical")
        self.scrollBar.grid(row=5, column=4, sticky="NSE")

        self.stockTV.configure(yscrollcommand=self.scrollBar.set)

        self.stockTV.heading('#0',text="PRODUCT ID")
        self.stockTV.heading('#1',text="PRODUCT NAME")
        self.stockTV.heading('#2',text="QUANTITY")
        self.stockTV.heading('#3',text="PRICE")
    

        self.btncheck = Button(self.framepr,text = "CHECK",width = 7,font = ('arial',10,'bold'),command = self.print_stock)
        self.btncheck.grid(row =10,column = 4 )


#====================================STOCK WINDOW CHECK BUTTON====================================================================

    
    def print_stock(self):
            query = "SELECT * FROM STOCK"
            try:
                conn = pymysql.connect(host="localhost",user="root", passwd="deepak@123",database="pharmacy")
                with conn:
                    with conn.cursor() as cur:
                        cur.execute(query)
                        rows = cur.fetchall()
                        for row in rows:
                            #print(row)
                            self.stockTV.insert("",'end',text = row[0],values = row[1:])
            except Exception as e:
                tkinter.messagebox.showerror(" STOCK ",e)
            






if __name__ == "__main__":
    main()