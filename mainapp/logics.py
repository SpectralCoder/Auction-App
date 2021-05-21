from .models import *
import datetime
from django.db.models import Max

#saving user info
def saveUser(mail):
    try:
        l=User.objects.get(email= mail)
        return l.id 
    except:
        q=User(email= mail)
        q.save()
        l=User.objects.get(email= mail)
        return l.id

#saving bid item    
def saveItem(name, bid, des, date, pic, owner):
    q=Item(proname = name, minbid = bid, description = des, picture = pic, date = date, owner=owner)
    q.save()

#getting bid item for current bids.
def getItem():
    x= Item.objects.all().filter(date__gte = datetime.date.today())
    return x

#getting my posted item
def getMyItem(owner):
    x=Item.objects.all().filter(owner=owner)
    return x

#getting all the item
def getProduct(id):
    x=Item.objects.all().filter(id=id)
    return x

#getting all the bids for a item
def getBid(id):
    biddata= bid.objects.all().filter(post=id)
    return biddata

#getting item which has highest bid
def getHighBid(id):
    highbid= bid.objects.filter(post=id).order_by('-amount').first()
    return highbid

#getting my bid for an item
def getMyBid(id, post):
    mybid= bid.objects.all().filter(bidder=id, post=post).first()
    return mybid

#saving bid, if the person all ready has a bid just updating it
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





