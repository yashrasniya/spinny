# Spinny
###### This project is for a Internship.

##### In this project I build a store api system where staff of store can add Cuboid and user can see these Cuboid by api. User can update the dimensions but not able delete Cuboid this permission is only given to creator of that Cuboid. there is much more...

### Requirements 
* Python
* Postman

### Install Project

` $ git clone https://github.com/yashrasniya/spinny `

` $ cd spinny `

` $ pip install -r req.txt `

` $ python manage.py runserver`

### Api 

[Postman Link](https://www.postman.com/lively-satellite-954449/workspace/spinny)
#### Login

 ```cUrl
 curl --location 'http://127.0.0.1:8000/api/login/' \
--form 'username="happy"' \
--form 'password="YasH*8938#"' 
```
User added by admin
` $ python manage.py createsuperuser `

#### Create Cuboid 

 ```js
curl --location 'http://127.0.0.1:8000/api/box/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1NTM5Mjk1LCJpYXQiOjE2OTI5NDcyOTUsImp0aSI6ImIyYjZiNDM1NzljZTQxODI5OGRjNTAyY2NkMjdhNzU2IiwidXNlcl9pZCI6MX0.yeIJFEKyn5khSwBl0O9677nG5kDX3SR2LM64Pas3liY' \
--form 'Length="1"' \
--form 'width="2"' \
--form 'Height="3"'
```
#### Delete Cuboid 

 ```js
curl --location --request DELETE 'http://127.0.0.1:8000/api/box/delete/7/' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1NTM5Mjk1LCJpYXQiOjE2OTI5NDcyOTUsImp0aSI6ImIyYjZiNDM1NzljZTQxODI5OGRjNTAyY2NkMjdhNzU2IiwidXNlcl9pZCI6MX0.yeIJFEKyn5khSwBl0O9677nG5kDX3SR2LM64Pas3liY'
```

#### List Cuboid 

 ```js
curl --location 'http://127.0.0.1:8000/api/box/ \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1NTM5MTg3LCJpYXQiOjE2OTI5NDcxODcsImp0aSI6ImZjNWNjMjViNjEzYjQ1M2FiMTRlMWU0MjExOTQzMzI3IiwidXNlcl9pZCI6Mn0.jhQDChxd2MdMRHasrzs1Va7emAWrXx4LO6967xT8AkY'
```
###### List Filter 

length_more_than,
length_less_than,
breadth_more_than,
breadth_less_than,
height_more_than,
Area_less_than,
Area_more_than,
Volume_less_than,
Volume_more_than,
Ceated_after,
Ceated_before,
username

###### List Filter Example

``` js
curl --location 'http://127.0.0.1:8000/api/box/?Ceated_after=2023-12-12' \
--header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1NTM5MTg3LCJpYXQiOjE2OTI5NDcxODcsImp0aSI6ImZjNWNjMjViNjEzYjQ1M2FiMTRlMWU0MjExOTQzMzI3IiwidXNlcl9pZCI6Mn0.jhQDChxd2MdMRHasrzs1Va7emAWrXx4LO6967xT8AkY'
```


