import csv
import requests
import pandas
c=pandas.read_csv("https://raw.githubusercontent.com/fivethirtyeight/guns-data/master/interactive_data.csv")
data=c.values
intent=1
gender=2
age=3
race=4
deaths=5
population=6
rate=7
result=[0]*12
result[1]=int(data[0][deaths])
nulls=[0]*11
for row in data:
    result[0]+=int(row[deaths])
    if(row[intent]=="None selected"): nulls[1]+=int(row[deaths]) #intent
    #suicide
    if(row[intent]=="Suicide"): 
        result[2]+=int(row[deaths])
        if(row[gender]=="None selected"): nulls[2]+=int(row[deaths]) #suicide-gender
        #suicide-male
        if(row[gender]=="Male"): 
            result[3]+=int(row[deaths])
            if(row[age]=="None selected"): nulls[3]+=int(row[deaths]) #suicide-male-age
            #suicide-old
            if(row[age]=="65+"): result[4]+=int(row[deaths])
            elif(row[age]=="35 - 64"): result[4]+=int(row[deaths])/2 
    #homicide
    if(row[intent]=="Homicide"):
        result[5]+=int(row[deaths])
        if(row[gender]=="None selected"): nulls[5]+=int(row[deaths]) #homicide-gender
        #homicide-male
        if(row[gender]=="Male"):
            result[6]+=int(row[deaths])
            if(row[age]=="None selected"): nulls[6]+=int(row[deaths]) #homicide-male-age
            #homicide-male-young
            if(row[age]=="Under 15") | (row[age]=="15 - 34") | (row[age]=="5"): 
                result[7]+=int(row[deaths])
                if(row[race]=="None selected"): nulls[8]+=int(row[deaths]) #homicide-male-young-race
                #homicide-male-young-black
                if(row[race]=="Black"): result[8]+=int(row[deaths])
        #homicide-female
        if(row[gender]=="Female"):
            result[9]+=int(row[deaths])
    if(row[intent]=="Accident"):
        result[10]+=int(row[deaths])
    if(row[intent]=="Unknown"):
        result[11]+=int(row[deaths])
        
def percentage(_x,_sum,_null,sum=None,null=None):
    if sum==None:
        return str(_x/(_sum-_null)*100)
    else:
        return str((_x/(_sum-_null))*(_sum/(sum-null))*100)
#2 More than 33000 people shot in US
print(result[0])
print(str(result[1]) +" people shot in US")
#3 We tend to focus on terrorism and mass shootings, police officers killed in the line of duty, and police shootings of civilians

#4 2/3 is Suicide
print(percentage(result[2],result[0],nulls[1])+" are suicides")
#5 85% of suicide are male
print(percentage(result[3],result[2],nulls[2])+" of suiciders are male")
#6 half of the males are 45 older
print(percentage(result[4],result[3],nulls[3],result[2],nulls[2])+" of suiciders are 45+ men")
#7 1/3 is homicide
print(percentage(result[5],result[0],nulls[1])+" are homicides")
#8 50+% is young men
print(percentage(result[7],result[6],nulls[6],result[5],nulls[5])+" of homicide victims are young men") #! 
#9 2/3 of it are black
print(percentage(result[8],result[7],nulls[7])+" of them are black")
#10 1700 women killed each year
print(percentage(result[9],result[5],nulls[5],result[0],nulls[1])+" of homicide victims are women")
#11 remaining are accidents and unknown
print(percentage(result[10],result[0],nulls[1])+" "+percentage(result[11],result[0],nulls[1])+" are accidents and unknown")
