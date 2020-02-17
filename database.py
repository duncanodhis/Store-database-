# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:30:06 2019

@author: duncan odhiambo
"""


import sqlite3

def create_table():
    
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE   TABLE  IF NOT EXISTS store(item TEXT,quantity INTEGER,price REAL)")
    
    conn.commit()
    conn.close()

def insert_table(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()
    
def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT *  FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows
def update(quantity,price,item):
     conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity?,price=? WHERE item=?",(quantity,price,item))
    conn.commit()
    conn.close()