from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from flask_login import current_user
from flask import redirect, url_for, flash

class SecuredModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                return redirect(url_for("main.home"))
            else:
                flash("You need to be logged in to access this page")
                return redirect(url_for("authentication.login"))
            
class SecureAdminView(AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role("admin")
    def inaccessible_callback(self, name, **kwargs):
        if not self.is_accessible():
            if current_user.is_authenticated:
                return redirect(url_for("main.home"))
            else:
                flash("You need to be logged in to access this page")
                return redirect(url_for("authentication.login"))
        
class UserModelView(SecuredModelView):
    column_exclude_list = ["_password"]
