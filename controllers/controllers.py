# -*- coding: utf-8 -*-
from odoo import http

# class Elsafwa(http.Controller):
#     @http.route('/elsafwa/elsafwa/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/elsafwa/elsafwa/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('elsafwa.listing', {
#             'root': '/elsafwa/elsafwa',
#             'objects': http.request.env['elsafwa.elsafwa'].search([]),
#         })

#     @http.route('/elsafwa/elsafwa/objects/<model("elsafwa.elsafwa"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('elsafwa.object', {
#             'object': obj
#         })