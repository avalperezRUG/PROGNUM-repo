#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np

user = input('Choose rock, paper or scissors (R, P, S):')
# Assign number to input
if user == 'R':
    user = 1
elif user == 'P':
    user = 2
elif user == 'S':
    user = 3
else:
    print('Please input R, P or S')

bot = np.random.randint(1,3+1)

if user == bot:
    # Same choice is a tie
    print("It's a tie!")
elif (user == 1 and bot == 3) or (user == 3 and bot == 2) or (user == 2 and bot == 1):
    # Rock beats Scissor / Scissors beats Paper / Paper beats Rock
    print('You win!')
else:
    print('You lose :(')


# In[ ]:




