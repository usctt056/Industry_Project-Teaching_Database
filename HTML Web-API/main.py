import mysql.connector
import webbrowser
import os
from bottle import route, run, request, template, static_file, response
from xml.dom import minidom, Node
from classDb import DatabaseConnect as db_connection
# from bottle import Bottle, template


# Home Page
@route('/')
def index():
    title = 'Welcome home'
    info = {'title': title,
            'content': 'Default Home page.'
            }
    # Generates HTML webpage.
    return template('./views/Home_Page.html', info)

# Teaching Staff Portal
@route('/Teaching_Staff_Portal.html')
def index():
    title = 'Teaching Staff'
    info = {'title': title,
            'content': 'Teaching Staff page.'
            }
    # Generates HTML webpage.
    return template('Teaching_Staff_Portal.html', info)

# Home Page 2
@route('/Home_Page.html')
def index():
    title = 'Welcome home 2'
    info = {'title': title,
            'content': 'Home Page 2'
            }
    # Generates HTML webpage.
    return template('Home_Page.html', info)

# Admin Portal 2
@route('/Admin_Portal_2.html')
def index():
    title = 'Admin Portal 2'
    info = {'title': title,
            'content': 'Admin Portal 2 page.'
            }
    # Generates HTML webpage.
    return template('Admin_Portal_2.html', info)

# Admin Portal
@route('/Admin_Portal.html')
def index():
    title = 'Admin Portal'
    info = {'title': title,
            'content': 'Admin Portal page.'
            }
    # Generates HTML webpage.
    return template('Admin_Portal.html', info)

# New Teaching Staff
@route('/New_Teaching_Staff.html')
def index():
    title = 'New Teaching Staff'
    info = {'title': title,
            'content': 'New Teaching Staff page.'
            }
    #return info
    return template('New_Teaching_Staff.html', info)

# View Staff Records.
@route('/staffRecords.html')
def admin_review_form():
    title = 'Staff Records'
    info = {'title': title,
            'content': 'Staff Records Page.'
            }

    # Generates HTML webpage.
    return template('staffRecords.html', info)

# Delete Staff
@route('/staffDelete.html')
def admin_staff_delete():
    title = 'Staff Delete Records'
    info = {'title': title,
            'content': 'Staff Delete Page'
            }

    # Generates HTML webpage.
    return template('staffDelete.html', info)

# Approval of staff
@route('/adminApp.html')
def admin_approval_form():
    title = 'Admin Approval Form'
    info = {'title': title,
            'content': 'Admin Approval Form Page'
            }

    # Generates HTML webpage.
    return template('adminApp.html', info)

# Review of Staff
@route('/adminRev.html')
def admin_review_form():
    title = 'Admin Review Form'
    info = {'title': title,
            'content': 'Admin Review Form Page'
            }

    # Generates HTML webpage.
    return template('adminRev.html', info)

# View AQF records.
@route('/aqfRecords.html')
def admin_review_form():
    title = 'AQF Records'
    info = {'title': title,
            'content': 'AQF Records Page'
            }

    # Generates HTML webpage.
    return template('aqfRecords.html', info)

# View Approval records.
@route('/approvalRecords.html')
def admin_review_form():
    title = 'Appproval Records'
    info = {'title': title,
            'content': 'Approval Records Page'
            }

    # Generates HTML webpage.
    return template('approvalRecords.html', info)

# Delete Approval
@route('/approvalDelete.html')
def admin_del_approval():
    title = 'Delete Appproval Records'
    info = {'title': title,
            'content': 'Delete Approvals Page'
            }

    # Generates HTML webpage.
    return template('approvalDelete.html', info)

# View Review rcords.
@route('/reviewRecords.html')
def admin_review_form():
    title = 'Review Records'
    info = {'title': title,
            'content': 'Review Records Page'
            }

    # Generates HTML webpage.
    return template('reviewRecords.html', info)

# Delete Review
@route('/reviewDelete.html')
def admin__del_review():
    title = 'Delete Review Records'
    info = {'title': title,
            'content': 'Delete Reviews Page'
            }

    # Generates HTML webpage.
    return template('reviewDelete.html', info)

