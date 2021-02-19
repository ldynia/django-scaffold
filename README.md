# Instructions

```bash
$ docker-compose up
$ docker exec -it django-demo ash
$ umask 113
$ python manage.py seed
```

```bash
$ python manage.py leon -h
$ python manage.py leon docs
$ python manage.py leon init demo Dummy
```
**Finally edit** `urls.py` and `schema.py`


# Examples

### Queries
```
query {
  allDummy {
    results(limit: 3) {
      id
      day
      weekday
      month
      year
      preSeeded
      createdAt
    }
  }
}
```


### Mutations

```
mutation {
  createDummy(newDummy:{ day:1, weekday: "Monday", month: "December", year: 2020}) {
    ok
    dummy {
      id
      day
      weekday
      month
      year
    }
  }
}
```