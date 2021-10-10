from main_funtion import *
import random,os,pickle,time
from Chemistry12Funtion import *
from math import *
from chemistry_use import *
def question():
    d={"A":1,"B":2,"C":3,"D":4}
    whatcome=list()
    reaction=[]
    def first(l):
        os.system("cls")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("             Level ",l)
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("Note")
        print("..................")
        print('For skip the question click q')
        print("Press s so that programm tell the question by speech")
        print("For any right answer you get positive 4 marks ")
        print("For any wrong answer you will get 1 negative marks")
        print("................................................................................")
    #####################################################lavel 1
    first(1)
    data=pickle.load(open("SolutionLevel1Question.dat","rb"))
    Lavel1=[]
    for x in range(10):
        x=random.choice(data)
        data.pop(data.index(x))
        Lavel1+=[x]
    del data
    whatcome+=[Lavel1]
    Ans1=[]
    start=time.time()
    for x in range(10):
        print("\n\n")
        print(x+1,") ",Lavel1[x][0].capitalize())
        print("A)",Lavel1[x][2][0].capitalize())
        print("B)",Lavel1[x][2][1].capitalize())
        print("C)",Lavel1[x][2][2].capitalize())
        print("D)",Lavel1[x][2][3].capitalize())
        while(1==1):
            a=input("Enter your answer\t:")
            if(a.upper() in "ABCDQ"):
                break
            elif(a.upper()=="S"):
                say("Question is "+Lavel1[x][0])
                say("Option A is "+Lavel1[x][2][0])
                say("Option B is "+Lavel1[x][2][1])
                say("Option C is "+Lavel1[x][2][2])
                say("Option D is "+Lavel1[x][2][3])
            else:
                print("There is only 4 option avalaible a,b,c,d  (not case sensitive)")
        if(a.upper()=="Q"):
            Ans1+=[None]
        else:
            Ans1+=[d[a.upper()]]
    end=time.time()
    right=0;wrong=0;none=0
    re=[]
    for x in range(10):
        if(Ans1[x]==Lavel1[x][1]):
            re+=[4]
            right+=1
        elif(Ans1[x]==None):
            re+=[0]
            none+=1   
        elif(Ans1[x]!=Lavel1[x][1]):
            re+=[-1]
            wrong+=1
    reaction+=[re]
    del re
    if(right+wrong!=0):                   
        accuracy=(right/(right+wrong))*100
    else:
        accuracy=0
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("Result")
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("Total question That Answered\t:\t",right+wrong)
    print("Total right answer\t:\t",right)
    print("Total wrong answer\t:\t",wrong)
    print("Total skiped question\t:\t",none)
    print("Marks\t:\t",(right*4)-wrong)
    print("Percentage of marks\t:\t",((right*4)-wrong)*2.5)
    print("Accuracy\t:\t",accuracy,"%")
    print("Time taken\t:\t",end-start,"s")
    print("Average no question in a minute\t:\t",int((right+wrong)/(end-start)*60))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    performance1={"Total question":right+wrong,"right":right,"wrong":wrong,"skiped":none,"Marks":(right*4)-wrong,"Pencentage of marks":((right*4)-wrong)*2.5,"accuracy":accuracy,"time taken":end-start}
    del accuracy,start,end,right,wrong,none,Lavel1
    cho=input("Only press enter for next lever or for exit enter any charter\t:")
    if(cho!=""):
        Chemistry()
    Nsec(1)
    #####################################################lavel 2
    first(2)
    data=pickle.load(open("SolutionLevel2Question.dat","rb"))
    Lavel2=[]
    for x in range(10):
        x=random.choice(data)
        data.pop(data.index(x))
        Lavel2+=[x]
    del data
    whatcome+=[Lavel2]
    Ans1=[]
    start=time.time()
    for x in range(10):
        print("\n\n")
        print(x+1,") ",Lavel2[x][0].capitalize())
        print("A)",Lavel2[x][2][0].capitalize())
        print("B)",Lavel2[x][2][1].capitalize())
        print("C)",Lavel2[x][2][2].capitalize())
        print("D)",Lavel2[x][2][3].capitalize())
        while(1==1):
            a=input("Enter your answer\t:")
            if(a.upper() in "ABCDQ"):
                break
            elif(a.upper()=="S"):
                say("Question is "+Lavel2[x][0])
                say("Option A is "+Lavel2[x][2][0])
                say("Option B is "+Lavel2[x][2][1])
                say("Option C is "+Lavel2[x][2][2])
                say("Option D is "+Lavel2[x][2][3])
            else:
                print("There is only 4 option avalaible a,b,c,d  (not case sensitive)")
        if(a.upper()=="Q"):
            Ans1+=[None]
        else:
            Ans1+=[d[a.upper()]]
    end=time.time()
    right=0;wrong=0;none=0
    re=[]
    for x in range(10):
        if(Ans1[x]==Lavel2[x][1]):
            re+=[4]
            right+=1
        elif(Ans1[x]==None):
            re+=[0]
            none+=1   
        elif(Ans1[x]!=Lavel2[x][1]):
            re+=[-1]
            wrong+=1
    reaction+=[re]
    del re
    if(right+wrong!=0):                   
        accuracy=(right/(right+wrong))*100
    else:
        accuracy=0
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("Result")
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("Total question That Answered\t:\t",right+wrong)
    print("Total right answer\t:\t",right)
    print("Total wrong answer\t:\t",wrong)
    print("Total skiped question\t:\t",none)
    print("Marks\t:\t",(right*4)-wrong)
    print("Percentage of marks\t:\t",((right*4)-wrong)*2.5)
    print("Accuracy\t:\t",accuracy,"%")
    print("Time taken\t:\t",end-start,"s")
    print("Average no question in a minute\t:\t",int((right+wrong)/(end-start)*60))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    performance2={"Total question":right+wrong,"right":right,"wrong":wrong,"skiped":none,"Marks":(right*4)-wrong,"Pencentage of marks":((right*4)-wrong)*2.5,"accuracy":accuracy,"time taken":end-start}
    del accuracy,start,end,right,wrong,none
    cho=input("Only press enter for next lever or for exit enter any charter\t:")
    if(cho!=""):
        Chemistry()
    Nsec(1)
    #####################################################lavel 3
    first(3)
    data=pickle.load(open("SolutionLevel3Question.dat","rb"))
    Lavel2=[]
    for x in range(10):
        x=random.choice(data)
        data.pop(data.index(x))
        Lavel2+=[x]
    del data
    whatcome+=[Lavel2]
    Ans1=[]
    start=time.time()
    for x in range(10):
        print("\n\n")
        print(x+1,") ",Lavel2[x][0].capitalize())
        print("A)",Lavel2[x][2][0].capitalize())
        print("B)",Lavel2[x][2][1].capitalize())
        print("C)",Lavel2[x][2][2].capitalize())
        print("D)",Lavel2[x][2][3].capitalize())
        while(1==1):
            a=input("Enter your answer\t:")
            if(a.upper() in "ABCDQ"):
                break
            elif(a.upper()=="S"):
                say("Question is "+Lavel2[x][0])
                say("Option A is "+Lavel2[x][2][0])
                say("Option B is "+Lavel2[x][2][1])
                say("Option C is "+Lavel2[x][2][2])
                say("Option D is "+Lavel2[x][2][3])
            else:
                print("There is only 4 option avalaible a,b,c,d  (not case sensitive)")
        if(a.upper()=="Q"):
            Ans1+=[None]
        else:
            Ans1+=[d[a.upper()]]
    end=time.time()
    right=0;wrong=0;none=0
    re=[]
    for x in range(10):
        if(Ans1[x]==Lavel2[x][1]):
            re+=[4]
            right+=1
        elif(Ans1[x]==None):
            re+=[0]
            none+=1   
        elif(Ans1[x]!=Lavel2[x][1]):
            re+=[-1]
            wrong+=1
    reaction+=[re]
    del re
    for x in range(10):
        if(Ans1[x]==Lavel2[x][1]):
            right+=1
        elif(Ans1[x]==None):
            none+=1   
        elif(Ans1[x]!=Lavel2[x][1]):
            wrong+=1
    if(right+wrong!=0):
        accuracy=(right/(right+wrong))*100
    else:
        accuracy=0
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("Result")
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("Total question That Answered\t:\t",right+wrong)
    print("Total right answer\t:\t",right)
    print("Total wrong answer\t:\t",wrong)
    print("Total skiped question\t:\t",none)
    print("Marks\t:\t",(right*4)-wrong)
    print("Percentage of marks\t:\t",((right*4)-wrong)*2.5)
    print("Accuracy\t:\t",accuracy,"%")
    print("Time taken\t:\t",end-start,"s")
    print("Average no question in a minute\t:\t",int((right+wrong)/(end-start)*60))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    performance3={"Total question":right+wrong,"right":right,"wrong":wrong,"skiped":none,"Marks":(right*4)-wrong,"Pencentage of marks":((right*4)-wrong)*2.5,"accuracy":accuracy,"time taken":end-start}
    del accuracy,start,end,right,wrong,none
    cho=input("Only press enter for next lever or for exit enter any charter\t:")
    if(cho!=""):
        Chemistry()
    Nsec(1)
    #####################################################lavel Main
    first("JEE MAINS")
    data=pickle.load(open("SolutionLevelMAINSQuestion.dat","rb"))
    Lavel2=[]
    for x in range(10):
        x=random.choice(data)
        data.pop(data.index(x))
        Lavel2+=[x]
    del data
    whatcome+=[Lavel2]
    Ans1=[]
    start=time.time()
    for x in range(10):
        print("\n\n")
        print(x+1,") ",Lavel2[x][0].capitalize(),"\n\t,(year of question in jee mains is"+str(Lavel2[x][3]))
        print("A)",Lavel2[x][2][0].capitalize())
        print("B)",Lavel2[x][2][1].capitalize())
        print("C)",Lavel2[x][2][2].capitalize())
        print("D)",Lavel2[x][2][3].capitalize())
        while(1==1):
            a=input("Enter your answer\t:")
            if(a.upper() in "ABCDQ"):
                break
            elif(a.upper()=="S"):
                say("Question is "+Lavel2[x][0])
                say("Option A is "+Lavel2[x][2][0])
                say("Option B is "+Lavel2[x][2][1])
                say("Option C is "+Lavel2[x][2][2])
                say("Option D is "+Lavel2[x][2][3])
            else:
                print("There is only 4 option avalaible a,b,c,d  (not case sensitive)")
        if(a.upper()=="Q"):
            Ans1+=[None]
        else:
            Ans1+=[d[a.upper()]]
    end=time.time()
    right=0;wrong=0;none=0
    re=[]
    for x in range(10):
        if(Ans1[x]==Lavel2[x][1]):
            re+=[4]
            right+=1
        elif(Ans1[x]==None):
            re+=[0]
            none+=1   
        elif(Ans1[x]!=Lavel2[x][1]):
            re+=[-1]
            wrong+=1
    reaction+=[re]
    
    del re
    if(right+wrong!=0):                   
        accuracy=(right/(right+wrong))*100
    else:
        accuracy=0
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("Result")
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("Total question That Answered\t:\t",right+wrong)
    print("Total right answer\t:\t",right)
    print("Total wrong answer\t:\t",wrong)
    print("Total skiped question\t:\t",none)
    print("Marks\t:\t",(right*4)-wrong)
    print("Percentage of marks\t:\t",((right*4)-wrong)*2.5)
    print("Accuracy\t:\t",accuracy,"%")
    print("Time taken\t:\t",end-start,"s")
    print("Average no question in a minute\t:\t",int((right+wrong)/(end-start)*60))
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    performanceMain={"Total question":right+wrong,"right":right,"wrong":wrong,"skiped":none,"Marks":(right*4)-wrong,"Pencentage of marks":((right*4)-wrong)*2.5,"accuracy":accuracy,"time taken":end-start}
    del accuracy,start,end,right,wrong,none
    cho=input("Only press enter for next lever or for exit enter any charter\t:")
    if(cho!=""):
        Chemistry()
    #####################################################explaination
    #whatcome=list()reaction=[]
    os.system("cls")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("            Explaination of wrong or unanswered question")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("---------------------------------------------------------------------------------")
    print("Leval 1")
    print("----------------------------------------------------------------------------------")
    for x in range(len((reaction[0]))):
        Lavel2=whatcome[0]
        if(reaction[0][x]!=4):
             print(x+1,") ",Lavel2[x][0].capitalize())
             print("A)",Lavel2[x][2][0].capitalize())
             print("B)",Lavel2[x][2][1].capitalize())
             print("C)",Lavel2[x][2][2].capitalize())
             print("D)",Lavel2[x][2][3].capitalize(),"\tAns:-",Lavel2[x][1])
             print("\n")
    print("---------------------------------------------------------------------------------")
    print("Leval 2")
    print("----------------------------------------------------------------------------------")
    for x in range(len((reaction[1]))):
        Lavel2=whatcome[1]
        if(reaction[1][x]!=4):
             print(x+1,") ",Lavel2[x][0].capitalize())
             print("A)",Lavel2[x][2][0].capitalize())
             print("B)",Lavel2[x][2][1].capitalize())
             print("C)",Lavel2[x][2][2].capitalize())
             print("D)",Lavel2[x][2][3].capitalize(),"\tAns:-",Lavel2[x][1])
             print("\n")
    print("---------------------------------------------------------------------------------")
    print("Leval 3")
    print("----------------------------------------------------------------------------------")
    for x in range(len((reaction[2]))):
        Lavel2=whatcome[2]
        if(reaction[2][x]!=4):
             print(x+1,") ",Lavel2[2][0].capitalize())
             print("A)",Lavel2[x][2][0].capitalize())
             print("B)",Lavel2[x][2][1].capitalize())
             print("C)",Lavel2[x][2][2].capitalize())
             print("D)",Lavel2[x][2][3].capitalize(),"\tAns:-",Lavel2[x][1])
             print("\n")
    print("---------------------------------------------------------------------------------")
    print("Leval Mains")
    print("----------------------------------------------------------------------------------")
    for x in range(len((reaction[3]))):
        Lavel2=whatcome[3]
        if(reaction[3][x]!=4):
             print(x+1,") ",Lavel2[x][0].capitalize())
             print("A)",Lavel2[x][2][0].capitalize())
             print("B)",Lavel2[x][2][1].capitalize())
             print("C)",Lavel2[x][2][2].capitalize())
             print("D)",Lavel2[x][2][3].capitalize(),"\tAns:-",Lavel2[x][1])
             print("\n")
    input("Click enter")
    os.system("cls")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("            Report")
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("             Leval1")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Total question That Answered\t:\t",performance1["Total question"])
    print("Total right answer\t:\t",performance1["right"])
    print("Total wrong answer\t:\t",performance1["wrong"])
    print("Total skiped question\t:\t",performance1["skiped"])
    print("Marks\t:\t",performance1["Marks"])
    print("Percentage of marks\t:\t",performance1["Pencentage of marks"])
    print("Accuracy\t:\t",performance1["accuracy"],"%")
    print("Time taken\t:\t",performance1["time taken"],"s")
    print("Average no question in a minute\t:\t",int(performance1["Total question"]/performance1["time taken"]*60))
    speed1=performance1["Total question"]/performance1["time taken"]
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("             Leval2")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Total question That Answered\t:\t",performance2["Total question"])
    print("Total right answer\t:\t",performance2["right"])
    print("Total wrong answer\t:\t",performance2["wrong"])
    print("Total skiped question\t:\t",performance2["skiped"])
    print("Marks\t:\t",performance2["Marks"])
    print("Percentage of marks\t:\t",performance2["Pencentage of marks"])
    print("Accuracy\t:\t",performance2["accuracy"],"%")
    print("Time taken\t:\t",performance2["time taken"],"s")
    print("Average no question in a minute\t:\t",int(performance2["Total question"]/performance2["time taken"]*60))
    speed2=performance2["Total question"]/performance2["time taken"]
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("             Leval3")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Total question That Answered\t:\t",performance3["Total question"])
    print("Total right answer\t:\t",performance3["right"])
    print("Total wrong answer\t:\t",performance3["wrong"])
    print("Total skiped question\t:\t",performance3["skiped"])
    print("Marks\t:\t",performance3["Marks"])
    print("Percentage of marks\t:\t",performance3["Pencentage of marks"])
    print("Accuracy\t:\t",performance3["accuracy"],"%")
    print("Time taken\t:\t",performance3["time taken"],"s")
    print("Average no question in a minute\t:\t",int(performance3["Total question"]/performance3["time taken"]*60))
    speed3=performance3["Total question"]/performance3["time taken"]
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("             Jee mains")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Total question That Answered\t:\t",performanceMain["Total question"])
    print("Total right answer\t:\t",performanceMain["right"])
    print("Total wrong answer\t:\t",performanceMain["wrong"])
    print("Total skiped question\t:\t",performanceMain["skiped"])
    print("Marks\t:\t",performanceMain["Marks"])
    print("Percentage of marks\t:\t",performanceMain["Pencentage of marks"])
    print("Accuracy\t:\t",performanceMain["accuracy"],"%")
    print("Time taken\t:\t",performanceMain["time taken"],"s")
    print("Average no question in a minute\t:\t",int(performanceMain["Total question"]/performanceMain["time taken"]*60))
    speedm=performanceMain["Total question"]/performanceMain["time taken"]
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("             Overall Report")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Total question That Answered\t:\t",performanceMain["Total question"]+performance1["Total question"]+performance2["Total question"]+performance3["Total question"])
    print("Total right answer\t:\t",performanceMain["right"]+performance1["right"]+performance2["right"]+performance3["right"])
    print("Total wrong answer\t:\t",performanceMain["wrong"]+performance1["wrong"]+performance2["wrong"]+performance3["wrong"])
    print("Total skiped question\t:\t",performanceMain["skiped"]+performance1["skiped"]+performance2["skiped"]+performance3["skiped"])
    print("Marks\t:\t",performanceMain["Marks"]+performance1["Marks"]+performance2["Marks"]+performance2["Marks"])
    print("Percentage of marks\t:\t",(performanceMain["Pencentage of marks"]+performance1["Pencentage of marks"]+performance2["Pencentage of marks"]+performance3["Pencentage of marks"])/4,"%")
    print("Accuracy\t:\t",(performanceMain["accuracy"]+performance1["accuracy"]+performance2["accuracy"]+performance3["accuracy"])/4,"s")
    print("Time taken\t:\t",performanceMain["time taken"]+performance1["time taken"]+performance2["time taken"]+performance3["time taken"])
    print("Average no question in a minute\t:\t",(speed1+speed2+speed3+speedm)*15)
    print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
    input("Click enter")
    os.system("cls")
    Chemistry()
