# flask-blog

This project is originated from [Bluelog](https://github.com/greyli/bluelog.git) developed by [GreyLi](http://greyli.com).


## Installation

clone:
```
$ git clone https://github.com/mutalisk999/flask-blog.git
$ cd flask-blog
```
create & activate virtual env then install dependency:

with venv/virtualenv + pip:
```
$ python -m venv env  # use `virtualenv env` for Python2, use `python3 ...` for Python3 on Linux & macOS
$ source env/bin/activate  # use `env\Scripts\activate` on Windows
$ pip install -r requirements.txt
```
or with Pipenv:
```
$ pipenv install --dev
$ pipenv shell
```

init database:
```
$ flask init

Username: <admin name>
Password: <admin password>
Repeat for confirmation: <admin password again>
```

generate fake data: 

with **username** `admin` and **password** `helloflask`
```
$ flask forge
```


run
```
$ flask run

* Running on http://127.0.0.1:5000/
```


## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
