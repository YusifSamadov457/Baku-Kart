import time
def kecid_yazisi(i):
    print("\t\t\t.................................................")
    print("\t\t\t\t\t Bakı Kart")
    time.sleep(i)
userDb = { 1 :{"pword" : 1234,
                    "balance" : 12.40,
                   "limit" : 100.00,
                   "Borc" : 0.00,
                   "Student" : True,
                   "Retired" : False,
                   "card_status":True,
                   "rejim" : 4.20,
                   "əməliyyatlar":[]},
           2 :{"pword" : 2222,
                    "balance" : 0.40,
                   "limit" : 100.00,
                   "Borc" : 1.00,
                   "card_status":True,
                   "Student" : False,
                   "Retired" : False,
                   "rejim" : 4.20,
                   "əməliyyatlar":[]},
           3 :{"pword" : 4444,
                    "balance" : 500.00,
                   "limit" : 300.00,
                   "Borc" : 0.00,
                   "card_status":True,
                   "Student" : False,
                   "Retired" : True,
                   "rejim" : 4.20,
                   "əməliyyatlar":[]},
           4 :{"pword" : 9999,
                    "balance" : 3.30,
                   "limit" : 20.00,
                   "Borc" : 0.00,
                   "card_status":True,
                   "Student" : False,
                   "Retired" : False,
                   "rejim" : 4.20,
                   "əməliyyatlar":[]}
             }
while True:
    try:
        kecid_yazisi(2)
        userkey = False
        print("1)Kart 1 (CardID:1234)\n2)Kart 2 (CardID:2222)\n3)Kart 3 (CardID:4444)\n4)Kart 4 (CardID:9999)")
        try:
            c_user = int(input("Kart seçin:"))
        except KeyError:
            print("Uğursuz seçim.")
        if userDb[c_user]["card_status"] == False:
            print("Kart bloklanıb. Əməliyyat ləğv edildi.")
            pass
        current_pword = userDb[c_user]["pword"]
        current_balance = userDb[c_user]["balance"]
        current_limit = userDb[c_user]["limit"]
        current_debt = userDb[c_user]["Borc"]
        current_std = userDb[c_user]["Student"]
        current_rtr = userDb[c_user]["Retired"]
        current_rejim = userDb[c_user]["rejim"]
        current_last_ops = userDb[c_user]["əməliyyatlar"]
        limit_status = 0.00
        pass_count = 0
        payment_amount = 0.00
        endirim_miqdari = 0.00
        for i in range(3):
            password = int(input("Şifrəni daxil edin:"))
            if password == current_pword:
                userkey = True
                current_last_ops.append("Log in")
                break
            else:
                if i == 2:
                    print("Şifrə yalnışdır. Kartınız bloklandı.")
                    userDb[c_user]["card_status"] = False
                    current_last_ops.append("Card Blocked")
                else:
                    print("Şifrə yanlışdır. Yenidən cəhd edin.")
        while userkey == True:
            kecid_yazisi(2)
            print("\t\t\t\t\tƏməliyyatlar\n 1) Balansa baxmaq\n 2) Balansı artırmaq\n 3) Gediş et\n 4) Son əməliyyatlar\n 5) Günlük statistika\n 6) Parametrlər\n 0) Çıxış")
            selection = int(input("Seçiminizi qeyd edin:"))
            if selection == 1:
                print("Sizin balansınız:",current_balance)
                current_last_ops.append("Balansın göstərilməsi")
                if current_debt > 0.00:
                    print("Sizin borcunuz:",current_debt)
            elif selection == 2:
                amount = float(input("Artırılacaq məbləği qeyd edin")) #(!Limit = {}):".format(current_limit)))
                if limit_status + amount > current_limit:
                    print("Limiti keçdiniz, balans artırma baş tutmadı.")
                elif current_debt == 0.00:
                    limit_status += amount
                    current_balance = current_balance + amount
                    print("Balans artırma tamamlandı. Balansınız:",current_balance)
                    current_last_ops.append("Balansın artırılması:{}>>{}".format(current_balance-amount,current_balance))
                else:
                    current_balance = current_balance + amount - current_debt
                    current_debt -= amount
                    if current_debt < 0.00:
                        current_debt == 0.00
                        print("Balans artırma tamamlandı. Balansınız:",current_balance)
                        current_last_ops.append("Balansın artırılması:{}>>{}".format(current_balance-amount,current_balance))
                    print("Yüklədiyiniz pulla borcunuz ödəndi. Qalıq borc:{}".format(current_debt))
                    current_last_ops.append("Borc ödənişi. Qalıq borc:{}".format(current_debt))
            elif selection == 3:
                if current_balance > current_rejim:
                    current_balance -= current_rejim
                    print("Turniketdən keçə bilərsiniz.")
                    current_last_ops.append("Turniket keçişi:{} AZN".format(current_rejim))
                    endirim_miqdari = 4.20 - current_rejim
                    pass_count += 1
                    payment_amount += current_rejim
                elif current_balance - 1.00 <= current_rejim:
                    current_balance -= 2.60
                    current_debt = current_debt + current_rejim - 2.60
                    print("Turniketdən keçə bilərsiniz.")
                    current_last_ops.append("Turniket keçişi:{} AZN".format(current_rejim))
                    endirim_miqdari = 4.20 - current_rejim
                    pass_count += 1
                    payment_amount += current_rejim
            elif selection == 4:
                try:
                    current_last_ops.append("Son əməliyyatların göstərilməsi.")
                    i = int(input("Əməliyyat sayı:"))
                    for i in range(i):
                        print(i+1,") ",current_last_ops[i])
                except IndexError:
                    pass
            elif selection == 5:
                print("Bu gün...")
                print("1)...balansın artırılma miqdarı:{}\n2)...edilən gedişlərin sayı:{}\n3)...edilən ödəniş miqdarı:{}\n4)...edilən endirim:{}".format(limit_status,pass_count,payment_amount,endirim_miqdari))
            elif selection == 6:
                while True:
                    kecid_yazisi(2)
                    print("\t\t\t\t\tƏməliyyatlar\n 1) Gündəlik balans artırma limitinin dəyişdirilməsi\n 2) Ödəniş rejiminin dəyişdirilməsi\n 3)Şifrənin dəyişdirilməsi \n 0) Çıxış")
                    selection = int(input("Seçiminizi qeyd edin:"))
                    if selection == 1:
                        print("Cari limit:",current_limit)
                        current_limit = int(input("Yeni limiti daxil edin:"))
                        print("Limit yeniləndi:",current_limit)
                        current_last_ops.append("Limit changed")
                    elif selection == 2:
                        while True:
                            kecid_yazisi(2)
                            print("\t\t\t\t\tƏməliyyatlar\n 1) Normal\n 2)Tələbə\n 3)Təqaüdçü\n 0) Çıxış")
                            selection = int(input("Keçmək istədiyiniz rejimi qeyd edin:"))
                            if selection == 1:
                                wanted_rejim = 4.20
                                current_rejim = wanted_rejim
                                print("Rejiminiz uğurla yeniləndi.")
                                current_last_ops.append("Rejim dəyişmə:>>Normal")
                            elif selection == 2 and current_std == True:
                                wanted_rejim = 3.80
                                current_rejim == wanted_rejim
                                print("Rejiminiz uğurla yeniləndi.")
                                current_last_ops.append("Rejim dəyişmə:>>Tələbə")
                            elif selection == 2 and current_rtr == True:
                                wanted_rejim = 3.60
                                current_rejim == wanted_rejim
                                print("Rejiminiz uğurla yeniləndi.")
                                current_last_ops.append("Rejim dəyişmə:>>Təqaüdçü")
                            elif selection == 0:
                                break
                            else:
                                print("Uğursuz seçim")
                                current_last_ops.append("Rejim dəyişmə:X Uğursuz seçim.")
                    elif selection == 3:
                        for i in range(3):
                            password = int(input("Köhnə şifrəni daxil edin:"))
                            if password == current_pword:
                                current_pword = int(input("Yeni şifrəni daxil edin."))
                                print("Şifrəniz uğurla yeniləndi.")
                                break
                            else:
                                if i == 2:
                                    print("Şifrə yalnışdır. Kartınız bloklandı.")
                                else:
                                    print("Şifrə yanlışdır. Yenidən cəhd edin.")
                    elif selection == 0:
                        break
                    else:  
                        print("Uğursuz seçim")
            elif selection == 0:
                print("Logging out...")
                current_last_ops.append("Log out")
                userDb[c_user]["pword"] = current_pword
                userDb[c_user]["balance"] = current_balance
                userDb[c_user]["limit"] = current_limit
                userDb[c_user]["Borc"] = current_debt
                userDb[c_user]["Student"] = current_std
                userDb[c_user]["Retired"] = current_rtr
                userDb[c_user]["rejim"] = current_rejim
                userDb[c_user]["əməliyyatlar"] = current_last_ops
                userkey = False
            else:  
                print("Uğursuz seçim")
    except ValueError:
        print("Uğursuz seçim")