#!/usr/bin/env python
# coding: utf-8

# In[17]:


import sqlite3
import geopy.distance
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def home():
    return render_template("index.html")


# conn = sqlite3.connect('test.db')
# conn.execute('''CREATE TABLE COMPANY
#          (slot_id INT PRIMARY KEY     NOT NULL,
#           lattitude          float    NOT NULL,
#          longitude            float     NOT NULL,
#          landmark        VARCHAR(100),
#          area Varchar(100),
#          pincode varchar(100),
#          city varchar(100),
#          state varchar(100),
#          owner varchar(100),
#          status varchar(20),
#          capacity int);''')
# print ("Table created successfully")


# In[68]:

@app.route('/register', methods =["GET", "POST"])
def register():
    if request.method=="POST":
        slotid=request.form.get("slotid")
        lattitude=request.form.get("lattitude")
        longitude=request.form.get("longitude")
        landmark=request.form.get("landmark")
        area=request.form.get("area")
        pincode=request.form.get("pincode")
        city=request.form.get("city")
        state=request.form.get("state")
        owner=request.form.get("owner")
        status=request.form.get("status")
        capacity=request.form.get("capacity")
        conn = sqlite3.connect('test.db')
        conn.execute("INSERT INTO COMPANY (slot_id,lattitude,longitude,landmark,area,pincode,city,state,owner,status,capacity)            values(?,?,?,?,?,?,?,?,?,?,?);",(slotid,lattitude,longitude,landmark,area,pincode,city,state,owner,status,capacity))
        conn.commit()
        return "User Registered"

             


# In[75]:


# conn = sqlite3.connect('test.db')


# cursor=conn.execute("select slot_id,owner from Company")

# for row in cursor:
#    print ("ID = ", row[0])
#    print ("NAME = ", row[1],"\n")
   

# print ("Operation done successfully")


# In[74]:


@app.route('/input', methods =["GET", "POST"])
def input():
    if request.method=="POST":
        lat1=request.form.get("lattitude")
        long1=request.form.get("longitude")
        coord1=(lat1,long1)
        # coord2=(52.406374,16.9251681)
        conn = sqlite3.connect('test.db')
        cursor = conn.execute("SELECT lattitude,longitude from Company where status='available';")
        coord2=[]
        dist=[]

        for row in cursor:
            coord2.append((row[0],row[1]))



        # dist1=geopy.distance.distance(coord1,coord2[1]).km
        for i in (0,len(coord2)-1):
            dist.append(geopy.distance.distance(coord1,coord2[i]).km)
            
        return dist

# In[67]:


@app.route('/remove_user', methods =["GET", "POST"])
def remove_user():
    if request.method=="POST":
        ownername=request.form.get(owner)
        conn = sqlite3.connect('test.db')
        print ("Opened database successfully")

        conn.execute("DELETE from COMPANY where slot_id = ?", ownername)
        conn.commit()
        conn.close()
        return "Operation done successfully"


# In[ ]:




