# Test FastAPI with async and sync 

## 1. create database and create table and run application
```shell
$ cd ./fastapi
$ docker-compose up
```

## 2. run test fastapi application
### 2.1. test blocking endpoint
```shell
$ ab -n 100 -c 100 http://127.0.0.1:8000/blocking-items/
```

### 2.2. test non-blocking endpoint (sync)
```shell
$ ab -n 100 -c 100 http://127.0.0.1:8000/items/
```

### 2.3. test non-blocking endpoint (async)
```shell 
$ ab -n 100 -c 100 http://127.0.0.1:8000/async-items/
```
## 3. run test django application
### 3.1. create database and table and run application
```shell    
$ cd ./django
$ docker-compose up
```

### 3.2. test endpoint
```shell
$ ab -n 100 -c 100 http://127.0.0.1:8000/items/
```