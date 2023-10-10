from odoo import models, fields, api
from datetime import datetime

class ListaTarea(models.Model):
    _name = "tareas.lista_tarea"
    _description = "Lista de Tareas"

    def button_hecho(self):
        for rec in self:
            rec.write({"state": "hecho"})

    def button_cancelar(self):
        for rec in self:
            rec.write({"state": "cancelar"})

    titulo = fields.Char(string="Titulo", required=True)
    descripcion = fields.Text(string="Descripción", required=True)
    fecha_limite = fields.Datetime(string="Fecha Límite", required=True)
    usuario_asignado = fields.Many2one(
        "res.users", string="Usuario Asignado", required=True
    )
    categoria = fields.Selection(
        [
            ("pendiente", "Pendiente"),
            ("terminado", "Terminado"),
            ("atrasado", "Atrasado"),
        ],
        default="pendiente",
        string="Categoria",
        required=True,
    )
    motivo_reapertura = fields.Text(string="Motivo de reapertura", required=True)

    state = fields.Selection(
        [("borrador", "Borrador"), ("hecho", "Hecho"), ("cancelar", "Cancelar")],
        required=True,
        default="borrador",
    )

    def _cron_tareas_atrasadas(self):
        today = datetime.now()
        tasks_to_update = self.search(
            [("fecha_limite", "<", today), ("categoria", "=", "pendiente")]
        )
        for task in tasks_to_update:
            task.write({"categoria": "atrasado"})
            if task.usuario_asignado:
                template_id = self.env.ref("tareas.lista_tarea.email_tarea_atrasada")
                template_id.send_mail(task.id, force_send=True)
                                
