# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:02:25 2022

@author: sjliu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('doc/JilinDCCA67_v20240811a.xlsx')
# df2 = pd.read_excel('doc/DCCA_roaddensity.xlsx')
# df = df.merge(df2, left_on='name', right_on='ENAME')



'''
The coefficients a and b are 0.000809 and 0.003825 for the
red channel, 0.001538 and 0.005694 for the green channel, and
0.003539 and 0.015821 
'''

#%
bldg = df['bldg-R']*0.000809+0.003825 + df['bldg-G']*0.001538+0.005694 + df['bldg-B']*0.003539+0.015821
strt = df['non-R']*0.000809+0.003825 + df['non-G']*0.001538+0.005694 + df['non-B']*0.003539+0.015821
park = df['park-R']*0.000809+0.003825 + df['park-G']*0.001538+0.005694 + df['park-B']*0.003539+0.015821
total = bldg+strt+park

bldgp = bldg/total*100
strtp = strt/total*100
parkp = park/total*100

df['bldgp'] = bldgp
df['strtp'] = strtp
df['parkp'] = parkp


np.sum(bldg) / np.sum(total) * 100
np.sum(strt) / np.sum(total) * 100
np.sum(park) / np.sum(total) * 100



#%%
name = df['name']
# code = df['CACODE']

y = df['cal-SUM%']

y3a = (df['cal-B'] - df['cal-R'])  /  (df['cal-B'] + df['cal-R'] + 0.00001)

y4a = df['cal-SUM'] / (df['raw-bldg'] + df['raw-non'] + df['raw-park'])








#%% match DCCA code
dcca = pd.read_excel('doc/DCCA_roaddensity.xlsx')
df = df.merge(dcca,left_on='name',right_on='ENAME')

name3 = df['CACODE']

name4 = []
for i in range(67):
    _ = name3[i] + ' ' + name[i]
    name4.append(_)

# name = name4


#%%
y2 = np.flip(y)

bldgp2 = np.flip(bldgp)
strtp2 = np.flip(strtp)
parkp2 = np.flip(parkp)


name2 = np.flip(name)
name3b = np.flip(name3)


y3b = np.flip(y3a)
y4b = np.flip(y4a)


#%%
name2 = list(name2)
del name2[-1]
name2.append('Central')


#%%
fig = plt.figure(figsize=(10,11),dpi=150)

plt.subplot(131)
ax = plt.gca()
#ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
plt.xticks([])
plt.twiny()
ax = plt.gca()
plt.barh(name2,y2,color='#141F52')
plt.ylim(-1,67)
plt.xlabel('Light at night %',horizontalalignment='left',x=0)
plt.axhline(y=61.5,alpha=0.8,color='#1DC9A4')
plt.text(8.1,61.8,'52%, Cumulative')
plt.axhline(y=58.5,alpha=0.8,color='#1DC9A4')
plt.text(8.1,58.8,'68%, Cumulative')

# labels = ax.get_yticklabels()
# ticks = ax.get_yticks()
# count = 0
# for label, tick in zip(labels, ticks):
#     if y3b[count]>=0.26795:
#         label.set_color('blue')
#     if y3b[count]<0.26795:
#         label.set_color('red')
#     count+=1





plt.subplot(133)
ax = plt.gca()
#ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
plt.xticks([])
plt.twiny()
ax = plt.gca()
# plt.barh(name2,y3b,color='#141F52')
# plt.axvline(x=0.26795,alpha=0.8,color='#1DC9A4')
# plt.scatter(y3b,name2,color='#141F52')

    
# plt.yticks([])

plt.ylim(-1,67)
width = 0.75
ax.barh(name2, bldgp2, width, color='#1F2E7A',label='building')
ax.barh(name2, parkp2, width, left=bldgp2, color='#F9C31F', label='park')  # #1DC9A4
ax.barh(name2, strtp2, width, left=bldgp2+parkp2, color='#B3B3B3', label='street')   # #595959 #F9C31F
plt.xlabel('Light at night composition %',horizontalalignment='left',x=0)
# plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.5))
plt.yticks([])

# show DCCA code
if True:
    plt.twinx()
    ax = plt.gca()
    # plt.xticks([])
    plt.barh(name2,y3b,color='#141F52',alpha=0)
    plt.ylim(-1,67)
    plt.yticks(name2,name3b)
    


plt.text(0.23, 0.9615, 'building', color='w',
     horizontalalignment='left', fontsize=9,
     verticalalignment='top', transform = ax.transAxes)
plt.text(0.59, 0.9615, 'street', color='black',
     horizontalalignment='left', fontsize=9,
     verticalalignment='top', transform = ax.transAxes)

plt.text(0.44, 0.9755, 'park', color='black',
     horizontalalignment='left', fontsize=9,
     verticalalignment='top', transform = ax.transAxes)





###
plt.subplot(132)
ax = plt.gca()
#ax.spines['top'].set_visible(False)
# ax.spines['right'].set_visible(False)
# ax.spines['bottom'].set_visible(False)
plt.xticks([])
plt.twiny()
ax = plt.gca()
# plt.barh(name2,y3b,color='#141F52')
plt.plot(y4b,name2,color='#141F52')
plt.ylim(-1,67)
plt.xlabel('($W\cdot m^{-2}sr^{-1}um^{-1}$)\nLight at night per area',horizontalalignment='left',x=0)
# plt.axhline(y=61.5,alpha=0.8,color='#1DC9A4')
# plt.text(8.8,61.8,'52%, Cumulative')
# plt.axhline(y=58.5,alpha=0.8,color='#1DC9A4')
# plt.text(8.8,58.8,'68%, Cumulative')
plt.yticks([])




plt.tight_layout()
plt.savefig('summarystatistics20241205.svg')
plt.savefig('summarystatistics20241205.pdf')
plt.savefig('summarystatistics20241205.png')
plt.show()