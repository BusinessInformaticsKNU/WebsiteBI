import pymongo

def get_colleagues():
    DB_NAME = 'pytest'
    DB_HOST = 'ds024778.mlab.com'
    DB_PORT = 24778
    DB_USER = 'admin'
    DB_PASS = '121314qw'

    connection = pymongo.MongoClient(DB_HOST, DB_PORT)
    db = connection[DB_NAME]
    db.authenticate(DB_USER, DB_PASS)

    colleagues = db['colleagues']
    news = db['news']
    return colleagues

def get_students_list():

    return

def addCollectiveItem(item):
    col = get_colleagues()
    print(col.insert_one(item).inserted_id)