# Approval Form
@route('/staffApprovalForm')
def submit_staff_app():

    # Parse XML document.
    staff = request.query.staffXML
    print(staff)
    DOMTree = minidom.parseString(staff)
    file_name = "Approval Details"
    print(file_name)

    # Extract data in XML tags and store them as variables. Eg. appstaffid_data
    appstaffid_tag = DOMTree.getElementsByTagName('appstaffid')
    appstaffid_data = appstaffid_tag[0].firstChild.data
    print(appstaffid_data)

    levelteach_tag = DOMTree.getElementsByTagName('levelteach')
    levelteach_data = levelteach_tag[0].firstChild.data
    print(levelteach_data)

    discipline_tag = DOMTree.getElementsByTagName('discipline')
    discipline_data = discipline_tag[0].firstChild.data
    print(discipline_data)

    location_tag = DOMTree.getElementsByTagName('location')
    location_data = location_tag[0].firstChild.data
    print(location_data)

    appdate_tag = DOMTree.getElementsByTagName('appdate')
    appdate_data = appdate_tag[0].firstChild.data
    print(appdate_data)

    revdate_tag = DOMTree.getElementsByTagName('revdate')
    revdate_data = revdate_tag[0].firstChild.data
    print(revdate_data)

    appby_tag = DOMTree.getElementsByTagName('appby')
    appby_data = appby_tag[0].firstChild.data
    print(appby_data)

    appnote_tag = DOMTree.getElementsByTagName('appnote')
    appnote_data = appnote_tag[0].firstChild.data
    print(appnote_data)


# Create connection with Teaching Database and execute SQL statement/s into Staff.
    with db_connection() as db:
        conx = db.opendb()

        sql1 = "INSERT INTO approval (Staff_id, Level_to_teach, Discipline_area, Location, Approval_date, Approval_by, Approval_notes, Review_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        val1 = (appstaffid_data, levelteach_data, discipline_data, location_data, appdate_data, appby_data, appnote_data, revdate_data)

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(sql1, val1)

        conx.commit()

        print(mycursorsql1.rowcount, "Approval updated.")
# Review form.
@route('/staffReviewForm')
def submit_staff_rev():

    # Parse XML document.
    staff = request.query.staffXML
    print(staff)
    DOMTree = minidom.parseString(staff)
    file_name = "Review Details"
    print(file_name)

    # Extract data in XML tags and store them as variables. Eg. appstaffid_data
    revappid_tag = DOMTree.getElementsByTagName('revappid')
    revappid_data = revappid_tag[0].firstChild.data
    print(revappid_data)

    revstaffid_tag = DOMTree.getElementsByTagName('revstaffid')
    revstaffid_data = revstaffid_tag[0].firstChild.data
    print(revstaffid_data)

    revdate_tag = DOMTree.getElementsByTagName('revdate')
    revdate_data = revdate_tag[0].firstChild.data
    print(revdate_data)

    revby_tag = DOMTree.getElementsByTagName('revby')
    revby_data = revby_tag[0].firstChild.data
    print(revby_data)

    revoutcome_tag = DOMTree.getElementsByTagName('revoutcome')
    revoutcome_data = revoutcome_tag[0].firstChild.data
    print(revoutcome_data)

    revnote_tag = DOMTree.getElementsByTagName('revnote')
    revnote_data = revnote_tag[0].firstChild.data
    print(revnote_data)

# Create connection with Teaching Database and execute SQL statement/s into Staff.
    with db_connection() as db:
        conx = db.opendb()

        sql1 = "INSERT INTO review (Approval_id, Staff_id, Reviewed_on, Reviewed_by, Outcome, Notes) VALUES (%s, %s, %s, %s, %s, %s)"
        val1 = (revappid_data, revstaffid_data, revdate_data, revby_data, revoutcome_data, revnote_data)

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(sql1, val1)

        conx.commit()

        print(mycursorsql1.rowcount, "Review updated.")

