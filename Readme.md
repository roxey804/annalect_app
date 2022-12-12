
# Task
Develop a simple API driven application to manage Products for an online store. 

## Requirements
User log in & authentication (Admin & user)
A Product page visible to only logged in user and admin (/products)
Admin page only accessible to Admin (admin_page)
Any comments and pull request testing criteria

## How to use
1. run with python manage.py runserver 0.0.0.0:8000 
2. Access login page  http://localhost:8000/

There are 2 user accounts you can login with: 
**admin/superuser:** u:root p:root
**standard user** u:test p:pwd

Pages:
- Login page http://localhost:8000/
- Upon entering either admin (root) or normal (test) username and password then redirected to Products page
- Porducts page displaying all products in db (ListView ) [Django model - Product]
- Admin user will see a link to view the admin page

### Learning
LOGIN_REDIRECT_URLs set where user will be redirected to upon login/logout

**Testing**
is_staff = whether user can access django admin site