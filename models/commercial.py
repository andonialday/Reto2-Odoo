# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-

from odoo import models, fields, api

class commercial(models.Model):
     _name = 'rentalg1c.commercial'
     _inherit = 'res.users'
     
     especialization = fields.Selection([('0','SONIDO'),
                                         ('1','ILUMINACION'),
                                         ('2','PIROTECNIA'),
                                         ('3','LOGISTICA')
                                        ],string='Especializacion', copy='False' )

     client = fields.One2many('rentalg1c.client','client', ondelete='set null', string="Client")
     