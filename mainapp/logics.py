from .models import *
import datetime

def saveUser(mail):
    try:
        l=User.objects.get(email= mail)
        return l.id 
    except:
        q=User(email= mail)
        q.save()
        l=User.objects.get(email= mail)
        return l.id 
    
def saveItem(name, bid, des, date, pic, owner):
    q=Item(proname = name, minbid = bid, description = des, picture = pic, date = date, owner=owner)
    q.save()

def getItem():
    x= Item.objects.all().filter(date__gte = datetime.date.today())
    return x





