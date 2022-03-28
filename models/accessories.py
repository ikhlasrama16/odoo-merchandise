from odoo import api, fields, models


class Accessories(models.Model):
    _name = 'merch.accessories'
    _description = 'New Description'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
    
