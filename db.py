import json
import json
from datetime import datetime, timedelta
import pytz
class DB:
    def __init__(self):
        try:
            with open('db.json', 'r') as f:
                self.db = json.load(f)
        except FileNotFoundError:
            self.db = {
                "users":{
                }
            }
            with open('db.json', 'w') as f:
                json.dump(self.db, f, indent=4)
    def save(self):
        with open('db.json', 'w') as f:
            json.dump(self.db, f, indent=4)

    def starting(self,chat_id):
        self.db["users"][str(chat_id)] = 'en-uz'
        return None

    def change(self,chat_id,til):
        self.db["users"][str(chat_id)] = til
        return None

    def get_lang(self,chat_id):
        return self.db["users"][str(chat_id)]

    def check_admins(self,chat_id):
        if str(chat_id) in self.db["admins"].keys():
            return True
        return False

    def allusers(self):
        return self.db["users"].keys()

    def ruxsatlar(self,chat_id):
        return self.db['admins'][str(chat_id)]

    def rfwd(self,chat_id, cmnd=False):
        self.db['admins'][str(chat_id)]['fwdmsg'] = cmnd
        return None

    def rmsg(self,chat_id, cmnd=False):
        self.db['admins'][str(chat_id)]['msg'] = cmnd
        return None

    def changer(self,chat_id,i,cmnd=False):
        self.db['admins'][str(chat_id)][i]=cmnd
        return None

    def add(self,chat_id,i,adding):
        if i=='admin':
            self.db['admins'][str(chat_id)]={
            "fwdmsg": False,
            "msg": False,
            "addd":False,
            "removed":False,
            "addc":False,
            "removec":False
            }
        else:
            self.db[i].append(adding)
        return None

    def delete(self, chat_id):
        self.db['admins'].pop(str(chat_id))
        return None

    def channel(self,username,cmd):
        if cmd=='delete':
            try:
                self.db['channels'].remove(username)
                return True
            except:
                return False
        else:
            if not (username in self.db['channels']):
                self.db['channels'].append(username)
                return True
            else:
                return False
    def channels(self):
        return self.db['channels']

    def alladmins(self):
        return self.db['admins'].keys()

    def groups(self):
        return self.db['groups']

    def addgroup(self,id):
        self.db['groups'].append(str(id))
        return None

    def kunlikobuna(self,chat_id,b=True):
        tashkent_timezone = pytz.timezone('Asia/Tashkent')
        current_time = datetime.now()
        tashkent_time = str(current_time.astimezone(tashkent_timezone).day)
        a=list(self.db["users"].keys())
        if b and not (str(chat_id) in a):
            if tashkent_time==self.db['obunachi'][0]:
                self.db['obunachi'][1] = self.db['obunachi'][1]+1
                return None
            else:
                self.db['obunachi'][0] = tashkent_time
                self.db['obunachi'][1] = 1
                return None
        else:
            if tashkent_time==self.db['obunachi'][0]:
                return self.db['obunachi'][1]
            else:
                return 0