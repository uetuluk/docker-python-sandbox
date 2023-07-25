# Docker Based Python sandbox

The Python sandbox image for [Code Interpreter Lite](https://github.com/uetuluk/code-interpreter-lite) project.

## Build Image

You can build the image or pull it from Docker Hub.

```bash
make build-production-image
```

```bash
docker pull uetuluk/docker-python-sandbox:latest
```

This container can be run by itself, but it is intended to be used by the Code Interpreter Lite project.

```bash
make production
```

## Development Quickstart

If you are interested in developing more features for the sandbox, you can use the development image.
Build or pull it from the Docker Hub, then run the container.

```bash
make build-development-image
```

```bash
docker pull uetuluk/docker-python-sandbox-development:latest
```

Run the container.
```bash
make development
```
