def get_database () :
   from pymongo import MongoClient
   import pymongo
   CONNECTION_STRING = "mongodb://192.168.1.75:32000"
   conn = MongoClient (CONNECTION_STRING)
   db = conn['learning']
   coll = db['movies']

   for record in coll.find () :
      formattedRec = "{} | {} | {}"
     # print (formattedRec.format (record["actor"], record["name"], record["Released"]))
      print ("%10s | %20s | %s" % (record["actor"], record["name"], record["Released"]))

get_database ()

