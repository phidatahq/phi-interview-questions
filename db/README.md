## Add tables to the database

Steps to add a new table to the database using alembic:

1. Add SqlAlchemy tables in the `db/tables` directory.
2. Import the SqlAlchemy class in the `db/tables/__init__.py` file.
3. Create a database revision using: `docker exec -it dev-phi-interview-questions -c db/alembic.ini revision --autogenerate -m "Revision Name"`
4. Upgrade database using: `docker exec -it dev-phi-interview-questions -c db/alembic.ini upgrade head`
5. Downgrade database using: `docker exec -it dev-phi-interview-questions -c db/alembic.ini downgrade -1`
