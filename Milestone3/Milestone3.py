# Import the required libraries
from datetime import date
import tkinter as tk
from tkinter import messagebox, ttk
from click import command
import mysql.connector as mc

mydb = mc.connect(
    host='sql.freedb.tech',
    user='freedb_Karim',
    password="&Tfy76R%XZBVTmB", 
    database='freedb_Wuzzuf'
)

cursor = mydb.cursor()

# Define a function for switching the frames
def change_to_signin():
    root['pady'] = 100 
    siginFrame()
    sigin.pack()
    register.pack_forget()
    
def change_to_signin2():
    root['pady'] = 100 
    siginFrame()
    sigin.pack()
    home.pack_forget()

def change_to_register():
    root['pady'] = 0
    registerFrame()
    register.pack()
    sigin.pack_forget()
    
def change_to_home(email):
    root['pady'] = 0
    homeFrame(email)
    home.pack()
    sigin.pack_forget()
   
def change_to_result(query, email):
    root['pady'] = 0
    resultFrame(query, email)
    result.pack()
    home.pack_forget()
       
def change_to_home2(email):
    root['pady'] = 0
    homeFrame(email)
    home.pack()
    result.pack_forget()
    

def siginFrame():
    def my_show():
        if(c_v1.get()==1):
            passEntry.config(show='')
        else:
            passEntry.config(show='*')
    
    def on_entry_focus_in(event):
            if userEntry.get() == userText:
                userEntry.delete(0, tk.END)
                userEntry.configure(show="")
                userEntry.configure(fg="black")
    
    def on_entry_focus_in1(event):
        if passEntry.get() == passText:
            passEntry.delete(0, tk.END)
            passEntry.configure(show="*")
            passEntry.configure(fg='black')

    def on_entry_focus_out(event):
        if userEntry.get() == "":
            userEntry.insert(0, userText)
            userEntry.configure(fg="black")
        
    def on_entry_focus_out1(event):
        if passEntry.get() == "":
            passEntry.insert(0, passText)
            passEntry.configure(show="")
            userEntry.configure(fg="black")
            
    def check_signin():
        sql = '''
        Select *
        From ApplicantPassword
        Where ApplicantEmail = %(email)s
        '''

        cursor.execute(sql, {'email': userEntry.get()})

        result = cursor.fetchone()
        
        # messagebox.showwarning('Warning', "Don't leave the email entry empty")
        #     return

        if result == None:
            messagebox.showwarning('Warning', "Email does not exist")
            return
        elif passEntry.get() != result[1]:
            messagebox.showwarning('Warning', "Password is incorrect")
            return
        else:
            change_to_home(result[0])
    
        
    # sigin.configure(width=350, height=400, bg='white', highlightbackground='gray', highlightthickness=1)
    # sigin.pack()
    sigin.pack_propagate(False)
    sigin.grid_propagate(False)

    headerLabel = tk.Label(master=sigin, text='Wuzzuf', font=('Segoe UI', 25), bg='white', fg='black',anchor='center')
    # headerLabel.pack(pady=20)
    headerLabel.grid(row=0, pady=20, columnspan=3) 


    #username
    userText = 'Email'
    userEntry = tk.Entry(sigin, fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', font=('Segoe UI', 18), width=29, insertbackground='black')
    userEntry.insert(0, userText)

    userEntry.bind('<FocusIn>', on_entry_focus_in)
    userEntry.bind('<FocusOut>', on_entry_focus_out)
    # userEntry.pack(pady=20)
    userEntry.grid(row=1,padx= 10, pady=10, columnspan=4)

    #password
    passText = 'Password'
    passEntry = tk.Entry(sigin, fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', font=('Segoe UI', 18), width=29,insertbackground='black')
    passEntry.insert(0, passText)

    passEntry.bind('<FocusIn>', on_entry_focus_in1)
    passEntry.bind('<FocusOut>', on_entry_focus_out1)
    # passEntry.pack(pady=20)
    passEntry.grid(row=2,padx= 10, pady=2, columnspan=4)
    
    c_v1=tk.IntVar(value=0)
    c1 = tk.Checkbutton(sigin,text='Show Password',variable=c_v1,
	onvalue=1,offvalue=0, bg='white', fg='black', command=my_show)
    c1.grid(row=3,column=1, pady=10) 

    #button 
    logBtn = tk.Button(sigin, text='Log in', width= 30, height=2, command=check_signin)
    # logBtn.pack(pady=20)
    logBtn.grid(row=4,padx= 10, pady= 5, columnspan=4)


    fsLabel = tk.Label(sigin, text='First Time?', font=('Segoe UI', 13), bg='white', fg='black')
    # fsLabel.pack(anchor='w', padx=10)
    fsLabel.grid(row=5, column=0, padx= 10, pady = 80, sticky="nsew")

    caBtn = tk.Button(sigin, text='Register', width=22, height=2, command=change_to_register)
    # caBtn.pack(anchor='e', padx=10)
    caBtn.grid(row=5, column=1,pady = 80, sticky="nsew")

def registerFrame():
    
    def my_show():
        if(c_v1.get()==1):
            passwordEntry.config(show='')
        else:
            passwordEntry.config(show='*')
    
    
    def check_register():
        if emailEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the email entry empty")
            return
        elif usernameEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the username entry empty")
            return
        elif passwordEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the password entry empty")
            return
        elif fnameEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the firstname entry empty")
            return
        elif lnameEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the lastname entry empty")
            return
        elif genderEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the gender entry empty")
            return
        elif birthEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the birtdate(yyyy-mm-dd) entry empty")
            return
        elif phoneEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the phone number entry empty")
            return
        elif nationalEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the nationality entry empty")
            return
        elif gpaEntry.get() == '':
            messagebox.showwarning('Warning', "Don't leave the GPA entry empty")
            return
        else:
            
            eduLevel = None if eduEntry.get() == '' else eduEntry.get()
            carLevel = None if carEntry.get() == '' else carEntry.get()
            
            #mysql_connector
            # Insert into ApplicantPassword Values('ks@example.com', 'Madpro2002');
            sql = "INSERT INTO ApplicantPassword (ApplicantEmail, Password) VALUES (%s, %s)"
            val = (emailEntry.get(), passwordEntry.get())
            cursor.execute(sql, val)
            mydb.commit()
            print(cursor.rowcount, "record inserted.")
            
            sql = '''
            INSERT INTO Applicant (EmailAddress, Username, Fname, Lname, Gender, Birthdate, PhoneNo, Nationality, GPA, EducationLevel, CareerLevel)
            VALUES
            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''
            val = (emailEntry.get(), usernameEntry.get(), fnameEntry.get(), lnameEntry.get(), genderEntry.get(), birthEntry.get(), phoneEntry.get(), nationalEntry.get(), gpaEntry.get(), eduLevel, carLevel)
            cursor.execute(sql, val)

            mydb.commit()
                        
            change_to_signin()

    register.configure(width=1000, height=1000, bg='white', highlightbackground='gray', highlightthickness=1)
    register.pack_propagate(False)
    register.grid_propagate(False)
    
    rgLabel = tk.Label(register, text="Registeration:", font= ('SegoeUI 30 underline'),anchor='w',bg='white', fg='black')
    rgLabel.grid(row=0, pady=5)
    
    # email
    emailLabel = tk.Label(register, text="Email Address:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    emailLabel.grid(row=1, column=0)
    
    emailEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    emailEntry.grid(row=1, column=1, columnspan=2, pady=10)

    
    # username
    usernameLabel = tk.Label(register, text="Username:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black', )
    usernameLabel.grid(row=2, column=0)
    
    usernameEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    usernameEntry.grid(row=2, column=1, columnspan=2, pady=10)
    
    # password
    passwordLabel = tk.Label(register, text="Password:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    passwordLabel.grid(row=3, column=0)
    
    passwordEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=3, bg='#FAFAFA', show='*', width=20, insertbackground='black')
    
    passwordEntry.grid(row=3, column=1, columnspan=2, pady=10)
    
    c_v1=tk.IntVar(value=0)
    c1 = tk.Checkbutton(register,text='Show Password',variable=c_v1,
	onvalue=1,offvalue=0, bg='white', fg='black', command=my_show)
    c1.grid(row=3,column=4) 
    
    # fname
    fnameLabel = tk.Label(register, text="First Name:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    fnameLabel.grid(row=4, column=0)
    
    fnameEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    fnameEntry.grid(row=4, column=1, columnspan=2, pady=10)
    
    # lname
    lnameLabel = tk.Label(register, text="Last Name:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    lnameLabel.grid(row=5, column=0)
    
    lnameEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    lnameEntry.grid(row=5, column=1, columnspan=2, pady=10)
    
    # gender
    genderLabel = tk.Label(register, text="Gender(M/F):", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    genderLabel.grid(row=6, column=0)
    
    genderEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    genderEntry.grid(row=6, column=1, columnspan=2, pady=10)
    
    # Birthdate
    birthLabel = tk.Label(register, text="Birtdate(yyyy-mm-dd):", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    birthLabel.grid(row=7, column=0)
    
    birthEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    birthEntry.grid(row=7, column=1, columnspan=2, pady=10)
    
    # PhoneNo
    phoneLabel = tk.Label(register, text="Phone Number:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    phoneLabel.grid(row=8, column=0)
    
    phoneEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    phoneEntry.grid(row=8, column=1, columnspan=2, pady=10)
    
    # Nationality
    nationalLabel = tk.Label(register, text="Nationality:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    nationalLabel.grid(row=9, column=0)
    
    nationalEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    nationalEntry.grid(row=9, column=1, columnspan=2, pady=10)
    
    # GPA
    gpaLabel = tk.Label(register, text="GPA:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    gpaLabel.grid(row=10, column=0)
    
    gpaEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
    gpaEntry.grid(row=10, column=1, columnspan=2, pady=10)
    
    # EducationLevel
    eduLabel = tk.Label(register, text="Education Level:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    eduLabel.grid(row=11, column=0)
    
    # eduEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20)
    # eduEntry.grid(row=11, column=1, columnspan=2, pady=10)
    # style = ttk.Style()
    # style.map('TCombobox', selectbackground=[('readonly', '#FAFAFA')])
    # style.map('TCombobox', fieldbackground=[('readonly','white')])
    # style.map('TCombobox', selectforeground=[('readonly', 'black')])
    
    eduEntry = ttk.Combobox(
        master=register,
        font=('SegoeUI 18'),
        foreground='white',
        width=18,
        state="readonly",
        values=["Bachelor Degree", "Master Degree", "PhD Degree"]
    )
    eduEntry.grid(row=11, column=1, columnspan=2, pady=10)
    
    # CareerLevel
    carLabel = tk.Label(register, text="Career Level:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
    carLabel.grid(row=12, column=0)
    
    # carEntry = tk.Entry(register, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20)
    # carEntry.grid(row=12, column=1, columnspan=2, pady=10)
    
    carEntry = ttk.Combobox(
        master=register,
        font=('SegoeUI 18'),
        foreground='white',
        width=18,
        state="readonly",
        values=["Entry Level", "Junior Level", "Senior Level"]
    )
    carEntry.grid(row=12, column=1, columnspan=2, pady=10)
    
    # create button
    createBtn = tk.Button(register, text='Create Account', width=20, height=2,command=check_register)
    createBtn.grid(row=13, column=1, columnspan=2, pady=20)
    
    # return button
    returnBtn = tk.Button(register, text='Return Page', width=20, height=2, command=change_to_signin)
    returnBtn.grid(row=13, column=5, columnspan=2, padx=20)

def homeFrame(email):
    
    home.configure(width=1000, height=1000, bg='white', highlightbackground='gray', highlightthickness=1)
    home.pack_propagate(False)
    home.grid_propagate(False)
    
    sql = '''
    Select Fname, Lname
    From Applicant
    Where EmailAddress = %(email)s
    '''

    cursor.execute(sql, {'email': email})

    result = cursor.fetchone()
    
    # rgLabel = tk.Label(register, text="Registeration:", font= ('SegoeUI 30 underline'),anchor='w',bg='white', fg='black')
    # rgLabel.grid(row=0, pady=5)
    
    homeHeader = tk.Label(master=home, text=f"Welcome, {result[0]} {result[1]}:", font=('SegoeUI 30 underline'), anchor='w', bg='white', fg='black')
    homeHeader.grid(row=0, column=0, pady=20, sticky='w')
    

    # apply for job
    applyLabel = tk.Label(home, text="Apply for a Job:", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    applyLabel.grid(row=1, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    applyBtn = tk.Button(home, text="Apply",font=('SegoeUI 20'), command=lambda: change_to_result(applyLabel.cget("text"), email))
    applyBtn.grid(row=1, column=3, columnspan=3)
    
    # Show all the job postings for a given sector
    show1Label = tk.Label(home, text="All Job Postings for a given Sector:", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    show1Label.grid(row=2, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    show1Btn = tk.Button(home, text="Show",font=('SegoeUI 20'), command=lambda: change_to_result(show1Label.cget("text"), email))
    show1Btn.grid(row=2, column=3, columnspan=3)
    
    # Show all the job postings for a given set of skills
    show2Label = tk.Label(home, text="All Job Postings for a given Set of Skills:", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    show2Label.grid(row=3, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    show2Btn = tk.Button(home, text="Show",font=('SegoeUI 20'), command=lambda: change_to_result(show2Label.cget('text'), email))
    show2Btn.grid(row=3, column=3, columnspan=3, padx=100)
    
    # Show the top 5 sectors by number of job posts, and the average salary range for each
    show3Label = tk.Label(home, text="Show the Top 5 Sectors:", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    show3Label.grid(row=4, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    show3Btn = tk.Button(home, text="Show",font=('SegoeUI 20'), command=lambda: change_to_result(show3Label.cget('text'), email))
    show3Btn.grid(row=4, column=3, columnspan=3)
    
    # Show the top 5 skills that are in the highest demand
    show4Label = tk.Label(home, text="Show the Top 5 Skills:", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    show4Label.grid(row=5, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    show4Btn = tk.Button(home, text="Show",font=('SegoeUI 20'), command=lambda: change_to_result(show4Label.cget('text'), email))
    show4Btn.grid(row=5, column=3, columnspan=3)
    
    # Show the top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date
    show5Label = tk.Label(home, text="Show the Top 5 Growing Startups:", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    show5Label.grid(row=6, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    show5Btn = tk.Button(home, text="Show",font=('SegoeUI 20'), command=lambda: change_to_result(show5Label.cget('text'), email))
    show5Btn.grid(row=6, column=3, columnspan=3)
    
    # Show the top 5 most paying companies in the field in Egypt
    show6Label = tk.Label(home, text="Show the Top 5 Most Paying Companies:", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    show6Label.grid(row=7, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    show6Btn = tk.Button(home, text="Show",font=('SegoeUI 20'), command=lambda: change_to_result(show6Label.cget('text'), email))
    show6Btn.grid(row=7, column=3, columnspan=3)
    
    # Show all the postings for a given company / organization
    show7Label = tk.Label(home, text="Show the posts for a given Company:", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    show7Label.grid(row=8, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    show7Btn = tk.Button(home, text="Show",font=('SegoeUI 20'), command=lambda: change_to_result(show7Label.cget('text'), email))
    show7Btn.grid(row=8, column=3, columnspan=3)
    
    # Show the top 5 categories (other than IT/Software Development) that the postings are cross listed under based on the volume of postings
    show8Label = tk.Label(home, text="Show the Top 5 Categories (other than IT/Software Development):", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
    show8Label.grid(row=9, column=0, columnspan=3, padx= 10, pady=15, sticky='w')
    
    show8Btn = tk.Button(home, text="Show",font=('SegoeUI 20'), command=lambda: change_to_result(show8Label.cget('text'), email))
    show8Btn.grid(row=9, column=3, columnspan=3)
    
    # logout button
    logoutBtn = tk.Button(home, text="Logout",font=('SegoeUI 20'), command=change_to_signin2)
    logoutBtn.grid(row=10, column=3, columnspan=3)
    
    
def resultFrame(query, email):
    for widget in result.winfo_children():
        widget.destroy()
    
    result.configure(width=1000, height=1000, bg='white', highlightbackground='gray', highlightthickness=1, pady= 10)
    result.pack_propagate(False)
    result.grid_propagate(False)
    
    resultHeader = tk.Label(master=result, text=f"{query}", font=('SegoeUI 25 underline'), anchor='w', bg='white', fg='black')
    resultHeader.grid(row=0, column=0, pady=20)
    
    
    if query == 'Apply for a Job:':
        def check_rseult():
            if input2E.get() == '':
                messagebox.showwarning('Warning', "Don't leave the Company entry empty")
                return
            elif input3E.get() == '':
                messagebox.showwarning('Warning', "Don't leave the JobTitle entry empty")
                return
            elif input4E.get() == '':
                messagebox.showwarning('Warning', "Don't leave the Textual Cover letter entry empty")
                return
            else:
                sql = f'''
                SELECT DatePosted 
                FROM JobPost 
                Where CompanyName = "{input2E.get()}" AND JobTitle = "{input3E.get()}"
                '''
                cursor.execute(sql)
                
                r = cursor.fetchall()
                
                datePosted = str(r[0][0])
                
                #mysql_connector
                sql = "INSERT INTO AppliesFor (ApplicantEmail, CompanyName, JobTitle, DatePosted, ApplicationDate, TextualCoverLetter) VALUES (%s, %s, %s, %s, %s, %s)"
                val = (input1E.get(), input2E.get(), input3E.get(), datePosted, date.today(), input4E.get())
                cursor.execute(sql, val)
                mydb.commit()
                print(cursor.rowcount, "record inserted.")
            
                change_to_home2(email)
        
        rgLabel = tk.Label(result, text="Apply For a Job:", font= ('SegoeUI 30 underline'),anchor='w',bg='white', fg='black')
        rgLabel.grid(row=0, pady=5)
        
        # email
        input1L = tk.Label(result, text="Email Address:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black')
        input1L.grid(row=1, column=0)
        
        input1E = tk.Entry(result, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
        input1E.insert(0, email)
        # input1E.config(state='disabled')
        input1E.grid(row=1, column=1, columnspan=2, pady=10)

        # company
        input2L = tk.Label(result, text="CompanyName:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black', )
        input2L.grid(row=2, column=0)
        
        input2E = tk.Entry(result, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
        input2E.grid(row=2, column=1, columnspan=2, pady=10)
        
        # jobtitle
        input3L = tk.Label(result, text="Jobtitle:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black', )
        input3L.grid(row=3, column=0)
        
        input3E = tk.Entry(result, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
        input3E.grid(row=3, column=1, columnspan=2, pady=10)
        
        # textual letter
        input4L = tk.Label(result, text="TextualCover:", font=('SegoeUI 18'), anchor='w', justify='left', bg='white', fg='black', )
        input4L.grid(row=4, column=0)
        
        input4E = tk.Entry(result, font=('SegoeUI 18'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', width=20, insertbackground='black')
        input4E.grid(row=4, column=1, columnspan=2, pady=10)
        
        # Create button
        applyBtn = tk.Button(result, text="Apply",font=('SegoeUI 20'), command=check_rseult)
        applyBtn.grid(row=5, column=1, columnspan=2)
    
    # Show all the job postings for a given sector
    elif query == 'All Job Postings for a given Sector:':
        def showResult():
            sol = set()
            sql = f'''
                SELECT jp.CompanyName, jp.JobTitle, jp.DatePosted, JobType, City, CareerLevel
                FROM JobPost jp
                JOIN JobPostCategory jps ON jp.CompanyName = jps.CompanyName AND jp.JobTitle = jps.JobTitle AND jp.DatePosted = jps.DatePosted
                WHERE CategoryName = "{inputEntry.get()}"
            '''
            cursor.execute(sql)
            r = cursor.fetchall()
            for i in r:
                    sol.add(i)
        
            sol = list(sol)
            sol.sort(key=lambda x: x[0])
            
            solBox = tk.Listbox(result, font=('SegoeUi 18'), bg='white', fg='black', width=88, height=20)
            i = 0
            for i in range(0, len(sol), 1):
                r = ', '.join(str(item) for item in sol[i])
                solBox.insert(i, r)
            
            solBox.grid(row=2, column=0, columnspan=4, padx=20, pady=20)
            
            # go back btn
            goBackBtn = tk.Button(result, text='Go Back to Home', font=('SegoeUI 18'), command=lambda: change_to_home2(email))
            goBackBtn.grid(row=3, column=0)
            
                    
            
        
        inputLabel = tk.Label(result, text="Sector:", font=('SegoeUI 20'), anchor='w', bg='white', fg='black')
        inputLabel.grid(row=1, column=0)
        
        inputEntry = tk.Entry(result, font=('SegoeUI 20'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', justify='left', insertbackground='black')
        inputEntry.grid(row=1, column=1, columnspan=2, pady=20)
        
        inputBtn = tk.Button(result, font=('SegoeUI 20'), text='Enter', command=showResult)
        inputBtn.grid(row=1, column=3, padx=10)
    # Show all the job postings for a given set of skills
    elif query == "All Job Postings for a given Set of Skills:":
        def showResult():
            
            skills = tuple(inputEntry.get().split(','))
            sol = set()
    
            sql = f"""
            SELECT jp.CompanyName, jp.JobTitle, jp.DatePosted, JobType, City, CareerLevel
            FROM JobPost jp
            JOIN JobPostSkills jps ON jp.CompanyName = jps.CompanyName AND jp.JobTitle = jps.JobTitle AND jp.DatePosted = jps.DatePosted
            WHERE jps.SkillName IN {skills}
            GROUP BY 1, 2, 3, 4, 5, 6
            HAVING COUNT(DISTINCT jps.SkillName) = {len(skills)}
            """
            
            cursor.execute(sql)
            r = cursor.fetchall()
            for i in r:
                sol.add(i)
        
            sol = list(sol)
            sol.sort(key=lambda x: x[0])
            
            solBox = tk.Listbox(result, font=('SegoeUi 18'), bg='white', fg='black', width=88, height=20)
            i = 0
            for i in range(0, len(sol), 1):
                r = ', '.join(str(item) for item in sol[i])
                solBox.insert(i, r)
            
            solBox.grid(row=2, column=0, columnspan=4, padx=20, pady=20)
            
            # go back btn
            goBackBtn = tk.Button(result, text='Go Back to Home', font=('SegoeUI 18'), command=lambda: change_to_home2(email))
            goBackBtn.grid(row=3, column=0)
            
                    
            
        
        inputLabel = tk.Label(result, text="Skills(CommaSeparated):", font=('SegoeUI 20'), anchor='w', justify='left', bg='white', fg='black')
        inputLabel.grid(row=1, column=0, padx=0, columnspan=1)
        
        inputEntry = tk.Entry(result, font=('SegoeUI 20'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', justify='left', width=30, insertbackground='black')
        inputEntry.grid(row=1, column=1, columnspan=2, pady=20, padx=0)
        
        inputBtn = tk.Button(result, font=('SegoeUI 20'), text='Enter', command=showResult)
        inputBtn.grid(row=1, column=3, padx=10)
    # Show the top 5 sectors by number of job posts, and the average salary range for each
    elif query == "Show the Top 5 Sectors:":
        sol = set()

        sql = f"""
        SELECT SectorName, Count(*), AVG(MinimumSalary), AVG(MaximumSalary)
        FROM CompanySector cs
        JOIN JobPost jp on cs.CompanyName = jp.CompanyName 
        Group BY 1
        ORDER BY 2 DESC
        LIMIT 5;
        """
        
        cursor.execute(sql)
        r = cursor.fetchall()
         
        solBox = tk.Listbox(result, font=('SegoeUi 18'), bg='white', fg='black', width=88, height=20)
        i = 0
        for i in range(0, len(r), 1):
            a = ', '.join(str(item) for item in r[i])
            solBox.insert(i, a)
        
        solBox.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
        
        # go back btn
        goBackBtn = tk.Button(result, text='Go Back to Home', font=('SegoeUI 18'), command=lambda: change_to_home2(email))
        goBackBtn.grid(row=3, column=0)
    # Show the top 5 skills that are in the highest demand
    elif query == "Show the Top 5 Skills:":
        sol = set()

        sql = f"""
        SELECT SkillName, Count(*)
        FROM JobPostSkills
        GROUP BY 1
        ORDER BY 2 DESC
        LIMIT 5
        """
        
        cursor.execute(sql)
        r = cursor.fetchall()
         
        solBox = tk.Listbox(result, font=('SegoeUi 18'), bg='white', fg='black', width=88, height=20)
        i = 0
        for i in range(0, len(r), 1):
            # a = ', '.join(str(item) for item in r[i])
            solBox.insert(i, r[i][0])
        
        solBox.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
        
        # go back btn
        goBackBtn = tk.Button(result, text='Go Back to Home', font=('SegoeUI 18'), command=lambda: change_to_home2(email))
        goBackBtn.grid(row=3, column=0)
    # Show the top 5 growing startups in Egypt by the amount of vacancies they have compared to their foundation date
    elif query == "Show the Top 5 Growing Startups:":
        sol = set()

        sql = f"""
        SELECT cs.CompanyName, cs.FoundationDate, COUNT(jp.JobTitle) as NumVacancies, COUNT(jp.JobTitle) / (2024 - cs.FoundationDate) as GrowthRate
        FROM Company cs
        JOIN JobPost jp on jp.CompanyName = cs.CompanyName
        WHERE cs.FoundationDate is not NULL
        GROUP BY 1, 2
        HAVING COUNT(jp.CompanyName) > 0
        ORDER BY GrowthRate DESC
        LIMIT 5;
        """
        
        cursor.execute(sql)
        r = cursor.fetchall()
         
        solBox = tk.Listbox(result, font=('SegoeUi 18'), bg='white', fg='black', width=88, height=20)
        i = 0
        for i in range(0, len(r), 1):
            # a = ', '.join(str(item) for item in r[i])
            solBox.insert(i, r[i][0])
        
        solBox.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
        
        # go back btn
        goBackBtn = tk.Button(result, text='Go Back to Home', font=('SegoeUI 18'), command=lambda: change_to_home2(email))
        goBackBtn.grid(row=3, column=0)
    # Show the top 5 most paying companies in the field in Egypt
    elif query == "Show the Top 5 Most Paying Companies:":
        sol = set()

        sql = f"""
        SELECT CompanyName, MaximumSalary
        FROM JobPost
        ORDER BY 2 DESC
        LIMIT 5
        """
        
        cursor.execute(sql)
        r = cursor.fetchall()
         
        solBox = tk.Listbox(result, font=('SegoeUi 18'), bg='white', fg='black', width=88, height=20)
        i = 0
        for i in range(0, len(r), 1):
            a = ', '.join(str(item) for item in r[i])
            solBox.insert(i, a)
        
        solBox.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
        
        # go back btn
        goBackBtn = tk.Button(result, text='Go Back to Home', font=('SegoeUI 18'), command=lambda: change_to_home2(email))
        goBackBtn.grid(row=3, column=0)
    # Show all the postings for a given company / organization
    elif query == "Show the posts for a given Company:":
        def showResult():
            sol = set()
            sql = f'''
                SELECT CompanyName, JobTitle, DatePosted, JobType
                FROM JobPost
                WHERE CompanyName = '{inputEntry.get()}'
            '''
            cursor.execute(sql)
            r = cursor.fetchall()
            for i in r:
                    sol.add(i)
        
            sol = list(sol)
            sol.sort(key=lambda x: x[0])
            
            solBox = tk.Listbox(result, font=('SegoeUi 18'), bg='white', fg='black', width=88, height=20)
            i = 0
            for i in range(0, len(sol), 1):
                r = ', '.join(str(item) for item in sol[i])
                solBox.insert(i, r)
            
            solBox.grid(row=2, column=0, columnspan=4, padx=20, pady=20)
            
            # go back btn
            goBackBtn = tk.Button(result, text='Go Back to Home', font=('SegoeUI 18'), command=lambda: change_to_home2(email))
            goBackBtn.grid(row=3, column=0)
            
                    
            
        
        inputLabel = tk.Label(result, text="CompanyName:", font=('SegoeUI 20'), anchor='w', bg='white', fg='black')
        inputLabel.grid(row=1, column=0)
        
        inputEntry = tk.Entry(result, font=('SegoeUI 20'), fg='black', highlightbackground='lightgray', highlightthickness=2, bg='#FAFAFA', justify='left', insertbackground='black')
        inputEntry.grid(row=1, column=1, columnspan=2, pady=20)
        
        inputBtn = tk.Button(result, font=('SegoeUI 20'), text='Enter', command=showResult)
        inputBtn.grid(row=1, column=3, padx=10)
    # Show the top 5 categories (other than IT/Software Development) that the postings are cross listed under based on the volume of postings
    elif query == "Show the Top 5 Categories (other than IT/Software Development):":
        sol = set()

        sql = f"""
        SELECT CategoryName, Count(*)
        FROM JobPostCategory jpc
        JOIN JobPost jp on jpc.CompanyName = jp.CompanyName AND jpc.JobTitle = jp.JobTitle AND jpc.DatePosted = jp.DatePosted
        WHERE CategoryName != 'IT/Software Development'
        Group BY 1
        ORDER BY 2 DESC
        LIMIT 5
        """
        
        cursor.execute(sql)
        r = cursor.fetchall()
         
        solBox = tk.Listbox(result, font=('SegoeUi 18'), bg='white', fg='black', width=88, height=20)
        i = 0
        for i in range(0, len(r), 1):
            # a = ', '.join(str(item) for item in r[i])
            solBox.insert(i, r[i][0])
        
        solBox.grid(row=1, column=0, columnspan=4, padx=20, pady=20)
        
        # go back btn
        goBackBtn = tk.Button(result, text='Go Back to Home', font=('SegoeUI 18'), command=lambda: change_to_home2(email))
        goBackBtn.grid(row=3, column=0)
        
    
# Create an instance of tkinter frame or window
root = tk.Tk()

# Set the size of the window
root.geometry("1000x1000")
root['background'] = 'white'
root.title('Wuzzuf')

# add all configurations here for the root


# Create two frames in the window
sigin = tk.Frame(root, width=350, height=400, bg='white', highlightbackground='gray', highlightthickness=2)
register = tk.Frame(root, width=1000, height=1000, bg='white', highlightbackground='gray', highlightthickness=1)
home = tk.Frame(root, width=1000, height=1000, bg='white', highlightbackground='gray', highlightthickness=1)
result = tk.Frame(root, width=1000, height=1000, bg='white', highlightbackground='gray', highlightthickness=1)

# siginFrame()
# registerFrame()
#homeFrame()
#resultFrame

change_to_signin()
# change_to_register()
# change_to_home('Ahmed@ex.com')


root.mainloop()