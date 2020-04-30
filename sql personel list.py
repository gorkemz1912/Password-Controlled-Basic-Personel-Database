import sqlite3 as sql
import time

psw = 0
tryagain = 0
vt = sql.connect("personel_list.nmtl")

im = vt.cursor()
while(psw == 0):
    im.execute("""CREATE TABLE IF NOT EXISTS password(nickname , password)""")
    if(tryagain == 0):
        logorsign = input("Type 'login' to login\nType 'sign' to sign up:  ")
    else:
        pass
    if(logorsign == 'sign' or tryagain == 1):
        nickname = input("Nickname: ")
        password1 = input("Password: ")
        password2 = input("Password again: ")
        if(password1 == password2):
            psw = 0
        else:
            print("passwords are incompatible. Try Again")
            psw = 0
            tryagain = 1
        im.execute("""INSERT INTO password VALUES(? , ? )""" , (nickname , password1))
        vt.commit()
        logorsign == ' '
        nickname = ' '
        password1 = ' '
        password2 = ' '
    if(logorsign == 'login'):
        nickname = input("Nickname: ")
        password = input("Password: ")
        im.execute("""SELECT * FROM password""")
        data1920 = im.fetchall()
        for i in range(len(data1920)):
            im.execute("""SELECT * FROM password""")
            data1920 = im.fetchall()
            if(data1920[i][0] == nickname and data1920[i][1] == password):
                psw = 1
                print("TRUE PASSWORD")
                break
            if(data1920[i][0] == nickname and data1920[i][1] != password):
                psw = 0
                print("WRONG PASSWORD")
            if(data1920[i][0] != nickname and i == len(data1920)):
                print("User Not Found")
                

im.execute("CREATE TABLE IF NOT EXISTS Personel( isim , soyisim , memleket , email , telefon_no , gorev)")
print("Personel Database v1.0 ")


while(psw == 1):
    x = 1 
    if(x == 1):
        choose = input("Type 'add' to add data \nType 'read' to read datas:  ")

    while(choose == 'add'):
        print("    ")
        print("---------------")
        print("   ")
        print("Type esc to exit")
        name = input("Name: ")
        if(name == 'esc'):
            choose = ' '
            break
        surname = input("Surname: ")
        if(surname == 'esc'):
            choose = ' '
            break
        place = input("Place of Birth: ")
        if(place == 'esc'):
            choose = ' '
            break
        
        email = input("E-Mail Adress: ")
        if(email == 'esc'):
            choose = ' '
            break
        tel = input("Telephone Number: ")
        if(tel == 'esc'):
            choose = ' '
            break
        gorev = input("Job Position: ")
        if(gorev == 'esc'):
            choose = ' '
            break
        
        data = [name , surname , place , email , tel , gorev]
        print("Succesfully Saved")
        print("---------------")
        im.execute("""INSERT INTO personel VALUES
                    (?, ?, ? , ? , ? , ?)""", (name , surname , place , email , tel , gorev))
        vt.commit()
        x = 0

    if(x == 0):
        choose = input("Type 'add' to add data \nType 'read' to read datas:  ")
    if(choose == 'read'):
        im.execute("""SELECT * FROM Personel""")
        datass = im.fetchall()
        print(datass)   
        print("")
        print("---------------")
        print("")
        print("---------------")
        
        
        x = 1





vt.close()

