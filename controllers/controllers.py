# -*- coding: utf-8 -*-
from odoo import http

# class Rentalg1c(http.Controller):
#     @http.route('/rentalg1c/rentalg1c/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rentalg1c/rentalg1c/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rentalg1c.listing', {
#             'root': '/rentalg1c/rentalg1c',
#             'objects': http.request.env['rentalg1c.rentalg1c'].search([]),
#         })

#     @http.route('/rentalg1c/rentalg1c/objects/<model("rentalg1c.rentalg1c"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rentalg1c.object', {
#             'object': obj
#         })