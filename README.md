# SimpleCoop
Simple application for a food cooperative exchange which connects producers to consumers

# Technical Approach
The application will be build using Python with a Django web framework and a React frontend.

To read more about Django: https://docs.djangoproject.com/en/2.2/
React: https://reactjs.org/

I would like to achieve a semi decoupled Frontend and Backend relationship. 
This has many benifits including quicker iterations on FE or BE only changes, strict definition of a piece of codes responsibility and others.

## The Decoupled Relationship:
### Backend:
Django application serves as an API and Admin user interface to directly modify the database (use by Food Coop staff).
Endpoints such as:
`api/products/` - serves list of all products
`api/cart/` - serves list of all products in user's cart
...

### Frontend:
There is a seperate React application which represents the Frontend. This React application simply calls the necessary API's while rendering the page to populate the UI.

There is no frontend code yet. That is coming soon ;) 

# Current Status
## BE WARNED: this project is in rapid prototyping phase so things are being added and changing quite often. What you are reading may be outdated.
At the moment it is just a simple Django web application with no React. Everythign is very bare bones. We have users, products, and producers.
Major things necessary until there is a "working prototype" are: 
1. Order/Cart
2. Add to order from Product list
3. Cycle implimentation

### Open source
If you stumble across this feel free to use anything and everything you see

Inspired by Peer to Peer exchanges

# Use it yourself
Please clone the reposity and run the application yourself if you are interested!

I highly recommend using Pyenv (https://github.com/pyenv/pyenv) to manage Python versions.

I built this application on Python 3.6 and Django 2.2.6

So create a virtualenv with that Python version and install the above version of Django.

Then you should be ready to rock:

activate your virtual env and run `python manage.py runserver`




