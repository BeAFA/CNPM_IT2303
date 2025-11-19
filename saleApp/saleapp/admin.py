from flask_admin import Admin, AdminIndexView, expose
from flask_admin.theme import Bootstrap4Theme
from flask_admin.contrib.sqla import ModelView
from saleapp import app, db
from models import Category, Product


class MyCategoryView(ModelView):
    column_list = ['name', 'created_date', 'products']
    column_searchable_list = ['name']
    column_filters = ['name']

    column_labels = {
        'name': 'Tên loại',
        'created_date': 'Ngày tạo',
        'products': 'Danh sách sản phẩm'
    }

class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self) -> str:
        return self.render('admin/index.html')
admin = Admin(app=app, name="E-Shop", theme=Bootstrap4Theme(), index_view=MyAdminIndexView())

admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(ModelView(Product, db.session))
