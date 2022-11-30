from app import app
from . import views

app.add_url_rule('/', view_func=views.transaction_list, endpoint='transaction_list')
app.add_url_rule('/transaction/<int:id>', view_func=views.transaction_detail, endpoint='transaction_detail')
app.add_url_rule('/transaction/create', view_func=views.transaction_create, methods=['GET', 'POST'], endpoint='transaction_create')
app.add_url_rule('/transaction/<int:id>/update', view_func=views.transaction_update, methods=['GET', "POST"], endpoint='transaction_update')
app.add_url_rule('/transaction/<int:id>/delete', view_func=views.transaction_delete, methods=['GET', "POST"], endpoint='transaction_delete')

app.add_url_rule('/register', view_func=views.register_view, methods=['GET', 'POST'], endpoint='register')
app.add_url_rule('/login', view_func=views.login_view, methods=['GET', 'POST'], endpoint='login')
app.add_url_rule('/logout', view_func=views.logout_view, endpoint='logout')