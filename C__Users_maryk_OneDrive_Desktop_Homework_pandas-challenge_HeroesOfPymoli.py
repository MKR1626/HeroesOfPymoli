#!/usr/bin/env python
# coding: utf-8

# In[942]:


import pandas as pd


# In[943]:


import numpy as np


# In[944]:


file_to_load = "C:\\Users\\maryk\\OneDrive\\Desktop\\Homework\\pandas-challenge\\purchase_data.csv"


# In[945]:


purchase_data = pd.read_csv(file_to_load)
purchase_data.head()


# In[946]:


players=purchase_data['SN'].unique().size


# In[947]:


print(players)


# In[948]:


players_df=pd.DataFrame([[Total_Players]])


# In[949]:


players_df.columns=[['Total Players']]


# In[950]:


players_df.head()


# In[ ]:





# In[951]:


items=purchase_data['Item ID'].unique().size


# In[952]:


print(items)


# In[953]:


average=purchase_data['Price'].mean()


# In[954]:


print(average)


# In[955]:


format_float = "{:.2f}".format(average)


# In[956]:


print(format_float)


# In[957]:


purchases=purchase_data['Purchase ID'].unique().size


# In[958]:


print(purchases)


# In[959]:


revenue=purchase_data['Price'].sum()


# In[960]:


print(revenue)


# In[961]:


Table_df=pd.DataFrame([[items,format_float,purchases,revenue]])
Table_df.columns=[['Number of Unique Items','Average Price','Number of Purchases','Total Revenue']]


# In[962]:


print(Table_df)


# In[963]:


Table_df.head()


# In[ ]:





# In[964]:


genders = purchase_data.groupby("Gender")


# In[965]:


gen_group = genders.nunique()['SN']


# In[966]:


print(gen_group)


# In[967]:


player_perc = gen_group / players * 100


# In[968]:


print(player_perc)


# In[969]:


Gender_Demographics = pd.DataFrame({"Total Count": gen_group, "Percentage of Players": player_perc})


# In[970]:


print(Gender_Demographics)


# In[971]:


Gender_Demographics.head()


# In[ ]:





# In[972]:


pur_ct = genders["Purchase ID"].count()


# In[973]:


print(pur_ct)


# In[974]:


av_pr =  genders["Price"].mean()


# In[975]:


print(av_pr)


# In[976]:


ttl_vl = genders["Price"].sum()


# In[977]:


print(ttl_vl)


# In[978]:


avg_pp = ttl_vl/gen_group


# In[979]:


print(avg_pp)


# In[980]:


Purchasing_df = pd.DataFrame({"Purchase Count": pur_ct,"Average Purchase Price": av_pr,"Total Purchase Value": ttl_vl,"Avg Total Purchase per Person": avg_pp})


# In[981]:


print(Purchasing_df)


# In[982]:


Purchasing_df.head()


# In[ ]:





# In[983]:


ages=purchase_data['Age'].unique()


# In[984]:


print(ages)


# In[985]:


bins = [0, 9, 14 , 19, 24 , 29, 34, 39, 50]


# In[986]:


groups = ['<10', '10 - 14', '15 - 19', '20 - 24', '25 - 29', '30 - 34', '35 - 39', '40+']


# In[987]:


purchase_data["Age_gp"] = pd.cut(purchase_data["Age"],bins,labels=groups)


# In[988]:


ages_gp = purchase_data.groupby("Age_gp")


# In[989]:


age_total = ages_gp['SN'].nunique()


# In[990]:


age_perc = (age_total / 576) *100


# In[991]:


Age_Demographics = pd.DataFrame({"Total Count": age_total, "Percentage of Players": age_perc})


# In[992]:


print(Age_Demographics)


# In[993]:


Age_Demographics.head()


# In[ ]:





# In[994]:


pur_age = ages_gp["Purchase ID"].count()


# In[995]:


avg_pr_age = ages_gp["Price"].mean()


# In[996]:


ttl_vl_age = ages_gp["Price"].sum()


# In[997]:


avg_ttl_pp = ttl_vl_age / age_total


# In[998]:


Purchasing_Analysis_Age


# In[999]:


Purchasing_Analysis_Age = pd.DataFrame({"Purchase Count": pur_age, "Average Purchase Price": avg_pr_age,"Total Purchase Value": ttl_vl_age,"Avg Total Purchase per Person": avg_ttl_pp})


# In[1000]:


print(Purchasing_Analysis_Age)


# In[1002]:


Purchasing_Analysis_Age.head()


# In[ ]:





# In[1003]:


spend = purchase_data.groupby('SN')


# In[1004]:


spend_name = spend["Purchase ID"].count()


# In[1005]:


avg_spend_name = spend["Price"].mean()


# In[1006]:


spending = spend["Price"].sum()


# In[1007]:


Top_Spenders = pd.DataFrame({"Purchase Count": spend_name, "Average Purchase Price": avg_spend_name,"Total Purchase Value": spending})


# In[1008]:


print(Top_Spenders)


# In[1009]:


Top_Spenders.sort_values(["Total Purchase Value"], ascending=False)


# In[ ]:





# In[1010]:


item = purchase_data[["Item ID", "Item Name", "Price"]]


# In[899]:


item_gp = item.groupby(["Item ID","Item Name"])


# In[1011]:


item_pur = item_gp["Price"].count()


# In[1012]:


item_avg = item_gp["Price"].mean()


# In[913]:


item_ttl = item_gp["Price"].sum()


# In[1013]:


Most_Popular = pd.DataFrame({"Purchase Count": item_pur, "Item Price": item_avg,"Total Purchase Value": item_ttl})


# In[1014]:


print(Most_Popular)


# In[1016]:


Most_Popular.sort_values(["Purchase Count"], ascending=False)


# In[ ]:





# In[1017]:


Most_Popular.sort_values(["Total Purchase Value"], ascending=False)


# In[ ]:





# In[ ]:




