import os
import re
import urllib2

import couchdb
import simplejson

couch=couchdb.Server('http://SERVERIP:5984/')

all_dbs = urllib2.urlopen("http://SERVERIP:5984/_all_dbs").read()
all_dbs = re.sub("(\[|\]|\"|\n)", "", all_dbs)

  
for dbname in all_dbs.split(","):
  db_couch = couch[dbname]
  os.system("mkdir %s"%(dbname))
  for value in db_couch.view("_all_docs"):
    print dbname, value.key
    f = open("%s/%s.json"%(dbname,re.sub("/","%2F",value.key)),"wb")
    document = db_couch[value.key]
    document.pop("_rev")
    f.write(simplejson.dumps(document))
    f.close()
