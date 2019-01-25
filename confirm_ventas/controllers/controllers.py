# -*- coding: utf-8 -*-
from odoo import http

# class ConfirmVentas(http.Controller):
#     @http.route('/confirm_ventas/confirm_ventas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/confirm_ventas/confirm_ventas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('confirm_ventas.listing', {
#             'root': '/confirm_ventas/confirm_ventas',
#             'objects': http.request.env['confirm_ventas.confirm_ventas'].search([]),
#         })

#     @http.route('/confirm_ventas/confirm_ventas/objects/<model("confirm_ventas.confirm_ventas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('confirm_ventas.object', {
#             'object': obj
#         })