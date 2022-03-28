# -*- coding: utf-8 -*-
# from odoo import http


# class Merch(http.Controller):
#     @http.route('/merch/merch/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/merch/merch/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('merch.listing', {
#             'root': '/merch/merch',
#             'objects': http.request.env['merch.merch'].search([]),
#         })

#     @http.route('/merch/merch/objects/<model("merch.merch"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('merch.object', {
#             'object': obj
#         })
