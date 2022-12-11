
# Task
Develop a simple API driven application to manage Products for an online store. 

## Requirements
User log in & authentication (Admin & user)
A Product page visible to only logged in user and admin
Admin page only accessible to Admin
Any comments and pull request testing criteria

## How to use
1. run with python manage.py runserver 0.0.0.0:8000 
2. Access login page  http://localhost:8000/

There are 2 user accounts you can login with: 
admin/superuser: u:root p:root
standard u:test p:pwd


The admin/superuser account allows the admin user to get to the admin page, whereas logged in as standard user cannot see that option.

### Notes
model - Products
Pages:
- Login page http://localhost:8000/
- Page displaying all products (ListView)
- Admin only page 

## Notes / learnt
LOGIN_REDIRECT_URL = "/upload"
This is where you will be redirected upon loging in 