# Submit filled outStaff form into the Teaching Org database.
@route('/submitStaffForm')
def submit_staff():

    # Parse XML document.
    staff = request.query.staffXML
    print(staff)
    DOMTree = minidom.parseString(staff)
    file_name = "Staff Details"
    print(file_name)

    # Extract data in XML tags and store them as variables. Eg. title_data
    title_tag = DOMTree.getElementsByTagName('title')
    title_data = title_tag[0].firstChild.data
    print(title_data)

    f_name_tag = DOMTree.getElementsByTagName('fname')
    f_name_data = f_name_tag[0].firstChild.data
    print(f_name_data)

    l_name_tag = DOMTree.getElementsByTagName('lname')
    l_name_data = l_name_tag[0].firstChild.data
    print(l_name_data)

    address_tag = DOMTree.getElementsByTagName('address')
    address_data = address_tag[0].firstChild.data
    print(address_data)

    email_tag = DOMTree.getElementsByTagName('email')
    email_data = email_tag[0].firstChild.data
    print(email_data)

    phone_tag = DOMTree.getElementsByTagName('phone')
    phone_data = phone_tag[0].firstChild.data
    print(phone_data)

    # Extract data in XML tags and store them as variables. Eg. qual_data
    qual_tag = DOMTree.getElementsByTagName('qual')
    qual_data = qual_tag[0].firstChild.data
    print(qual_data)

    subject_tag = DOMTree.getElementsByTagName('subject')
    subject_data = subject_tag[0].firstChild.data
    print(subject_data)

    insti_tag = DOMTree.getElementsByTagName('institution')
    insti_data = insti_tag[0].firstChild.data
    print(insti_data)

    qualyear_tag = DOMTree.getElementsByTagName('year')
    qualyear_data = qualyear_tag[0].firstChild.data
    print(qualyear_data)

    # Extract data in XML tags and store them as variables. Eg. per_data
    period_tag = DOMTree.getElementsByTagName('period')
    period_data = period_tag[0].firstChild.data
    print(period_data)

    field_tag = DOMTree.getElementsByTagName('field')
    field_data = field_tag[0].firstChild.data
    print(field_data)

    teachinsti_tag = DOMTree.getElementsByTagName('teachinsti')
    teachinsti_data = teachinsti_tag[0].firstChild.data
    print(teachinsti_data)

    role_tag = DOMTree.getElementsByTagName('role')
    role_data = role_tag[0].firstChild.data
    print(role_data)

    # Extract data in XML tags and store them as variables. Eg. per_data
    empper_tag = DOMTree.getElementsByTagName('empperiod')
    empper_data = empper_tag[0].firstChild.data
    print(empper_data)

    fte_tag = DOMTree.getElementsByTagName('fte')
    fte_data = fte_tag[0].firstChild.data
    print(fte_data)

    emp_tag = DOMTree.getElementsByTagName('employer')
    emp_data = emp_tag[0].firstChild.data
    print(emp_data)

    ptitle_tag = DOMTree.getElementsByTagName('postitle')
    ptitle_data = ptitle_tag[0].firstChild.data
    print(ptitle_data)

    duty_tag = DOMTree.getElementsByTagName('duty')
    duty_data = duty_tag[0].firstChild.data
    print(duty_data)

    # Extract data in XML tags and store them as variables. Eg. other_data
    other_tag = DOMTree.getElementsByTagName('otherinfo1')
    other_data = other_tag[0].firstChild.data
    print(other_data)

    # Extract data in XML tags and store them as variables. Eg. author_data
    author_tag = DOMTree.getElementsByTagName('author')
    author_data = author_tag[0].firstChild.data
    print(author_data)

    yearpub_tag = DOMTree.getElementsByTagName('yearpub')
    yearpub_data = yearpub_tag[0].firstChild.data
    print(yearpub_data)

    titlepub_tag = DOMTree.getElementsByTagName('titlepub')
    titlepub_data = titlepub_tag[0].firstChild.data
    print(titlepub_data)

    jvp_tag = DOMTree.getElementsByTagName('jvp')
    jvp_data = jvp_tag[0].firstChild.data
    print(jvp_data)

    typepub_tag = DOMTree.getElementsByTagName('typepub')
    typepub_data = typepub_tag[0].firstChild.data
    print(typepub_data)

    peerrev_tag = DOMTree.getElementsByTagName('peerrev')
    peerrev_data = peerrev_tag[0].firstChild.data
    print(peerrev_data)

    resclass_tag = DOMTree.getElementsByTagName('resclass')
    resclass_data = resclass_tag[0].firstChild.data
    print(resclass_data)

    fieldedu_tag = DOMTree.getElementsByTagName('fieldedu')
    fieldedu_data = fieldedu_tag[0].firstChild.data
    print(fieldedu_data)

    # Create connection with Teaching Database and execute SQL statement/s into Staff.
    with db_connection() as db:
        conx = db.opendb()

        sql1 = "INSERT INTO staff (Title, F_name, L_name, Address, Email, Phone, qual_id, Subject_area, institution, Year_awarded, Teaching_period, Courses_taught, Org_name, Role_in_course, Emp_period, Status_of_emp, Prev_emp, Pos_title, Duties, Other_info, Author, Year_of_pub, Title_of_pub, Volume, Type_of_pub, Peer_reviewed, Research_class, Field_of_edu) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val1 = (title_data, f_name_data, l_name_data, address_data, email_data, phone_data, qual_data, subject_data, insti_data, qualyear_data, period_data, field_data, teachinsti_data, role_data, empper_data, fte_data, emp_data, ptitle_data, duty_data, other_data, author_data, yearpub_data, titlepub_data, jvp_data, typepub_data, peerrev_data, resclass_data, fieldedu_data)

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(sql1, val1)

        conx.commit()

        print(mycursorsql1.rowcount, "Staff details inserted.")

    """# Create connection with Teaching Database and execute SQL statement/s into Qualification.
    with db_connection() as db:
        conx = db.opendb()

        sql2 = "INSERT INTO staff (Name_of_qual, Subject_area, Institution, Year_awarded) VALUES (%s, %s, %s, %s)"
        val2 = (qual_data, subject_data, insti_data, qualyear_data)

        mycursorsql2 = conx.cursor()

        mycursorsql2.execute(sql2, val2)

        conx.commit()

        print(mycursorsql2.rowcount, "Qualification details inserted.")"""


