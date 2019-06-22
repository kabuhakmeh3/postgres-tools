# postgres-tools

**NOTE:** this repository is now a part of the enrollment-tools repo -- no
further updates will be made here.

Contains tools and scripts to clean daily enrollment file and add to postgres
database. To update the database daily, include the following in a script which
runs daily:

```
python insertEnrollments.py
```
