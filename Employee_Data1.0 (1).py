


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import pandas_profiling as pf
import plotly.offline as py
import warnings
warnings.filterwarnings('ignore')


# In[428]:


from datetime import datetime, date
import datetime


# In[429]:


df = pd.read_csv('employee- data-1671012257799.csv')


# In[430]:


df.head()


# In[431]:


df.shape


# In[432]:


df.columns


# In[433]:


# Panda Profiling
#pf.ProfileReport(df)


# In[434]:


df.dtypes


# In[435]:


df.info()


# In[436]:


df.isnull().sum()


# In[437]:


df['higherqualification'].value_counts()[:20]


# In[438]:


df['higherqualification'].value_counts().tail(25)


# In[439]:


df['f_designationid'].value_counts()[:50]


# In[440]:


df['f_designationid'].value_counts().tail(25)


# In[441]:


df['totalexperince'].value_counts()[:30]


# In[442]:


df['relevantexperience'].value_counts()


# In[443]:


df['englishmarks'].value_counts()


# In[444]:


df['gender'].value_counts()


# In[445]:


df['collegename'].value_counts()[:50]


# In[446]:


df['graduationtype'].value_counts()


# In[447]:


df['maritalstatus'].value_counts()


# In[448]:


df['typingspeedtype'].value_counts()


# In[449]:


df['marks'].value_counts()


# In[450]:


df['anniversarydate'].value_counts()[:25]


# In[451]:


df['actualjoiningdate'].value_counts()


# In[452]:


df['f_resignreasonid'].value_counts()


# In[453]:


df['resigndate'].value_counts()


# In[454]:


df['shift'].value_counts()


# In[455]:


df['actualjoiningdate'].dtype


# In[456]:


df['actualjoiningdate'][1]


# In[457]:


a = df['actualjoiningdate'][1].split()
a


# In[458]:


a[0]


# In[459]:


df.shape[0]


# In[460]:


for i in range(df.shape[0]):
    df['actualjoiningdate'][i]=df['actualjoiningdate'][i].split()[0]


# In[461]:


df['actualjoiningdate'][:10]


# In[462]:


df['actualjoiningdate'].dtype


# In[463]:


df['joining_date'] = pd.to_datetime(df['actualjoiningdate'])


# In[464]:


df['joining_date'][1]


# In[465]:


df['relievingdate'].dtype


# In[466]:


df['relievingdate'].value_counts()


# In[467]:


# this 1/1/1900 + Null + are still working person in the company 


# In[468]:


df['relievingdate'][7]


# In[469]:


df[df['relievingdate']== '1/1/1900 0:00']


# In[470]:


df[df['relievingdate'].isna()]


# In[471]:


df['relievingdate'].dtype


# In[472]:


df['relievingdate']


# In[473]:


df['relievingdate'].isna().sum()


# ### Task:- 1  
# ###### 1) convert the joining date into datetime format
# 
# 
# * 2) "is current" --> 0 - out 
#               1- in 
#             
#  * if 1 then it contain the (null value + 01-01-1900 + Blank)---> convert to "present date" (16-12-2022)
#  
#  * if 0 then it contain all date format value 
#  
# ###### 2) Convert the  relievingDate data into Datetime format
#  

# In[474]:


########################################################


# ### Task:-2    Experience
# 
# ###### 1) Now from JoiningDate --> joining month + joining year
# ###### 2)  relievingdate --> relieving month + relieving year
# ###### experience --> if "iscurrent  = 0" relieving date - joining date 
# ###### if  "iscurrent = 1"  current date - joining date
# 

# In[475]:


########################################################


# In[476]:


df['joining_date'].dtype


# In[477]:


df['joining_date'].dt.year


# In[478]:


df['iscurrentemployee'].value_counts()


# ##### a = working data
# 

# In[479]:


a = df[df['iscurrentemployee']==1]['relievingdate']


# In[480]:


a.value_counts()


# In[481]:


b = df[df['iscurrentemployee'] == 0 ]['relievingdate']
b.value_counts()


# #### Note:-
# * In case "a"--> contain working employee with date "01-01-1900 00:00"---> 1225
# * In case "b"---> contain non-working employee that left the company and data is not found due arccrm data making time.
# * for "a" we can change date into "01-01-2023"
# * for "b" we can delete the data .

# In[482]:


df['relievingdate'].dtype


# In[483]:


type(df['relievingdate'][0])


# In[484]:


a = df[(df['iscurrentemployee']==1) & (df['relievingdate'] =='01-01-1900 00:00')]
a.index


# In[485]:


