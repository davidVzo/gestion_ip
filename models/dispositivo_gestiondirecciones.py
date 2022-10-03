from odoo import models, fields
class dispositivo(models.Model):
    _name = 'dispositivo.gestiondirecciones'
    _descripcion = 'Dispositivos'

    name = fields.Char(string="Nombre de Dispositivo" , required=True)
    descripcion = fields.Char(string="Descripción")
    
