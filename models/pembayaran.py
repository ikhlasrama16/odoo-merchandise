from odoo import api, fields, models


class Pembayaran(models.Model):
    _name = 'merch.pembayaran'
    _description = 'New Description'

    name = fields.Char(string='Name')
    order_id = fields.Many2one(comodel_name='merch.order', string='Order')
    tgl_pembayaran = fields.Date(string='', default=fields.Date.today())
    tagihan = fields.Char(compute='_compute_tagihan', string='tagihan')

    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total
    
    @api.model
    def create(self,vals):
        record = super(Pembayaran, self).create(vals) 
        if record.tgl_pembayaran:
            self.env['merch.order'].search([('id','=',record.order_id.id)]).write({'sudah_dibayar':True})
            return record 
    
    def unlink(self):
        for x in self:
            self.env['merch.order'].search([('id', '=', x.order_id.id)]).write({'sudah_dibayar':False})           
        record = super(Pembayaran, self).unlink()