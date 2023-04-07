#!/usr/bin/env python
# coding: utf-8

# #### EDA



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# matplotlib inline
# get_ipython().run_line_magic('matplotlib', 'inline')
# import pandas_profiling as pf
import warnings




import plotly.graph_objects as gr
import plotly.express as px
import plotly.figure_factory as ff




df = pd.read_csv('Update_Data.csv')




# df.head()
# print(df.columns)


df.drop(columns='Unnamed: 0', axis=1, inplace = True)
df.describe().T


### Current Working Employee Data



df1 = pd.read_csv('Working_Employee.csv')

a = df1['iscurrentemployee'].value_counts()
pd.DataFrame(a)

print(df.head())
def extract_data(time_frame, x):
    df1 = pd.read_csv('Working_Employee.csv')

    a = df1['iscurrentemployee'].value_counts()
    pd.DataFrame(a)
    if time_frame == "yearly":
        pass
    
    
def get_working_employees(): 
    # declaring the data
    data = [8732, 1965]
    keys = ['Left','Working']

    # declaring the exploding pie
    explode = [0,0.1]
    # define Seaborn color palette to use
    palette_color = sns.color_palette('deep')

    # plotting data on chart
    plt.figure(figsize=(10,10))
    plt.title("Employee Working in the Company",fontsize = 20, loc = 'center', color = 'purple')
    plt.pie(data, labels=keys, colors= palette_color, explode = explode, autopct = '%.0f%%', textprops={'fontsize':13})

    # displaying chart
    plt.show()

    # # * From this Pie chart we observe that Only 18% employee is still working in the company 

# get_working_employees()

def get_shift_percent():
    shift_counts = df1['shift'].value_counts()
    shift_counts.values

    # declaring the data
    data = shift_counts.values
    keys = ['Moring','Night']

    # declaring the exploding pie
    explode = [0,0.1]
    # define Seaborn color palette to use
    palette_color = sns.color_palette('colorblind')

    # plotting data on chart
    plt.figure(figsize=(10,10))
    plt.title("Shift Of the Employees",fontsize = 20, loc = 'center', color = 'purple')
    plt.pie(data, labels=keys, colors= palette_color, explode = explode, autopct = '%.0f%%',textprops={'fontsize':13})

    # displaying chart
    # plt.show()

# get_shift_percent()
    # * From the Data we observe that only 6% from current employee is doing night shift



def get_gender_ratio():
    mf = df1['gender'].value_counts()
    pd.DataFrame(mf)

    # declaring the data
    data = mf.values
    keys = ['Male','Female']

    # declaring the exploding pie
    #explode = [0,0.1]
    # define Seaborn color palette to use
    palette_color = sns.color_palette('deep')

    # plotting data on chart
    plt.figure(figsize=(10,10))
    plt.title("Gender Ratio In Company",fontsize = 20, loc = 'center', color = 'purple')
    plt.pie(data, labels=keys, colors= palette_color, autopct = '%.0f%%',textprops={'fontsize':13})

    # displaying chart
    plt.show()


def get_age_distribution():
    fig = px.histogram(df1, x = 'age', nbins= 20, title= 'Age Distribution in the Company',text_auto=True)
    fig.show()

get_age_distribution()

def get_marital_status():
    stat = df1['maritalstatus'].value_counts()
    pd.DataFrame(stat)

    plt.figure(figsize=(13,13))
    ax = stat
    labels = ax.index
    plt.pie(ax, labels = labels, autopct='%.0f%%',textprops={'fontsize':12})
    plt.legend()
    plt.show()







# ### Graduation:-

# #### a) From both left and current working employee


grad = df['graduationtype'].value_counts()[:7]
pd.DataFrame(grad)


