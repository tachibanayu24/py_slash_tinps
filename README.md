# py/tinps

## How to build react

You can build the React app just run the follow command.
`
./manage.py runserver react
`

then check `http://127.0.0.1:8000/`

## How to connect to mysql

`pip install PyMySQL==0.8.0`

`mysql -u root`
`CREATE DAtABASE py_slash_tinps`
`¥q`

`./manage.py migrate`

`mysql -u root`
`SHOW TABLES FROM py_slash_tinps`

You can check the tables added by migrations.