# Review AQF details.
@route('/adminViewAqfRecord')
def retrieve_aqf_lev():

    # Create connection with Teaching Database and retrieve AQF Information.
    with db_connection() as db:
        conx = db.opendb()

        approval_sel = """SELECT * FROM aqf"""

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(approval_sel)

        result = mycursorsql1.fetchall()

        app_table = []

        table_format = "<tr><td>AQF ID</td><td>AQF Level</td><td>Qualification Type</td><td>Level to Teach</td></tr>"

        app_table.append(table_format)

        for row in result:
            a = "<tr><td>%s</td>"%row[0]
            app_table.append(a)

            b = "<td>%s</td>"%row[1]
            app_table.append(b)

            c = "<td>%s</td>"%row[2]
            app_table.append(c)

            d = "<td>%s</td></tr>"%row[3]
            app_table.append(d)

        contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
            <html>
            <head>
            <meta content="text/html; charset=ISO-8859-1"
            http-equiv="content-type">
            <title>AQF Levels</title>
            </head>
            <body>
            <table>
            %s
            </table>
            </body>
            </html>
            '''%(app_table)

        filename = 'aqfRecords.html'

        def main(contents, filename):
                output = open(filename,"w")
                output.write(contents)
                output.close()

        main(contents, filename)
        webbrowser.open(filename)

        if(conx.is_connected()):
                mycursorsql1.close()
                conx.close()
                print("MySQL connection is closed.")


        print('Retrieved AQF!')


# Retrieve Approval records.
@route('/adminViewAppRecord')
def retrieve_staff_app():

    # Create connection with Teaching Database and retrieve Approval Information.
    with db_connection() as db:
        conx = db.opendb()

        approval_sel = """SELECT * FROM approval"""

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(approval_sel)

        result = mycursorsql1.fetchall()

        app_table = []

        table_format = "<tr><td>Approval ID</td><td>Staff ID</td><td>Level to Teach</td><td>Discipline Area</td><td>Location</td><td>Approval Date</td><td>Approved By</td><td>Additional Notes</td><td>Review Date</td></tr>"

        app_table.append(table_format)

        for row in result:
            a = "<tr><td>%s</td>"%row[0]
            app_table.append(a)

            b = "<td>%s</td>"%row[1]
            app_table.append(b)

            c = "<td>%s</td>"%row[2]
            app_table.append(c)

            d = "<td>%s</td>"%row[3]
            app_table.append(d)

            e = "<td>%s</td>"%row[4]
            app_table.append(e)

            f = "<td>%s</td>"%row[5]
            app_table.append(f)

            g = "<td>%s</td>"%row[6]
            app_table.append(g)

            h = "<td>%s</td></tr>"%row[7]
            app_table.append(h)

            i = "<td>%s</td></tr>"%row[8]
            app_table.append(i)

        contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
            <html>
            <head>
            <meta content="text/html; charset=ISO-8859-1"
            http-equiv="content-type">
            <title>Approval Records</title>
            </head>
            <body>
            <table>
            %s
            </table>
            </body>
            </html>
            '''%(app_table)

        filename = 'approvalRecords.html'

        def main(contents, filename):
                output = open(filename,"w")
                output.write(contents)
                output.close()

        main(contents, filename)
        webbrowser.open(filename)

        if(conx.is_connected()):
                mycursorsql1.close()
                conx.close()
                print("MySQL connection is closed.")


        print('Retrieved Approvals!')

