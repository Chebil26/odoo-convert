# -*- coding: utf-8 -*-
# from odoo import http


# class Co(http.Controller):
#     @http.route('/co/co/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/co/co/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('co.listing', {
#             'root': '/co/co',
#             'objects': http.request.env['co.co'].search([]),
#         })

#     @http.route('/co/co/objects/<model("co.co"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('co.object', {
#             'object': obj
#         })
