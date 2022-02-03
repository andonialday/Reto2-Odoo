# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models
from odoo import api
from odoo.exceptions import ValidationError

class client(models.Model):
    _name = 'rentalg1c.client'
    _inherit = 'rentalg1c.usr'

    tipo = fields.Selection([('0', 'PARTICULAR'), ('1', 'ASOCIATION'), ('2', 'ENTERPRISE'), ('3', 'PUBLIC_ENTITY')], string='Type', default='0', required=True)

    event = fields.One2many('rentalg1c.event', 'client', ondelete='set null', string='Event')
    commercial = fields.Many2one('rentalg1c.commercial', ondelete='set null', string='Commercial')
    
    @api.constrains('login')
    def _vali_null_login(self):
        if len(str(self.login)) > 25:
            raise ValidationError("El campo login no puede tener mas de 25 caracteres")
          
    
    @api.onchange('name')
    def _verify_valid_name(self):
        if len(str(self.name)) > 25:
            return {
                'warning': {
                    'title': "Error",
                    'message': "El nombre del cliente no puede superar los 50 caracteres",
                },
            }