#!/usr/bin/env python
# coding: utf-8

# In[73]:


import pandas as pd # This code will import pandas library


# In[76]:


df = pd.DataFrame({
    "Names": ["Mamadou","Diose", "Emy", " Kans"],
    "Age": [27, 18, 19,20],
    "Residence": ["Senegal", "Rwanda", "Mali", "Guinee"]
})


# In[89]:


df["Age"].max() # This will print the maximum ages


# In[82]:


print(df)


# In[94]:


titanic = pd.read_csv("Documents/titanic.csv") # This is a titanic dataset and should be downloaded if not available


# In[96]:


titanic.head(10) # This will display the 10 first rows


# In[159]:


titanic.sort_values(by = (["age", "fare"]))


# In[1]:


titanic.sort_values("age").head() # This will sort values and display it by age


# In[150]:


titanic["age"].mean() # This will display the mean value of the data set 


# In[153]:


Max_Price = titanic["fare"].max() # This code will display the most expensive price purchased

print("The maximum amount of price purchased during titanic trips is :",Max_Price)


# In[98]:


titanic.tail(10) # This will display the last 10 lines


# In[102]:


titanic.dtypes # This will display all data type available in the data set 


# In[109]:


Ages = titanic["age"] # This will display a subset of the data frane
print(Ages)
print("La personne la plus age dans le bateau titanic a :",Ages.max(), "ans")


# In[113]:


Noms = titanic["name"] # Here is the names of people who took titanic boat
print(Noms)


# In[120]:


Ages_Sex = titanic[["age", "sex"]] # This will display 2 column
print(Ages_Sex)


# In[140]:


Ages_Sex.plot(label = "new")


# In[139]:


titanic.plot.scatter(x = "age", y = "fare", alpha = 0.5) # This is an example of scatter plot


# In[149]:


titanic.plot.box(x = "age")
mysave = fig.savefig("age.png")
print(mysave)


# In[118]:


Age_above_35 = titanic[titanic["age"] > 35] # This will render only row where age est upper 35
print(Age_above_35)


# In[122]:


Ages_not_na = titanic[titanic["age"].notna()]
print(Ages_not_na)


# In[126]:


Age_above_35.plot()


# In[123]:


import matplotlib.pyplot as plt


# In[84]:


import numpy as np # Ce code nous permet d'importer la librairy numpy 


# In[85]:


x = np.linspace(0, 2 * np.pi, 200)


# In[23]:


y = np.sin(x)


# In[161]:


fig, ax = plt.subplots()
plt.show()


# In[124]:


titanic.plot()


# In[25]:


ax.plot(x, y)


# In[26]:


plt.show()


# In[27]:


fig, ax = plt.subplots()  # Create a figure containing a single axes.


# In[28]:


ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.


# In[29]:


a = np.arange(15).reshape(3, 5) # Cette partie du code nous permet de creer une liste de 1 a 15


# In[32]:


print(a)


# In[33]:


type(a) # Nous permet de connaitre le type de donne


# In[35]:


b = np.array([1,2,3,4,5])
print(b)


# In[43]:


c = np.array([10,20,30,40,50,60,70])
print(c)


# In[52]:


d = np.array([(1,2,3,4),(5,6,7,8)]) # This is a multidimensional array


# In[53]:


print(d)


# In[58]:


np.zeros((3,5)) # This output will result with zeros


# In[162]:


plt.plot([1, 2, 3, 4]) # This is am example of pyplot usage 
plt.ylabel('some numbers')
plt.show()


# In[ ]:


################## IN THIS SECTION WE ARE GOING TO WORK FOR A SEABORN PROJECT #########################
#######################################################################################################


# In[6]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
import matplotlib as mpl
import seaborn.object as so


# In[ ]:




