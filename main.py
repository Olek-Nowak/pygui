from tkinter import *
import tkinter.messagebox as msg
import mysql.connector as mysql

mysql_pass = "Ksiegarnia1"

# landing page
def landing():
    def login():
        u = username.get()
        p = password.get()
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select `idUzytkownik`,`Typ użytkownika_idTyp użytkownika`,`adres_email` from uzytkownik where nazwa_uzytkownika=%(user)s and haslo=%(pass)s;"
        cursor.execute(stmt, {'user': u, 'pass': p})
        out = cursor.fetchone()
        if out == None :
            msg.showerror("Błąd","Nie znaleziono użytkownika")
        else :
            connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
            cursor = connection.cursor()
            stmt = "select k.idKlient, k.imie_klienta, k.`nazwisko klienta` from mydb.uzytkownik as u left join mydb.klient as k on u.idUzytkownik=k.Uzytkownik_idUzytkownik where u.idUzytkownik=%(id)s;"
            cursor.execute(stmt, {'id': out[0]})
            klient = cursor.fetchone()
            if klient is None :
                # active_user = (id, username, typ, password, email, id_klient, imie, nazwisko)
                active_user = (out[0], u, out[1], p, out[2], '0', '', '')
            else :
                active_user = (out[0], u, out[1], p, out[2], klient[0], klient[1], klient[2])
            redraw(active_user)
    root.geometry("400x300")
    root.title("Księgarnia GUI - logowanie")

    label1 = Label(root,text="Witamy w systemie Księgarnia GUI v1.0",font=('bold', 14))
    label1.place(x=35,y=80)

    label2 = Label(root,text="Nazwa",font=('bold', 10))
    label2.place(x=30,y=150)

    username = Entry(root)
    username.place(x=80,y=150)

    label3 = Label(root,text="Hasło",font=('bold', 10))
    label3.place(x=30,y=180)

    password = Entry(root)
    password.place(x=80,y=180)

    b_login = Button(root, text="Zaloguj",font=('bold',10),bg="white",command=login)
    b_login.place(x=30,y=210)

    b_open_register = Button(root, text="Nie jesteś zarejestrowany?",font=('bold',10),bg="white",command=open_register)
    b_open_register.place(x=60,y=250)


# moderator window
def change_moderator(user):
    def delete():
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "delete from uzytkownik where idUzytkownik=%(id)s;"
        cursor.execute(stmt, {'id': user[0]})
        cursor.execute("commit")
        new_user = ('', '', '', '', '', '', '', '')
        redraw(new_user)
    def search():
        open_search(c)
    def reviews():
        open_reviews()
    def change():
        temp = 0

    c = []

    root.geometry("400x400")
    root.title("Księgarnia GUI - moderator")

    label1 = Label(root,text="Witamy w panelu moderatora",font=('bold', 14))
    label1.place(x=60,y=80)

    label2a = Label(root,text="Nazwa użytkownika",font=('bold', 10))
    label2a.place(x=40,y=110)
    label2b = Label(root,text=str(user[1]),font=('bold', 10))
    label2b.place(x=180,y=110)
    label3a = Label(root,text="Hasło",font=('bold', 10))
    label3a.place(x=40,y=130)
    label3b = Label(root,text=str(user[3]),font=('bold', 10))
    label3b.place(x=180,y=130)
    label4a = Label(root,text="Email",font=('bold', 10))
    label4a.place(x=40,y=150)
    label4b = Label(root,text=str(user[4]),font=('bold', 10))
    label4b.place(x=180,y=150)

    b_delete = Button(root, text="Usuń konto",font=('bold',10),bg="white",command=delete)
    b_delete.place(x=60,y=180)

    b_search = Button(root, text="Szukaj",font=('bold',10),bg="white",command=search)
    b_search.place(x=60,y=210)

    b_review = Button(root, text="Najnowsze recenzje",font=('bold',10),bg="white",command=reviews)
    b_review.place(x=60,y=240)


# user window
def change_user(user):
    def delete():
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "delete from uzytkownik where idUzytkownik=%(id)s;"
        cursor.execute(stmt, {'id': user[0]})
        cursor.execute("commit")
        new_user = ('', '', '', '', '', '', '', '')
        redraw(new_user)
    def search():
        open_search(c)
    def cart():
        open_cart(user, c)
    def orders():
        open_order_history(user)
    def change():
        temp = 0
    
    # normally would load cart state from database, but no such functionality
    c = []

    root.geometry("400x400")
    root.title("Księgarnia GUI - klient")

    label1 = Label(root,text="Witamy w panelu klienta",font=('bold', 14))
    label1.place(x=60,y=80)

    label2a = Label(root,text="Nazwa użytkownika",font=('bold', 10))
    label2a.place(x=40,y=110)
    label2b = Label(root,text=str(user[1]),font=('bold', 10))
    label2b.place(x=180,y=110)
    label3a = Label(root,text="Hasło",font=('bold', 10))
    label3a.place(x=40,y=130)
    label3b = Label(root,text=str(user[3]),font=('bold', 10))
    label3b.place(x=180,y=130)
    label4a = Label(root,text="Email",font=('bold', 10))
    label4a.place(x=40,y=150)
    label4b = Label(root,text=str(user[4]),font=('bold', 10))
    label4b.place(x=180,y=150)

    b_delete = Button(root, text="Usuń konto",font=('bold',10),bg="white",command=delete)
    b_delete.place(x=60,y=180)

    b_search = Button(root, text="Szukaj",font=('bold',10),bg="white",command=search)
    b_search.place(x=60,y=210)

    b_cart = Button(root, text="Koszyk",font=('bold',10),bg="white",command=cart)
    b_cart.place(x=60,y=240)

    b_orders = Button(root, text="Historia zamówień",font=('bold',10),bg="white",command=orders)
    b_orders.place(x=60,y=270)
    

# search product window
def open_search(c):
    # for listbox to be clickable, need to define and bind new event
    def select(event):
        cs = results_list.curselection()
        selection = results_list.get(cs)
        selection_id = selection.split()[0]
        open_product(selection_id, c)
    def pull_results():
        results_list.delete(0, END)
        string = searchbox.get()
        # splitting into substrings can compare to all inputs but can return multiple same results
        #substring = string.split()
        out = []
        #for s in substring :
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select * from produkt where nazwa_produktu like '%"+ string +"%';"
        cursor.execute(stmt)
        out = cursor.fetchall()
        for row in out :
            res = str(row[0]) + ' ' + str(row[1]) + '       Kup teraz: ' + str(row[2]) + ' zł'
            results_list.insert(results_list.size()+1, res)

    # TODO: add more info
    search = Toplevel()
    search.geometry("400x300")
    search.title("Księgarnia GUI - wyszukiwanie")

    searchbox = Entry(search)
    searchbox.place(x=30,y=80)

    b_search = Button(search, text="Szukaj",font=('bold',10),bg="white",command=pull_results)
    b_search.place(x=170,y=75)

    results_list = Listbox(search, width = 50)
    results_list.place(x=50,y=120)
    results_list.bind('<Double-1>', select)

# cart window
def open_cart(user, c):
    def select(event):
        cs = cart_list.curselection()
        selection = cart_list.get(cs)
        selection_id = selection.split()[0]
        open_product(selection_id, c)
    def order() :
        open_new_order(user, c)
    def remove() :
        cs = cart_list.curselection()
        selection = cart_list.get(cs)
        selection_id = selection.split()[0]
        c.remove(selection_id)
        refresh()
    def refresh():
        cart_list.delete(0, END)
        # out = (id, nazwa, cena, zakup, kat, typ)
        out = [('','','','','','')]
        for item in c :
            connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
            cursor = connection.cursor()
            stmt = "select * from produkt where idProdukt=%(id)s;"
            cursor.execute(stmt, {'id': item})
            out += cursor.fetchall()
        suma = 0
        out.remove(('','','','','',''))
        for row in out :
            suma += int(row[2])
            res = str(row[0]) + ' ' + str(row[1]) + '       ' + str(row[2]) + ' zł'
            cart_list.insert(cart_list.size()+1, res)
        label1.config(text="Łącznie: " + str(suma) + "zł")
    cart = Toplevel()
    cart.geometry("400x300")
    cart.title("Księgarnia GUI - mój koszyk")

    cart_list = Listbox(cart, width = 50)
    cart_list.place(x=50,y=50)
    cart_list.bind('<Double-1>', select)

    label1 = Label(cart,font=('bold', 10))
    label1.place(x=50,y=220)

    b_order = Button(cart, text="Zamów teraz",font=('bold',10),bg="white",command=order)
    b_order.place(x=145,y=215)

    b_order = Button(cart, text="Usuń z koszyka",font=('bold',10),bg="white",command=remove)
    b_order.place(x=250,y=215)

    refresh()

