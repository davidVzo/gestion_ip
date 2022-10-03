from pkg_resources import require
from odoo import models, fields
class puerto(models.Model):
    _name = 'puerto.gestiondirecciones'
    _descripcion = 'Puerto de Switch'

    name = fields.Char(string="Número de puerto", required=True)
    id_switch = fields.Many2one('switch.gestiondirecciones',string="Switch", required=True)


