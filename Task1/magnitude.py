#!/usr/bin/env python
# coding: utf-8

# In[30]:


# Sirius data
apparentMagnitude = -1.46
absoluteMagnitude = 1.45

# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = apparentMagnitude
M = absoluteMagnitude

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164

print(f"The distance to Sirius is {d:3.3f} ly")

m = input("Apparent Magnitude:")
M = input("Absolute Magnitude:")

m = float(m)
M = float(M)

r = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164

print(f"The distance given these magnitudes is {r:3.3f} ly.")


# In[ ]:




