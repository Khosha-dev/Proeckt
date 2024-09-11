from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk

window = Tk()
window.title("Rent Avto")
window.geometry("1028x768+790+250")
window.resizable(width=False, height=False)

Admin_Pasword = "Admin"
sort_mode = "name"


def start():
    # Start_frame def
    def Start_frame():
        start_frame = Frame(window, width=1020, height=768, bg="#999999")
        start_frame.place(x=0, y=0)
        # image
        # 1
        rent_car_image = PhotoImage(file=r"image/avto_rent7.png")
        image_rent_label = Label(image=rent_car_image)
        image_rent_label.image = rent_car_image
        image_rent_label.place(x=150, y=200)
        image_rent_label.config(bg="#999999")

        # logo
        label_logo = Label(start_frame, text="Avto Rent.az\n The best cars in Baku")
        label_logo.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 24))
        label_logo.place(x=270, y=15)

        def exit():
            start()

        exit = Button(start_frame, text="exit", bg="#999999",
                      fg="#ff0000",
                      width=5,
                      height=2, command=exit)
        exit.place(x=60, y=600)

        # def admin frame and config

        def Admin_frame():
            admin_frame = Frame(window, width=1020, height=768, bg="#999999")
            admin_frame.place(x=0, y=0)

            # Entry
            # 1

            name_car = Entry(admin_frame, width=30, bg="#800000", fg="white", font=("Comic Sans MS", 14))
            name_car.place(x=56, y=50)

            # 2

            Price_car = Entry(admin_frame, width=40, font=("Comic Sans MS", 14), bg="#800000", fg="white")
            Price_car.place(x=496, y=50)

            delet_entry = Entry(admin_frame, width=40, font=("Comic Sans MS", 14), bg="#800000", fg="white")
            delet_entry.place(x=200, y=720)

            # 3

            scroll_description = ScrolledText(admin_frame)
            scroll_description.insert("1.0", "")
            scroll_description.place(x=60, y=120)
            scroll_description.config(bg="#999999", width=100, height=32, font=(14), fg="red",
                                      wrap=WORD)

            # load_car()

            def save_admin_eco_avto():
                Care_name = name_car.get()
                Price = Price_car.get()
                description = scroll_description.get("1.0", "end")

                if Care_name == " " or Price == " " or Price == "" or Care_name == "" \
                        or description == " " or description == "":
                    messagebox.showinfo(message="zapolnite vse polya")

                else:
                    with open("car.txt", "a") as file:
                        file.write(f"{Care_name}:{Price}:{description}")

            # Label
            # 1

            name_label = Label(admin_frame, text="Car name:", font=("Comic Sans MS", 14), bg="#999999", fg="#ff0000")
            name_label.place(x=65, y=14)

            # 2

            description_label = Label(admin_frame, font=("Comic Sans MS", 18), bg="#999999",
                                      fg="#ff0000", text="Car description:")
            description_label.place(x=90, y=80)

            # 3
            Price_label = Label(admin_frame, text="Price:", font=("Comic Sans MS", 18), bg="#999999", fg="#ff0000")
            Price_label.place(x=500, y=10)

            # 4
            delet_label = Label(admin_frame, text="delete car:", width=10, height=2, bg="#999999", fg="#ff0000",
                                font=(6))
            delet_label.place(x=100, y=710)

            def back_eco():

                Avto_econom()

            save_car = Button(admin_frame, text="save", width=5, height=2,
                              command=save_admin_eco_avto, bg="#999999", fg="#ff0000")
            save_car.place(x=5, y=660)

            back_econom = Button(admin_frame, text="back", width=5, height=2, command=back_eco, bg="#999999",
                                 fg="#ff0000")
            back_econom.place(x=5, y=710)

            def delete_car():
                car_name_to_delete = delet_entry.get().strip()
                with open("car.txt", "r") as file:
                    cars = file.readlines()

                with open("car.txt", "w") as file:
                    for car in cars:
                        car_details = car.split(":")
                        if car_details[0].strip() != car_name_to_delete:
                            file.write(car)

                messagebox.showinfo("Успех", f"Машина '{car_name_to_delete}' успешно удалена")

            delet_button = Button(admin_frame, text="delet", width=5, height=2,
                                  command=delete_car, bg="#999999", fg="#ff0000")
            delet_button.place(x=60, y=710)

            def admin_2page():
                admin_2page_frame = Frame(window, width=1020, height=768, bg="#999999")
                admin_2page_frame.place(x=0, y=0)

                # Entry
                # 1

                new_name_car = Entry(admin_2page_frame, width=30, bg="#800000", fg="white", font=("Comic Sans MS", 14))
                new_name_car.place(x=56, y=50)

                # 2

                new_Price_car = Entry(admin_2page_frame, width=40, font=("Comic Sans MS", 14), bg="#800000", fg="white")
                new_Price_car.place(x=496, y=50)

                # 3

                new_scroll_description = ScrolledText(admin_2page_frame)
                new_scroll_description.insert("1.0", "")
                new_scroll_description.place(x=60, y=120)
                new_scroll_description.config(bg="#999999", width=100, height=32, font=(14), fg="red",
                                              wrap=WORD)

                def save_new_data():
                    car_name = new_name_car.get()
                    car_price = new_Price_car.get()
                    car_description = new_scroll_description.get("1.0", "end")

                    if car_name == " " or car_price == " " or car_price == "" or car_name == ""\
                        or car_description == " " or car_description == "":
                        messagebox.showinfo(message="zapolnite vse polya")

                    else:
                        with open("car.txt", "a") as file:
                            file.write(f"{car_name}:{car_price}:{car_description}\n")

                    messagebox.showinfo("Success", "Car details saved successfully")
                    Admin_frame()

                save_button = Button(admin_2page_frame, text="Save", width=5, height=2, command=save_new_data,
                                     bg="#999999", fg="#800000")
                save_button.place(x=5, y=650)

                car_label = Label(admin_2page_frame,width=9,height=2, bg="#999999",
                                       fg="#800000", font=("Comic Sans MS", 14),text="redact car:")
                car_label.place(x=90,y=700)

                car_name_entry = Entry(admin_2page_frame, width=30, bg="#800000",
                                       fg="white", font=("Comic Sans MS", 14))
                car_name_entry.place(x=200, y=720)

                def load_car_data():
                    car_name_to_load = car_name_entry.get().strip()  # Получаем имя машины из поля ввода
                    with open("car.txt", "r") as file:
                        cars = file.readlines()
                        for car in cars:
                            car_details = car.split(":")
                            if car_details[0].strip() == car_name_to_load:
                                new_name_car.delete(0, END)
                                new_name_car.insert(0, car_details[0].strip())

                                new_Price_car.delete(0, END)
                                new_Price_car.insert(0, car_details[1].strip())

                                new_scroll_description.delete("1.0", END)
                                new_scroll_description.insert("1.0", car_details[2].strip())

                                # 12

                                car_name_to_delete = car_name_entry.get().strip()
                                with open("car.txt", "r") as file:
                                    cars1 = file.readlines()

                                with open("car.txt", "w") as file:
                                    for car1 in cars1:
                                        car_details = car1.split(":")
                                        if car_details[0] != car_name_to_delete:
                                            file.write(car1)
                                break

                load_car_button= Button(admin_2page_frame, text="load car", width=8, height=2, command=load_car_data,
                                    bg="#999999",
                                    fg="#ff0000")
                load_car_button.place(x=580, y=710)

                # Label
                # 1

                new_name_label = Label(admin_2page_frame, text="New car name:",
                                       font=("Comic Sans MS", 14), bg="#999999",
                                       fg="#ff0000")
                new_name_label.place(x=65, y=14)

                # 2

                new_description_label = Label(admin_2page_frame, font=("Comic Sans MS", 18), bg="#999999",
                                              fg="#ff0000", text="New car description:")
                new_description_label.place(x=90, y=80)

                # 3
                new_Price_label = Label(admin_2page_frame, text="New price:", font=("Comic Sans MS", 18),
                                        bg="#999999", fg="#ff0000")
                new_Price_label.place(x=500, y=10)

                def back_1page():
                    Admin_frame()




                back_1page = Button(admin_2page_frame, text="back", width=5, height=2, command=back_1page,
                                    bg="#999999",
                                    fg="#ff0000")
                back_1page.place(x=5, y=710)





            page2_button = Button(admin_frame,text="2 page", width=6, height=2,
                                  command=admin_2page, bg="#999999", fg="#800000")
            page2_button.place(x=800,y=710)





        # def admin

        def admin_password():
            def admin_pas():
                global Admin_Pasword
                admin_pass = pass_adm_entry.get()
                if admin_pass == Admin_Pasword:
                    Admin_frame()
                elif admin_pass != Admin_Pasword:
                    messagebox.showerror("error", "ne pravilno vveli")
                    Avto_econom()

            # frame
            admin_reg = Frame(window, width=1020, height=768, bg="#999999")
            admin_reg.place(x=0, y=0)

            # def
            def back_eco():
                Avto_econom()

            # Entry
            pass_adm_entry = Entry(admin_reg, bg="#800000", width=25, font=("Comic Sans MS", 14), )
            pass_adm_entry.place(x=250, y=200)

            # Button(да,я решил их подписать и распределить. ну правда же я молодец. *>* )
            # 1
            back_eco_button = Button(admin_reg, text='back', width=5, height=2, bg="#999999", fg="#800000",
                                     command=back_eco)
            back_eco_button.place(x=10, y=650)
            # 2
            enter_button = Button(admin_reg, text='enter', width=5, height=2, fg="#800000", bg="#999999",
                                  command=admin_pas)
            enter_button.place(x=350, y=250)

            # label
            pass_label = Label(admin_reg, text="password:")
            pass_label.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 14))
            pass_label.place(x=150, y=195)

        # control
        def back():
            # Sigm_in_frame()
            Start_frame()

        # view

        def next():
            info_frame = Frame(window, width=1020, height=768, bg="#999999")
            info_frame.place(x=0, y=0)

            sing_button = Button(info_frame, text="back", command=back)
            sing_button.config(bg="#999999",
                               fg="#ff0000",
                               width=5,
                               height=2)
            sing_button.place(x=10, y=600)

            # def
            def Info_redact():
                info_redact = Frame(window, width=1020, height=768, bg="#999999")
                info_redact.place(x=0, y=0)

                # def
                def back_info():
                    next()

                # label
                # 1
                insta_label = Label(info_redact, text="instagram:", font=("Comic Sans MS", 14), bg="#999999")
                insta_label.place(x=10, y=6)

                # 2
                instaga_label = Label(info_redact, text="Telegram:", font=("Comic Sans MS", 14), bg="#999999")
                instaga_label.place(x=10, y=58)

                # 3

                telefon_label = Label(info_redact, text="Telefon:", font=("Comic Sans MS", 14), bg="#999999")
                telefon_label.place(x=25, y=105)

                # Entry
                # 1

                instagram_entry = Entry(info_redact, bg="#800000", width=25, font=("Comic Sans MS", 14))
                instagram_entry.place(x=110, y=10)

                # 2

                telegram_entry = Entry(info_redact, bg="#800000", width=25, font=("Comic Sans MS", 14))
                telegram_entry.place(x=110, y=60)

                # 3

                telefon_entry = Entry(info_redact, bg="#800000", width=25, font=("Comic Sans MS", 14))
                telefon_entry.place(x=110, y=110)

                # save
                def save_info():
                    instagram = instagram_entry.get()
                    telegram = telegram_entry.get()
                    telefon = telefon_entry.get()
                    # info=({"insta":instagram,"telega":telegram,"telefon":telefon})
                    info_list = [instagram, telegram, telefon]
                    with open("info.txt", "w") as file:
                        for info in info_list:
                            file.write(f"{info}\n")
                        # file.write(f"{instagram}\n")
                        # file.write(f"{telegram}\n")
                        # file.write(f"{telefon}\n")

                # Button
                # 1
                back3_button = Button(info_redact, bg="#999999", text="Back", width=5, height=2, command=back_info)
                back3_button.place(x=10, y=720)

                # 2
                info_save_button = Button(info_redact, bg="#999999", text="save", width=5, height=2, command=save_info)
                info_save_button.place(x=60, y=720)

            def info_admin_pass():
                info_admin_frame = Frame(window, width=1020, height=768, bg="#999999")
                info_admin_frame.place(x=0, y=0)

                # def
                def check():
                    global Admin_Pasword
                    password = pass_adm_entry.get()
                    if password == Admin_Pasword:
                        Info_redact()

                # Entry
                pass_adm_entry = Entry(info_admin_frame, bg="#800000", width=25, font=("Comic Sans MS", 14), )
                pass_adm_entry.place(x=250, y=200)

                # *>*

                # 1

                back_eco_button = Button(info_admin_frame, text='back', width=5, height=2, bg="#999999", fg="#800000",
                                         command=next)
                back_eco_button.place(x=10, y=650)

                # 2

                enter_button = Button(info_admin_frame, text='enter', width=5, height=2, fg="#800000", bg="#999999",
                                      command=check)
                enter_button.place(x=350, y=250)

                # label
                pass_label = Label(info_admin_frame, text="password:")
                pass_label.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 14))
                pass_label.place(x=150, y=195)

            # Button

            info_admin_button = Button(info_frame, text="redact", bg="#999999", fg="#800000", width=6, height=2,
                                       command=info_admin_pass)
            info_admin_button.place(x=800, y=10)

            # peremenn

            with open("info.txt", "r") as file:
                lines = file.readlines()

            if len(lines) >= 3:
                instagram = lines[0]
                telegram = lines[1]
                telefon = lines[2]
            else:
                instagram = ""
                telegram = ""
                telefon = ""

            # label
            # 1
            label_instagram = Label(info_frame, text=f"Instagram:\n{instagram}")
            label_instagram.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 28), width=20)
            label_instagram.place(x=250, y=100)
            # 2 text label
            label_telegram = Label(info_frame, text=f"Telegram:\n{telegram}")
            label_telegram.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 28), width=20)
            label_telegram.place(x=250, y=230)
            # 3
            label_telefon = Label(info_frame, text=f"Telefon:\n{telefon}")
            label_telefon.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 28), width=20)
            label_telefon.place(x=250, y=360)

        def Avto_econom():
            econom = Frame(window, width=1020, height=768, bg="#999999")
            econom.place(x=0, y=0)

            # scrol bar for car

            def load_car_data():
                with open("car.txt", "r") as file:
                    content = file.readlines()
                    scroll_info = ""
                    for line in content:
                        line = line.strip()
                        if ':' in line:
                            parts = line.split(':', 2)
                            if len(parts) == 3:
                                car_name = parts[0].strip()
                                car_price = parts[1].strip()
                                car_description = parts[2].strip()
                                scroll_info += (f"Car name: {car_name}"f"\nCar price: {car_price}"
                                                f"\nCar description: {car_description} \n\n")

                scroll.config(state=NORMAL)
                scroll.delete("1.0", END)
                scroll.insert("1.0", scroll_info)
                scroll.config(state=DISABLED)



            # sort

            # Функция сортировки по цене
            def sort():
                try:
                    price = sort_entry.get()
                    if price == "prise":
                         load_car_data()
                    else:
                        price = int(price)
                        scroll_info = ""

                        with open("car.txt", "r") as file:
                            car_data = file.readlines()

                            for line in car_data:
                                line = line.strip()
                                if ':' in line:
                                    parts = line.split(':', 2)
                                    if len(parts) == 3:
                                        car_name = parts[0].strip()
                                        car_price = int(parts[1].strip())
                                        car_description = parts[2].strip()

                                        if car_price <= price:
                                            scroll_info += (f"Car name: {car_name}"
                                                            f"\nCar price: {car_price}"
                                                            f"\nCar description: {car_description} \n\n")


                        scroll.config(state=NORMAL)
                        scroll.delete("1.0", END)
                        scroll.insert("1.0", scroll_info)
                        scroll.config(state=DISABLED)

                except ValueError:
                    pass

            def found_car():
                found = found_entry.get().strip().lower()
                if found == "":
                    return load_car_data()

                scroll_info = ""

                with open("car.txt", "r") as file:
                    car_data = file.readlines()

                    for line in car_data:
                        line = line.strip()
                        if ':' in line:
                            parts = line.split(':', 2)
                            if len(parts) == 3:
                                car_name = parts[0].strip()
                                car_price = parts[1].strip()
                                car_description = parts[2].strip()


                                if found in car_name.lower():
                                    scroll_info += (f"Car name: {car_name}"
                                                    f"\nCar price: {car_price}"
                                                    f"\nCar description: {car_description} \n\n")


                scroll.config(state=NORMAL)
                scroll.delete("1.0", END)
                scroll.insert("1.0",
                scroll_info if scroll_info else "Car not found.")
                scroll.config(state=DISABLED)





            price_label = Label(econom, text="Sort by price", bg="#999999", fg="#800000", font=("Comic Sans MS", 14))
            price_label.place(x=800, y=10)

            sort_button = Button(econom, bg="#999999", fg="#800000", text="sort", width=6, height=2,command=sort)
            sort_button.place(x=800, y=100)

            price_list=["prise",100,200,500,1000,10000,100000,1000000]

            sort_entry = ttk.Combobox(econom,values=price_list, width=13, font=("Comic Sans MS", 14), )
            sort_entry.place(x=800, y=50)
            sort_entry.current(0)

            # found

            found_entry = Entry(econom, bg="#800000", fg="white", width=15, font=("Comic Sans MS", 14))
            found_entry.place(x=800, y=190)

            car_found_label = Label(econom, text="Found car by name", bg="#999999", fg="#800000",
                                    font=("Comic Sans MS", 14))
            car_found_label.place(x=800, y=150)

            found_button = Button(econom, bg="#999999", fg="#800000", text="found", width=6, height=2,command=found_car)
            found_button.place(x=800, y=240)

            # scroll

            scroll = ScrolledText(econom)
            scroll.insert("1.0", "")
            scroll.place(x=10, y=50)
            scroll.config(bg="#999999", width=85, height=35, font=(14), fg="#800000", state=DISABLED, wrap=WORD)
            load_car_data()

            # Label
            car_info_label = Label(econom, text="A list of cars is available for rent. To rent, call from page 2"
                                   , bg="#999999", fg="#800000", font=("Comic Sans MS", 14))
            car_info_label.place(x=100, y=10)

            # Button
            admin_button = Button(econom, text="admin", width=5, height=2, command=admin_password, bg="#999999",
                                  fg="#ff0000")
            admin_button.place(x=10, y=5)

            def start_frame_back():
                Start_frame()

            back_start_frame = Button(econom, text="back", width=5, height=2, command=start_frame_back,
                                      bg="#999999", fg="#ff0000")
            back_start_frame.place(x=10, y=700)



        Avto_button = Button(start_frame, text="Econom avto", command=Avto_econom)
        Avto_button.config(bg="#999999",
                           fg="#ff0000",
                           width=11,
                           height=2,
                           font="14")
        Avto_button.place(x=20, y=50)

        sing_button = Button(start_frame, text="next", command=next)  # command=Sing_in)
        sing_button.config(bg="#999999",
                           fg="#ff0000",
                           width=5,
                           height=2)
        sing_button.place(x=10, y=600)

    def Log_in():

        login = log_entry.get()
        password = pas_entry.get()
        mail = mail_entry.get()
        with open("account.txt", "a") as file:
            with open("account.txt", "r") as file:
                account = file.readlines()
            estno = 0
            for user in account:
                proverka = login + ":" + password + ":" + mail + "\n"
                if proverka == user:
                    estno = 1
                    Start_frame()
        if estno == 0:
            messagebox.showerror("error", "ne pravilno vveli")

    def sing():

        def Sing_up():

            login = log1_entry.get()
            password = pas1_entry.get()
            rep_password = second_pas.get()
            mail = mail_entry.get()
            if login == " " or password == " " or login == "" or password == "" or mail == " " or mail == "" \
                    or rep_password == "" or rep_password == " ":
                messagebox.showinfo(message="zapolnite vse polya")
                sing()
            elif password != rep_password:
                messagebox.showinfo(message="parol ne sovpadaet")
                sing()

            elif login != None and password != None and mail_entry != None and rep_password != None:
                if password == rep_password:
                    with open("account.txt", "a") as file:
                        file.write(f"{login}:{password}:{mail}\n")
                    messagebox.showinfo(message="reqistraciya uspeshna")
                    start()

        # sing def
        s_up = Frame(window, width=1020, height=768, bg="#999999")
        s_up.place(x=0, y=0)

        def nazad():
            start()

        sing1_button = Button(s_up, text="back", command=nazad)
        sing1_button.config(bg="#999999",
                            fg="#ff0000",
                            width=5,
                            height=2)
        sing1_button.place(x=260, y=340)

        sing1_button = Button(s_up, text="registr", command=Sing_up)
        sing1_button.config(bg="#999999",
                            fg="#ff0000",
                            width=5,
                            height=2)
        sing1_button.place(x=360, y=340)

        log_label = Label(s_up, text="Avto")
        log_label.config(background="#999999",
                         fg="white",
                         font=("Comic Sans MS", 28, "italic"))
        log_label.place(x=100, y=10)

        login1_label = Label(s_up, text="Login")
        login1_label.config(background="#999999",
                            fg="#ff0000",
                            font=("Comic Sans MS", 14, "italic"))
        login1_label.place(x=100, y=120)

        pas1_label = Label(s_up, text="Pasword")
        pas1_label.config(background="#999999",
                          fg="#ff0000",
                          font=("Comic Sans MS", 14, "italic"))
        pas1_label.place(x=100, y=172)

        mail_label = Label(s_up, text="Mail")
        mail_label.config(background="#999999",
                          fg="#ff0000",
                          font=("Comic Sans MS", 14, "italic"))
        mail_label.place(x=100, y=222)

        repear_password = Label(s_up, text="Repear password")
        repear_password.config(bg="#999999", fg="#ff0000", font=("Comic Sans MS", 14, "italic"))
        repear_password.place(x=100, y=270)

        second_pas = Entry(s_up)
        second_pas.config(bg="#800000",
                          fg="#ff0000",
                          font=("Comic Sans MS", 14),
                          width=25,
                          show="*"
                          )
        second_pas.place(x=100, y=300)

        show_var = IntVar()

        def show():
            if show_var.get():
                pas1_entry.config(show="")
                second_pas.config(show="")
            else:
                pas1_entry.config(show="*")
                second_pas.config(show="*")

        check_button = Checkbutton(s_up, text="Show password", command=show, bg="#999999",
                                   fg="#ff0000",
                                   font=("Comic Sans MS", 14),
                                   width=12, variable=show_var)
        check_button.place(x=450, y=200)

        pas1_entry = Entry(s_up)
        pas1_entry.config(bg="#800000",
                          fg="#ff0000",
                          font=("Comic Sans MS", 14),
                          width=25,
                          show="*"
                          )
        pas1_entry.place(x=100, y=200)

        log1_entry = Entry(s_up)
        log1_entry.config(bg="#800000",
                          fg="#ff0000",
                          font=("Comic Sans MS", 14),
                          width=25
                          )
        log1_entry.place(x=100, y=150)

        mail_entry = Entry(s_up)
        mail_entry.config(bg="#800000",
                          fg="#ff0000",
                          font=("Comic Sans MS", 14),
                          width=25
                          )
        mail_entry.place(x=100, y=250)

    # start def
    sign_in_frame = Frame(window, width=1020, height=768, bg="#999999")
    sign_in_frame.place(x=0, y=0)
    si_up = Button(window, text="sing up", bg="#999999", fg="#ff0000", height=2, width=5, command=sing)
    si_up.place(x=100, y=310)

    # image
    # 1
    rent_car_image2 = PhotoImage(file=r"image/avto_rent16.png")
    image_rent_label2 = Label(sign_in_frame, image=rent_car_image2)
    image_rent_label2.image = rent_car_image2
    image_rent_label2.place(x=80, y=250)
    image_rent_label2.config(bg="#999999", fg="#999999")

    pas_entry = Entry(window)
    pas_entry.config(bg="#800000",
                     fg="#ff0000",
                     font=("Comic Sans MS", 14),
                     width=25,
                     show="*"
                     )
    pas_entry.place(x=100, y=200)

    log_entry = Entry(window)
    log_entry.config(bg="#800000",
                     fg="#ff0000",
                     font=("Comic Sans MS", 14),
                     width=25
                     )
    log_entry.place(x=100, y=130)

    mail_entry = Entry(window)
    mail_entry.config(bg="#800000",
                      fg="#ff0000",
                      font=("Comic Sans MS", 14),
                      width=25
                      )
    mail_entry.place(x=100, y=270)

    login_label = Label(window, text="Login")
    login_label.config(background="#999999",
                       fg="#ff0000",
                       font=("Comic Sans MS", 14, "italic"))
    login_label.place(x=100, y=95)

    mail_label = Label(window, text="Mail")
    mail_label.config(background="#999999",
                      fg="#ff0000",
                      font=("Comic Sans MS", 14, "italic"))
    mail_label.place(x=100, y=235)

    pas_label = Label(window, text="Pasword")
    pas_label.config(background="#999999",
                     fg="#ff0000",
                     font=("Comic Sans MS", 14, "italic"))
    pas_label.place(x=100, y=165)

    log_button = Button(window, text="login", command=Log_in)
    log_button.config(bg="#999999", fg="#ff0000", height=2, width=5)
    log_button.place(x=150, y=310)

    def destroy():
        window.destroy()

    destroy = Button(window, text="exit program", background="#999999",
                     fg="#ff0000"
                     , command=destroy, width=11, height=2)
    destroy.place(x=360, y=310)


#
#
#     image for program
#
#


start()

window.mainloop()
