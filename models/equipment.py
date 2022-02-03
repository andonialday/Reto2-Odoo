# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class equipment(models.Model):
    _name = 'rentalg1c.equipment'

    name = fields.Char()
    dateadd = fields.Date()
    cost = fields.Float()
    description = fields.Text()
     
    event_equipments = fields.One2many('rentalg1c.event_equipment', 'equipment', string="events")
    
    @api.constrains('cost')
    def _verify_positive_cost(self):
        for record in self:
            if record.cost < 1:
                raise ValidationError("An Equipment cannot have a negative or zero cost")
            
    @api.onchange('cost')
    def _control_positive_cost(self):
        for record in self:
            if record.cost < 1:
                raise ValidationError("An Equipment cannot have a negative or zero cost")        