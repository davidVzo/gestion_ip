import string
from odoo import models, fields
class direccion(models.Model):
    _name = 'direccion.gestiondirecciones'
    _descripcion = 'Direcciones'

    name = fields.Char(string="Dirección" , required=True)
    siglas = fields.Char(string="Siglas")
    responsable = fields.Char(string="Responsable")
