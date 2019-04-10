# -*- coding: utf-8 -*-
from odoo import http

# class Quantities(http.Controller):
#     @http.route('/quantities/quantities/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/quantities/quantities/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('quantities.listing', {
#             'root': '/quantities/quantities',
#             'objects': http.request.env['quantities.quantities'].search([]),
#         })

#     @http.route('/quantities/quantities/objects/<model("quantities.quantities"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('quantities.object', {
#             'object': obj
#         })