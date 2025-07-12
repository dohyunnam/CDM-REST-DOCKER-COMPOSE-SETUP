# build

## prerequisites:
#### add ```./restapi/keys.env``` with defined ```CLIENT_ID``` and ```CLIENT_SECRET```

after keys.env is made, run the commands below in the terminal (within the repo directory)

```
docker compose build
docker compose up -d
```

after the restapi image is up and running, type ```http://localhost:1241/``` in the browser to see if the message ```{"message":"Hello, World!"}``` is properly being displayed. If yes, the server is live!

# use

### FASTapi
- accessible through ```http://localhost:1241/```
- currently implemented endpoints: 
- - ```/```
- - ```/get-token```