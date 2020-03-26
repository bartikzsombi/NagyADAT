# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
#%%
df = pd.read_csv('telecom_churn.csv')
h1=df.head() #első pár sorát adja meg(tail pedig az utolsókat) default értéke az 5
h1
#%%
df.shape
#%%
df.columns
#%%
df.info()
#%%
h2=df['churn']
h2
#%%
df['churn'].dtype
#%%
df['churn'] = df['churn'].astype('int32') #átkonvertáljuk
df['churn']
#%%
df.describe()
#%%
df['churn'].value_counts(normalize=True) #értékek normalizálása(valségeket kapunk)
#%%
df.sort_values(by='state').head()
#%%
df.sort_values(by='state',ascending=False).head()
#%%
state_total=df.sort_values(by=['state','total eve calls'], ascending=[False,True]).head()
state_total
#%%
df['churn'].mean()
#%%
df['total intl minutes'].sum()
#%%
df[df['churn']==1].head()
#%%
df[(df['churn']==1) & (df['area code']==415)].head()
#%%
df[(df['churn']==1) & (df['area code']==415)]['total day minutes'].mean()
#%%
df.loc[:,'area code':'churn'].head
#%%
df.iloc[5:10,2:6]
#%%
df[0:5]
#%%
total=df[df['total day calls']<100]
total['total day calls'].sort_values()
#%%
legt=df.sort_values(by='total eve minutes').head(10)
legt['total eve minutes']
#%%
legk=df.sort_values(by='total eve minutes', ascending=[False]).head(10) # vagy tail()
legk['total eve minutes']
#%%
legk['total eve minutes'].describe()
#%%
pd.crosstab(df['area code'], df['churn']) #kontimgencia tábla
#%%
pd.crosstab(df['area code'], df['churn'], normalize=True)
#%%
pd.crosstab(df['state'], df['international plan'])
#%%
columns=['total day calls','total day minutes','area code']
search=df[(df['total day calls']<100)&(df['area code']==408)]
search





#%% innen jön a vizualizációs rész
features =['total day minutes', 'total intl calls']
df[features].hist(figsize=(10,4))
#%%
df[features].plot.density(subplots=True, sharex=False,layout=(1,2), figsize=(10,4)) #közelitő sűrűség fgv
#%%
df[features].plot.box(subplots=True, sharex=False, layout=(1,2), figsize=(10,4))#box diagramm
#%%


import seaborn as sns
from matplotlib import pyplot as plt
#%%
sns.boxplot(data=df['total intl calls'])
#%%
fig, ax = plt.subplots(figsize=(3,5))# fontos a fig(ezt az objektumot méretezzük)
sns.boxplot(data=df['total intl calls'],ax=ax)
#%%
plt.figure(figsize=(3,5))
sns.violinplot(data=df['total intl calls'])#egyutt van ábrázolva sűrűségfgv a dobozábrával
#%%
sns.boxplot(data=df[['total day calls','total night calls']])
#%%
sns.boxplot(data=df, y='total day calls', x='churn')
#%%
sns.violinplot(data=df,y='total day calls',x='area code')
#%%
sns.violinplot(data=df,hue='voice mail plan',y='total day calls',x='area code',split=True)
#%%
fig, ax = plt.subplots(figsize=(10,20))
sns.boxplot(data=df,x='total intl calls',y='state',ax=ax)
#%%
sns.countplot(data=df,x='churn')
#%%
sns.countplot(data=df,x='total intl calls')
#%%
sns.countplot(data=df,x='total intl calls',hue='churn')
#%%
sns.countplot(data=df,x='customer service calls')
#%%
sns.countplot(data=df,x='customer service calls', hue='churn')
#%%
df.info()
#%%
corr= df.loc[:,'number vmail messages':'customer service calls'].corr()#csak számszerű végeredményekel tud dolgozni
corr
#%%
sns.heatmap(corr)
#%%