# previous orders window
def open_order_history(user):
    def select(event):
        cs = order_list.curselection()
        selection = order_list.get(cs)
        selection_id = selection.split()[0]
        open_order(selection_id, user)
    def refresh() :
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select z.idZakup, z.czy_zrealizowany, k.idKlient, count(p.idProdukt), sum(p.cena_produktu) from mydb.zakup as z left join mydb.klient as k on z.Klient_idKlient=k.idKlient left join mydb.produkt as p on z.idZakup=p.Zakup_idZakup group by z.idZakup, z.czy_zrealizowany, k.idKlient having k.idKlient=%(id)s"
        cursor.execute(stmt, {'id': user[5]})
        rev = cursor.fetchall()
        for r in rev :
            temp = str(r[0]) + "    "
            if int(r[1]) == 1 :
                temp += "Zrealizowane"
            else :
                temp += "W trakcie"
            temp += "   Ilość produktów: " + str(r[3])
            temp += "   Łączna cena: " + str(r[4])
            order_list.insert(order_list.size()+1, temp)
    orders = Toplevel()
    orders.geometry("400x300")
    orders.title("Księgarnia GUI - historia zamówień")

    order_list = Listbox(orders, width=100)
    order_list.place(x=40,y=50)
    order_list.bind('<Double-1>', select)

    refresh()

# single order product list window
def open_order(id, user):
    def check_repeat_review(order_id, client_id, product_id):
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select idRecenzja from recenzja where Produkt_Zakup_idZakup=%(o)s and Klient_idKlient=%(c)s and Produkt_idProdukt=%(p)s;"
        cursor.execute(stmt, {'o': order_id,'c': client_id,'p': product_id})
        out = cursor.fetchone()
        if out is None :
            return 1
        else :
            return 0
    def new_id_review():
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select idRecenzja from recenzja order by idRecenzja desc limit 1"
        cursor.execute(stmt)
        out = cursor.fetchone()
        if out is None :
            return 1
        else :
            return int(out[0]) + 1
    # looks dumb but i dont think you can edit buttons automatically / by indexing
    def set_1(stars):
        b_1.config(bg="black")
        b_2.config(bg="white")
        b_3.config(bg="white")
        b_4.config(bg="white")
        b_5.config(bg="white")
        stars[0] = 1
    def set_2(stars):
        b_1.config(bg="black")
        b_2.config(bg="black")
        b_3.config(bg="white")
        b_4.config(bg="white")
        b_5.config(bg="white")
        stars[0] = 2
    def set_3(stars):
        b_1.config(bg="black")
        b_2.config(bg="black")
        b_3.config(bg="black")
        b_4.config(bg="white")
        b_5.config(bg="white")
        stars[0] = 3
    def set_4(stars):
        b_1.config(bg="black")
        b_2.config(bg="black")
        b_3.config(bg="black")
        b_4.config(bg="black")
        b_5.config(bg="white")
        stars[0] = 4
    def set_5(stars):
        b_1.config(bg="black")
        b_2.config(bg="black")
        b_3.config(bg="black")
        b_4.config(bg="black")
        b_5.config(bg="black")
        stars[0] = 5
    def select(event):
        cs = item_list.curselection()
        selection = item_list.get(cs)
        selection_id = selection.split()[0]
        open_product(selection_id)
    def add_review(stars, all_info, user):
        cs = item_list.curselection()
        selection = item_list.get(cs)
        id_product = selection.split()[0]
        temp = all_info[0]
        id_order = temp[0]
        if check_repeat_review(id_order, user[5], id_product) :
            id = new_id_review()
            text = comment.get()
            connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
            cursor = connection.cursor()
            stmt = "insert into recenzja values (%(id)s,%(id_p)s,%(id_o)s,%(id_c)s,%(com)s,%(star)s);"
            cursor.execute(stmt, {'id': str(id),'id_p': str(id_product),'id_o': str(id_order),'id_c': str(user[5]),'com': text,'star': str(stars[0]),})
            cursor.execute("commit")
            msg.showinfo("Dodano recenzję","Poprawnie dodano recenzję. Dziękujemy!")
        else :
            msg.showerror("Błąd","Nie można dodawać wielu recenzji do pojedynczego zakupu danego produktu")

    connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
    cursor = connection.cursor()
    stmt = "select z.idZakup, z.czy_zrealizowany, p.idProdukt, p.nazwa_produktu, p.cena_produktu from mydb.zakup as z left join mydb.produkt as p on z.idZakup=p.Zakup_idZakup where z.idZakup=%(id)s;"
    cursor.execute(stmt, {'id': id})
    out = cursor.fetchall()

    order = Toplevel()
    order.geometry("800x600")
    order.title("Księgarnia GUI - przegląd zamówienia")

    label1 = Label(order, font=('bold',12))
    label1.place(x=40,y=50)

    label2 = Label(order, font=('bold',10))
    label2.place(x=190,y=50)

    item_list = Listbox(order, width=100)
    item_list.place(x=40,y=80)
    item_list.bind('<Double-1>', select)

    label3 = Label(order, font=('bold',10))
    label3.place(x=50,y=250)

    suma = 0
    for i in out :
        label1.config(text="Zamówienie nr. " + str(i[0]))
        temp = str(i[2]) + "    " + str(i[3]) + "    " + str(i[4]) + "zł"
        if int(i[1]) == 1 :
            label2.config(text="Zrealizowane")
        else :
            label2.config(text="W trakcie")
        suma += int(i[4])
        item_list.insert(item_list.size()+1, temp)
    label3.config(text="Łącznie: " + str(suma) + "zł")

    stars = [0]

    label4 = Label(order, text="Dodaj recenzję tego produktu: ", font=('bold',10))
    label4.place(x=50,y=280)

    b_1 = Button(order, text='\u2B50',font=('bold',10),bg="white", width=1,command= lambda: set_1(stars))
    b_1.place(x=50,y=310)
    b_2 = Button(order, text='\u2B50',font=('bold',10),bg="white", width=1,command= lambda: set_2(stars))
    b_2.place(x=70,y=310)
    b_3 = Button(order, text='\u2B50',font=('bold',10),bg="white", width=1,command= lambda: set_3(stars))
    b_3.place(x=90,y=310)
    b_4 = Button(order, text='\u2B50',font=('bold',10),bg="white", width=1,command= lambda: set_4(stars))
    b_4.place(x=110,y=310)
    b_5 = Button(order, text='\u2B50',font=('bold',10),bg="white", width=1,command= lambda: set_5(stars))
    b_5.place(x=130,y=310)

    comment = Entry(order, width=100)
    comment.place(x=50,y=350)

    all_info = out
    b_add = Button(order, text="Dodaj recenzję",font=('bold',10),bg="white", width=10,command= lambda: add_review(stars, all_info, user))
    b_add.place(x=130,y=380)

