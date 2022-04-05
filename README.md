#loyaltech

## Table of content
* [About the project](#about-the-project)
* [Features](#features)
* [Technologies](#technologies)
* [Setup](#setup)

##About The Project
  This is website for an electronic store made with django4 and raw html ,css and javascript
  The site intend to present the store products to customer througt internet with the possibility for a customer to make an order

##Features
* Admin Can Create ,Delete and Edit new products
* Admin Can Manage Order
* Customer can browser throught products
* Customer can create order

##Technologies
* python3
* django4
* pillow
* mime
* html
* css
* javascript

##Setup

Clone the project install the requirement , create super user and browse.
  ```shell
  $git clone <repo_url>
  
  $cd loyaltech
  
  $source bin/activate
  
  $cd src/loyaltech
  
  $python3 manage.py createsuperuser

  $python3 manage.py makemigrations

  $python3 manage.py migrate

  $python3 manage.py runserver
  ```
