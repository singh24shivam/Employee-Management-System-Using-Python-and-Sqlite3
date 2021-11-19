from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import bs4
import operator

def f1():
	root.withdraw()
	add_emp.deiconify()

def f2():
	add_emp.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	view_emp.deiconify()
	view_emp_empdata.delete(1.0, END)
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "select * from employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data:
			info = info + "id = " + str(d[0]) + " name = " + str(d[1]) + " salary = " + str(d[2]) + "\n"
		view_emp_empdata.insert(INSERT, info)
	except Exception as e:
		showerror("issue ", e)
	finally:
		if con is not None:
			con.close()
		
def f4():
	view_emp.withdraw()
	root.deiconify()

def f5():
	root.withdraw()
	update_emp.deiconify()
	
def f6():
	update_emp.withdraw()
	root.deiconify()

def f7():
	root.withdraw()
	delete_emp.deiconify()

def f8():
	delete_emp.withdraw()
	root.deiconify()

def f9():
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "insert into employee values('%d', '%s', '%d')"
		id = int(add_emp_entid.get())
		name = add_emp_entname.get()
		salary = int(add_emp_entsalary.get())
		if id <= 0:
			showerror("Error", "id should not be 0 or negative")
			add_emp_entid.delete(0, END)
			add_emp_entid.focus()	
		elif len(name) == 0:
			showerror("Error", "Name Cannot be empty")
			add_emp_entname.delete(0, END)
			add_emp_entname.focus()			
		elif len(name) < 2:
			showerror("Error", "Name should contain more than 1 alphabets")
			add_emp_entname.delete(0, END)
			add_emp_entname.focus()
		elif not name.isalpha():
			showerror("Error", "Name should contain only alphabets")
			add_emp_entname.delete(0, END)
			add_emp_entname.focus()
		elif salary <= 0:
			showerror("Error", "Salary should not be 0 or negative")
			add_emp_entsalary.delete(0, END)
			add_emp_entsalary.focus()			
		elif salary < 8000:
			showerror("Error", "Salary must be greater than or equal to 8000")
			add_emp_entsalary.delete(0, END)
			add_emp_entsalary.focus()			
		else:
			cursor.execute(sql % (id, name, salary))
			con.commit()
			showinfo("success", "record added")
			add_emp_entid.delete(0, END)
			add_emp_entid.focus()
			add_emp_entname.delete(0, END)
			add_emp_entname.focus()
			add_emp_entsalary.delete(0, END)
			add_emp_entsalary.focus()
	except ValueError as e:
		showerror("Error", "Enter Valid Id Or Valid Salary")
	except NameError as e:
		showerror("Error", "Enter Valid Name")
		add_emp_entname.delete(0, END)
		add_emp_entname.focus()
	except IntegrityError as e:
		showerror("Error", "Id Already Exists")
	except Exception as e:
		showerror("Issue", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f10():
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "update employee set name = '%s', salary = '%d' where id = '%d'"
		id = int(update_emp_entid.get())
		name = update_emp_entname.get()
		salary = int(update_emp_entsalary.get())
		if id <= 0:
			showerror("Error", "id should not be 0 or negative")
			update_emp_entid.delete(0, END)
			update_emp_entid.focus()
		elif len(name) == 0:
			showerror("Error", "Name Cannot be empty")
			update_emp_entname.delete(0, END)
			update_emp_entname.focus()
		elif len(name) < 2:
			showerror("Error", "Name should contain more than 1 alphabets")
			update_emp_entname.delete(0, END)
			update_emp_entname.focus()
		elif not name.isalpha():
			showerror("Error", "Name should contain only alphabets")
			update_emp_entname.delete(0, END)
			update_emp_entname.focus()
		elif salary <= 0:
			showerror("Error", "Salary should not be 0 or negative")
			update_emp_entsalary.delete(0, END)
			update_emp_entsalary.focus()			
		elif salary < 8000:
			showerror("Error", "Salary must be greater than or equal to 8000")
			update_emp_entsalary.delete(0, END)
			update_emp_entsalary.focus()
		else:
			cursor.execute(sql % (name, salary, id))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("success ", str(id) + " updated")
				update_emp_entid.delete(0, END)
				update_emp_entid.focus()
				update_emp_entname.delete(0, END)
				update_emp_entname.focus()
				update_emp_entsalary.delete(0, END)
				update_emp_entsalary.focus()
			else:
				showwarning("Error", str(id) + " does not exists")
				update_emp_entid.delete(0, END)
				update_emp_entid.focus()
				update_emp_entname.delete(0, END)
				update_emp_entname.focus()
				update_emp_entsalary.delete(0, END)
				update_emp_entsalary.focus()
	except ValueError as e:
		showerror("Error", "Enter Valid Id Or Valid Salary")
	except NameError as e:
		showerror("Error", "Enter Valid Name")
		update_emp_entname.delete(0, END)
		update_emp_entname.focus()
	except Exception as e:
		showerror("Issue ", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f11():
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "delete from employee where id = '%d'"
		id = int(delete_emp_entid.get())
		if id <= 0:
			showerror("Error", "Id should not be 0 or negative")
			delete_emp_entid.delete(0, END)
			delete_emp_entid.focus()
		else:
			cursor.execute(sql % (id))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("success ", str(id) + " deleted")
				delete_emp_entid.delete(0, END)
				delete_emp_entid.focus()
			else:
				showwarning("Error", str(id) + " does not exists")
				delete_emp_entid.delete(0, END)
				delete_emp_entid.focus()
	except ValueError as e:
		showerror("Error", "Enter valid Id")
		delete_emp_entid.delete(0, END)
		delete_emp_entid.focus()
	except Exception as e:
		showerror("Issue ", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def f12():
	emp_dict = {}
	con = None
	try:
		con = connect("employee.db")
		cursor = con.cursor()
		sql = "select * from employee"
		cursor.execute(sql)
		data = cursor.fetchall()
		data = list(data)
#		print(data)
		for index in range(len(data)):
			emp_dict[data[index][1]] = data[index][2]
#			print(emp_dict)
			asc = dict(sorted(emp_dict.items(), key=operator.itemgetter(1)))
			dsc = dict(sorted(emp_dict.items(), key=operator.itemgetter(1), reverse=True))
#			print(dsc)
			dict_items = dsc.items()
			first_five = list(dict_items)[:5]
			result = dict(first_five)
#			print(first_five)
			x = list(result.keys())
			y = list(result.values())
			c = ["red", "blue", "green", "orange", "purple"]
		plt.bar(x, y, color=c)
		plt.title("Chart of top5 highest earning salaried employees")
		plt.xlabel("emp_name")
		plt.ylabel("emp_salary")
		plt.show()
	except Exception as e:
		showerror("issue ", e)
	finally:
		if con is not None:
			con.close()	
	
root = Tk()
root.title("E.M.S")
root.geometry("430x430+500+200")

try:
	web_address = "https://www.brainyquote.com/quote_of_the_day"
	try:
		res = requests.get(web_address)
	except requests.exceptions.ConnectionError:
		r.status_code = "Connection refused"

	data = bs4.BeautifulSoup(res.text, "html.parser")
	#print(data)

	info = data.find("img", {"class":"p-qotd"})
	#print(info)

	quote = info['alt']
	#print(quote)

	T = Text(root, height=6, width=58, font=('arial', 10, 'bold'))
	T.place(x=5, y=310)

	T.insert(END, quote)
	T.configure(state='disabled')
except Exception as e:
	showerror("isuue ", e)

btn_Add = Button(root, text="Add", width=10, font=('arial', 15, 'bold'), command=f1)
btn_View = Button(root, text="View", width=10, font=('arial', 15, 'bold'), command=f3)
btn_Update = Button(root, text="Update", width=10, font=('arial', 15, 'bold'), command=f5)
btn_Delete = Button(root, text="Delete", width=10, font=('arial', 15, 'bold'), command=f7)
btn_Charts = Button(root, text="Charts", width=10, font=('arial', 15, 'bold'), command=f12)
lbl_QOTD = Label(root, text="QOTD:", font=('arial', 18, 'bold'))

btn_Add.pack(pady=5)
btn_View.pack(pady=5)
btn_Update.pack(pady=5)
btn_Delete.pack(pady=5)
btn_Charts.pack(pady=5)
lbl_QOTD.place(x=10, y=270)

add_emp = Toplevel(root)
add_emp.title("Add Emp")
add_emp.geometry("430x430+500+200")


add_emp_id = Label(add_emp, text="enter id", font=('arial', 15, 'bold'))
add_emp_entid = Entry(add_emp, bd=5, font=('arial', 15, 'bold'))
add_emp_entid.focus()
add_emp_name = Label(add_emp, text="enter name", font=('arial', 15, 'bold'))
add_emp_entname = Entry(add_emp, bd=5, font=('arial', 15, 'bold'))
add_emp_salary = Label(add_emp, text="enter salary", font=('arial', 15, 'bold'))
add_emp_entsalary = Entry(add_emp, bd=5, font=('arial', 15, 'bold'))
add_emp_btnSave = Button(add_emp, text="Save", width=10, font=('arial', 15, 'bold'), command=f9)
add_emp_btnBack = Button(add_emp, text="Back", width=10, font=('arial', 15, 'bold'), command=f2)

add_emp_id.pack(pady=5)
add_emp_entid.pack(pady=5)
add_emp_name.pack(pady=5)
add_emp_entname.pack(pady=5)
add_emp_salary.pack(pady=5)
add_emp_entsalary.pack(pady=5)
add_emp_btnSave.pack(pady=5)
add_emp_btnBack.pack(pady=5)

add_emp.withdraw()

view_emp = Toplevel(root)
view_emp.title("View Emp")
view_emp.geometry("430x430+500+200")

view_emp_empdata = ScrolledText(view_emp, width=35, height=15, font=('arial', 15, 'bold'))
view_emp_btnBack = Button(view_emp, text="Back", width=10, font=('arial', 15, 'bold'), command=f4)

view_emp_empdata.pack(pady=5)
view_emp_btnBack.pack(pady=5)

view_emp.withdraw()

update_emp = Toplevel(root)
update_emp.title("Update Emp")
update_emp.geometry("430x430+500+200")

update_emp_id = Label(update_emp, text="enter id", font=('arial', 15, 'bold'))
update_emp_entid = Entry(update_emp, bd=5, font=('arial', 15, 'bold'))
update_emp_entid.focus()
update_emp_name = Label(update_emp, text="enter name", font=('arial', 15, 'bold'))
update_emp_entname = Entry(update_emp, bd=5, font=('arial', 15, 'bold'))
update_emp_salary = Label(update_emp, text="enter salary", font=('arial', 15, 'bold'))
update_emp_entsalary = Entry(update_emp, bd=5, font=('arial', 15, 'bold'))
update_emp_btnSave = Button(update_emp, text="Save", width=10, font=('arial', 15, 'bold'), command=f10)
update_emp_btnBack = Button(update_emp, text="Back", width=10, font=('arial', 15, 'bold'), command=f6)

update_emp_id.pack(pady=5)
update_emp_entid.pack(pady=5)
update_emp_name.pack(pady=5)
update_emp_entname.pack(pady=5)
update_emp_salary.pack(pady=5)
update_emp_entsalary.pack(pady=5)
update_emp_btnSave.pack(pady=5)
update_emp_btnBack.pack(pady=5)

update_emp.withdraw()

delete_emp = Toplevel(root)
delete_emp.title("Delete Emp")
delete_emp.geometry("430x430+500+200")

delete_emp_id = Label(delete_emp, text="enter id", font=('arial', 15, 'bold'))
delete_emp_entid = Entry(delete_emp, bd=5, font=('arial', 15, 'bold'))
delete_emp_entid.focus()
delete_emp_btnSave = Button(delete_emp, text="Save", width=10, font=('arial', 15, 'bold'), command=f11)
delete_emp_btnBack = Button(delete_emp, text="Back", width=10, font=('arial', 15, 'bold'), command=f8)

delete_emp_id.pack(pady=5)
delete_emp_entid.pack(pady=5)
delete_emp_btnSave.pack(pady=5)
delete_emp_btnBack.pack(pady=5)

delete_emp.withdraw()

root.mainloop()