# Delete approval records.
@route('/approvalIdDelete')
def del_approval():

    # Parse XML document.
    staff = request.query.staffXML
    print(staff)
    DOMTree = minidom.parseString(staff)
    file_name = "Approval ID Details"
    print(file_name)

    # Extract data in XML tags and store them as variables. Eg. delappid_data
    delappid_tag = DOMTree.getElementsByTagName('delappid')
    delappid_data = delappid_tag[0].firstChild.data
    print(delappid_data)


    # Create connection with Teaching Database and execute SQL statement/s into Staff.
    with db_connection() as db:
        conx = db.opendb()

        sql1 = "DELETE FROM Approval WHERE Approval_id = %s"
        val1 = (delappid_data, )

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(sql1, val1)

        conx.commit()

        print(mycursorsql1.rowcount, "Approval deleted.")

# Retrieve Review records.
@route('/adminViewRevRecord')
def retrieve_staff_rev():

    # Create connection with Teaching Database and retrieve Review records.
    with db_connection() as db:
        conx = db.opendb()

        approval_sel = """SELECT * FROM review"""

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(approval_sel)

        result = mycursorsql1.fetchall()

        app_table = []

        table_format = "<tr><td>Review ID</td><td>Approval ID</td><td>Staff ID</td><td>Reviewed On</td><td>Reviewed By</td><td>Outcome</td><td>Notes</td></tr>"

        app_table.append(table_format)

        for row in result:
            a = "<tr><td>%s</td>"%row[0]
            app_table.append(a)

            b = "<td>%s</td>"%row[1]
            app_table.append(b)

            c = "<td>%s</td>"%row[2]
            app_table.append(c)

            d = "<td>%s</td>"%row[3]
            app_table.append(d)

            e = "<td>%s</td>"%row[4]
            app_table.append(e)

            f = "<td>%s</td>"%row[5]
            app_table.append(f)

            g = "<td>%s</td>"%row[6]
            app_table.append(g)

        contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
            <html>
            <head>
            <meta content="text/html; charset=ISO-8859-1"
            http-equiv="content-type">
            <title>Review Records</title>
            </head>
            <body>
            <table>
            %s
            </table>
            </body>
            </html>
            '''%(app_table)

        filename = 'reviewRecords.html'

        def main(contents, filename):
                output = open(filename,"w")
                output.write(contents)
                output.close()

        main(contents, filename)
        webbrowser.open(filename)

        if(conx.is_connected()):
                mycursorsql1.close()
                conx.close()
                print("MySQL connection is closed.")


        print('Retrieved Reviews!')

# Delete Review records
@route('/reviewIdDelete')
def del_approval():

    # Parse XML document.
    staff = request.query.staffXML
    print(staff)
    DOMTree = minidom.parseString(staff)
    file_name = "Review ID Details"
    print(file_name)

    # Extract data in XML tags and store them as variables. Eg. delappid_data
    delrevid_tag = DOMTree.getElementsByTagName('delrevid')
    delrevid_data = delrevid_tag[0].firstChild.data
    print(delrevid_data)


    # Create connection with Teaching Database and execute SQL statement/s into Staff.
    with db_connection() as db:
        conx = db.opendb()

        sql1 = "DELETE FROM review WHERE Review_id = %s"
        val1 = (delrevid_data, )

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(sql1, val1)

        conx.commit()

        print(mycursorsql1.rowcount, "Review deleted.")

# Retrieve Staff records.
@route('/viewStaffRecord')
def retrieve_staff_rec():

    # Create connection with Teaching Database and retrieve Staff records.
    with db_connection() as db:
        conx = db.opendb()

        approval_sel = """SELECT * FROM staff"""

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(approval_sel)

        result = mycursorsql1.fetchall()

        app_table = []

        table_format = "<tr><td>Staff ID</td><td>Title</td><td>First Name</td><td>Last Name</td><td>Address</td><td>Email</td><td>Phone</td><td>Qualification ID</td><td>Subject Area</td><td>Institution</td><td>Year Awarded</td><td>Teaching Period</td><td>Courses Taught</td><td>Organisation Name</td><td>Role In Course</td><td>Employment Period</td><td>Status of Employment</td><td>Previous Employment</td><td>Position Title</td><td>Duties</td><td>Other Information</td><td>Author</td><td>Year of Publication</td><td>Title of Publication</td><td>Volume</td><td>Type of Publication</td><td>Peer Reviewed</td><td>Research Classification</td><td>Field of Education</td></tr>"

        app_table.append(table_format)

        for row in result:
            a = "<tr><td>%s</td>"%row[0]
            app_table.append(a)

            b = "<td>%s</td>"%row[1]
            app_table.append(b)

            c = "<td>%s</td>"%row[2]
            app_table.append(c)

            d = "<td>%s</td>"%row[3]
            app_table.append(d)

            e = "<td>%s</td>"%row[4]
            app_table.append(e)

            f = "<td>%s</td>"%row[5]
            app_table.append(f)

            g = "<td>%s</td>"%row[6]
            app_table.append(g)

            h = "<td>%s</td>"%row[7]
            app_table.append(h)

            i = "<td>%s</td>"%row[8]
            app_table.append(i)

            j = "<td>%s</td>"%row[9]
            app_table.append(j)

            k = "<td>%s</td>"%row[10]
            app_table.append(k)

            l = "<td>%s</td>"%row[11]
            app_table.append(l)

            m = "<td>%s</td>"%row[12]
            app_table.append(m)

            n = "<td>%s</td>"%row[13]
            app_table.append(n)

            o = "<td>%s</td>"%row[14]
            app_table.append(o)

            p = "<td>%s</td>"%row[15]
            app_table.append(p)

            q = "<td>%s</td>"%row[16]
            app_table.append(q)

            r = "<td>%s</td>"%row[17]
            app_table.append(r)

            s = "<td>%s</td>"%row[18]
            app_table.append(s)

            t = "<td>%s</td>"%row[19]
            app_table.append(t)

            u = "<td>%s</td>"%row[20]
            app_table.append(u)

            v = "<td>%s</td>"%row[21]
            app_table.append(v)

            w = "<td>%s</td>"%row[22]
            app_table.append(w)

            x = "<td>%s</td>"%row[23]
            app_table.append(x)

            y = "<td>%s</td>"%row[24]
            app_table.append(y)

            z = "<td>%s</td>"%row[25]
            app_table.append(z)

            aa = "<td>%s</td>"%row[26]
            app_table.append(aa)

            ab = "<td>%s</td>"%row[27]
            app_table.append(ab)

            ac = "<td>%s</td></tr>"%row[28]
            app_table.append(ac)

        contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
            <html>
            <head>
            <meta content="text/html; charset=ISO-8859-1"
            http-equiv="content-type">
            <title>Staff Records</title>
            </head>
            <body>
            <table>
            %s
            </table>
            </body>
            </html>
            '''%(app_table)

        filename = 'staffRecords.html'

        def main(contents, filename):
                output = open(filename,"w")
                output.write(contents)
                output.close()

        main(contents, filename)
        webbrowser.open(filename)

        if(conx.is_connected()):
                mycursorsql1.close()
                conx.close()
                print("MySQL connection is closed.")


        print('Retrieved Staff Records!')

@route('/staffIdDelete')
def del_approval():

    # Parse XML document.
    staff = request.query.staffXML
    print(staff)
    DOMTree = minidom.parseString(staff)
    file_name = "Staff ID Details"
    print(file_name)

    # Extract data in XML tags and store them as variables. Eg. delappid_data
    delstaffid_tag = DOMTree.getElementsByTagName('delstaffid')
    delstaffid_data = delstaffid_tag[0].firstChild.data
    print(delstaffid_data)


    # Create connection with Teaching Database and execute SQL statement/s into Staff.
    with db_connection() as db:
        conx = db.opendb()

        sql1 = "DELETE FROM staff WHERE staff_id = %s"
        val1 = (delstaffid_data, )

        mycursorsql1 = conx.cursor()

        mycursorsql1.execute(sql1, val1)

        conx.commit()

        print(mycursorsql1.rowcount, "Staff record deleted.")


run(host='172.23.20.81', port=80, debug=True)