plt.figure(figsize=(15,4))
labels = grad.keys()
sns.barplot(x = grad.index, y = grad.values, palette='deep')
plt.legend(labels = grad.index)
plt.title("Graduation Type For Company", fontsize = 15, loc = "center", color = 'purple')
plt.xlabel("GraduationType", fontsize=15)
plt.ylabel("Person's Counts", fontsize=15)


# ### Location 
# * This is location on basis of College city
# * In this we consider [both data]--> left as wells as working employee
# * In case "Rajasthan" state we classify the data on the basis of city 
# * And for the other we listed only state name and consider the most populated region
# * Mandsaur and Neemuch has larger counts in MP state --> main reason to seprate the data

loca = df['college_city'].value_counts()[:30]
pd.DataFrame(loca)


# * From above tabel we know that there is large no. of Employee is Hire From Udaipur City 
# * Let's Visulaize from 3 rd row --> From Jaipur


loc1 = loca[2:]


plt.figure(figsize=(15,10))
ax = sns.barplot(x = loc1.index, y = loc1.values)
plt.title("Selected Student From Different Area",fontdict={'color':'blue','size':15})
plt.ylabel("Employee Counts", fontdict={'size':15})
plt.xlabel("Location", fontdict={'size':15})
plt.xticks(rotation = 90)
# plt.show()


# ### College

# * From above Data Let's Categorise the Data on the Bases of City 

# ##### 1) Jaipur


jai = df[df['college_city']=='Jaipur']['Edited_CollegeName'].value_counts()[:15]
pd.DataFrame(jai)

plt.figure(figsize=(14,10))
sns.barplot(x = jai.index, y = jai.values, palette='deep')
plt.title("Employee From the Jaipur College", fontsize = 15, loc = "center", color = 'purple')
plt.ylabel("Employee_Counts", fontsize=15)
plt.xlabel("Jaipur College", fontsize=15)
plt.xticks(rotation = 90)
# plt.show()


# ##### 2) Nathdwara

nath = df[df['college_city']=='Nathdwara']['Edited_CollegeName'].value_counts()
pd.DataFrame(nath)

plt.figure(figsize=(14,8))
sns.barplot(x = nath.index, y = nath.values, palette='deep')
plt.title("Employee From the Nathdwara College", fontsize = 15, loc = "center", color = 'purple')
plt.ylabel("Employee_Counts", fontsize=15)
plt.xlabel("Nathdwara College", fontsize=15)


# ##### 3) Chittorgarh

chitt = df[df['college_city']=='Chittorgarh']['Edited_CollegeName'].value_counts()
pd.DataFrame(chitt)

plt.figure(figsize=(14,10))
sns.barplot(x = chitt.index, y = chitt.values, palette='deep')
plt.title("Employee From the Chittorgarh College", fontsize = 15, loc = "center", color = 'purple')
plt.ylabel("Employee_Counts", fontsize=15)
plt.xlabel("Chittorgarh College", fontsize=15)
plt.xticks(rotation = 90)
# plt.show()


# ### Udaipur College

udai = df[df['college_city']=='Udaipur']['Edited_CollegeName'].value_counts()[:40]
pd.DataFrame(udai)

# * Top 40 Colloege in the list


udai = df[df['college_city']=='Udaipur']['Edited_CollegeName'].value_counts()[:15]


plt.figure(figsize=(14,10))
sns.barplot(x = udai.index, y = udai.values, palette='deep')
plt.title("Employee From the Udaipur College", fontsize = 15, loc = "center", color = 'purple')
plt.ylabel("Employee_Counts", fontsize=15)
plt.xlabel("Udaipur City College", fontsize=15)
plt.xticks(rotation = 90)
# plt.show()


# * Top 15 College in Udaipur Whose Student are Working the Arcgate Company

college = df['Edited_CollegeName'].value_counts()


# Top 50 Counts()
pd.DataFrame(college)[:50]

## ==========================================================
### Hiring Data
## ==========================================================

###### Hiring On the basis of Year

join = pd.DataFrame(df['joining_year'].value_counts())
join

