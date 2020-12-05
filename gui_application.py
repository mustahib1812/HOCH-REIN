import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()

my_w.title("HOCH REIN GUI Application")

l0 = tk.Label(my_w,  text='Add Details',
            font=('Helvetica', 16), 
            width=30,anchor="c" )  
l0.grid(row=2,column=1,columnspan=4) 

#adding label
l1 = tk.Label(my_w,  text='Enter Details: ', width=12,
            anchor="c" )  
l1.grid(row=3,column=1) 

# add one text box
t1 = tk.Text(my_w,  height=1, width=35,bg='white') 
t1.grid(row=3,column=2) 

b1 = tk.Button(my_w,  text='Add Record', width=10, 
            command=lambda: add_data()) 
b1.grid(row=7,column=2) 

my_str = tk.StringVar()
l5 = tk.Label(my_w,  textvariable=my_str, width=10 )  
l5.grid(row=3,column=3) 
my_str.set("Output")


def add_data():
    flag_validation=True # set the flag 
    details =t1.get("1.0",END) # read details

    if(flag_validation):
        my_str.set("Adding data...")
        try:
            from sqlalchemy import create_engine
            from sqlalchemy.exc import SQLAlchemyError
            
            # Connection to database 
            engine = create_engine("mysql+mysqldb://root:insert_password@localhost/ASPF_schema")
            
            query="INSERT INTO  `test_details` (`details`) VALUES(%s)"
            my_data=(details)

            id=engine.execute(query,my_data) # query executed here
            
            t1.delete('1.0',END)  # reset the text entry box
            l5.grid() 
            l5.config(fg='green') # foreground color 
            l5.config(bg='white') # background color 
            my_str.set("ID:" + str(id.lastrowid))
            l5.after(3000, lambda: l5.grid_remove() )
                
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
            l5.grid() 
            #return error
            l5.config(fg='red')   # foreground color
            l5.config(bg='yellow') # background color
            print(error)
            my_str.set(error)
        
        
    else:
        l5.grid() 
        l5.config(fg='red')   # foreground color
        l5.config(bg='yellow') # background color
        my_str.set("check inputs.")
        l5.after(3000, lambda: l5.grid_remove() )

my_w.mainloop()