#Importing the Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Importing the dataset
dataset=pd.read_csv("student-math.csv",sep=';')
dataset_arr=np.array(dataset)



#Adding total_grades to the dataframe

final_grade=[0]*395
for i in range(0,395):
    final_grade[i]=dataset_arr[i][30]+dataset_arr[i][31]+dataset_arr[i][32]
dataset['final_grade']=final_grade



#Drop individual grades 
dataset=dataset.drop(['G1','G2','G3'],axis=1)


#Encoding binary data values
dataset['school']=dataset['school'].map({"GP":'0',"MS":'1'})
dataset['sex']=dataset['sex'].map({"F":'0',"M":'1'})
dataset['address']=dataset['address'].map({"U":'0',"R":'1'})
dataset['famsize']=dataset['famsize'].map({"LE3":'0',"GT3":'1'})
dataset['Pstatus']=dataset['Pstatus'].map({"T":'0',"A":'1'})
dataset['schoolsup']=dataset['schoolsup'].map({"no":'0',"yes":'1'})
dataset['famsup']=dataset['famsup'].map({"no":'0',"yes":'1'})
dataset['paid']=dataset['paid'].map({"no":'0',"yes":'1'})
dataset['activities']=dataset['activities'].map({"no":'0',"yes":'1'})
dataset['nursery']=dataset['nursery'].map({"no":'0',"yes":'1'})
dataset['higher']=dataset['higher'].map({"no":'0',"yes":'1'})
dataset['internet']=dataset['internet'].map({"no":'0',"yes":'1'})
dataset['romantic']=dataset['romantic'].map({"no":'0',"yes":'1'})

#Boxplot 
dataset.boxplot(by='studytime',column=['final_grade'],grid=False)

#Scatter Plot between study time and final_grade
plt.scatter(dataset['studytime'],dataset['final_grade'],color='red',s=2,marker="*")
plt.xlabel("Study time(in Hours)")
plt.ylabel("final_grade")








    

    
    
    