## Change/ replace on the bases indexes:-

df.loc[a.index,'relievingdate']='01-01-2023'


# In[486]:


df['relievingdate'].value_counts()


# In[487]:


a = a[["iscurrentemployee","relievingdate"]]
a


# * For (318) which not present in the company so we can remove the data form sheet.

# In[488]:


b = df[(df['iscurrentemployee']== 0 ) & (df['relievingdate'] == '01-01-1900 00:00' )]
b.index


# In[489]:


df.drop(index=b.index, axis= 0 , inplace = True)


# In[490]:


a.shape
# according to data 1966 employee are working in the company


# ##### b = left data
# 

# In[491]:


df['iscurrentemployee'].dtype


# In[492]:


b = df[df['iscurrentemployee'] == 0 ]


# In[493]:


b['relievingdate'].value_counts()


# In[494]:


# 1/1/1900 in this case arccrm data is form in the 2013-2014 and there is no data available 


# In[495]:


df[['iscurrentemployee','relievingdate']][:5]


# In[496]:


b.shape


# In[497]:


b['iscurrentemployee'].value_counts()


# In[498]:


df['relievingdate'].value_counts()[:10]


# In[499]:


# in case it not show the null value it also contain the null value


# ### Convert into Datetime where it include the null value
# * df['relieving_date'] = pd.to_datetime(df['relievingdate'],errors = 'coerce')

# In[500]:


df['relievingdate'] is np.nan


# In[501]:


# in data 7 index value contain the null value in the relievingdate\
df.loc[10]['relievingdate']


# In[502]:


y = df[df['resourceid']==10197]['relievingdate']


# In[503]:


y


# In[504]:


y.values


# In[505]:


y.values[0]


# In[506]:


z = df[df.isna()['relievingdate']]['relievingdate']
z


# ##### Relievingdate:- replace null value , '1/1/1900 0:00' , with ------> Present Date(01-01-2023)

# In[507]:


type(df['relievingdate'].iloc[7])


# it show that  data contain in floating type
# 

# In[508]:


df['relievingdate'].head(10)


# In[509]:


### Replace the null value with '1/1/1900 0:00'


# In[510]:


df['relievingdate'].replace(float(np.nan),'1/1/1900 0:00',inplace=True)


# In[511]:


df['relievingdate'].head(10)


# In[512]:


df['relievingdate'].value_counts()


# * 2284 are still working employee in the company 

# #### Note:-
# * 1/1/1900 0:00  in relievingdate it's mean the no. of employee current working in the company 
# * 1/1/1900 0:00  change the date into 1/1/2023 --> it help us to find out the experience 
# * Convert relieving_date into datetime format

# In[513]:


df["relieving_date"] = df['relievingdate'].copy()


# In[514]:


df['relieving_date'].value_counts()


# In[515]:


type(df['relieving_date'][1])


# In[516]:


df['relieving_date'].replace(str('1/1/1900 0:00'),'01-01-2023', inplace = True)


# In[517]:


df['relieving_date'].value_counts()


# In[518]:


df['relieving_date'] = pd.to_datetime(df['relieving_date'])


# In[519]:


df['relieving_date'].dtype


# In[520]:


df[['joining_date','relieving_date']]


# In[ ]:





# ### Drop the unwanted or notneeded columns:-

# In[521]:


df.columns


# In[522]:


df.drop(columns=['accesscardserialno','accesscardno','isfandfdone','resigndate','eye_sight','anniversarydate','modifiedby','createddate','modifieddate','referralamount','postgraduate','undergraduate','diplomaholder','cardno','empuniqueid','createdby','arcgateexperience','arcinterviewid','employeeid','f_addresstypeid','totalexperince', 'relevantexperience','fname', 'lname', 'fathername'], inplace= True, axis= 1 )


# In[523]:


pd.DataFrame(df)


# ### Seprate the Month and year of ----[joining and relieving]

# In[524]:


df['joining_month'] = df['joining_date'].dt.month


# In[525]:


df['joining_year'] = df['joining_date'].dt.year


# In[526]:


df['joining_year'].value_counts()


# In[527]:


df[df['joining_year'] == 2023]


# * This exception and outlier case

# In[528]:


df['joining_date'].value_counts()


# * in case joining date shows :- 1900-01-01 and company start in 2005 this is employee which left the company before arccrm made (2013-14) so there is no data of joining

# In[529]:


j = df[df['joining_year']== 1900]['resourceid']


# In[530]:


j.reset_index()


# In[531]:


j.index


# In[532]:


df[df['joining_year'] == 2023]['joining_date']