# new order address form window - probably the biggest and messiest one
def open_new_order(user, c):
    def new_id_client():
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select idKlient from klient order by idKlient desc limit 1"
        cursor.execute(stmt)
        out = cursor.fetchone()
        if out is None :
            return 1
        else :
            return int(out[0]) + 1
    def new_id_order():
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select idZakup from zakup order by idZakup desc limit 1"
        cursor.execute(stmt)
        out = cursor.fetchone()
        if out is None :
            return 1
        else :
            return int(out[0]) + 1
    def new_id_address():
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select idadres_klienta from adres_klienta order by idadres_klienta desc limit 1"
        cursor.execute(stmt)
        out = cursor.fetchone()
        if out is None :
            return 1
        else :
            return int(out[0]) + 1
    def load_client(flags):
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select k.imie_klienta, k.`nazwisko klienta`, a.ulica, a.miasto, a.kod_pocztowy from mydb.klient as k left join adres_klienta as a on k.idKlient=a.Klient_idKlient where idKlient = %(id)s limit 1"
        cursor.execute(stmt, {'id': str(user[5])})
        out = cursor.fetchone()

        # TODO: fix streetnames - only work for single-words
        if out[2] == '' or out[2] == None :
            street.delete(0, END)
            street.insert(0, "None")
            address.delete(0, END)
            address.insert(0, "None")
        else :
            a = out[2].split()
            street.delete(0, END)
            street.insert(0, str(a[0]))
            address.delete(0, END)
            address.insert(0, str(a[1]))

        first_name.delete(0, END)
        first_name.insert(0, str(out[0]))
        surname.delete(0, END)
        surname.insert(0, str(out[1]))

        zip.delete(0, END)
        zip.insert(0, str(out[4]))
        city.delete(0, END)
        city.insert(0, str(out[3]))

        if city.get() == '' or city.get() == "None" :
            # no idea how to pass by reference in python, for some reason lists work?
            flags.clear()
            flags.append('0')
            flags.append('1')
    def add_client(f, s):
        id = new_id_client()
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "insert into klient values (%(id)s,%(fn)s,%(sn)s,%(usr)s);"
        cursor.execute(stmt, {'id_ad': str(id),'fn': f,'sn': s,'usr': user[0]})
        cursor.execute("commit")
        user[5] = id
        user[6] = f
        user[7] = s
    def add_address(a):
        id = new_id_address()
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "insert into adres_klienta values (%(id_ad)s,%(id_kl)s,%(c)s,%(z)s,%(s)s);"
        cursor.execute(stmt, {'id_ad': str(id),'id_kl': str(user[5]),'c': str(a[2]),'z': str(a[3]),'s': str(str(a[0])+" "+str(a[1]))})
        cursor.execute("commit")
    def add_order(flags, cart):
        fn = first_name.get()
        sn = surname.get()
        add = [street.get(), address.get(), city.get(), zip.get()]
        if fn == "None" or sn == "None" or add[0] == "None" or add[1] == "None" or add[2] == "None" or add[3] == "None" :
            msg.showerror("Błąd","Wszystkie pola wymagane")
        elif len(fn) == 0 or len(sn) == 0 or len(add[0]) == 0 or len(add[1]) == 0 or len(add[2]) == 0 or len(add[3]) == 0 :
            msg.showerror("Błąd","Wszystkie pola wymagane")
        else :
            # insert into client
            if flags[0] == '1' :
                add_client(fn, sn)
            # insert into zakup
            i = new_id_order()
            connection1 = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
            cursor1 = connection1.cursor()
            stmt = "insert into zakup values (%(id)s,'0',%(user)s);"
            cursor1.execute(stmt, {'id': str(i),'user': str(user[5])})
            cursor1.execute("commit")
            # insert into adres
            if flags[1] == '1' :
                add_address(add)
            cart.clear()
            msg.showinfo("Status","Zamówienie przyjęte do realizacji")
    buy = Toplevel()
    buy.geometry("400x400")
    buy.title("Księgarnia GUI - składanie zamówienia")
    flags = [0, 0]

    label1 = Label(buy,text="Imię",font=('bold', 10))
    label1.place(x=30,y=50)

    first_name = Entry(buy)
    first_name.place(x=120,y=50)

    label2 = Label(buy,text="Nazwisko",font=('bold', 10))
    label2.place(x=30,y=90)

    surname = Entry(buy)
    surname.place(x=120,y=90)

    label3 = Label(buy,text="Ulica",font=('bold', 10))
    label3.place(x=30,y=130)

    street = Entry(buy)
    street.place(x=120,y=130)

    label4 = Label(buy,text="Nr. lokalu",font=('bold', 10))
    label4.place(x=30,y=170)

    address = Entry(buy)
    address.place(x=120,y=170)

    label5 = Label(buy,text="Kod pocztowy",font=('bold', 10))
    label5.place(x=30,y=210)

    zip = Entry(buy)
    zip.place(x=120,y=210)

    label6 = Label(buy,text="Miejscowość",font=('bold', 10))
    label6.place(x=30,y=250)

    city = Entry(buy)
    city.place(x=120,y=250)

    if user[5] != '' :
        load_client(flags)
    else :
        flags = [1,1]

    b_register = Button(buy, text="Przejdź do systemu płatności",font=('bold',10),bg="white",command= lambda: add_order(flags, c))
    b_register.place(x=140,y=300)

