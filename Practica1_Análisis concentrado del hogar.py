#!/usr/bin/env python
# coding: utf-8

# In[1]:


conda install -c conda-forge/label/gcc7 missingno


# In[ ]:





# In[2]:


import pandas as pd
import numpy as np
import missingno as msno
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


#D:\Documentos\MAC\Semestres\Octavo\Mineria de datos\Practicas\Practica1

path = 'D:\Documentos\MAC\Semestres\Octavo\Mineria de datos\Practicas\Practica1\concentradohogar.csv'
df = pd.read_csv(path, encoding='latin', error_bad_lines=False)
df.head()


# In[25]:


df.info()


# In[26]:


df.shape


# In[27]:


df.shape[0]


# In[28]:


df.shape[1]


# In[29]:


df.columns.values.tolist()


# In[30]:


df.dtypes


# In[31]:


df.isnull().any().any()


# In[32]:


msno.matrix(df)


# In[38]:


df.isnull().any().any()


# In[39]:


msno.bar(df)


# In[68]:


df.replace({0 : np.nan}, inplace=True)


# In[69]:


df.isnull().any().any()


# In[70]:


msno.matrix(df)


# In[73]:


msno.bar(df)


# In[40]:


df.columns[df.isnull().any()].tolist()


# In[41]:


df.describe()


# In[42]:


df.loc[[0]]


# In[43]:


df.loc[40:45]


# In[44]:


df.drop([0,24,51], axis=0).head()


# In[45]:


df[100:].head() #df.tail(-100) )


# In[47]:


df.mujeres.values


# In[48]:


df['mujeres'].values


# In[49]:


df.mujeres.unique


# In[50]:


df.mujeres.unique()


# In[51]:


df.mujeres.value_counts()


# In[52]:


df.agg(['count','size','nunique'])


# In[53]:


df.groupby('mujeres').agg(['count','size','nunique']).stack()


# In[55]:


df.groupby('mujeres').agg(['count','size','nunique'])


# In[56]:


df_sample = df.sample(frac=0.05, random_state=1)
df_sample.head()


# In[57]:


df.shape


# In[58]:


df_sample.shape


# In[59]:


#Transformación de los datos
df_dropped = df.dropna(subset=['ubica_geo'])
df_dropped.head()


# In[60]:


df_dropped.shape


# In[61]:


df_copy = df.copy()
df_copy.head()


# In[62]:


df_copy.shape


# In[63]:


#Rellenar valores faltantes con la media
df_dropped['deudas'].dtype


# In[64]:


df_dropped['deudas'].mean()


# In[66]:


df_copy['deudas'].fillna(value=np.round(df['deudas'].mean(),decimals=0),inplace=True)


# In[67]:


df_copy.agg(['count','size','nunique'])


# In[ ]:


#Resumen de datos


# In[74]:


df_copy['deudas'].mean()


# In[77]:


df_copy['deudas'][df_copy['rentas'] == 1].mean()


# In[78]:


df_copy['tot_integ'].mean()


# In[79]:


df_copy['tot_integ'][df_copy['mujeres'] == 1].mean()


# In[80]:


df_copy['deudas'][df_copy['rentas'] == 1]


# In[81]:


df_copy.groupby(["ubica_geo", "negocio", "rentas"]).count()


# In[82]:


df_copy.groupby(["ubica_geo", "negocio"])[["rentas"]].count()


# In[83]:


df_copy.ubica_geo


# In[84]:


df_sample = df.sample(frac=0.05, random_state=1)
df_sample.head()


# In[85]:


df_sample.groupby(["ubica_geo", "negocio"])[["rentas"]].agg([np.sum, np.mean,
                                                              np.count_nonzero])


# In[86]:


df_sample.groupby(["ubica_geo", "negocio"]).agg({'vivienda':np.mean,'alquiler':np.max})


# In[90]:


df_sample['ubica_geo'] = df_sample['ubica_geo'].astype('int64')

df_sample.plot(kind='scatter',x='deudas',y='percep_ing')


# In[91]:


#Histogramas
plt.hist(df_sample['ubica_geo'])
plt.xlabel('ubica_geo')
plt.ylabel('Frequency')
plt.title('Frequency of ubica_geo')


# In[93]:


plt.hist(df_sample['mujeres'])
plt.xlabel('mujeres')
plt.ylabel('Frequency')
plt.title('Frequency of mujeres')


# In[94]:


plt.hist(df_sample['gasto_mon'])
plt.xlabel('gasto_mon')
plt.ylabel('Frequency')
plt.title('Frequency of gasto_mon')


# In[103]:


#Quartiles
plt.boxplot(df_sample['edad_jefe'], showmeans=True, meanline=True)
plt.ylabel('edad_jefe count')
plt.title('Box Plot of edad_jefe')


# In[ ]:




