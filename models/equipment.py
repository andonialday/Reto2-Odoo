# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-

from odoo import models, fields

class equipment(models.Model):
     _name = 'rentalg1c.equipment'

     name = fields.Char()
     dateadd = fields.Date()
     cost = fields.Float()
     description = fields.Text()
     
     event_equipments=fields.Many2one('rentalg1c.event_equipment',ondelete='set null', string='Rental')