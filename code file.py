#including or importing all modules
import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import sqlite3

er=int(input("ENTER 0 FOR SHOWING QR CODE: "))
def func():
    #here we used VideoCapture to start video capturing
    cap = cv2.VideoCapture(0)
    #setting the font on screen frame
    font = cv2.FONT_HERSHEY_PLAIN

    #setting frame size
    cap.set(3,640)
    cap.set(4,480)

    #using string variable to store the decoded qr code
    sr=" "
    decodedObjects=[]
    #running an infinite loop to read the qr code
    while len(decodedObjects)==0:
        _, frame = cap.read()
         #here the qr decode using decode() function and stored all data in decodedobjects
        decodedObjects = pyzbar.decode(frame)
        
       #We are taking variable and using that variable we are printing decoded one 
    for obj in decodedObjects:
        #print("Data", obj.data)
        sr=obj.data.decode('utf-8')
        #print("DECODED QR CODE IS: ",sr)
        cv2.putText(frame, str(obj.data), (50, 50), font, 2, (255, 0, 0), 3)

    cv2.imshow("Frame", frame)
    return sr

#THIS FUNCTION USED TO CONNECT WITH DATABASE AND SEARCHING IN DATABASE
def func2():
    conn=sqlite3.connect('owner.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS qcode ( pass varchar(40))""")
    c.execute("SELECT * FROM qcode ")
    if len(c.fetchall())==0:
        c.execute("INSERT INTO qcode VALUES('qwerty123')")
        c.execute("INSERT INTO qcode VALUES('poiu456')")
        c.execute("INSERT INTO qcode VALUES('asdfgh789')")
        c.execute("INSERT INTO qcode VALUES('hello')") 
    re=func()
    if re=='++NEW++':
        print("SHOW NEW QR CODE!!!!")
        re=func()
        c.execute("INSERT INTO qcode VALUES(?)",(re,))
        print("ADDED NEW QR CODE :)")
        c.execute("SELECT * FROM qcode where pass=?",(re,))
        le=len(c.fetchall())
        conn.commit()
        conn.close() 
        return le

def func3(num):
    conn=sqlite3.connect('owner.db')
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS ju ( pass varchar(20))""")
    c.execute("SELECT * FROM ju ")
    if len(c.fetchall())==0:
        c.execute("INSERT INTO ju VALUES('12345')")
        c.execute("INSERT INTO ju VALUES('112233')")
        c.execute("INSERT INTO ju VALUES('998877')")
    c.execute("SELECT * FROM ju where pass=?",(num,))
    le=len(c.fetchall())
    conn.commit()
    conn.close()
    return le

if er==0:
    while 1<2:
        if func2()>=1:
            print("DOOR UNLOCKED :)")
            break
        else:
            print("TRY AGAIN")
else:
    while 1<2:
        num=input("Enter number lock: ")
        if func3(num)>=1:
            print("DOOR UNLOCKED :)")
            break
        else:
            print("TRY AGAIN")
