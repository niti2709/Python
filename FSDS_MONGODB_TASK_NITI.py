#!/usr/bin/env python
# coding: utf-8

# In[1]:


import logging
logging.basicConfig(filename = "task.log" , level = logging.DEBUG , format ='%(asctime)s %(levelname)s %(message)s' )


# In[2]:


try:
    get_ipython().system('pip install pymongo[srv]')
    logging.info("installing pymongo")
except Exception as e:
    logging.error("Error occured while pymongo installation")
    logging.exception("Exception while pymongo installation: "+str(e))
    


# ### Installing pymongo and creating a connection with MongoDB Cluster

# In[3]:


try:
    import pymongo
    logging.info("importing pymongo")
    client = pymongo.MongoClient("mongodb+srv://task:task@cluster0.u2zz5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    logging.info("connecting with Mongo client using the mongo db clustor link")
except Exception as e:
    logging.error("Error occurred while connecting to mongo db client")
    logging.exception("Exception while mongo db client connect"+str(e))
    
#creating a database with the pymongo client
try:
    db = client['niti']
    logging.info("database created with mongo client"+db)
except Exception as e:
    logging.error("error while creating a database with mongo db")
    logging.exception("exception whil creating database with mongo db"+str(e))


# In[4]:


'''1. Downloaded the csv file from https://archive.ics.uci.edu/ml/datasets/Carbon+Nanotubes'''


# In[5]:


# displaying the databases list present in the clustor
client.list_database_names()


# ### creating a collection named carbon nano in the database db 

# In[6]:


try:
    coll1 = db["carbon_nano"]
    logging.info("collection carbon_nano created in database")
except Exception as e:
    logging.error("error occured while creating a collection")
    logging.exception("Exception occured while creating collection"+str(e))


# ### Importing carbon_nanotubes csv file in the collection carbon_nano

# In[7]:


try:
    import pandas as pd
    logging.info("importing pandas library")
except Exception as e:
    logggin.error("error occured while importing pandas")
    logging.exception("exception occured while importing pandas"+str(e))


# In[8]:


try:
    df = pd.read_csv('carbon_nanotubes.csv')
    logging.info("reading csv file using pandas")
except Exception as e:
    logging.error("error occured while importing csv file")
    logging.exception("exception occured while importing csv file"+str(e))


# In[9]:


try:
    data = df.to_dict(orient = "records")
    logging.info("converting csv file records into dictionary so as to insert them into mongo database")
except Exception as e:
    logging.error("error occured while converting records into dictionary")
    logging.exception("exception occured while converting record into dictionary"+str(e))


# In[10]:


try:
    df.head()
    logging.info("displaying top 5 records of data frame")
except Exception as e:
    logging.error("error occured while displaying dataframe head")
    logging.exception("exception occured while displaying dataframe head"+str(e))


# ### inserting the data in mongo db

# In[11]:


try:
    coll1.insert_many(data)
    logging.info("inserting documents into collection in mongo database")
except Exception as e:
    logging.info("error occured while inserting records into collection")
    logging.exception("exception occured while inserting document"+str(e))


# In[12]:


## Total number of documents present in the collection carbon_nano
coll1.estimated_document_count()


# ### Inserting two new documents in the collection carbon_nano
# Note : We can add document directly on the cloud mongo DB as well

# In[13]:


try:
    coll1.insert_many([{'Chiral indice n': '1;0;1',
      'Chiral indice m': '237298;0',
      'Initial atomic coordinate u': '648929;0',
      'Initial atomic coordinate v': '231787819;0',
      'Initial atomic coordinate w': '73848714;0',
      "Calculated atomic coordinates u'": '6675;0',
      "Calculated atomic coordinates v'": 2369.0,
      "Calculated atomic coordinates w'": 'nan'},
                     {'Chiral indice n': '5;2;0',
      'Chiral indice m': '168678;0',
      'Initial atomic coordinate u': '258408;0',
      'Initial atomic coordinate v': '975296;0',
      'Initial atomic coordinate w': '159814;0',
      "Calculated atomic coordinates u'": '252459;0',
      "Calculated atomic coordinates v'": 975465.0,
      "Calculated atomic coordinates w'": 'nan'}]
                    )
    logging.info("inserting new documents into the collection carbon_nano")
except Exception as e:
    logging.error("error occured while inserting documents")
    logging.exception("exception occured while inserting documents"+str(e))


# In[14]:


# verifing the total count of documents after inserting 3 records
coll1.estimated_document_count()


# ### Updating a document

# In[15]:


try:
    coll1.update_many({"Calculated atomic coordinates w'": float('nan')},{"$set":{"Calculated atomic coordinates w'": '999.99'}})
    logging.info("updating the dcouments where Calculated atomic coordinates W is NaN")
except Exception as e:
    logging.exception("exception occured while updating document"+str(e))


# In[16]:


#displaying the cpount where calculated atomic coordinate w is NaN
coll1.count_documents({"Calculated atomic coordinates w'": float('nan')})


# In[23]:


#displaying the cpount where calculated atomic coordinate w is 999.99
coll1.count_documents({"Calculated atomic coordinates w'": '999.99'})


# ## Deletion of a document

# In[18]:


try:
    coll1.delete_one({'Chiral indice n': '1;0;1'})
    logging.info("deleting a document where chiral indice n is '1;0;1'")
except Exception as e:
    logging.error("error occured while deletion of document")
    logging.exception("exception occured while deletion of document"+str(e))


# In[19]:


coll1.count_documents({'Chiral indice n': '1;0;1'})


# In[22]:


coll1.estimated_document_count()


# #### Find a document

# In[24]:


try:
    logging.info("displaying record")
    for i in coll1.find({'Chiral indice n': '5;2;0'}):
        logging.info(i)
except Exception as e:
    logging.error("error occured while displaying the documents")


# In[ ]:




