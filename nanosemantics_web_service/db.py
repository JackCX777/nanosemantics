import aiopg.sa
from sqlalchemy import MetaData, Table, Column, Integer, String


__all__ = ['employees']

meta = MetaData()

employees = Table(
    'employees',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(200), nullable=False),
    Column('surname', String(200), nullable=False),
    Column('salary', Integer, server_default="0", nullable=False),
)


class RecordNotFound(Exception):
    """Requested record in database was not found"""


async def pg_context(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()


async def create_employee(conn, name, surname, salary):
    stmt = employees.insert().values(name=name, surname=surname, salary=salary)
    await conn.execute(stmt)


async def get_employees(conn):
    stmt = employees.select()
    result = await conn.execute(stmt)
    dep_records = await result.fetchall()
    return dep_records


async def get_employee(conn, employee_id):
    stmt = employees.select().where(employees.c.id == employee_id)
    result = await conn.execute(stmt)
    record = await result.first()
    if not record:
        msg = f'Employee with id: {employee_id} does not exists'
        raise RecordNotFound(msg)
    return dict(record)


async def update_employee(conn, employee_id, data):
    stmt = employees.update().values(**data).where(employees.c.id == employee_id)
    await conn.execute(stmt)


async def delete_employee(conn, employee_id):
    stmt = employees.delete().where(employees.c.id == employee_id)
    await conn.execute(stmt)
