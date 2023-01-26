from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_points = fields.Float(string="Total Points",  compute='get_total_points')

    @api.depends('order_line')
    def get_total_points(self):
        for rec in self:
            rec.total_points = sum(rec.order_line.mapped('product_points'))
