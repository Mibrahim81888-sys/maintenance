from odoo import fields, models


class VisitDetails(models.Model):
    _name = 'visit.details'
    _description = 'Visit Details'

    name = fields.Char(string='name', required=True)
    ticket_id = fields.Many2one(
        'maintenance.ticket',
        string='Ticket',
        ondelete='cascade',
    )
    date = fields.Date(string='Date', default=fields.Date.today)
