from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import mysql.connector



app = Flask(__name__)


#Configure db
mydb = mysql.connector.connect(host='localhost',user='root',password='Sinha@17',database='feedback')
mycursor = mydb.cursor()

mycursor.execute('select * from Admin')
for i in mycursor:
    print(i)

msg = '' 

#API for home page

@app.route("/")
def home():
    return render_template('home.html')

#API for student pages

@app.route("/studentLogin",methods = ['GET','POST'])
def studentLog():
    if request.method == 'POST':
        #Fetch form data
        studLogDetail = request.form
        studLogReg = studLogDetail['studentReg']
        studLogPass = studLogDetail['studentPass']
        mycursor.execute("SELECT * FROM Student WHERE studentReg = %s AND studentPassword = %s", [studLogReg, studLogPass])
        isPresent = mycursor.fetchone()
        global msg 
        if not isPresent: 
            msg = "Incorrect username & password. Please try again."
        else:
           msg = "Welcome"
        return render_template('student_home.html', msg=msg)
    return render_template('student_login.html')

@app.route("/studentHome")
def studentHome():
    return render_template('student_home.html')

@app.route("/studentFeedback",methods = ['GET','POST'])
def studentFeedback():
    if request.method == 'POST':
        #Fetch form data
        feedDetail = request.form
        sem=[{'name':1}, {'name':2}, {'name':3}, {'name':4}, {'name':5}, {'name':6}, {'name':7}, {'name':8}]  
        select = request.form.get('slct1')
        return(str(select)) 
        subjectList=[{'name':1}, {'name':2}, {'name':3}, {'name':4}, {'name':5}, {'name':6}, {'name':7}, {'name':8}]            
    return render_template('student_feedback.html')


#API for faculty pages

@app.route("/facLogin",methods = ['GET','POST'])
def facultyLog():
    if request.method == 'POST':
        #Fetch form data
        facultyDetail = request.form
        facMail = facultyDetail['facultyEmail']
        facPass = facultyDetail['facultyPass'] 
        mycursor.execute("SELECT * FROM Faculty WHERE facultyEmail = %s AND facultyPass = %s", [facMail, facPass])
        isPresent = mycursor.fetchone()
        global msg 
        if not isPresent: 
            msg = "Incorrect username & password. Please try again."
        else:
           msg = "Welcome"
        return render_template('faculty_dashboard.html', msg=msg)
    return render_template('faculty_login.html')

@app.route("/facultyHome")
def facultyHome():
    return render_template('faculty_dashboard.html')

@app.route("/facultyFeedack")
def facultyFeedack():
    return render_template('faculty_feedback.html')




@app.route("/adminHome")
def adminHome():
    return render_template('admin_dashboard.html')

@app.route("/adminAddFaculty",methods = ['GET','POST'])
def adminAddFaculty():
    if request.method == 'POST':
        #Fetch form data
        facultyDetail = request.form
        facName = facultyDetail['facultyName']
        facMail = facultyDetail['facultyEmail']
        facDeg = facultyDetail['facultyDesignation']
        facPhone = facultyDetail['facultyPhone']
        facPass = facultyDetail['facultyPass']  
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Faculty WHERE facultyEmail = %s", [facMail])
        isPresent = mycursor.fetchone()
        #isPresent = false
        global msg 
        if not isPresent: 
            msg = "Faculty added successfully."
            mycursor.execute("INSERT INTO Faculty(facultyName, facultyEmail, facultyDesignation, facultyPhone, facultyPass) VALUES (%s, %s, %s,%s, %s)", (facName, facMail, facDeg,facPhone,facPass))
            mydb.commit()
        else:
           msg = "Faculty already exits. Please enter new faculty data."
        return render_template('admin_addFaculty.html', msg=msg)
    return render_template('admin_addFaculty.html')

@app.route("/adminAddStudent",methods = ['GET','POST'])
def adminAddStudent():
    if request.method == 'POST':
        #Fetch form data
        studDetail = request.form
        studName = studDetail['studentName']
        studMail = studDetail['studentEmail']
        studReg = studDetail['studentReg']
        studDOB = studDetail['studentDOB']
        studPhone = studDetail['studentPhone']
        studRoll = studDetail['studentRoll']
        studBranch = studDetail['studentBranch']
        studPass = studDetail['studentPass']  
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM Student WHERE studentReg = %s", [studReg])
        isPresent = mycursor.fetchone()
        #isPresent = false
        global msg 
        if not isPresent: 
            msg = "Student added successfully."
            mycursor.execute("INSERT INTO Student(studentName,studentEmail,studentReg,studentDOB,studentPhone,studentRoll,studentBranch, studentPassword) VALUES (%s, %s, %s,%s, %s, %s,%s, %s)", (studName, studMail, studReg,studDOB,studPhone,studRoll,studBranch,studPass))
            mydb.commit()
        else:
           msg = "Student already exits. Please enter new student data."
        return render_template('admin_addStudent.html', msg=msg)
    return render_template('admin_addStudent.html')

#API for admin create pages

@app.route("/adminCreate",methods = ['GET','POST'])
def adminCreate():
    if request.method == 'POST':
        #Fetch form data
        adminDetail = request.form
        adminName = adminDetail['Adminname']
        adminMail = adminDetail['Adminemail']
        adminPass = adminDetail['AdminPassword']
        mycursor.execute("SELECT * FROM Admin WHERE adminEmail = %s", [adminMail])
        isPresent = mycursor.fetchone()
        #isPresent = false
        global msg 
        if not isPresent: 
            msg = "Account created successfully."
            mycursor.execute("INSERT INTO Admin(adminName, adminEmail, adminPassword) VALUES (%s, %s, %s)", (adminName, adminMail, adminPass))
            mydb.commit()
        else:
           msg = "Account already exits. Please login."
        mycursor.close()
        return render_template('admin_login.html', msg=msg)
    return render_template('admin_create.html')


#API for admin login pages

@app.route("/adminLogin", methods = ['GET','POST'])
def adminLogin():
    if request.method == 'POST':
        #Fetch form data
        adminDetail = request.form
        adminMail = adminDetail['Adminemail']
        adminPass = adminDetail['AdminPass']
        mycursor.execute("SELECT * FROM Admin WHERE adminEmail = %s AND adminPassword = %s", [adminMail, adminPass])
        isPresent = mycursor.fetchone()
        global msg 
        if not isPresent: 
            msg = "Incorrect email & password. Please try again."
        else:
           msg = "Welcome"
        return render_template('admin_dashboard.html', msg=msg)
    return render_template('admin_login.html')

if __name__ == '__main__':
    app.run(debug=True)