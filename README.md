# postgres-tools

Contains tools and scripts to clean daily enrollment file and add to postgres
database. To update the database daily, include the following in a script which
runs daily:

```
python insertEnrollments.py
```
