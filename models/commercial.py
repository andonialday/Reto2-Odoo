# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models
from odoo import api
from odoo.exceptions import ValidationError

class commercial(models.Model):
    _name = 'rentalg1c.commercial'
    _inherit = 'rentalg1c.usr'
     
    especialization = fields.Selection([('0', 'SONIDO'),
                                       ('1', 'ILUMINACION'),
                                       ('2', 'PIROTECNIA'),
                                       ('3', 'LOGISTICA')
                                       ], string='Especializacion', copy='False')



    client = fields.One2many('rentalg1c.client', 'commercial', ondelete='set null', string="Client")
     
    @api.constrains('email')
    def _vali_null_email(self):
        if len(str(self.email)) < 10:
            raise ValidationError("No existen emails validos tan cortos, revisalo")
            
    @api.onchange('name')
    def _verify_valid_name(self):
        if len(str(self.name)) > 25:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El nombre del cliente no puede superar los 50 caracteres",
                },
            }