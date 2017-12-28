# flask-web-service
Olá, esse repositório é destinado a criação de um simples Web Service utilizando a biblioteca Flask do Python :cow:

## Requirements
- Python (3.6)
- Mysql
- Flask
- Mysql-python

## Run Server

```shell
python server.py
```

## Use Web Service

### Insert product
Access `url`
```
http://127.0.0.1:5000/add/<codigo>/<nome>/<descrição>/<preço>/<quantidade>
```

### Update product
Access `url`
```
http://127.0.0.1:5000/upd/<codigo>/<new_nome>/<new_descrição>/<new_preço>/<new_quantidade>
```

### Select All products
Access `url`
```
http://127.0.0.1:5000/all
```
