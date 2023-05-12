from odoo import fields, models
from odoo.exceptions import UserError, ValidationError

class Spacecrew(models.Model):
    _name = "space_mission.spaceship"
    _description = "Spaceship info"
    
    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    type = fields.Selection(
        [
            ('freighter', 'Freighter'),
            ('transport', 'Transport'),
            ('scout_ship', 'Scout Ship'),
            ('fighter', 'Fighter'),
        ],'Type')
    model = fields.Char(string="Model", required=True)
    build_date = fields.Date()
    captain = fields.Char(string="Captain")
    required_crew = fields.Integer(string="Required crew")
    length = fields.Float(string="Length")
    width = fields.Float(string="Width")
    height = fields.Float(string="Height")
    engine_number = fields.Char(string="Engine number")
    fuel_type = fields.Selection(
        [
            ('solid_fuel', 'Solid Fuel'),
            ('liquid_fuel', 'Liquid Fuel'),
        ],'Fuel type')
    
    base_price = fields.Floar(string='Base Price', default=0.00)

    additional_fee = fields.Float(string='Additional Fee', default=0.00)

    total_price = fields.Float(string='Total Price', readonly=True)

    @api.onchange('base_price', 'additional_fee')
    def _onchange_total_price(self):
        if self.base_price < 0.00:
            raise UserError('Base Price cannot be set as Negative.')

        self.total_price = self.base_price + self.additional_fee

    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError('Additional Fees cannot be less than 10.00: %s' % record.additional_fee)
                