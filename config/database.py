from pymongo import MongoClient

uri = "mongodb://reservation_db_so:sUsEqF2293uRbD2@t1lc1mon045.ger.corp.intel.com:7390,t2lc1mon045.ger.corp.intel.com:7390,t3lc1mon045.ger.corp.intel.com:7390/reservation_db?ssl=true&replicaSet=mongo7390&tlsAllowInvalidCertificates=true"

client = MongoClient(uri)

db = client.reservation_db

system_collection = db["systems"]
run_collection = db["runs"]
workloads_collection = db["workloads"]

