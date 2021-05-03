# Chat
Simple chat app use django and redis


1. Clone the repository

2. create a virtual environment using `virtualenv venv`

3. Activate the virtual environment by running `source venv/bin/activate`

- On Windows use `source venv\Scripts\activate`

4. Install the dependencies using `pip install -r requirements.txt`

5. docker(you need install docker in ypur pc) in linux or mac `sudo docker run -p 6379:6379 -d redis:5`

6. Migrate existing db tables by running `python manage.py migrate`

7. Run the django development server using `python manage.py runserver`


![alt text](https://alisamadzadeh.ir/chat/Screenshot_2021-05-03%20Chat.png)


![alt text](https://alisamadzadeh.ir/chat/Screenshot_2021-05-03%20Chat_1_.png)


![alt text](https://alisamadzadeh.ir/chat/Screenshot_2021-05-03%20Chat_2_.png)


![alt text](https://alisamadzadeh.ir/chat/Screenshot_2021-05-03%20Chat_3_.png)
