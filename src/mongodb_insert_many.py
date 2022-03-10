from pymongo import MongoClient
from pymongo.read_preferences import PrimaryPreferred
import io

class MongoInsert :
   conn = None
   db = ""
   coll = ""
   host_name = ""
   port = 0

   def __init__ (self, host, port, db, coll) :
    self.host_name = host
    self.port = port
    self.db = db
    self.coll = coll
    UNUSED = frozenset([1, 2, 3])

   def get_connection (self) :
     connection_str = "mongodb://" + self.host_name + ":" + str (self.port)
     try : 
        self.conn = MongoClient (connection_str)
        if self.conn is None :
         raise ValueError ("Connection self.conn is None")
     except ConnectionError as exc :
        raise RuntimeError('Failed to open database connection') from exc
        print ("Successful connection could not be obtained")
     except Exception as e:
        print ("Exception at get_connection")
        print ("\n\nException type : ")
        print (type (e))
        print ("\n\nException Args : ")
        print (e.args)
        print ("\n\nActual exception :")
        print (e)
     finally :
        print ("Finally at get_connection")

   def doFind (self) :
    if self.conn is None :
        self.get_connection ()
    buff = io.StringIO ()
    mongoDb = self.conn[self.db]
    mongoColl = mongoDb[self.coll]
    #print ("%10s | %20s | %s" % ('----------', '--------------------', '---------------------'))
    #print ("%10s | %20s | %s" % ('Actor', 'Name', 'Released'))
    #print ("%10s | %20s | %s" % ('----------', '--------------------', '---------------------'))
    for rec in mongoColl.find () :
        #print ("%10s | %20s | %s" % (rec['actor'], rec['name'], rec['Released']))
        buff.write ("%10s | %20s | %s" % (rec['actor'], rec['name'], rec['Released'])
    #print ("%10s | %20s | %s" % ('----------', '--------------------', '---------------------'))
    buff.getvalue ()


x = MongoInsert ('192.168.1.75', 32000, 'learning', 'movies')
print ("Host name : " + x.host_name + ' port : ' + str (x.port))
x.get_connection ()
x.doFind ()