# ###### Remove the Row :-
# * which contain j0ining date --1/1/1900
# * joining_year -- 2023 year

# In[533]:


df.drop(index= j.index, axis= 0 ,inplace= True)


# In[534]:


df.drop(index=2213, axis = 0, inplace = True)


# In[535]:


df.joining_date.value_counts()


# In[536]:


df.columns


# In[537]:


df['relieving_month'] = df['relieving_date'].dt.month
df['relieving_year'] = df['relieving_date'].dt.year


# In[538]:


df[['joining_month', 'joining_year','relieving_month','relieving_year']][:10]


# ### Date of Birth
# * convert into datetime :-
# * after convert into datetime format find the current age 

# In[539]:


# convert the age into datetime format
df['dob'] = pd.to_datetime(df['dob'])


# In[540]:


df['dob'].value_counts()


# In[541]:


d = df[df['dob']== '1900-01-01']['dob']


# In[542]:


d = pd.DataFrame(d).reset_index()
d.head()


# In[543]:


d['index'].head()


# In[544]:


df.drop(index= d['index'], axis=0, inplace = True)


# In[545]:


df['dob'].value_counts()


# In[546]:


df['dob'].isna().sum()


# * It mean it contain 0 null element

# In[547]:


now = pd.Timestamp('now')
#df['dob'] = pd.to_datetime(df['dob'], format='%m%d%y')    # 1
df['dob'] = df['dob'].where(df['dob'] < now, df['dob'] -  np.timedelta64(100, 'Y'))   # 2
df['age'] = (now - df['dob']).astype('<m8[Y]')    # 3
df.head()


# ### Joining Age && Relieving age && Experience in present Company

# ###### Experience :-
# * Days, Months, Years

# In[548]:


# Days
df['exp_days'] = df['relieving_date']-df['joining_date']


# In[549]:


# Months
df['exp_month'] = df['exp_days']/np.timedelta64(1,'M')


# In[550]:


df['exp_month'] = df['exp_month'].astype(int)
df['exp_month']


# In[551]:


# Years
df['exp_years'] = df['exp_days']/np.timedelta64(1,'Y')


# In[552]:


df['exp_years'] = df['exp_years'].astype(int)
df['exp_years']


# ### Joining Age && Relieving age

# In[553]:


# joining age:-\
df['joining_age'] = df['joining_date']-df['dob']
df['joining_age'] = df['joining_age']/np.timedelta64(1,'Y')
df['joining_age']


# In[554]:


df['joining_age'] = df['joining_age'].astype(int)
df['joining_age'][:5]


# In[555]:


# Relieving Age:-
df['relieving_age'] = df['relieving_date']-df['dob']
df['relieving_age'] = df['relieving_age']/np.timedelta64(1,'Y')
df['relieving_age'] = df['relieving_age'].astype(int)
df['relieving_age'][:5]


# In[556]:


df


#  ### Departmentid

# In[557]:


df['f_departmentid'].value_counts()

1	SOFTWARE	
2	ADMINISTRATOR	
4	ELECTRICAL	
5	KPO	
6	GENERAL	
9	IT	
10	BUSINESS DEVELOPMENT	
11	OPERATION	
# In[558]:


dep_id = df[df['iscurrentemployee']==1]['f_departmentid']
pd.DataFrame(dep_id.value_counts())


# ### Designation

# In[559]:


df['f_designationid'].value_counts()

