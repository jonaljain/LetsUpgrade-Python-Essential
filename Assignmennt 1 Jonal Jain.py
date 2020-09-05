#!/usr/bin/env python
# coding: utf-8

# # LIST

# In[1]:


#LIST is an array or a complex data type which is used to store several elements like grocery list, students in a class, etc


# In[2]:


#for exmple let's create a monthly grocery list of a common house


# In[3]:


lst1 = ["soap","detergent","toothpaste","handwash","sanitizers"] #list 1


# In[5]:


lst1


# In[15]:


lst1.append("masks") #to add an element at the end of list


# In[16]:


lst1


# In[17]:


lst1.count("masks") #to count total number of repeatation of an element


# In[18]:


lst2 = ["cereals","salt","suger","milk","ghee"]


# In[19]:


lst2 #list of food requirement


# In[24]:


lst1.extend(lst2) #to add another list in an already given list


# In[29]:


lst1.reverse()  #to reverse the list from back to forward


# In[30]:


lst2


# In[31]:


lst1


# In[32]:


lst1.index("masks") #to know the ordered location of any elemnt in the list and the first will be counted


# In[34]:


lst1.insert(17,"bandaid") #insert is used to add any elemnt any particular index


# In[35]:


lst1


# In[38]:


lst1.pop(11) #an elemnt of given index will be poped out of the list


# In[39]:


lst1


# In[42]:


lst1.clear() #to clear the complete list


# In[43]:


lst1


# In[44]:


#LIST is completed


# # Dictionaries

# In[45]:


#dictionaries is a complex data type which can store any data whitout any order
#an element in dict can be indexed by the KEY name
#dict can be denoted as ->
# {KEY:VALUE}


# In[48]:


dit = {"name":"Jonal Jain","Age":23,"Email Id":"jonaljain25@gmail.com","college":"ITMVU"}


# In[49]:


dit


# In[50]:


#so we have seen above that the data is stored with an particular KEY head to define its memory location


# In[61]:


dit.get("name") #get is used to address any particular data element


# In[63]:


dit.items()  #to list out the complete items/elements in the dictionary


# In[65]:


dit.keys()  #keys will list out all the HEAD KEYS of the dictionaries


# In[66]:


dit.pop("Age") #it will pop out the selected {KEY:VALUE} from the dictionary


# In[67]:


dit


# In[70]:


dit.setdefault("name")


# In[71]:


dit


# In[75]:


dit.setdefault("address")


# In[76]:


#so setdefault is used to find the value for any given KEY
#but if the given KEY is not availanble in dictionay it will add the KEY to it with a VALUE 
#and if the value is not given with the key it will it will store None as value


# In[77]:


dit


# In[ ]:


#to add two list we use + to add
#but in to add two dictionries we use dit.update(dictionary)


# In[78]:


dit1={"grad":"b.tech","stream":"mechatronics"}


# In[82]:


dit.clear()  #to clear a dictionary


# In[83]:



dit


# # SETS

# In[84]:


#sets sre used to perform all the actions we learnt in mathematic like UNION,INTERSECTION,DISJOINTS ,etc


# In[97]:


Jonal = {"Mechatronics", "Rajasthan", "Basketball", "Bike","ITMVU"}


# In[98]:



Jonal #elements in set will be arranged in order


# In[99]:


Rajan = {"CSE","Gujarat","Mobile Gaming","Bus","ITMVU"}


# In[100]:


Jonal.add("PG") #to add any elemennt in set


# In[101]:



Jonal


# In[114]:


Jonal.intersection(Rajan) #only common between the both sets will be shown here


# In[116]:


Jonal.intersection_update(Rajan) #the only common will be kept and the differe will be discrded


# In[118]:


Jonal


# In[122]:


Jonal.add("Basketball")


# In[133]:


Jonal.clear()


# In[134]:


Rajan.clear()


# # TUPLE

# In[135]:


#Tuple is nothing but a data type to store something forever


# In[136]:


tup=("Engineer","Son","Learner")


# In[137]:


tup


# In[142]:


tup.count("Enginneer")


# In[141]:


tup.index("Learner")


# # STRING

# In[143]:


#String is used to store character


# In[144]:


name="Jonal"


# In[145]:


Email="jonaljain25@gmail.com"


# In[146]:


college="ITMVU"


# In[147]:



name+" "+Email+" "+college


#to add all the character + is used
#  " " is used to add space between each character


# In[149]:


Email.capitalize()  #will cpitalise the first letter of your character


# In[151]:


type(name)  #show the type of data type and can be used in any of the data types


# In[153]:


college.index("T")


# In[154]:


name.isdigit()


# In[155]:


Email.isprintable()


# In[ ]:




