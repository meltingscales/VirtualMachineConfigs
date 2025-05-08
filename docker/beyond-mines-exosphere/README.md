## Building Docker image

```bash
bash build-docker.sh
```

## Running server

```bash
# start attached
bash start-server.sh

# start detached
bash start-server-detached.sh
```

## Attach to a detached instance

```bash
docker ps #get an id

docker attach <id>
```


## Server files

See `./minecraft-data/`
