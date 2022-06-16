import requests
from flask import Flask
from flask import request
from flask import render_template
from flask_cors import CORS
import mysql.connector
from flask import jsonify
import os

try:
    sysdb = mysql.connector.connect(
            host = "db-awan-ticket-system.cej9rpbmgo1q.us-west-2.rds.amazonaws.com", 
            user = "admin",
            password = "Awan123!"
    )
        
    mycursor = sysdb.cursor()
except Exception as e:
    print(e)

app = Flask(__name__)
CORS(app)
app.config["JSON_AS_ASCII"] = False

@app.route('/')
def index():
    return "Larry is a sweet potato."

@app.route('/api/login', methods=["POST"])
def login():
    data = request.get_json()
    account = data["account"]
    password = data["password"]
    # Get Admins info
    query_get_userinfo = "SELECT admin_id, admin_name, admin_role FROM awan_ticket_system.Admins WHERE admin_account=(%s) AND admin_password=(%s);"
    mycursor.execute(query_get_userinfo, (account, password))
    admin_info = mycursor.fetchall()
    # Get Cusotmers info
    query_get_userinfo = "SELECT customer_id, customer_name, customer_level FROM awan_ticket_system.Customers WHERE customer_account=(%s) AND customer_password=(%s);"
    mycursor.execute(query_get_userinfo, (account, password))
    customer_info = mycursor.fetchall()
    
    if admin_info != []:
        #return str(admin_info)
        return jsonify({"data": {
                                    "id": admin_info[0][0],
                                    "name": admin_info[0][1],
                                    "role": admin_info[0][2]
                                }
                        })
    elif customer_info != []:
        return jsonify({"data": {
                                    "id": customer_info[0][0],
                                    "name": customer_info[0][1],
                                    "role": customer_info[0][2]
                                }
                        })
    else:
        return jsonify({"data": {
		                               "error": "無此帳號或密碼"
                                }	
                        })
    
@app.route('/api/tickets/create', methods=["POST"])
def create():
    data = request.get_json()
    customer_id = data["customer_id"]
    service_id = data["service_id"]
    ticket_title = data["ticket_title"]
    ticket_content = data["ticket_content"]
    urgency = data["urgency"]
    admin_id = 1 # Default to admin manager
    try:
      # Insert data into Tickets table
      query_ticket = "INSERT INTO awan_ticket_system.Tickets (admin_id, customer_id, service_id, ticket_title, urgency) VALUES (%s, %s, %s, %s, %s)"
      mycursor.execute(query_ticket, (admin_id, customer_id, service_id, ticket_title, urgency))
      sysdb.commit()
      
      # Get ticket_id from Tickets table
      query_get_info = "SELECT ticket_id FROM awan_ticket_system.Tickets WHERE customer_id=(%s) ORDER BY created_at DESC LIMIT 1"
      mycursor.execute(query_get_info, (customer_id,))
      ticket_info = mycursor.fetchall()
      
      # Insert data into Ticket_Contents table
      query_ticket_content = "INSERT INTO awan_ticket_system.Ticket_Contents (ticket_id, ticket_content, owner) VALUES (%s, %s, %s)"
      mycursor.execute(query_ticket_content, (ticket_info[0][0], ticket_content, "customer"))
      sysdb.commit()
      
      # Insert data into Ticket_Status table
      query_ticket_content = "INSERT INTO awan_ticket_system.Ticket_Status (ticket_id, ticket_status) VALUES (%s, %s)"
      mycursor.execute(query_ticket_content, (ticket_info[0][0], "Not Processed"))
      sysdb.commit()
      
      # Call the Azure AI service
      def azure_lps():
        appId = 'ed9df540-88a5-4c60-9486-f63efbf929f9'
      
        prediction_key = 'b533a315f26e4d559bae183cd68404df'
        
        prediction_endpoint = 'https://larry-tickets.cognitiveservices.azure.com/'
        
        utterance = ticket_title
        
        headers = {}
        
        params ={
            'query': utterance,
            'timezoneOffset': '0',
            'verbose': 'true',
            'show-all-intents': 'true',
            'spellCheck': 'false',
            'staging': 'false',
            'subscription-key': prediction_key
        }
        direc = None
        response = requests.get(f'{prediction_endpoint}luis/prediction/v3.0/apps/{appId}/slots/production/predict', headers=headers, params=params)
        direc = response.json()
        
        prediction_label = ""
        if direc['prediction']['entities'] != {}:
          temp = direc['prediction']['entities']['$instance']
          for key in temp.keys() :
            prediction_label += f" {key}"
        return prediction_label
      
      prediction_label = azure_lps()
      
      # Insert data into Ticket_Tags table
      query_ticket_tag = "INSERT INTO awan_ticket_system.Ticket_Tags (ticket_id, ticket_tags) VALUES(%s, %s)"
      mycursor.execute(query_ticket_tag, (ticket_info[0][0], prediction_label))
      sysdb.commit()
      
      # Call the autoSendEmail API to notify customers
      try:
        # Get the email of whom just created the ticket
        query_email = "SELECT DISTINCT(customer_mail) FROM awan_ticket_system.Tickets INNER JOIN awan_ticket_system.Customers on Tickets.customer_id = Customers.customer_id WHERE Customers.customer_id=(%s)"
        mycursor.execute(query_email, (customer_id,))
        customer_email = mycursor.fetchall()
      
        api_url = "https://zu5i0fjspa.execute-api.us-west-2.amazonaws.com/Post"
        response = requests.post(api_url, json={"toAddress": customer_email[0][0]})
      except Exception as e:
        return str(e)
      
      return jsonify({"data": {
		                               "message": "成功建單",
                                   "ticket_id": ticket_info[0][0]
                              }	
                    })
    except Exception as e:
      return str(e)

