# Safe Register & Login Administration

__Safe mode for Demonstration.__

Build with:

__BACKEND:__ _Python 3.9 & Flask_

__FRONTEND:__ _JS, HTML & CSS_

__INTEGRATIONS:__ _Jinja2_

Deployed over Docker, inorder to contain a safety lab environment\

_PLEASE TAKE NOTICE:_ __runs only with Chrome,Modzilla and Explorer.__ 

## Endpoints

**Home**

**User**

* Registration
* Login
* Change Password
* Logout

**Admin**

* Admin's Menu
    * View all Users List
    * Change Password Configuration

## Home

endpoint: `/`\
![Home](https://user-images.githubusercontent.com/71320956/128612948-87c16955-b0cb-451b-95ac-9ef09cde5ca4.PNG)


## User

### Register

User Register by given _Name_, _E-mail_, _Password_ and _re-Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/register`
![Register](https://user-images.githubusercontent.com/71320956/128612974-48a73d9a-335d-43ee-85d8-12c54adee72f.PNG)

__CSRF attack on endpoint:__
````
$ curl -X POST -F 'username=Hacker' -F 'email=yougot@HACKED.com' 
-F 'password=AAaa1212@!12' -F 're_password=AAaa1212@!12' 
http://127.0.0.1:5000/users/register
````
__Result of attack:__\
![ResultRegiser](https://user-images.githubusercontent.com/71320956/131083301-c028f6b0-aef1-4eda-a506-fea45ac57e01.png)


### Login

User Login by given _Username_ and _Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/login`

![Login](https://user-images.githubusercontent.com/71320956/131085044-e6f5d58e-ea7c-4c64-b22a-4974d39b1308.png)
__CSRF attack on endpoint:__
````
$ curl -X POST -F 'name_email=Hacker' -F'password=AAaa1212@!12' 
http://127.0.0.1:5000/users/login
````
__Result of attack:__\
![ResultLogin](https://user-images.githubusercontent.com/71320956/131083477-de7f2399-6bdb-4a78-a9b5-997f5c92fecb.png)

### Change Password

User Change Password by given _Username_, _E-mail_, _New Password_ and _re-Password_

__methods:__ `GET`, `POST`\
__endpoint:__ `/users/change_password`

![ChangePassword](https://user-images.githubusercontent.com/71320956/128613009-17531174-2d74-4d45-a03c-2272917365bc.PNG)
__CSRF attack on endpoint:__
````
$ curl -X POST -F 'username=Hacker' -F 'email=yougot@HACKED.com' 
-F 'password=BBbb1212@!12' -F 're_password=BBbb1212@!12' 
http://127.0.0.1:5000/users/change_password
````
__Result of attack:__\
![ResultChangePassword](https://user-images.githubusercontent.com/71320956/131084746-01e2fa5d-c966-406f-a5be-6a1f1a1d4e51.png)

### Logout

User Logout

__methods:__ `GET`\
__endpoint:__ `/users/logout`
![AfterUserLogin](https://user-images.githubusercontent.com/71320956/128613030-143e994e-e4ed-4eb4-b8b5-2d9aa5479443.PNG)

## Admin

### Admin's Menu

__methods:__ `GET`\
__endpoint:__ `/admin/menu`

![AdminMenu](https://user-images.githubusercontent.com/71320956/128613037-286c71ef-8872-4de2-9754-b1c94eddbb96.PNG)

### User's List

Display all registered users & __Block/Unblock__ users

__methods:__ `GET`\
__endpoint:__ `/admin/all_users`

![UsersList](https://user-images.githubusercontent.com/71320956/128613054-b72342c5-5f27-47d0-b48d-fe734f4b6339.PNG)

### Password Configuration

Change password configuration:

* Length
* Complexity
* History
* Fail attempts

__methods:__ `GET`, `POST`\
__endpoint:__ `/admin/password_config`

![PasswordConfiguration](https://user-images.githubusercontent.com/71320956/128613057-39b79463-7f29-4bdc-bc55-f6d82e6c8a24.PNG)

__CSRF attack on endpoint:__
````
$ curl -X POST -F 'upper=0' -F 'lower=0' -F 'digits=0' 
-F 'spec=0' -F 'use_dict=0' -F 'length=0' -F 'history=10' 
-F 'tries=1000'  http://127.0.0.1:5000/admin/password_config
````
__Result of attack:__\
![ResultChangePassword](https://user-images.githubusercontent.com/71320956/131085277-0d0d257f-2e7e-4e15-a4d5-57a06e3adf1f.png)
