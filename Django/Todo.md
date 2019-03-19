# Todo

UC버클리 DB 수업 추천

```bash
$ python manage.py makemigrations
You are trying to add a non-nullable field 'user' to todo without a default; we can't do that (the database needs something to populate existing rows
).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option:

```

DB에 column을 새로 추가시키려면 default 문제로 `db.sqlite3`와 `XXXX_initial.py`를 삭제하고 다시 만드는 것이 쉽다. 테이블을 추가로 만들어서 삭제하지 않게 할 수 있으나 성능이 떨어진다.