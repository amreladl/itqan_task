from odoo import _, api, fields, models
from datetime import date
from odoo.exceptions import UserError


class ProductPoint(models.Model):
    _name = "product.point"
    _rec_name = "product_id"

    def get_product_domain(self):
        confirmed_points = self.env['product.point'].search([('state', '=', 'confirm')]).mapped('product_id')
        return [('sale_ok', '=', True), ('id', 'not in', confirmed_points.ids)]

    product_id = fields.Many2one(comodel_name="product.product", string="Product", required=True, domain=get_product_domain)
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
    points = fields.Float(string="Points", required=True)
    state = fields.Selection(string="Status", selection=[('draft', 'Draft'), ('confirm', 'Confirmed'), ('end', 'Ended'), ('cancel', 'Canceled')], default='draft')
    status_update_user_id = fields.Many2one(comodel_name="res.users", string="Latest Status Update User", readonly=True)

    @api.onchange('start_date')
    def onchange_start_date(self):
        if self.start_date:
            self.end_date = False

    def action_confirm(self):
        confirmed_points = self.env['product.point'].search([('state', '=', 'confirm')]).mapped('product_id')
        if self.product_id.id not in confirmed_points.ids:
            self.write({'state': 'confirm'})
        else:
            raise UserError('You can not have 2 records confirmed of the same product at the same time')

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_end(self):
        records = self.search([])
        for rec in records:
            if rec.end_date and rec.end_date >= date.today():
                rec.write({'state': 'end'})

    def write(self, vals):
        if vals.get('state'):
            vals['status_update_user_id'] = self.env.uid
        return super(ProductPoint, self).write(vals)
