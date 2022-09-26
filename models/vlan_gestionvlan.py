from odoo import models, fields

class vlan(models.Model):
    _name = 'vlan.gestionvlan'
    _description = 'Vlan'

    name = fields.Integer(string="Vlan", required=True)
    direccion = fields.Char(string="Dirección")
 