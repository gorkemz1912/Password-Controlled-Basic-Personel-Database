import sqlite3 as sql #sqlite kütüphanesi koda eklendi
psw = 0 
tryagain = 0
vt = sql.connect("personel_list1.db") #kodumuzu personel_list.db isimli veritabanına (db) bağladık. Eğer bu isimde bir db yoksa oluşturulur. 
while 1:
    im = vt.cursor() #imlecimizi im ismine atadık. fonksiyonları im kısaltması ile çağıracağız. 
    while(psw == 0):
        im.execute("""CREATE TABLE IF NOT EXISTS password(nickname , password)""") #eğer halihazırda yoksa nickname ve password bilgilerini içeren bir tablo oluturduk. 
        if(tryagain == 0):
            logorsign = input("Type 'login' to login\nType 'sign' to sign up:  ") #yeni bir hesapla mı giriş yapılacak halihazırda bulunan bir hesapla mı giriş yapılacak kullanıcıya soruldu
        else:
            pass
        if(logorsign == 'sign' or tryagain == 1 or logorsign == 'sig'): #eğer yeni hesap oluşturulacaksa...
            nickname = input("Nickname: ") #verileri alıyoruz
            password1 = input("Password: ")
            password2 = input("Password again: ") 
            if(password1 == password2): 
                psw = 0
            else:
                print("passwords are incompatible. Try Again") #eğer ard arda girilen iki şifre farklıysa kullanıcıyı tekrar hesap oluşturma kısmına gönderir. 
                psw = 0
                tryagain = 1
            im.execute("""INSERT INTO password VALUES(? , ? )""" , (nickname , password1)) #gelen nickname ve password verileri tabloya işlenir. 
            vt.commit() #hafızadaki veriyi veritabanına kaydeder. 
            logorsign == ' ' #verileri db'ye kaydettiğimiz için eskilerini siliyorum. hem daha sonra kullanmak gerekebilir temiz dursunlar.
            nickname = ' '
            password1 = ' '
            password2 = ' '
        if(logorsign == 'login' or logorsign == 'log'): #eğer giriş yapılacaksa...
            nickname = input("Nickname: ")
            password = input("Password: ")
            im.execute("""SELECT * FROM password""") #password tablosundan veriler çekilir
            data = im.fetchall() #veriler data isimli list değişkenine kaydedildi                
            for i in range(len(data)): #datayı db'deki her satırla tek tek karşılaştırıyorum
                if(data[i][0] == nickname and data[i][1] == password):
                    psw = 1
                    print("TRUE PASSWORD")
                    break
                if(data[i][0] == nickname and data[i][1] != password):
                    psw = 0
                    print("WRONG PASSWORD")
                if(data[i][0] != nickname and i == len(data)):
                    print("User Not Found")        

    im.execute("CREATE TABLE IF NOT EXISTS Personel(isim , soyisim , memleket , email , telefon_no , gorev)") #(eğer yoksa)Personel isimli tablo oluşturuldu.
    print("Personel Database v1.1 ")


    while(psw == 1):
        x = 1 
        if(x == 1):
            choose = input("Type 'add' to add data \nType 'read' to read datas: \nType 'update' to update data: \nType 'esc' to exit: ")

        while(choose == 'add'):#veri işleme yapılacaksa...
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
            
            print("Succesfully Saved")
            print("---------------")
            im.execute("""INSERT INTO personel VALUES    (?, ?, ? , ? , ? , ?)""", (name , surname , place , email , tel , gorev))
            vt.commit()
            x = 0

        if(x == 0):
            choose = input("Type 'add' to add data \nType 'read' to read datas: \nType esc to exit: ")
        if(choose == 'read'):
            im.execute("""SELECT * FROM Personel""")
            datass = im.fetchall()
            print("-*-*-*-*-*-*-*-*-*-*-*-*-*\n-*-*-*-*-*-*-*-*-*-*-*-*-*\n")
            
            
            for l in range(len(datass)):
                print("Personal" , l+1)
                print("Name Surname: " , datass[l][0] , datass[l][1])
                print("Place of Birth: " , datass[l][2])
                print("E-Mail Adress: " , datass[l][3])
                print("GSM: " , datass[l][4])
                print("Job Position: " , datass[l][5])
                print("-----------")
 
            print("")
            print("---------------")
            print("")
            print("---------------")
        elif(choose == 'esc'):
            psw = 0
            break
        elif(choose == 'update'):
            name_change = input("Enter the name of the employee whose data you want to update: ")
            new_name = input("Enter the new name: ")
            new_surname = input("Enter the new surname: ")
            new_nationality = input("Enter the new place of birth: ")
            new_email = input("Enter the new E-mail adress: ")
            new_tel = input("Enter the new GSM: ")
            new_job = input("Enter the new position: ")
            im.execute("""Update Personel set gorev = ? where isim = ?""" , (new_job , name_change))
            im.execute("""Update Personel set telefon_no = ? where isim = ?""" , (new_tel , name_change))
            im.execute("""Update Personel set email = ? where isim = ?""" , (new_email , name_change))
            im.execute("""Update Personel set memleket = ? where isim = ?""" , (new_nationality , name_change))
            im.execute("""Update Personel set soyisim = ? where isim = ?""" , (new_surname , name_change))
            im.execute("""Update Personel set isim = ? where isim = ?""" , (new_name , name_change))
            vt.commit()


        else:
            print("")
            print("---------------")
            print("")
            print("---------------")
            print("invalid request. Please try again.")
            print("---------------")
            pass  
        x = 1
    





vt.close()
