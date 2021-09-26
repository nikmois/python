import datetime
from dateutil.relativedelta import relativedelta

ik = input("Enter your id code: ")
if ik:
    if ik.isdigit():                  #проверка введен ли код
        if len(ik) == 11:     #проверка на длинну кода
            ik = int(ik)      #set type int
            if ik > 10000000000 and ik < 100000000000: #проверка попадания в диапазон целого числа
                genderCode = str(ik)[0:1]
                if int(genderCode) > 0 and int(genderCode) < 7:
                    ik = str(ik)
                    ikSum = 1*int((ik[0:1]))+2*int((ik[1:2]))+3*int((ik[2:3]))+4*int((ik[3:4]))+5*int((ik[4:5]))+6*int((ik[5:6]))+7*int((ik[6:7]))+8*int((ik[7:8]))+9*int((ik[8:9]))+1*int((ik[9:10]))    
                    k1 = ikSum%11             #проверка на контрольную цифру
                    if k1 == 10:
                        ikSum = 3*int((ik[0:1]))+4*int((ik[1:2]))+5*int((ik[2:3]))+6*int((ik[3:4]))+7*int((ik[4:5]))+8*int((ik[5:6]))+9*int((ik[6:7]))+1*int((ik[7:8]))+2*int((ik[8:9]))+3*int((ik[9:10]))
                        k2 = ikSum%11
                        if k1 == 10 and k2 == 10:
                            k1 = 0
                        elif k1 == 10 and k2 != 10:
                            k1 = k2
                    if k1 == int((ik[10:11])):           
                        centuries = [0,1800,1800,1900,1900,2000,2000]
                        ikGender = int(ik[0:1])
                        ikYearTile = int(ik[1:3])
                        fullYear = centuries[ikGender]+ikYearTile
                        ikMonth = (ik[3:5])
                        ikDay = (ik[5:7])
                        today = datetime.date.today()
                        now = today.strftime("%Y%m%d")
                        testDate = (str(fullYear) + ikMonth + ikDay)
                        checkYear = int(today.strftime("%Y")) - int(fullYear)
                        if checkYear < 120 and checkYear > 0:      
                            if int(ikMonth) > 0 and int(ikMonth) <= 12: 
                                try:                                       #проверка на существование даты
                                    datetime.date(int(ikYearTile), int(ikMonth), int(ikDay))
                                    fullYear = int(now) - int(testDate)
                                    if fullYear >= 180000:
                                        print("ACCESS GRANTED")
                                        birthYear = centuries[ikGender]+ikYearTile
                                        birthDate = datetime.date(int(birthYear), int(ikMonth), int(ikDay))
                                        birthMonthName = birthDate.strftime("%b")
                                        print("Birthday:",ikDay, birthMonthName, birthYear)
                                        print("Age:", today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)))
                                        birth = datetime.date.fromisoformat(str(birthDate))
                                        age = relativedelta(today, birth)
                                        print("Years:",age.years,"Months:",age.months,"Days:",age.days)
                                        print("ADULT")
                                    else:
                                        print("ACCESS DENIED, TEENAGE")
                                except (ValueError):
                                    print("Wrong id code, unreal date")                                 
                            else:
                                print("Wrong id code, incorrect month")
                        else: 
                            print("Wrong id code, incorrect year of birth")
                    else: 
                        print("Entered unexisting id code")  
                else: 
                    print("Wrong first number of id code")
            else:
                print("Entered incorrect id code")    
        else:
            print("Id code doesn't match allowed length, please check if it is correct")    
    else: 
        print("Id code should contain only digits")
else:
    print("Please enter your id code")