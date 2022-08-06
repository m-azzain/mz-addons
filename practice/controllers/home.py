
from odoo.addons.website.controllers.main import Website
from odoo import http

class Home(Website):

    def index(self, **kw):
        # return """
        #    <h1> hello there </h1>
        # """
        return super().index(**kw)
        # if request.session.uid and not is_user_internal(request.session.uid):
        #     return request.redirect_query('/web/login_successful', query=request.params)
        # return request.redirect_query('/web', query=request.params)