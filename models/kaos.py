from odoo import api, fields, models


class Kaos(models.Model):
    _name = 'merch.kaos'
    _description = 'New Description'

    name = fields.Char(string='Name')
    deskripsi = fields.Char(string='Deskripsi')
    size = fields.Char(string='Size')
    bahan = fields.Char(string='Bahan')
    harga = fields.Integer(string='Harga')
    
    
    
