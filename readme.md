# instruction to run all the files

## 1) frame work setup

    a. run app.py file.
    b. click on the link in terminal.

## 2) Restful API

    a. run app.py file
    b. Open postman app for api testing
    c. use this api : http://127.0.0.1:5000/items in post request
    d. Json body : {"name": "books", "price": 19.99}

## 3) database interaction

    a. run sql_app.py file
    b. use this api : http://127.0.0.1:5000/tasks in post request
    c. Json body: {"title": "New Task"}
    d. make sure to edit the database connectivity.

## 4) authentication

    a. run app.py
    b. use this api : http://127.0.0.1:8080/login
    c. json body: {"username": "user1", "password": "boston@123"}
    d. you will get the access token
    e. use this api: http://127.0.0.1:8080/protected enter the bearer token and check the authentication.

## 5) video

    a. run video_app.py file and click on the link in terminal
    b. use the ui to upload the video file and click generate
    c. after generation video will get download.



