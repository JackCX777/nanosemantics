from aiohttp import web
import db


async def employee_create(request):
    """
        ---
        tags:
        - Employees
        description: This end-point allows to create employee.
        parameters:
        - in: body
          name: employees name
          surname: employees surname
          salary: employees salary
          description: The employee to create.
          schema:
            type: object
            required:
              - name
              - surname
              - salary
            properties:
              name:
                type: string
              surname:
                type: string
              salary:
                type: integer
    """
    if request.method == 'POST':
        data = await request.json()
        async with request.app['db'].acquire() as conn:
            await db.create_employee(conn, data.get('name'), data.get('surname'), data.get('salary'))
            raise web.HTTPCreated
    else:
        raise web.HTTPMethodNotAllowed


async def employees(request):
    """
        ---
        tags:
        - Employees
        description: This end-point allows to get all employees.
    """
    print("Yahoo!!!")
    if request.method == 'GET':
        async with request.app['db'].acquire() as conn:
            records = await db.get_employees(conn)
            employees_list = [dict(emp) for emp in records]
            return web.json_response({'employees': employees_list})
    else:
        raise web.HTTPMethodNotAllowed


async def employee_detail_update(request):
    """
        ---
        tags:
        - Employees
        description: This end-point allows to view employees detail or update employee.
        parameters:
        - in: path
          name: employee_id
          required: true
          schema:
            type: integer
            minimum: 1
          description: The employee ID
        - in: body
          name: employees name
          surname: employees surname
          salary: employees salary
          description: The employee to update.
          schema:
            type: object
            properties:
              name:
                type: string
              surname:
                type: string
              salary:
                type: integer
    """
    async with request.app['db'].acquire() as conn:
        employee_id = request.match_info['employee_id']
        if request.method == 'GET':
            try:
                record = await db.get_employee(conn, employee_id)
            except db.RecordNotFound as e:
                raise web.HTTPNotFound(text=str(e))
            return web.json_response(record)
        elif request.method == 'POST':
            data = await request.json()
            await db.update_employee(conn, employee_id, data)
            raise web.HTTPOk
        else:
            raise web.HTTPMethodNotAllowed


async def employee_delete(request):
    """
        ---
        tags:
        - Employees
        description: This end-point allows to delete employee.
        parameters:
        - in: path
          name: employee_id
          required: true
          schema:
            type: integer
            minimum: 1
          description: The employee ID
      """
    employee_id = request.match_info['employee_id']
    if request.method == 'POST':
        async with request.app['db'].acquire() as conn:
            await db.delete_employee(conn, employee_id)
            raise web.HTTPOk
    else:
        raise web.HTTPMethodNotAllowed
