import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
from datetime import datetime, date
import datetime


df = pd.read_csv('Update_Data.csv')
df.drop(columns = 'Unnamed: 0', axis=1, inplace = True)

df['joining_date'] = pd.to_datetime(df['joining_date'])
df['relieving_date'] = pd.to_datetime(df['relieving_date'])

def outer(year):
    user_input = input("""
    Select the Option:-
    1. Press 1 to create Yearly data
    2. Press 2. to create Halfely data
    3. Press 3. to create Quaterley Data   
    """)   
    if user_input == '1':
        data_fetch = df.iloc[np.where((df['joining_year']<=year) & (df['relieving_year'] > year))]
        

    elif user_input == '2':
        user_month = input("""
        Select the Option:-
        1. Press 1 for "0-6" Data 
        2. Press 2 for "7-12" Data 
        """)
        
       # data_fetch = df.iloc[np.where((df['joining_year']<=year) & (df['relieving_year'] > year))]
        if user_month == "1":
            start_date = '01-01-{}'.format(year)
            end_date = '30-06-{}'.format(year) 
            mask = (data_fetch['joining_date'] < start_date) & (data_fetch['relieving_date'] >= end_date)
            data_fetch = data_fetch.loc[mask]
            
            
           
        elif user_month == '2':
            start_date = '01-07-{}'.format(year)
            end_date = '31-12-{}'.format(year) 
            mask = (data_fetch['joining_date'] < start_date) & (data_fetch['relieving_date'] >= end_date)
            data_fetch = data_fetch.loc[mask]

            
        else:
            exit()
        
    elif user_input == '3':
        user_month = input("""
        Select the Option:-
        1. Press 1 for "1-3" Data
        2. Press 2 for "4-6" Data
        3. Press 3 for "7-9" Data
        4. Press 4 for "10-12" Data
        """)
        
        #data_fetch = df.iloc[np.where((df['joining_year']<=year) & (df['relieving_year'] > year))]

        if user_month == "1":
            start_date = '01-01-{}'.format(year)
            end_date = '31-03-{}'.format(year) 
            mask = (data_fetch['joining_date'] < start_date) & (data_fetch['relieving_date'] >= end_date)
            data_fetch = data_fetch.loc[mask]
        elif user_month == "2":
            start_date = '01-04-{}'.format(year)
            end_date = '30-06-{}'.format(year) 
            mask = (data_fetch['joining_date'] < start_date) & (data_fetch['relieving_date'] >= end_date)
            data_fetch = data_fetch.loc[mask]
        elif user_month == "3":
            start_date = '01-07-{}'.format(year)
            end_date = '30-09-{}'.format(year) 
            mask = (data_fetch['joining_date'] < start_date) & (data_fetch['relieving_date'] >= end_date)
            data_fetch = data_fetch.loc[mask]
         
        elif user_month == "4":
            start_date = '01-10-{}'.format(year)
            end_date = '31-12-{}'.format(year) 
            mask = (data_fetch['joining_date'] < start_date) & (data_fetch['relieving_date'] >= end_date)
            data_fetch = data_fetch.loc[mask]
         
        else:
            exit()
    
    else:
        exit()
        
    return(data_fetch)

def manual_input(new_df):
    start_date = input("Enter the starting Date: ") # 02-03-2021 format
    end_date = input('Enter the ending Date: ')
    mask = (new_df['joining_date'] < start_date) & (new_df['relieving_date'] >= end_date)
    new_df = new_df.loc[mask]
    
    return(new_df)




def current_working(new_df):
    #new_df = outer(year)
    working = new_df['iscurrentemployee'].value_counts()
    data = working.values
    keys = ['Left','Working']
    # declaring the exploding pie
    explode = [0,0.1]
    #define Seaborn color palette to use
    print(working)
    palette_color = sns.color_palette('deep')
    
    # Plotting data on chart
    plt.figure(figsize=(10,10))
    plt.title("Employee Working in the Company",fontsize = 20, loc = 'center', color = 'purple')
    plt.pie(data, labels=keys, colors= palette_color, explode = explode, autopct = '%.0f%%', textprops={'fontsize':13})
    plt.legend()

    plt.show()
    
# shift

def shift_working(new_df):
    working = new_df['shift'].value_counts()
    data = working.values
    keys = ['Morning', 'Night']
    explode = [0,0.1]
    print(working)
    palette_color = sns.color_palette('colorblind')
    
    # plotting data on chart
    plt.figure(figsize=(10,10))
    plt.title("Shift Of the Employees",fontsize = 20, loc = 'center', color = 'purple')
    plt.pie(data, labels=keys, colors= palette_color, explode = explode, autopct = '%.0f%%',textprops={'fontsize':13})
    plt.legend()
    
    plt.show()

# Gender Ratio
    
def gender_ratio(new_df):
    ratio = new_df['gender'].value_counts()
    data = ratio.values
    keys = ['Male','Female']
    print(ratio)
    palette_color = sns.color_palette('deep')
    
    # plotting data on chart
    plt.figure(figsize=(10,10))
    plt.title("Gender Ratio In Company",fontsize = 20, loc = 'center', color = 'purple')
    plt.pie(data, labels=keys, colors= palette_color, autopct = '%.0f%%',textprops={'fontsize':13})
    plt.legend()

    plt.show()

# Maritals Status:

def marital_status(new_df):
#     new_df = year_wise(year)
    status = new_df['maritalstatus'].value_counts()
    plt.figure(figsize=(13,13))
    print(status)
    labels = status.index
    
    plt.pie(status, labels = labels, autopct='%.0f%%',textprops={'fontsize':12})
    plt.legend()
    plt.show()
    
    
def graduation(new_df):
#     new_df = year_wise(year)
    grad = new_df['graduationtype'].value_counts()
    print(grad)
    plt.figure(figsize=(15,4))
    labels = grad.keys()
    sns.barplot(x = grad.index, y = grad.values, palette='deep')
    plt.legend(labels = grad.index)
    plt.title("Graduation Type For Company", fontsize = 15, loc = "center", color = 'purple')
    plt.xlabel("GraduationType", fontsize=15)
    plt.ylabel("Person's Counts", fontsize=15)
    
def whole_location(new_df):
    #new_df = year_wise(year)
    whole_loc = new_df['college_city'].value_counts()
    print(whole_loc)
    
def college_loc(new_df,college_city):
    coll = new_df[new_df['college_city']==college_city]['Edited_CollegeName'].value_counts()
    print(coll)
   
    
# Hiring on the Particular city or College Bases
def city_month(new_df,college_city):
    hiring_month = new_df[new_df['college_city']==college_city]['joining_month'].value_counts()
    print(hiring_month)
    
    
# Experience:-
## 1) experience those who left the company:-
def exp_left(new_df):
    exl = new_df[new_df['iscurrentemployee']==0]['exp_years'].value_counts()
    print(exl)
    
    
# Department:-
def department_counts(new_df):
    dep = new_df['f_departmentid'].value_counts()
    print(dep)
    
    
# Resign Reason:-
def resign_res(new_df):
    resign = new_df['f_resignreasonid'].value_counts()
    print(resign)
    
    
# Religion:-

def religion_counts(new_df):
    religion = new_df['religionid'].value_counts()
    print(religion)
    
    

year = int(input("Enter the year: "))
new_df=outer(year)                             # outer return store in the new_df
college_city = input("Enter the College City : ")
college_loc(new_df,college_city)




""" This is used to abract the year wise data the final project is for """ 
