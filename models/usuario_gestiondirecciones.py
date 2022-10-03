from odoo import models, fields

class usuario(models.Model):
    _name = 'usuario.gestiondirecciones'
    _description = 'Usuarios'

    name = fields.Char(string="Hostname", required=True)
    nombre = fields.Text(string="Nombre")
    apellido = fields.Text(string="Apellido")
    cedula = fields.Char(string="Cédula")

    usuario = fields.Char(string="Usuario")
    ext_telefonica = fields.Char(string="Extención telefónica")
    
    """
    celular = fields.Char(string="Celular", size=9)
    n_colegiatura = fields.Char(string="Número de colegiatura")
    id_cita = fields.One2many('cita.gestionhospital', 'cod_cita', string="Citas del doctor")
    """