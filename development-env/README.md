# Development Environment for the "Geodata for Testing Automated Driving Systems" Project

The docker-compose file provides the configuration for the development environment.

## Containing Services

| Service Name  |                             Description                             |   Ports   | Notes                                                                                           |
|:-------------:|:--------------------------------------------------------------------|:----------|:------------------------------------------------------------------------------------------------|
| `3DCityDB`    | geo database to store, represent, and manage virtual 3D city models | 5432:5432 | User: `postgre`; Password: `changeMe!`                                                          |
| `PgAdmin`     | web-based administration tool for PostgreSQL                        | 8080:8080 | Email: `postgre@example.com`; Password: `secret`                                               |
| `citygml2osi` | prototyp converts from CityGML to OSI                               |           | Requires `GITLAB_CI_TOKEN` environment variable; keeps running with `command: tail -F anything` |

## Prerequisite

A [Docker](https://www.docker.com/) or similar installation is needed to build and run the docker-compose file.

## Starting the environment

```bash
$ docker-compose up
```

### Starting a single service

```bash
$ docker-compose up <service name>
```

## Stoping the environment

```bash
$ docker-compose down
```

### Stoping a single service

```bash
$ docker-compose down <service name>
```

### Building a service

```bash
$ docker-compose build <service name>
```

> **Note:** This is usefull to update the `citygml2osi` service.


### Generate mapping schema 
```python
sqlacodegen "postgresql://${DATABASE_USER}:${DATABASE_PASSWORD}@${DATABASE_HOST}:${DATABASE_PORT}/citydb" --noinflect --schema osi --outfile osidb.py
```
> **Note:** Tables should be transforemd into classes manually