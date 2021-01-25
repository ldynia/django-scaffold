# Instructions

```bash
$ docker-compose up
$ docker exec -it django-demo ash
$ umask 113
```


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