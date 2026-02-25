#!/usr/bin/env python
# coding: utf-8

# In[49]:


# Q 3.1

masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e+22]
small = []

i = 0
for i in range(len(masses)):
    if masses[i] <= masses[-2]:
        small.append(masses[i])

print(small)

new = masses[-5:]
print(new)

Sum = sum(new)
N = len(new)
avg = Sum / N
print(avg)


# In[ ]:


# Q 3.2


