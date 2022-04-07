import pandas
import mysql.connector

sysdb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
)

mycursor = sysdb.cursor()

# insert data in Admins table
pd = pandas.read_csv("fake-data/admin.csv")
admin_id = list(pd["admin_id"])
admin_name = list(pd["admin_name"])
admin_role = list(pd["admin_role"])
admin_account = list(pd["admin_account"])
admin_password = list(pd["admin_password"])

for id, name, role, account, password in zip(admin_id, admin_name, admin_role, admin_account, admin_password):
    query_admin = '''
                        INSERT INTO awan_ticket_system.Admins(admin_id, admin_name, admin_role, admin_account, admin_password)
                        VALUES (%s, %s, %s, %s, %s)
                '''
    mycursor.execute(query_admin, (id, name, role, account, password))
    sysdb.commit()

# insert data in Customers table
pd = pandas.read_csv("fake-data/customer.csv")
customer_id = list(pd["customer_id"])
customer_name = list(pd["customer_name"])
customer_level = list(pd["customer_level"])
customer_mail = list(pd["customer_mail"])
customer_company = list(pd["customer_company"])
customer_account = list(pd["customer_account"])
customer_password = list(pd["customer_password"])

for id, name, level, mail, company, account, password in zip(customer_id, customer_name, customer_level, customer_mail, customer_company, customer_account, customer_password):
    query_admin = '''
                        INSERT INTO awan_ticket_system.Customers(customer_id, customer_name, customer_level, customer_mail, customer_company, customer_account, customer_password)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                '''
    mycursor.execute(query_admin, (id, name, level, mail, company, account, password))
    sysdb.commit()
    
# insert data in Services table
pd = pandas.read_csv("fake-data/service.csv")
service_id = list(pd["service_id"])
service_type = list(pd["service_type"])
service_name = list(pd["service_name"])

for id, type, name in zip(service_id, service_type, service_name):
    query_admin = '''
                        INSERT INTO awan_ticket_system.Services(service_id, service_type, service_name)
                        VALUES (%s, %s, %s)
                '''
    mycursor.execute(query_admin, (id, type, name))
    sysdb.commit()

# insert data in Tickets table
pd = pandas.read_csv("fake-data/ticket.csv")
ticket_id = list(pd["ticket_id"])
admin_id = list(pd["admin_id"])
customer_id = list(pd["customer_id"])
service_id = list(pd["service_id"])
ticket_title = list(pd["ticket_title"])

for tid, aid, cid, sid, tt in zip(ticket_id, admin_id, customer_id, service_id, ticket_title):
    query_admin = '''
                        INSERT INTO awan_ticket_system.Tickets(ticket_id, admin_id, customer_id, service_id, ticket_title)
                        VALUES (%s, %s, %s, %s, %s)
                '''
    mycursor.execute(query_admin, (tid, aid, cid, sid, tt))
    sysdb.commit()
    
# insert data in Ticket_Status
pd = pandas.read_csv("fake-data/ticket_status.csv")
ticket_id = list(pd["ticket_id"])
ticket_status = list(pd["ticket_status"])

for tid, ts in zip(ticket_id, ticket_status):
    query_admin = '''
                        INSERT INTO awan_ticket_system.Ticket_Status(ticket_id, ticket_status)
                        VALUES (%s, %s)
                '''
    mycursor.execute(query_admin, (tid, ts))
    sysdb.commit()
    
# insert data in Ticket_Contents
pd = pandas.read_csv("fake-data/ticket_content.csv")
content_id = list(pd["content_id"])
ticket_id = list(pd["ticket_id"])
ticket_content = list(pd["ticket_content"])

for cid, tid, tc in zip(content_id, ticket_id, ticket_content):
    query_admin = '''
                        INSERT INTO awan_ticket_system.Ticket_Contents(content_id, ticket_id, ticket_content)
                        VALUES (%s, %s, %s)
                '''
    mycursor.execute(query_admin, (cid, tid, tc))
    sysdb.commit()
    
# insert data in Ticket_Images
pd = pandas.read_csv("fake-data/ticket_image.csv")
image_id = list(pd["image_id"])
content_id = list(pd["content_id"])
image_url = list(pd["image_url"])

for ii, ci, iu in zip(image_id, content_id, image_url):
    query_admin = '''
                        INSERT INTO awan_ticket_system.Ticket_Images(image_id, content_id, image_url)
                        VALUES (%s, %s, %s)
                '''
    mycursor.execute(query_admin, (ii, ci, iu))
    sysdb.commit()
