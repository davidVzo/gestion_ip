from email.policy import default
from itertools import chain
import string
from odoo import models, fields
class ip(models.Model):
    _name = 'ip.gestiondirecciones'
    _descripcion = 'Ips'

    name = fields.Char(string="Dirección ip" , required=True)
    cod_vlan = fields.Many2one('vlan.gestionvlan',string="Vlan",required=True)
 
    