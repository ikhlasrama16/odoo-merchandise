from odoo import api, fields, models


class Order(models.Model):
    _name = 'merch.order'
    _description = 'New Description'

    
    orderjaketdetail_ids = fields.One2many(comodel_name='merch.orderjaketdetail', inverse_name='orderj_id', string='Jaket')
    orderkaosdetail_ids = fields.One2many(comodel_name='merch.orderkaosdetail', inverse_name='orderk_id', string='Kaos')
    orderaccessoriesdetail_ids = fields.One2many(comodel_name='merch.orderaccessoriesdetail', inverse_name='ordera_id', string='Accessories')


    name = fields.Char(string='Kode Order', required=True)
    tanggal_pesan = fields.Datetime('Tanggal Pemesanan',default=fields.Datetime.now())
    total = fields.Char(compute='_compute_total', string='Total')
    
    
    @api.depends('orderkaosdetail_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['merch.orderkaosdetail'].search([('orderk_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['merch.orderjaketdetail'].search([('orderj_id', '=', record.id)]).mapped('harga'))
            c = sum(self.env['merch.orderaccessoriesdetail'].search([('ordera_id', '=', record.id)]).mapped('harga'))
            record.total = a + b + c
    sudah_dibayar = fields.Boolean(string='Sudah Dibayar', default=False)
    

class OrderKaosDetail(models.Model):
    _name = 'merch.orderkaosdetail'
    _description = 'New Description'

    orderk_id = fields.Many2one(comodel_name='merch.order', string='Order')
    kaos_id = fields.Many2one(comodel_name='merch.kaos', string='Kaos')

    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    
    @api.depends('kaos_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.kaos_id.harga

    
    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for  record in self:
            record.harga = record.harga_satuan * record.qty
    


class OrderJaketDetail(models.Model):
    _name = 'merch.orderjaketdetail'
    _description = 'New Description'

    orderj_id = fields.Many2one(comodel_name='merch.order', string='Order')
    jaket_id = fields.Many2one(comodel_name='merch.jaket', string='Jaket')


    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('jaket_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.jaket_id.harga

    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for  record in self:
            record.harga = record.harga_satuan * record.qty

    



class OrderAccessoriesDetail(models.Model):
    _name = 'merch.orderaccessoriesdetail'
    _description = 'New Description'

    ordera_id = fields.Many2one(comodel_name='merch.order', string='Order')
    accessories_id = fields.Many2one(comodel_name='merch.accessories', string='Accessories')

    name = fields.Char(string='Name')
    harga = fields.Integer(compute='_compute_harga', string='Harga')
    qty = fields.Integer(string='Quantity')
    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('accessories_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.accessories_id.harga

    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for  record in self:
            record.harga = record.harga_satuan * record.qty
    
    
    