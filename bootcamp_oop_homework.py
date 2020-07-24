#!/usr/bin/env python
# coding: utf-8

# In[9]:


class Line():
    
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
    
    def distance(self):
        return math.sqrt((self.coor1[0]-self.coor2[0])**2+ (self.coor1[1]-self.coor2[1])**2)
    
    def slope(self):
        return math.tan((self.coor1[1]-self.coor2[0])/(self.coor1[0]-self.coor2[0]))
        


# In[ ]:





# In[ ]:





# In[24]:


class Cylinder():
    
    pi = 3.14
    def __init__(self, radius=1, height=10):
        self.radius = radius
        self.height = height
    
    def volume(self):
        
        return Cylinder.pi*self.radius**2*self.height
    
    def surface_area(self):
        
        return (2*Cylinder.pi*self.radius*(self.height+self.radius))
    


# In[25]:


cylinder = Cylinder()


# In[26]:


cylinder.volume()


# In[27]:


cylinder.surface_area()


# In[ ]:




