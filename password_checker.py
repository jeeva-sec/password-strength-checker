import re
import getpass as a
import sys,time
def passwd_strength_checker():

    passwd=a.getpass("Enter your password : ")
    length=len(passwd)
    score=[]
    point = 0
    #length of the passwd
    if(length>13):
        point+=10
    elif(length>7):
        point+=5
    else :
        score.append("lenth not enough")
    #upper case in passwd
    if re.search(r"[A-Z]",passwd):
        point+=5
    else:
        score.append("Add at least one uppercase letter")
    #lower  case
    if re.search(r"[a-z]",passwd):
        point+=5
    else :
        score.append("Add at least one lowercase letter")
    #specail symbol
    if re.search(r"[^a-zA-z0-9]",passwd):
        point+=5
    else:
        score.append("add atleast one spacial charactor")
    #passwd strength determination
    if(point==25):
        print("----------It's strong password-----------")
    elif(point==20):
        print("----------It's moderate password---------")
    else:
        print("----------It's weak password-------------")
    #feedback for strong passwd
    for items in score:
        for c in items:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.03)
        print(c)
    while point!=25:
        passwd_strength_checker()     
    
passwd_strength_checker()

        
        
     
