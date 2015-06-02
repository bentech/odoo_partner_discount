# -*- encoding: utf-8 -*-
from openerp import models, fields

class ResPartnerDiscount(models.Model):

    _inherit = 'res.partner'
 
    discount = fields.Float(string="Discount %")
