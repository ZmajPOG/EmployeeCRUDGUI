from tkinter import *
from tkinter import messagebox
import mysql.connector

def insertData():
    empID=enterId.get()
    empName=enterName.get()
    empDept=enterDept.get()

    if(empID == "" or empName == "" or empDept == ""):
        messagebox.showwarning("Cannot Insert", "All the fields are required!")
        return
    
    try:
        myDB = mysql.connector.connect(host='localhost', user="root", database='employee')
        myCur= myDB.cursor()

        query = "INSERT INTO empDetails (empID, empName, empDept) VALUES (%s, %s, %s)"
        values = (empID, empName, empDept)
        myCur.execute(query, values)
        myDB.commit()

        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()

        messagebox.showinfo("insert Status", "Data Inserted Successfully")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if myCur:
            myCur.close()
        if myDB:
            myDB.close()

def updateData():
    empID=enterId.get()
    empName=enterName.get()
    empDept=enterDept.get()

    if(empID == "" or empName == "" or empDept == ""):
        messagebox.showwarning("Cannot Update", "All the fields are required!")
        return
    
    try:
        myDB = mysql.connector.connect(host='localhost', user="root", database='employee')
        myCur= myDB.cursor()

        query = "UPDATE empDetails SET empName = %s, empDept = %s Where empID = %s"
        values = (empName, empDept, empID)
        myCur.execute(query, values)
        myDB.commit()

        enterId.delete(0,"end")
        enterName.delete(0,"end")
        enterDept.delete(0,"end")

        show()

        messagebox.showinfo("Update Status", "Data Updated Successfully")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if myCur:
            myCur.close()
        if myDB:
            myDB.close()

def getData():
    if enterId.get() == "":
        messagebox.showwarning("Fetch Status", "Please provide the Employee ID to fetch the data")
        return

    try:
        myDB = mysql.connector.connect(host='localhost', user="root", database='employee')
        myCur = myDB.cursor()
        
        query = "SELECT * FROM empDetails WHERE empID = %s"
        myCur.execute(query, (enterId.get(),))
        row = myCur.fetchone()

        if row:
            enterName.delete(0, "end")
            enterDept.delete(0, "end")
            
            enterName.insert(0, row[1])
            enterDept.insert(0, row[2])
        else:
            messagebox.showinfo("Fetch Status", "No employee found with the given ID")
    
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if myCur:
            myCur.close()
        if myDB:
            myDB.close()

def deleteData():
    if enterId.get() == "":
        messagebox.showwarning("Cannot Delete", "Please provide the Employee ID to delete the data")
        return

    try:
        myDB = mysql.connector.connect(host='localhost', user="root", database='employee')
        myCur = myDB.cursor()

        query = "DELETE FROM empDetails WHERE empID = %s"
        values = (enterId.get(),)
        myCur.execute(query, values)
        myDB.commit()

        if myCur.rowcount == 0:
            messagebox.showinfo("Delete Status", "No employee found with the given ID")
        else:
            enterId.delete(0, "end")
            enterName.delete(0, "end")
            enterDept.delete(0, "end")

            show()

            messagebox.showinfo("Delete Status", "Data Deleted Successfully")

    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")

    finally:
        if myCur:
            myCur.close()
        if myDB:
            myDB.close()

def resetFields():
    enterId.delete(0, "end")
    enterName.delete(0, "end")
    enterDept.delete(0, "end")

def show():
    try:
        myDB = mysql.connector.connect(host='localhost', user="root", database='employee')
        myCur = myDB.cursor()
        
        myCur.execute("select * from empDetails")
        rows = myCur.fetchall()
        showData.delete(0, showData.size())

        for row in rows:
            addData = str(row[0]) + ' ' + row[1] + ' ' + row[2]
            showData.insert(showData.size() + 1, addData)
    
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error: {err}")
    
    finally:
        if myCur:
            myCur.close()
        if myDB:
            myDB.close()




window = Tk()
window.geometry("500x270")
window.title("Employee CRUD App")

empId = Label(window, text='Employee ID', font=('Serif', 12))
empId.place(x=20, y=30)

empName = Label(window, text='Employee Name', font=('Serif', 12))
empName.place(x=20, y=60)

empDept = Label(window, text='Employee Dept', font=('Serif', 12))
empDept.place(x=20, y=90)


enterId = Entry(window)
enterId.place(x=170, y=30)

enterName = Entry(window)
enterName.place(x=170, y=60)

enterDept = Entry(window)
enterDept.place(x=170, y=90)

insertBtn=Button(window, text='Insert', font=("sans", 12), bg='White', command=insertData) 
insertBtn.place(x=20, y=160)
updateBtn=Button(window, text='Update', font=("sans", 12), bg='White', command=updateData)
updateBtn.place(x=80, y=160)
getBtn=Button(window, text='Fetch', font=("sans", 12), bg='White', command=getData)
getBtn.place(x=150, y=160)
deleteBtn=Button(window, text='Delete', font=("sans", 12), bg='White', command=deleteData)
deleteBtn.place(x=210, y=160)
resetBtn=Button(window, text='Reset', font=("sans", 12), bg='White', command=resetFields)
resetBtn.place(x=20, y=210)

showData = Listbox(window)
showData.place(x=330, y=30)

show()


window.mainloop()

'''import mysql.connector

try:
    myDB = mysql.connector.connect(host='localhost', user='root', database='employee')
    print("Connection successful")
except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'myDB' in locals():
        myDB.close()'''



