import os
import shutil
import re

while True:
    print("\nenter file extension:")
    print("for example 'mp3','mp4','exe' etc...")
    file_type=input("enter here = ").replace(".","")
    print("\nyou want to full scan your multiple disc or folder for those",file_type,"files ?")
    print("NOTE: it can also include all subfolder")
    print("                               or                              ")
    print("you want to scan a particular folder or disc for those",file_type,"files  ?")
    print("NOTE: it cannot include subfolder")
    print("enter '1' for full scan multiple disc or folder\n      '2' for scan multiple particular folder or disc")


    while True:
        try:
            choose=int(input("enter here : "))
        except:
            continue

        if choose==1:
            print("\nenter your disc name :")
            print("example 'c:' or 'd:' or 'e:' anything\n         or")
            print("enter folder path :")
            print("example 'D:\video\MARVEL\IRON MAN'")
            print("when you complete it enter 'end'")

            listp=[]
            d=0
            while True:
                d+=1
                disc=str(input(f"enter your {d} disc name here : "))
                disc=disc.lower()
                if disc=="end":
                    break
                listp.append(disc)

            cm=str(input("enter c->copy or m->move or d->permanently_delete or s->search here: ")).lower()
            if cm=='c' or cm=='m':
                destination=input("enter destination path here: ")
            if cm=='c' or cm=='m' or cm=='d':
                ok=input("are you sure . enter 'y'->yes , 'n'->no here : ") 
            elif cm=='s':
                ok='y'

            if ok=='n':
                print("operation cancelled")
            elif ok=='y':
                try:
                    roo=None
                    for path in listp:
                        flag=0
                        for root, dirs, files in os.walk(path+'\\', topdown=False):
                            i=0
                            j=1
                            for name in files:
                                if re.match(f'.*\.{file_type}',name.lower()):
                                    i+=1
                                    if roo!=root:
                                        print("###################################",root,"###################################\n") #return folder path
                                    roo=root

                                    source=os.path.join(root, name).replace("\\\\","\\")
                                    print("             ",source) # returns the path of the file

                                    try:
                                        if cm=='c':
                                            dest = shutil.copy(source,destination)
                                            print("                     successfully copied")
                                        elif cm=='m':
                                            dest = shutil.move(source,destination)
                                            print("                     successfully moved")
                                        elif cm=='d':
                                            os.remove(source)
                                            print("                     successfully deleted")
                                    except Exception as e:
                                        print(e)

                                    j=0
                            if j==0:
                                print("no.of item found",i)
                                flag=1

                        if flag==0:
                            print('\n\n##############################################################\n')
                            print("no '",file_type,"' type files found in",path)
                            print('\n##############################################################\n\n')

                except Exception as e:
                    print(e)

            break


        elif choose==2:
            print("\nenter your disc name :")
            print("example 'c:' or 'd:' or 'e:' anything\n         or")
            print("enter folder path :")
            print("example 'D:\video\MARVEL\IRON MAN'")
            print("when you complete it enter 'end'")

            listp=[]
            d=0
            while True:
                d+=1
                disc=str(input(f"enter your {d} path here : "))
                disc=disc.lower()
                if disc=="end":
                    break
                listp.append(disc)

            cm=str(input("enter c->copy or m->move or d->permanently_delete or s->search here: ")).lower()
            if cm=='c' or cm=='m':
                destination=input("enter destination path here: ")
            if cm=='c' or cm=='m' or cm=='d':
                ok=input("are you sure . enter 'y'->yes , 'n'->no here : ") 
            elif cm=='s':
                ok='y'

            if ok=='n':
                print("operation cancelled")
            elif ok=='y':
                try:
                    for path in listp:
                        path=path+'\\'
                        i=0
                        print("###################################",path,"###################################\n")
                        for item in os.listdir(path):
                            item=path+item
                            if re.match(f'.*\.{file_type}',item.lower()):
                                i+=1
                                source=os.path.join(path,item).replace("\\\\","\\")
                                print("             ",source)

                                try:
                                    if cm=='c':
                                        dest = shutil.copy(source,destination)
                                        print("                     successfully copied")
                                    elif cm=='m':
                                        dest = shutil.move(source,destination)
                                        print("                     successfully moved")
                                    elif cm=='d':
                                        os.remove(source)
                                        print("                     successfully deleted")
                                except Exception as e:
                                    print(e)
                            flag=i
                            
                        print("no.of item found",i,"\n")
                        if flag==0:
                            print('\n\n##############################################################\n')
                            print("no '",file_type,"' type files found in",path)
                            print('\n##############################################################\n\n')

                except Exception as e:
                    print(e)

            break


        else:
            print("enter valid number")
            
    print("\n\ndo you want to search again")
    print("enter 'y'->yes , 'n'->no")

    while True:
        yn=input("enter here : ")
        if yn=='n':
            break
        elif yn=='y':
            break
        else:
            print("enter valid input")
    
    if yn=='n':
        break