@app.route('/api/tickets/assign', methods=["POST"])
def assign():
    try:
      data = request.get_json()
      admin_id = data["admin_id"]
      ticket_id = data["ticket_id"]
      ticket_status = data["ticket_status"]
      
      # Update admin user
      query_ticket_update_admin = "UPDATE awan_ticket_system.Tickets SET admin_id=(%s) WHERE ticket_id=(%s)"
      mycursor.execute(query_ticket_update_admin, (admin_id, ticket_id))
      sysdb.commit()
      
      # Update ticket status
      query_ticket_update_status = "UPDATE awan_ticket_system.Ticket_Status SET ticket_status=(%s) WHERE ticket_id=(%s)"
      mycursor.execute(query_ticket_update_status, (ticket_status, ticket_id))
      sysdb.commit()
      
      return jsonify({"data": {
		                               "message": "成功修改"
                              }	
                    })
    except Exception as e:
      return str(e)
    

@app.route('/api/tickets', methods=["GET"])
def ticket():
    page = int(request.args.get("page"))
    status = request.args.get("status").lower()
    keyword = request.args.get("keyword", None)
    user_id = int(request.args.get("user_id"))
    role = request.args.get("role").lower()
    
    #if status == "all":
      #status_string = ""
    #else:
      #status_string = "WHERE Tickets.{who}_id=(%s) AND ticket_status=(%s)"
      
    def get_pages(who):
      if status == "all":
        query_get_total = f'''SELECT COUNT(*)
                                FROM awan_ticket_system.Tickets
                                INNER JOIN awan_ticket_system.Ticket_Status
                                on Ticket_Status.ticket_id = Tickets.ticket_id
                                INNER JOIN awan_ticket_system.Customers
                                on Customers.customer_id = Tickets.customer_id
                                INNER JOIN awan_ticket_system.Admins
                                on Admins.admin_id = Tickets.admin_id
                            '''
        mycursor.execute(query_get_total)
      else:
        query_get_total = f'''SELECT COUNT(*)
                                FROM awan_ticket_system.Tickets
                                INNER JOIN awan_ticket_system.Ticket_Status
                                on Ticket_Status.ticket_id = Tickets.ticket_id
                                INNER JOIN awan_ticket_system.Customers
                                on Customers.customer_id = Tickets.customer_id
                                INNER JOIN awan_ticket_system.Admins
                                on Admins.admin_id = Tickets.admin_id
                                WHERE Tickets.{who}_id=(%s) AND ticket_status=(%s)
                            '''
        mycursor.execute(query_get_total, (user_id, status))
      result_ticket = mycursor.fetchall()
      total_ticket = result_ticket[0][0]
      total_page = total_ticket//12
      
      if page >= total_page:
        next_page = None
      else:
        next_page = page+1
      
      return [total_page, next_page]
      
    def get_tickets(who):
      if status == "all":
        query_get_ticket = f'''
  							                SELECT Tickets.ticket_id, ticket_title, ticket_status, customer_name, urgency, created_at, Admins.admin_id, admin_name
                                FROM awan_ticket_system.Tickets
                                INNER JOIN awan_ticket_system.Ticket_Status
                                on Ticket_Status.ticket_id = Tickets.ticket_id
                                INNER JOIN awan_ticket_system.Customers
                                on Customers.customer_id = Tickets.customer_id
                                INNER JOIN awan_ticket_system.Admins
                                on Admins.admin_id = Tickets.admin_id
                                LIMIT {(page+1)*12-12},12;
                            '''
        mycursor.execute(query_get_ticket)
      else:
        query_get_ticket = f'''
  							                SELECT Tickets.ticket_id, ticket_title, ticket_status, customer_name, urgency, created_at, Admins.admin_id, admin_name
                                FROM awan_ticket_system.Tickets
                                INNER JOIN awan_ticket_system.Ticket_Status
                                on Ticket_Status.ticket_id = Tickets.ticket_id
                                INNER JOIN awan_ticket_system.Customers
                                on Customers.customer_id = Tickets.customer_id
                                INNER JOIN awan_ticket_system.Admins
                                on Admins.admin_id = Tickets.admin_id
                                WHERE Tickets.{who}_id=(%s) AND ticket_status=(%s)
                                LIMIT {(page+1)*12-12},12;
                            '''
        mycursor.execute(query_get_ticket, (user_id, status))
      result_ticket = mycursor.fetchall()
      data = []
      for ticket in result_ticket:
        # Fetch AI tags info
        query_fetch_ai_tags = '''
                                SELECT ticket_tags 
                                FROM awan_ticket_system.Ticket_Tags 
                                INNER JOIN awan_ticket_system.Tickets
                                ON Tickets.ticket_id = Ticket_Tags.ticket_id
                                WHERE Tickets.ticket_id = (%s)
                            '''
        mycursor.execute(query_fetch_ai_tags, (ticket[0],))
        result_ai_ticket = mycursor.fetchall()
        if result_ai_ticket != []:
          result_ai_ticket = result_ai_ticket[0][0].split()
        else:
          result_ai_ticket = str(result_ai_ticket)
        
        data.append({
                      "ticket_id": ticket[0],
                      "ticket_title": ticket[1],
                      "ticket_status": ticket[2],
                      "customer_name": ticket[3],
                      "urgency": ticket[4],
                      "created_at": ticket[5],
                      "admin_id": ticket[6],
                      "admin_name": ticket[7],
                      "ticket_ai_tags": result_ai_ticket
                    })
      return data
    
    if role != "engineer" and role != "engineer supervisor": # Customers' perspectives
      page_info = get_pages("customer")
      data = get_tickets("customer")
      return {"data": data, "total_page": page_info[0], "next_page": page_info[1]}
    else: # Engineers' perspectives
      page_info = get_pages("admin")
      data = get_tickets("admin")
      return {"data": data, "total_page": page_info[0], "next_page": page_info[1]}

