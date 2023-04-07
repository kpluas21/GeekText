# GeekText
A RESTful API for a fictional online bookstore, GeekText using Django and written in Python

Make sure you have python , pip , and django already installed. I won't go over that here as there are plenty of resources that teach that. 

* #### Run It
    Fire up the server using this one simple command:
    ```bash
        $ python manage.py runserver
    ```
    If your terminal doesn't recognize python for whatever reason use python3 instead
    ```bash
        $ python3 manage.py runserver
    ```
    You can now access the file api service on your browser by using
    ```
        http://localhost:8000/
    ```
    
    When you want to create a new app to work on a new feature, use this command
    ```
        python manage.py startapp name_of_your_app
    ```
    As always, use python3 is python isn't recognized.
    

    The idea behind creating different apps is to separate the logic between several different unrelated applications. Book Browsing and sorting
    shouldn't be with the logic behind a Shopping cart, etc.

#### Testing your feature
Use Curl to test your feature. Again, teaching curl is outside the scope of this readme, but here is a quick example on using curl to post a discount
    based on the publisher of the book
    ```
    ➜  ~ curl -X PATCH http://localhost:8000/updatepricing/Owl%20Books/50/
    ```