designationid	f_departmentid	designation
1	1	Senior Software Developer
2	1	System Architect
4	2	Manager HR
5	2	Manager
6	1	Project Manager
10	5	Research Analyst
11	5	Sr. Research Analyst
12	4	Electrician
15	1	Senior Web Designer
16	1	Web Designer
17	6	Housekeeper
18	6	Guard
19	9	Network Administrator
20	9	Sr. Network Administrator
21	1	Associate Design Architect
22	1	Associate Project Manager
23	1	Associate Technical Architect
24	1	Junior Software Testing
25	1	Linus System Administrator
26	1	Mobile Application Developer Symbian
27	1	Mobile Software Developer
30	1	Senior Designer
31	1	Senior Mobile Software Developer
33	1	Senior Software Engineer
35	1	Senior Software QA Engineer
36	1	Senior Software Testing Engineer
37	1	Senior Technical Architect
38	1	Software Developer
39	1	Software Developer PHP
40	1	Software Test Engineer
41	1	Software Testing Engineer
42	1	Software Testing Analyst
45	1	Team Lead
46	1	Team Leader-Web Design
47	1	Technical Architect
48	1	Trainee-Software Developer
49	5	Asst. Project Lead
50	5	Data Analyst
51	5	Project Lead
52	5	Quality Analyst
53	5	Sr. Data Analyst
54	5	Sr. Quality Analyst
55	5	Team Leader
56	5	Content Writer
57	2	Front Office
58	5	General Manager-KPO Operations
59	5	Manager-KPO Operations
60	5	Senior Executive-BPO
61	5	Senior QA - Calling
62	5	Senior QA - Research
63	2	Store Keeper
64	9	Senior System Administrator
65	6	Driver
66	5	Associate - Learning & Development
67	5	Senior Training Executive
68	5	Senior Training Associate
69	6	Peon
70	2	General Manager-Finance & Accounts
71	2	Accounts Executive
72	9	System Administrator
73	6	Security Guard
74	6	Security Officer
75	4	Electrical Engineer
76	4	Electrical & Maintenance Engineer
77	10	Business Development Manager
78	2	General Manager-HR
79	5	Asst. Training Lead
80	5	Training lead
81	5	Assistant Project Lead
82	5	Senior Quality Analyst
83	5	Senior Research Analyst
84	5	Subject Matter Expert
85	2	Admin
87	5	Project Manager
88	5	Call Centre Executive
89	2	Manager - Resource Allocation & Project Coordination
90	1	Senior Software Developer PHP
91	1	Senior Design Architect
92	2	Assistant Manager HR
93	6	CCTV Operator
94	2	Senior HR Executive
95	2	Manager- Training & Talent Development
96	2	Training Associate
97	2	Manager- Recruitment & Public Relations
98	2	HR Executive
99	1	Senior User Experience Designer
100	9	Senior DevOps Engineer
101	11	Operations Manager
102	5	Customer Support Executive
103	5	Tableau Analyst
104	2	Assistant Manager - Learning & Development
105	2	Associate - Learning & Development
106	1	Digital Marketing Consultant
107	6	Carpenter
108	6	Security Supervisor
109	6	Office Boy
110	4	AC Technician
111	1	Front End Developer
112	5	Senior Associate - Learning & Development  
113	2	SME- Learning & Development  
114	6	Fire & Safety Officer
115	6	Plumber
116	6	Field Security Officer
117	6	F&B Executive
118	9	DevOps Engineer
119	6	Fire & Safety Executive
120	5	Copy Editor
121	1	Manager - Technology Services
122	9	Desktop Engineer & Inventory Management
123	6	Gardener
124	6	Gunman
125	2	Manager (MIS)
126	5	Accounting Associate
127	5	Graphic Designer
128	5	Video Editor
129	2	Recreation Associate
130	1	Software Engineer
132	5	Senior Account Executive
133	5	Accounts Executive
134	9	Junior Linux Admin
135	6	Housekeeping Supervisor
136	9	Hardware Engineer
137	5	Assistant Manager-Training
138	5	Senior Project Manager
139	5	Training Specialist
140	6	Cafeteria Supervisor
141	2	Store Keeping Executive
142	2	Senior Accounts Executive
143	1	Senior QA Engineer
144	1	Senior Frontend Architect
145	1	QA Engineer
146	1	Frontend Engineer
147	1	Senior QA Engineer
148	1	Senior UX Designer
149	1	Associate Frontend Architect
150	1	QA Automation Engineer
151	1	Associate QA Manager
152	1	QA Manager
153	1	Senior QA Automation Engineer
154	1	QA Engineer
155	9	Sr. Network Solution Engineer
156	9	Solution Architect
157	1	QA Lead
158	9	Network Engineer
159	2	Senior Manager Finance
160	2	HR Assistant
# In[560]:


desig_id = df[df['iscurrentemployee']==1]['f_designationid'].value_counts()
pd.DataFrame(desig_id)


# ### Gender

# In[561]:


df['gender'].value_counts()


# ngender = df[df.isna()['gender']]['gender']
# ngender.index

# In[562]:


df['relieving_date'].value_counts()


# In[563]:


df[:5]


# #### Experience Year

# In[564]:


df.exp_years.value_counts()


# In[565]:


t = df[df['exp_years']== -1]
t[['joining_date','relieving_date','iscurrentemployee']]


# In[566]:


# this is exception case we can remove the data
df.drop(index=3020, axis= 0 , inplace = True)


# In[567]:


df.isna().sum()


# In[568]:


df['higherqualification'].nunique()


# ### Fill na  

# #### Marital_na

# In[569]:


marital_na = df[df.isna()['maritalstatus']]['maritalstatus']


# In[570]:


marital_na.index


# In[571]:


df.loc[marital_na.index,'maritalstatus']= 'No_Entry'


# In[572]:


type(df['maritalstatus'][1])


# In[573]:


df.maritalstatus.value_counts()


# #### Graduation Type

# In[574]:


graduation_na = df[df.isna()['graduationtype']]['graduationtype']
graduation_na


# In[575]:


df.loc[graduation_na.index,'graduationtype']= "PrusingDegree or X or XII"


# In[576]:


type(df['graduationtype'][1])


# In[577]:


df['graduationtype'].value_counts()


# #### Refrence by 

# In[578]:


df['referencedby'].value_counts()


# In[579]:


referenceby_na = df[df.isna()['referencedby']]['referencedby']
referenceby_na


# In[580]:


df.loc[referenceby_na.index, "referencedby"] = 'Not_Refered'


# In[581]:


df['referencedby'].value_counts()


# In[582]:


df.isna().sum()


# In[583]:


df['pastemployer'].value_counts()


# In[584]:


df[df['pastemployer']=='Accenture']


# In[585]:


df.drop(columns=['higherqualification', 'telephonicinterview','personalinterview','englishmarks','internetmarks','pastemployer','typingspeed','typingspeedtype','accuracy','marks','exceltest','celebrationdate'], axis=1 , inplace= True)


# In[586]:


df.drop(columns=['f_breaksetid'], axis = 1, inplace = True)


# In[587]:


df.isna().sum() 


# #### Generalshift  

# In[588]:


df['generalshift'].value_counts()


# * In case 0.0 is default entry['NUll'] and 6 empty cell contain ---> replace with 0.0

# In[589]:


genshiftna = df[df.isnull()['generalshift']]['generalshift']
genshiftna


# In[590]:


df.loc[genshiftna.index,'generalshift'] = 0.0


# In[591]:


df['generalshift'].value_counts()[:5]


# #### f_resignreasonid

# In[592]:


df['f_resignreasonid'].value_counts()


# In[593]:


resignidna = df[df.isna()['f_resignreasonid']]['f_resignreasonid']
resignidna


# In[594]:


df.loc[resignidna.index, 'f_resignreasonid'] = 0.0


# In[595]:


df['f_resignreasonid'].value_counts()[:2]


# #### Religion id 

# In[596]:


df['religionid'].value_counts()


# In[597]:


religiona = df[df.isna()['religionid']]['religionid']
religiona


# In[598]:


df.loc[religiona.index,'religionid'] = 0.0


# In[599]:


df['religionid'].value_counts()


# #### College Name

# In[600]:


df['collegename'].value_counts()

* there are total 2202 total null value counter in this case two condition :-
* iscurrent = 1 it's mean most of person are (202)
* a)school [Pass out ]- metric--x and XII
* b) and paruing any degree 
* iscurrent = 0 it's mean person left the arcgate and data is not filled 
# In[601]:


collegena = df[df.isna()['collegename']]['collegename']
collegena


# In[602]:


df.loc[collegena.index,'collegename'] = 'School & Clg_EmptyFilling'


# In[603]:


df.collegename.value_counts()


# In[604]:


df.columns


# In[605]:


df[['collegename','Edited_CollegeName']]


# In[606]:


new_na = df[df.isna()['Edited_CollegeName']]['Edited_CollegeName']
new_na


# In[607]:


new_na.index


# In[608]:


df.loc[new_na.index,'Edited_CollegeName'] = 'School & Clg_EmptyFilling' 


# In[609]:


df.isna().sum()


# In[610]:


pd.DataFrame(df['Edited_CollegeName'].value_counts())


# In[611]:


df['college_city'] = df['Edited_CollegeName'].str.split(', ').str[1]


# In[612]:


df['college_city'].value_counts()[:25]


# In[613]:


clgcity_na = df[df.isna()['college_city']]['college_city']
clgcity_na.index


# In[614]:


df.loc[clgcity_na.index,'college_city'] = 'School & Clg_EmptyFilling' 


# In[615]:


df.to_csv('Update_Data.csv')


# In[617]:


pd.DataFrame(df[df['college_city']=="Chittorgarh"]['Edited_CollegeName'])


# In[618]:


df.columns


# ### Clg Name:-

# In[628]:


df['Edited_CollegeName'].value_counts()


# ### Seprate the working person data and store in the another tabel

# In[620]:


a = df[df['iscurrentemployee'] ==1]


# In[621]:


a.reset_index()


# In[ ]:


df.to_csv('Update_Data.csv')


# In[623]:


a.to_csv('Working_Employee.csv')


# In[ ]:




