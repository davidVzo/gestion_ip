import string
from odoo import models, fields
class switch(models.Model):
    _name = 'switch.gestiondirecciones'
    _descripcion = 'Switch'

    name = fields.Char(string="Número Switch", required=True)
    modelo = fields.Char(String="Modelo")
    piso = fields.Char(string="Número de Piso")
    numero_puertos = fields.Char(string="Número de puertos")
    id_puerto= fields.One2many('puerto.gestiondirecciones', 'id_switch',  string="Puertos de Switch")