# newest reviews window
def open_reviews():
    def delete() :
        cs = review_list.curselection()
        selection = review_list.get(cs)
        selection_id = selection.split()[0]
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "delete from recenzje where idRecenzja=%(id)s;"
        cursor.execute(stmt, {'id': selection_id})
        cursor.execute("commit")
        refresh()
    def refresh() :
        connection = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
        cursor = connection.cursor()
        stmt = "select r.idRecenzja, r.`ilosc giwazdek`, r.Komentarz, r.Produkt_idProdukt, k.imie_klienta, k.`nazwisko klienta` from mydb.recenzja as r left join mydb.klient as k on r.Klient_idKlient=k.idKlient order by idRecenzja desc limit 20"
        cursor.execute(stmt)
        rev = cursor.fetchall()
        for r in rev :
            temp = str(r[0]) + ' ' + str(r[4]) + ' ' + str(r[5]) + " mówi: "
            i = int(r[1])
            while(i > 0) :
                temp += '\u2B50'
                i = i - 1
            temp += ' '
            temp += r[2]
            review_list.insert(review_list.size()+1, temp)

    reviews = Toplevel()
    reviews.geometry("800x400")
    reviews.title("Księgarnia GUI - przegląd produktu")

    review_list = Listbox(reviews, width=100)
    review_list.place(x=40,y=50)

    b_delete = Button(reviews, text="Usuń komentarz",font=('bold',10),bg="white",command=delete)
    b_delete.place(x=120,y=230)

    refresh()

