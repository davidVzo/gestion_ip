from odoo import models, fields
class dispositivo(models.Model):
    _name = 'dispositivo.gestiondirecciones'
    _descripcion = 'Dispositivos'

    name = fields.Char(string="Nombre de Dispositivo" , required=True)
    description = fields.Char(string="Descripción")
    
