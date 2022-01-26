# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import ValidationError

class event_equipment(models.Model):
    _name = 'rentalg1c.event_equipment'
    
    quantity = fields.Integer(string="Quantity", required=True)
    
    event = fields.Many2one('rentalg1c.event', ondelete='set null', string="Event")
    equipment = fields.Many2one('rentalg1c.equipment', ondelete='set null', string="Equipment")

    @api.constrains('quantity')
    def _verify_positive_quantity(self):
        for record in self:
            if record.quantity < 1:
                raise ValidationError("The Equipment Quantity rented for an Event cannot be negative (In case of 0, the entry would not have sense for being recorded)")