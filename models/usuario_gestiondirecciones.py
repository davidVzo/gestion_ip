from odoo import models, fields

class usuario(models.Model):
    _name = 'usuario.gestiondirecciones'
    _description = 'Usuarios'

    name = fields.Char(string="Cédula del usuario", required=True)
    nombre = fields.Text(string="Nombre")
    apellido = fields.Text(string="Apellido")
    """
    celular = fields.Char(string="Celular", size=9)
    n_colegiatura = fields.Char(string="Número de colegiatura")
    id_cita = fields.One2many('cita.gestionhospital', 'cod_cita', string="Citas del doctor")
    """