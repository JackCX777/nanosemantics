from views import employee_create, employees, employee_detail_update, employee_delete


def setup_routes(app):
    app.router.add_route('POST', '/api/v1/create/employee', employee_create)
    app.router.add_route('GET', '/api/v1/employees', employees)
    app.router.add_route('GET', '/api/v1/employee/{employee_id}', employee_detail_update)
    app.router.add_route('POST', '/api/v1/employee/{employee_id}', employee_detail_update)
    app.router.add_route('POST', '/api/v1/delete/employee/{employee_id}', employee_delete)
