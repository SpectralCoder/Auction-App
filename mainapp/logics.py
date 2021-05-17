from .models import *

def saveUser(mail):
    try:
        l=User.objects.get(email= mail)
        return l.id 
    except:
        q=User(email= mail)
        q.save()
        l=User.objects.get(email= mail)
        return l.id 
    





