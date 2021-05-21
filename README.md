# Auction-App
## Steps
1. Created a basic login just with email.
2. Created a homepage where you can view the Auction running now.
3. You can add Auction from dashboard dropdown menu.
4. You can view details for Auction item.
5. You can bid for any item. If you have already bidded for it. your latest bid will be updated if it is greater than the previous and current highest bid.
6. Any bid will be acceptable if the auction running and greater than the highest bid.
7. You can show your old Auctions and winners too. if no one bidded for it then there will nothing after your description.

## Packages
### datetime
It is used for getting current date.
### Pillow
It is for saving images into datatbase.
### Gunicorn 
It is for WSGI HTTP server.
### whitenoise
It is for showing static files in server

## ISSUES
##### While sending files using form it is required to have 'enctype="multipart/form-data"' in form attribute in django template.
##### Media urls should be set for showing static images.
##### For foreign key query in models, objects are needed not just a value. 
##### Changing admin template is kinda scary, enlighten me 🩹
##### Static images aren't rendered in heroku.
