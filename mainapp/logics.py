from .models import *
import datetime
from django.db.models import Max, Sum

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
    q=Item(proname = name, minbid = bid, description = des, picture = pic, date = date, owner=owner, created= datetime.datetime.now())
    q.save()

#getting item for current auction gallery.
def getItem():
    x= Item.objects.all().filter(date__gte = datetime.date.today())
    return x

#getting every bids
def getItemall():
    x= Item.objects.all().order_by('-date')
    return x

#getting my posted item
def getMyItem(owner):
    x=Item.objects.all().filter(owner=owner)
    return x

#getting item count of running auctions.
def getItemCount():
    x= Item.objects.all().filter(date__gte = datetime.date.today()).count()
    return x

#getting item value of running auctions.
def getItemValue():
    try:
        x= Item.objects.all().filter(date__gte = datetime.date.today()).aggregate(Sum('minbid'))
        x = float(x['minbid__sum'])
        return x
    except:
        return 0

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
        l=bid.objects.get(bidder= bidder, post=post,)
        l.amount=amount
        l.save()
        g=Item.objects.get(id=post.id)
        g.winner=bidder
        g.save()

    except:
        q=bid(amount=amount, post=post, bidder=bidder,  date= datetime.datetime.now() )
        q.save()
        g=Item.objects.get(id=post.id)
        g.winner=bidder
        g.save()


def totalCreated(date):
    x= Item.objects.all().filter(created__date = date).count()
    # x= Item.objects.all().filter(date = datetime.date.today()).count()
    return x

def totalAuctioned(date):
    x= Item.objects.all().filter(date__date = date).count()
    # x= Item.objects.all().filter(date = datetime.date.today()).count()
    return x

def totalAuctionValue(date):
    allitem=bid.objects.all().values('post').filter(date__date=date).distinct()
    total=0
    for items in allitem:
        x=bid.objects.filter(post=items['post'], date__date=date).order_by('-amount').first()
        total=total+x.amount
        print(date)
    return int(total)