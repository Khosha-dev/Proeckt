from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Rent Avto")
window.geometry("1028x768+790+250")
window.resizable(width=False,height=False)


# window.config(bg="#999999")


# def user_file(username, password):
#     with open(user_file, "a") as file:
#         file.write(f"{username}:{password}\n")
# control
#
# window.iconbitmap("icon_image/cal.ico")
#
# window.config(bg="#999999")

# control

    # sing_button = Button(start_frame, text="next", command=next)  # command=Sing_in)
    # sing_button.config(bg="#999999",
    #                    fg="#ff0000",
    #                    width=5,
    #                    height=2)
    # sing_button.place(x=60, y=600)


# class sing_up:
#     def __init__(self,login,password):
#         self.login=login
#         self.password=password


# else:
#     messagebox.showerror(title="error", message="error")

Admin_Pasword="Admin"



def start():
    # Start_frame def
    def Start_frame():
        start_frame = Frame(window, width=1020, height=768, bg="#999999")
        start_frame.place(x=0, y=0)
        # image
        # 1
        rent_car_image=PhotoImage(file=r"image/avto_rent7.png")
        image_rent_label=Label(image=rent_car_image)
        image_rent_label.image = rent_car_image
        image_rent_label.place(x=150,y=200)
        image_rent_label.config(bg="#999999")


        # logo
        label_logo=Label(start_frame,text="Avto Rent.az\n Лучшие машины в баку")
        label_logo.config(bg="#999999",fg="#800000",font=("Comic Sans MS", 24))
        label_logo.place(x=270,y=15)

        def exit():
            start()
        exit=Button(start_frame,text="exit",bg="#999999",
                               fg="#ff0000",
                               width=5,
                               height=2,command=exit)
        exit.place(x=60,y=600)

        # def admin frame and config

        def admin_frame():
            admin_frame=Frame(window,width=1020, height=768,bg="#999999")
            admin_frame.place(x=0,y=0)

            def back_eco():
                Avto_econom()

            back_econom=Button(admin_frame,text="back",width=5,height=2,command=back_eco,bg="#999999")
            back_econom.place(x=10,y=600)

        # def admin

        def admin_password():
            def admin_pas():
                global Admin_Pasword
                admin_pass= pass_adm.get()
                if admin_pass == Admin_Pasword:
                    admin_frame()
                elif admin_pass !=Admin_Pasword:
                    messagebox.showerror("error", "ne pravilno vveli")
                    Avto_econom()

            # frame
            admin_reg=Frame(window,width=1020,height=768,bg="#999999")
            admin_reg.place(x=0,y=0)

            # def
            def back_eco():
                Avto_econom()

            # Entry
            pass_adm=Entry(admin_reg,bg="#800000",width=25,font=("Comic Sans MS", 14),)
            pass_adm.place(x=250,y=200)

            # Button(да,я решил их подписать и распределить. ну правда же я молодец. *>* )
            # 1
            back_eco=Button(admin_reg,text='back',width=5,height=2,bg="#999999",fg="#800000",command=back_eco)
            back_eco.place(x=10,y=650)
            # 2
            enter=Button(admin_reg,text='enter',width=5,height=2,fg="#800000",bg="#999999",command=admin_pas)
            enter.place(x=350,y=250)

            # label
            label_pass=Label(admin_reg,text="password:")
            label_pass.config(bg="#999999",fg="#800000",font=("Comic Sans MS", 14))
            label_pass.place(x=150,y=195)



        # control
        def back():
            # Sigm_in_frame()
            Start_frame()

        # view

        def next():
            info_frame = Frame(window, width=1020, height=768, bg="#999999")
            info_frame.place(x=0, y=0)

            sing_button = Button(info_frame, text="back", command=back)  # command=Sing_in)
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
                label_insta=Label(info_redact,text="instagram:",font=("Comic Sans MS", 14),bg="#999999")
                label_insta.place(x=10,y=6)

                # 2
                label_instaga = Label(info_redact, text="Telegram:", font=("Comic Sans MS", 14), bg="#999999")
                label_instaga.place(x=10, y=58)

                # 3

                telefon_label=Label(info_redact, text="Telefon:", font=("Comic Sans MS", 14), bg="#999999")
                telefon_label.place(x=25,y=105)



                # Entry
                # 1

                instagram_entry=Entry(info_redact,bg="#800000", width=25, font=("Comic Sans MS", 14))
                instagram_entry.place(x=110,y=10)

                # 2

                telegram_entry = Entry(info_redact, bg="#800000", width=25, font=("Comic Sans MS", 14))
                telegram_entry.place(x=110, y=60)

                # 3

                telefon_entry = Entry(info_redact, bg="#800000", width=25, font=("Comic Sans MS", 14))
                telefon_entry.place(x=110,y=110)

                # save
                def save_info():
                    instagram = instagram_entry.get()
                    telegram = telegram_entry.get()
                    telefon = telefon_entry.get()
                    # info=({"insta":instagram,"telega":telegram,"telefon":telefon})
                    info=[instagram,telegram,telefon]
                    with open("info.txt","a") as file:
                        file.write(f"{1}:{instagram}\n")
                        file.write(f"{2}:{telegram}\n")
                        file.write(f"{3}:{telefon}\n")










                # Button
                # 1
                back3=Button(info_redact,bg="#999999",text="Back",width=5,height=2,command=back_info)
                back3.place(x=10,y=720)

                # 2
                info_save=Button(info_redact,bg="#999999",text="save",width=5,height=2,command=save_info)
                info_save.place(x=60,y=720)



            def info_admin_pass():
                info_admin = Frame(window, width=1020, height=768, bg="#999999")
                info_admin.place(x=0, y=0)


                # def
                def check():
                    global Admin_Pasword
                    password=pass_adm.get()
                    if password == Admin_Pasword:
                        Info_redact()



                # Entry
                pass_adm = Entry(info_admin, bg="#800000", width=25, font=("Comic Sans MS", 14), )
                pass_adm.place(x=250, y=200)

                # *>*

                # 1

                back_eco = Button(info_admin, text='back', width=5, height=2, bg="#999999", fg="#800000",
                                  command=next)
                back_eco.place(x=10, y=650)

                # 2

                enter = Button(info_admin, text='enter', width=5, height=2, fg="#800000", bg="#999999",
                               command=check)
                enter.place(x=350, y=250)



                # label
                label_pass = Label(info_admin, text="password:")
                label_pass.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 14))
                label_pass.place(x=150, y=195)


            #Button

            info_admin=Button(info_frame,text="redact",bg="#999999",fg="#800000",width=6,height=2,
                              command=info_admin_pass)
            info_admin.place(x=800,y=10)









            # peremenn

            with open("info.txt","r") as file:
                file.readlines()

            instagram=""
            telegram=""
            telefon=""
            for line in "info.txt":
                if line == "1":
                    instagram = file
                elif line == "2":
                    telegram = file
                elif line == "3":
                    telefon = file

            # label
            # 1
            label_instagram=Label(info_frame,text=f"instagram:{instagram}")
            label_instagram.config(bg="#999999",fg="#800000",font=("Comic Sans MS", 28),width=20)
            label_instagram.place(x=300,y=100)
            # 2 text label
            label_telegram = Label(info_frame, text=f"telegram:{telegram}")
            label_telegram.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 28),width=20)
            label_telegram.place(x=300, y=200)
            # 3
            label_telefon = Label(info_frame, text=f"telefon:{telefon}")
            label_telefon.config(bg="#999999", fg="#800000", font=("Comic Sans MS", 28),width=20)
            label_telefon.place(x=300, y=300)





        def Avto_econom():
            econom=Frame(window,width=1020,height=768,bg="#999999")
            econom.place(x=0,y=0)




            admin=Button(econom,text="admin",width=5,height=2,command=admin_password,bg="#999999",fg="#ff0000")
            admin.place(x=10,y=10)

            def start_frame_back():
                Start_frame()

            back_start_frame= Button(econom, text="back", width=5, height=2, command=start_frame_back,
                                     bg="#999999", fg="#ff0000")
            back_start_frame.place(x=10, y=650)









        Avto_button = Button(start_frame, text="Econom avto", command=Avto_econom)
        Avto_button.config(bg="#999999",
                           fg="#ff0000",
                           width=10,
                           height=2)
        Avto_button.place(x=20, y=50)

        sing_button = Button(start_frame, text="next", command=next)  # command=Sing_in)
        sing_button.config(bg="#999999",
                           fg="#ff0000",
                           width=5,
                           height=2)
        sing_button.place(x=10, y=600)

    # Sing_up def

    # class login:
    #     def __init__(self,login,password):
    #         self.login=login
    #         self.password=password

    def Log_in():

        login = log_entry.get()
        password = pas_entry.get()
        with open("account.txt", "r") as file:
            account = file.readlines()
        estno = 0
        for user in account:
            proverka = login + ":" + password + "\n"
            if proverka == user:
                estno = 1
                # Sigm_in_frame()
                Start_frame()
        if estno == 0:
            messagebox.showerror("error", "ne pravilno vveli")

    def sing():

        def Sing_up():


            login = log1_entry.get()
            password = pas1_entry.get()
            if login == " " or password == " " or login == "" or password == "":
                messagebox.showinfo(message="zapolnite polya")
                sing()
            elif login != None and password != None:
                with open("account.txt", "a") as file:
                    file.write(f"{login}:{password}\n")
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
        sing1_button.place(x=260, y=250)

        sing1_button = Button(s_up, text="registr", command=Sing_up)
        sing1_button.config(bg="#999999",
                            fg="#ff0000",
                            width=5,
                            height=2)
        sing1_button.place(x=360, y=250)

        login1_label = Label(s_up, text="Avto")
        login1_label.config(background="#999999",
                            fg="white",
                            font=("Comic Sans MS", 28, "italic"))
        login1_label.place(x=100, y=10)

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




    # start def
    sign_in_frame = Frame(window, width=1020, height=768, bg="#999999")
    sign_in_frame.place(x=0, y=0)
    si_up = Button(window, text="sing up", bg="#999999", fg="#ff0000", height=2, width=5, command=sing)
    si_up.place(x=100, y=250)

    # image
    # 1
    rent_car_image2 = PhotoImage(file=r"image/avto_rent16.png")
    image_rent_label2 = Label(sign_in_frame,image=rent_car_image2)
    image_rent_label2.image = rent_car_image2
    image_rent_label2.place(x=80, y=200)
    image_rent_label2.config(bg="#999999",fg="#999999")





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

    login_label = Label(window, text="Login")
    login_label.config(background="#999999",
                       fg="#ff0000",
                       font=("Comic Sans MS", 14, "italic"))
    login_label.place(x=100, y=95)

    pas_label = Label(window, text="Pasword")
    pas_label.config(background="#999999",
                     fg="#ff0000",
                     font=("Comic Sans MS", 14, "italic"))
    pas_label.place(x=100, y=160)

    log = Button(window, text="login", command=Log_in)
    log.config(bg="#999999", fg="#ff0000", height=2, width=5)
    log.place(x=150, y=250)

    def destroy():
        window.destroy()

    destroy=Button(window,text="exit program",background="#999999",
                   fg="#ff0000"
                   ,command=destroy,width=11,height=2)
    destroy.place(x=360,y=250)


#
#
#     image for program
#
#















start()

window.mainloop()



