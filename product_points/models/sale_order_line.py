from odoo import _, api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    product_points = fields.Float(string="Points", compute="get_points")

    @api.depends('product_id', 'product_uom_qty')
    def get_points(self):
        for rec in self:
            print('ana geet')
            if rec.product_id:
                points_rec = self.env['product.point'].search([('product_id', '=', rec.product_id.id), ('state', '=', 'confirm')])
                print('ana geet', points_rec)
                if points_rec:
                    print('ana geet', points_rec.points * rec.product_uom_qty)
                    rec.product_points = points_rec.points * rec.product_uom_qty
                else:
                    print('ana mashiiii')
                    rec.product_points = 0.0
            else:
                print('ana mashiii')
                rec.product_points = 0.0
