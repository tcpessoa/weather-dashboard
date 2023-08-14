Generic single-database configuration.

# Init alembic
```
alembic init alembic
```
# Generate migrations
```
alembic revision --autogenerate -m "migration message"
```

# Run migrations
```
alembic upgrade head
```
