# build

## prerequisites:
#### add ```./restapi/keys.env``` with defined ```CLIENT_ID``` and ```CLIENT_SECRET```

```
#after keys.env is made, run 
docker compose build
docker compose up -d
```

# use

- accessible through ```http://localhost:1241/```
- currently implemented endpoints: ```/get-token```
- - ```http://localhost:1241/get-token```