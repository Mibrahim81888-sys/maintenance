from odoo import models, fields

class ResponsibleUser(models.Model):
    _name = 'responsible.user'
    _description = 'Responsible User'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone')