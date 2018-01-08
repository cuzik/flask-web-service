# flask-web-service
Olá, esse repositório é destinado a criação de um simples Web Service utilizando a biblioteca Flask do Python :cow:

## Requirements
- Python (3.6)
- Mysql
- Flask
- Mysql-python

## install [dependencias]
```shell
pip3 install flask
pip3 install flask-restful
pip3 install mysql-connector-python-rf
```

## Run Server

```shell
python server.py
```

## Use Web Service

### Insert product
Access `url`
```
http://127.0.0.1:5000/add/<cod>/<name>/<description>/<price>/<stock>
```

### Update product
Access `url`
```
http://127.0.0.1:5000/upd/<cod>/<attr_1_name>:<attr_1_value>,<...>,<attr_n_name>:<attr_n_value>
```

### Select All products
Access `url`
```
http://127.0.0.1:5000/all
```

### Get product by somethig
Access `url`
```
http://127.0.0.1:5000/get/<attr_1_name>:<attr_1_value>,<...>,<attr_n_name>:<attr_n_value>
```
