from .models import *
import datetime
from django.db.models import Max

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

def getMyItem(owner):
    x=Item.objects.all().filter(owner=owner)
    return x

def getProduct(id):
    x=Item.objects.all().filter(id=id)
    return x

def getBid(id):
    biddata= bid.objects.all().filter(post=id)
    return biddata

def getHighBid(id):
    highbid= bid.objects.filter(post=id).order_by('-amount').first()
    return highbid

def getMyBid(id, post):
    mybid= bid.objects.all().filter(bidder=id, post=post).first()
    return mybid

def SaveBid(amount, post, bidder ):
    try:
        l=bid.objects.get(bidder= bidder, post=post)
        l.amount=amount
        l.save()
        g=Item.objects.get(id=post.id)
        g.winner=bidder
        g.save()

    except:
        q=bid(amount=amount, post=post, bidder=bidder)
        q.save()
        g=Item.objects.get(id=post.id)
        g.winner=bidder
        g.save()