# * Form this we Clearley observe in 2017 Most hiring Year:-

plt.figure(figsize=(15,5))
sns.countplot(x = df['joining_year'], data = df)
plt.title("Hiring On The Bases OF Years")
plt.xlabel("Joining Year")
plt.ylabel("Employee Hiring Counts")
plt.xticks(rotation = 90)
# plt.show()


# #### Hiring On the Bases of Month [Total_counts]

mt = pd.DataFrame(df['joining_month'].value_counts()).reset_index()
mt = mt.rename(columns = {'index':'Joining_Months','joining_month':'counts'})
mt['Joining_Months'] = mt['Joining_Months'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'])

plt.figure(figsize=(15,5))
sns.barplot(x = mt.Joining_Months ,y = mt.counts, palette='deep')
plt.title("Hiring On The Bases OF Month")
plt.xlabel("Joining Month")
plt.ylabel("Employee Hiring Counts")
# plt.show()


# ### Joining on the Bases of Particular Months  [Joining Month --2017]

py = pd.DataFrame(df[df['joining_year']== 2019]['joining_month'].value_counts()).reset_index()
py = py.rename(columns = {'index':'Joining_Months','joining_month':'counts'})
py['Joining_Months'] = py['Joining_Months'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'])

plt.figure(figsize=(15,8))
sns.barplot(x = py.Joining_Months, y = py.counts, palette='deep')
plt.title("Hiring Year 2017 With  Month Counts")
plt.xlabel("Joining Month")
plt.ylabel("Employee Hiring Counts")
# plt.show()


# # ### Hiring on the perticular City or College Bases


hp = pd.DataFrame(df[df['college_city']=='Nathdwara']['joining_month'].value_counts())
hp = hp.reset_index()
hp = hp.rename(columns = {'index':'months','joining_month':'Counts'})
hp['months'] = hp['months'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'])

plt.figure(figsize=(15,8))
sns.barplot(x = hp.months, y = hp.Counts, palette='deep')
plt.title("Hiring Particular City and Overall Months Counts --'Nathdwara'", fontsize = 15, loc = "center", color = 'purple')
plt.xlabel("Joining Month",fontsize = 13, loc = "center")
plt.ylabel("Employee Hiring Counts",fontsize = 13, loc = "center")
# plt.show()


# ### Let's Find Out For the Particular College in Nathdwara

nat = pd.DataFrame(df[df['college_city']=='Nathdwara']['Edited_CollegeName'].value_counts()).reset_index()
nat = nat.rename(columns = {'index':'college','Edited_CollegeName':'counts'})
# let's take the Student of SITE

site = pd.DataFrame(df[df['Edited_CollegeName']=='SITE, Nathdwara']['joining_month'].value_counts()).reset_index()
site = site.rename(columns = {'index':'Months','joining_month':'Counts'})
site


plt.figure(figsize=(15,8))
sns.barplot(x = site.Months, y = site.Counts, palette='deep')
plt.title("Hiring From Site College --'Nathdwara'", fontsize = 15, loc = "center", color = 'purple')
plt.xlabel("Joining Month",fontsize = 13, loc = "center")
plt.ylabel("Employee Hiring Counts",fontsize = 13, loc = "center")
# plt.show()


# ### Experience:-

# * Experience  on the Bases of Years--> From the Total DataSet [left+ working emp]

expy = df['exp_years'].value_counts()
pd.DataFrame(expy)


# * 0 year  mean it contain both [left + current] employee data, it's mean it include the current joining 2022 year employee also.

# ######  Let's explore the experience Those who left the company :-

exl = df[df['iscurrentemployee']==0]['exp_years'].value_counts()
pd.DataFrame(exl)


# * From Data we can easily Conclude that Employee Left the company within a month, or after few year 
# 

# ###### Let's Understand On The Bases OF 24 Months 

mon = pd.DataFrame(df[df['iscurrentemployee']==0]['exp_month'].value_counts()).reset_index()
mon = mon.rename(columns = {'index':'month','exp_month':'counts'})


mone = mon.sort_values(by='month')[2:27]
mone


# * From This Tabel we can easily Conclude that :- Employee Left The company in the inital phase of the joining[1-5] month and left after complete the 1 year in the company  [12-17] 
# 

plt.figure(figsize=(20,10))
sns.barplot(x = mone.month, y = mone.counts, palette='deep')
plt.title("Observation 1-24 Month", fontsize = 15, loc = "center", color = 'purple')
plt.ylabel("Experience_Counts", fontsize=15)
plt.xlabel("Months", fontsize=15)
# plt.show()


# ### Every year Joining Data

df['joining_year'].value_counts()


# ###### Joining Year merge the Data with the Month

per_month_year = df.groupby('joining_year')['joining_month'].value_counts()
joining = pd.DataFrame(per_month_year)


joining = joining.rename(columns={'joining_month':'counts'})
joining


joining.loc[2019]


df.joining_year.unique()


# * We Have the Data From 2015 to 2022 
# * let's make function to show the data in b/w


def join(x,y):
    for i in range(x,y+1):
        print("The Data of Particular Year : {}".format(i))
        i = joining.loc[i]
        print(i)


join(2019,2021)


joining_2005 = joining.loc[2005]
joining_2006 = joining.loc[2006]
joining_2007 = joining.loc[2007]
joining_2008 = joining.loc[2008]
joining_2009 = joining.loc[2009]
joining_2010 = joining.loc[2010]
joining_2011 = joining.loc[2011]
joining_2012 = joining.loc[2012]
joining_2013 = joining.loc[2013]
joining_2014 = joining.loc[2014]
joining_2015 = joining.loc[2015]
joining_2016 = joining.loc[2016]
joining_2017 = joining.loc[2017]
joining_2018 = joining.loc[2018]
joining_2019 = joining.loc[2019]
joining_2020 = joining.loc[2020]
joining_2021 = joining.loc[2021]
joining_2022 = joining.loc[2022]


a = joining_2021
a = a.reset_index()
a['joining_month'] = a['joining_month'].replace([1,2,3,4,5,6,7,8,9,10,11,12],['Jan','Feb','Mar','Apr','May','June','July','Aug','Sep','Oct','Nov','Dec'])


plt.figure(figsize=(15,8))
sns.barplot(x = a.joining_month, y = a.counts, palette='deep')
plt.title("Hiring Year With  Month Counts",color='purple', loc = "center", fontsize = 15 )
plt.xlabel("Joining Month", fontsize = 15, loc = "center", color = 'black')
plt.ylabel("Employee Hiring Counts",fontsize = 15, loc = "center", color = 'black')
# plt.show()


# ### Relieving Data
# * This data study, On the bases of those Employee Who Leave the Company 
# * df2 = Those who left the company
# * df1 = Current data


df2 = df[df['iscurrentemployee']==0]


rev_yr = df2['relieving_year'].value_counts()
rev_yr= pd.DataFrame(rev_yr)
rev_yr



plt.figure(figsize=(15,5))
sns.countplot(x = df2['relieving_year'], data = df2)
plt.title("Employee Left the Company", color='purple', loc = "center", fontsize = 15)
plt.xlabel("Relieving Year", color='black', loc = "center", fontsize = 13)
plt.ylabel("Employee Relieving Counts", color='black', loc = "center", fontsize = 13)
# plt.show()


# ###### Relieving Year merge the Data with the Month

month_rel = df.groupby('relieving_year')['relieving_month'].value_counts()
reliev = pd.DataFrame(month_rel)


relieving = joining.rename(columns={'relieving_month':'counts'})
relieving


def rel(x,y):
    for i in range(x,y+1):
        print("The Data of Particular Year : {}".format(i))
        i = relieving.loc[i]
        print(i)



rel(2020,2022)


relieving_2005 = relieving.loc[2005]
relieving_2006 = relieving.loc[2006]
relieving_2007 = relieving.loc[2007]
relieving_2008 = relieving.loc[2008]
relieving_2009 = relieving.loc[2009]
relieving_2010 = relieving.loc[2010]
relieving_2011 = relieving.loc[2011]
relieving_2012 = relieving.loc[2012]
relieving_2013 = relieving.loc[2013]
relieving_2014 = relieving.loc[2014]
relieving_2015 = relieving.loc[2015]
relieving_2016 = relieving.loc[2016]
relieving_2017 = relieving.loc[2017]
relieving_2018 = relieving.loc[2018]
relieving_2019 = relieving.loc[2019]
relieving_2020 = relieving.loc[2020]
relieving_2021 = relieving.loc[2021]
relieving_2022 = relieving.loc[2022]


b = relieving_2017
b


plt.figure(figsize=(15,8))
sns.barplot(x = b.index, y = b.counts, palette='deep')
plt.title("Relieving Year With  Month Counts",color='purple', loc = "center", fontsize = 15 )
plt.xlabel("Relieving Month", fontsize = 15, loc = "center", color = 'black')
plt.ylabel("Employee Relieving Counts",fontsize = 15, loc = "center", color = 'black')
# plt.show()


# ### Department 

# * Current Employee Data with Distribution in Department

dep = df1['f_departmentid'].value_counts()


plt.figure(figsize=(13,13))
ax = dep
labels = ['KPO','General','Software','Administrator','IT','Electrical']
plt.pie(ax, labels = labels, autopct='%.0f%%',textprops={'fontsize':13})
plt.legend(loc = 'upper right')
# plt.show()


department = pd.DataFrame(dep).reset_index()
department = department.rename(columns = {'index':'Department','f_departmentid':'Counts'})
department['Department'] = department['Department'].replace([5,6,1,2,9,4],['KPO','General','Software','Administrator','IT','Electrical'])
department


# ### Resign Reason

resign = df2['f_resignreasonid'].value_counts()


plt.figure(figsize=(15,15))
ax = resign
labels = ['Not Mension','Personal Reason','Family Reason','Absconding','Higher Studies','Career Prospect','Performance Issue','Medical Issue','Low Requirement','Relocation','Marriage','Termination','Demise']
plt.pie(ax, labels = labels, autopct='%.0f%%',textprops={'fontsize':10})
plt.legend(loc = 'upper right')
# plt.show()


resign = pd.DataFrame(resign).reset_index()
resign = resign.rename(columns = {'index':'Reason','f_resignreasonid':'Counts'})
resign['Reason'] = resign['Reason'].replace([0.0, 6.0, 4.0, 7.0, 2.0, 3.0, 8.0, 9.0, 10.0, 11.0, 1.0, 5.0,12.0],['Not Mension','Personal Reason','Family Reason','Absconding','Higher Studies','Career Prospect','Performance Issue','Medical Issue','Low Requirement','Relocation','Marriage','Termination','Demise'])
resign


# ### Religion

religion = df1['religionid'].value_counts()
plt.figure(figsize=(15,15))
ax = religion
labels = ['Hindu','Muslim','Jain','Data Not Found','Sikh','Christian','Other Religion']
plt.pie(ax, labels = labels, autopct='%.0f%%',textprops={'fontsize':11})
plt.legend(loc = 'upper right')
# plt.show()


religion = pd.DataFrame(religion).reset_index()
religion = religion.rename(columns = {'index':'religion','religionid':'Counts'})
religion['religion'] = religion['religion'].replace([1.0, 2.0, 6.0, 0.0, 4.0, 3.0, 7.0],['Hindu','Muslim','Jain','Data Not Found','Sikh','Christian','Other Religion'])
religion

