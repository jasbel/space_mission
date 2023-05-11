from odoo import fields, models

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
   