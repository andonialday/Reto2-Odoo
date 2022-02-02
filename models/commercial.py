# -*- coding: utf-8 -*-

from odoo import models, fields

class commercial(models.Model):
    _name = 'res.users'
    _inherit = 'res.users'
     
    especialization = fields.Selection([('0', 'SONIDO'),
                                       ('1', 'ILUMINACION'),
                                       ('2', 'PIROTECNIA'),
                                       ('3', 'LOGISTICA')
                                       ], string='Especializacion', default='0')



    client = fields.One2many('res.users', 'commercial', ondelete='set null', string="Client")
     