# product / review window
def open_product(prod_id, c):
    def add_cart():
        if c is not None :
            msg.showinfo("Dodano do koszyka","Dodano do koszyka produkt: " + str(prod[1]))
            c.append(prod_id)
    
    # TODO: more info
    product = Toplevel()
    product.geometry("400x600")
    product.title("Księgarnia GUI - przegląd produktu")

    connection1 = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
    cursor1 = connection1.cursor()
    stmt = "select * from produkt where idProdukt=%(id)s;"
    cursor1.execute(stmt, {'id': prod_id})
    out = cursor1.fetchall()
    # out = (id, nazwa, cena, zakup, kat, typ, autor, rok)
    connection2 = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
    cursor2 = connection2.cursor()
    stmt = "select r.Klient_idKlient, r.Komentarz, r.`ilosc giwazdek` from mydb.produkt as p left join mydb.recenzja as r on p.idProdukt = r.Produkt_idProdukt where idProdukt = %(id)s;"
    cursor2.execute(stmt, {'id': prod_id})
    rev = cursor2.fetchall()
    # rev = (autor, kom, gwiazdki)
    for prod in out:
        label1 = Label(product,text=str(prod[1]),font=('bold', 12))
        label1.place(x=40,y=90)

        label2 = Label(product,text=str(prod[6]),font=('bold', 10))
        label2.place(x=40,y=120)

        label3 = Label(product,text="Rok wydania: " + str(prod[7]),font=('bold', 10))
        label3.place(x=190,y=120)

        label4 = Label(product,text="Kup teraz: " + str(prod[2]),font=('bold', 10))
        label4.place(x=40,y=150)

        b_cart = Button(product, text="Do koszyka",font=('bold',10),bg="white",command=add_cart)
        b_cart.place(x=190,y=150)

        label5 = Label(product,text="Recenzje tego produktu:",font=('bold', 10))
        label5.place(x=40,y=180)
        review_list = Listbox(product, width = 50)
        review_list.place(x=40,y=200)
        for r in rev :
            temp = ''
            i = int(r[2])
            while(i > 0) :
                temp += '\u2B50'
                i = i - 1
            temp += ' '
            temp += r[1]
            review_list.insert(review_list.size()+1, temp)

# register window
def open_register():
    def register():
        u = username.get()
        p = password.get()
        e = email.get()
        if len(u) == 0 or len(p) == 0 or len(e) == 0 :
            msg.showerror("Błąd","Wszystkie pola wymagane")
        else :
            c1 = mysql.connect(host="localhost",user="root",password=mysql_pass,database="mydb")
            cursor = c1.cursor()
            stmt = "select `idUzytkownik` from uzytkownik order by idUzytkownik desc limit 1"
            cursor.execute(stmt)
            out = cursor.fetchone()
            # should probably check for duplicates
            stmt = "insert into uzytkownik values (%(id)s,%(user)s,%(email)s,%(pass)s,'1');"
            cursor.execute(stmt, {'id': str(int(out[0])+1),'user': u,'email': e, 'pass': p})
            cursor.execute("commit")
            msg.showinfo("Status","Uzytkownik dodany")
    reg = Toplevel()
    reg.geometry("400x300")
    reg.title("Księgarnia GUI - rejestracja")
    label4 = Label(reg,text="Nazwa",font=('bold', 10))
    label4.place(x=30,y=150)

    username = Entry(reg)
    username.place(x=80,y=150)

    label5 = Label(reg,text="Hasło",font=('bold', 10))
    label5.place(x=30,y=180)

    password = Entry(reg)
    password.place(x=80,y=180)

    label6 = Label(reg,text="Email",font=('bold', 10))
    label6.place(x=30,y=210)

    email = Entry(reg)
    email.place(x=80,y=210)

    b_register = Button(reg, text="Zarejestruj",font=('bold',10),bg="white",command=register)
    b_register.place(x=60,y=250)


# refresh main window
def redraw(user):
    for element in root.winfo_children():
        element.destroy()
    if user[2] == 0 :
        change_moderator(user)
    elif user[2] == 1 :
        change_user(user)
    else :
        landing()

# main window
# making global appearently a bad idea
global root
root = Tk()
landing()
# mainloop() is not actually a loop? so have to make own update func
root.mainloop()