@app.route('/api/tickets/<int:ticket_id>')
def tickets(ticket_id):
    query_get_ticket = f'''
							                SELECT Tickets.ticket_id, ticket_title, ticket_status, customer_name, urgency, created_at, Admins.admin_id, admin_name
                              FROM awan_ticket_system.Tickets
                              INNER JOIN awan_ticket_system.Ticket_Status
                              on Ticket_Status.ticket_id = Tickets.ticket_id
                              INNER JOIN awan_ticket_system.Customers
                              on Customers.customer_id = Tickets.customer_id
                              INNER JOIN awan_ticket_system.Admins
                              on Admins.admin_id = Tickets.admin_id
                              WHERE Tickets.ticket_id=(%s);
                          '''
    mycursor.execute(query_get_ticket, (ticket_id,))
    result_ticket = mycursor.fetchall()
    
    # Fetch AI tags info
    query_fetch_ai_tags = '''
                            SELECT ticket_tags 
                            FROM awan_ticket_system.Ticket_Tags 
                            INNER JOIN awan_ticket_system.Tickets
                            ON Tickets.ticket_id = Ticket_Tags.ticket_id
                            WHERE Tickets.ticket_id = (%s)
                        '''
    mycursor.execute(query_fetch_ai_tags, (result_ticket[0][0],))
    result_ai_ticket = mycursor.fetchall()
    
    data = {
              "ticket_id": result_ticket[0][0],
              "ticket_title": result_ticket[0][1],
              "ticket_status": result_ticket[0][2],
              "customer_name": result_ticket[0][3],
              "urgency": result_ticket[0][4],
              "created_at": result_ticket[0][5],
              "admin_id": result_ticket[0][6],
              "admin_name": result_ticket[0][7],
              "ticket_ai_tags": str(result_ai_ticket[0][0]).split()
           }
    return {"data": data}
    
@app.route('/api/tickets/contents', methods=["POST"])
def create_content():
  try:
    data = request.get_json()
    ticket_id = data["ticket_id"]
    ticket_content = data["ticket_content"]
    owner = data["owner"]
    
    # Insert data into Ticket_Contents table
    query_ticket_content = "INSERT INTO awan_ticket_system.Ticket_Contents (ticket_id, ticket_content, owner) VALUES (%s, %s, %s)"
    mycursor.execute(query_ticket_content, (ticket_id, ticket_content, owner))
    sysdb.commit()
    
    return {
              "message": "Success"
           }
  except Exception as e:
    return str(e)

@app.route('/api/tickets/contents', methods=["GET"])
def content():
    ticket_id = int(request.args.get("ticket_id"))
    try:
      query_ticket_content = "SELECT ticket_content, owner, created_at FROM awan_ticket_system.Ticket_Contents WHERE ticket_id=(%s)"
      mycursor.execute(query_ticket_content, (ticket_id, ))
      ticket_content = mycursor.fetchall()
      data = []
      for content in ticket_content:
        data.append({
                      "ticket_content": content[0],
                      "owner": content[1],
                      "image": [],
                      "created_at": content[2]
                    })
      return {"data": data}
    except Exception as e:
      return str(e)
      
@app.route('/api/users', methods=["GET"])
def get_users():
    role = request.args.get("role")
    try:
      query_users = "SELECT admin_id, admin_name FROM awan_ticket_system.Admins WHERE admin_role=(%s)"
      mycursor.execute(query_users, (role, ))
      users = mycursor.fetchall()
      
      data = []
      for user in users:
        data.append({
                      "admin_id": user[0],
                      "admin_name": user[1]
                   })
      
      return {"data": data}
    except Exception as e:
      return str(e)

if __name__ == '__main__':
    app.run()
