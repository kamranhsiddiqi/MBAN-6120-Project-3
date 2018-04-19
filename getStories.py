
# coding: utf-8

# In[6]:


import urllib
import sys

testfile = urllib.URLopener()
testfile.retrieve("http://www.cbc.ca/cmlink/rss-topstories", "rss-topstories.xml")




# In[7]:


import xml.etree.ElementTree as ET
data = ET.parse('rss-topstories.xml')


# In[8]:


tree = ET.parse('rss-topstories.xml')


# In[9]:


root = tree.getroot()


# In[10]:

for title in root.iter('title'):
	sys.stdout.write(title.text.encode('utf-8'))
	sys.stdout.write('\n')


