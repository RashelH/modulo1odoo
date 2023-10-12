"""
 @autor Rashel Hernandez C. <rashel.oohel@gmail.com>
 @date: 12/10/23
 @name: 
"""
from odoo import models, fields


class WizardReapertura(models.TransientModel):
    """
    Modelo Transitorio que reapertura las tareas que se encuentran en categoria Atrasada
    """

    _name = "tarea.wizard_reapertura"
    _description = "TO-DO - Reapertura de Tarea"

    motivo_reapertura = fields.Text(
        string="Motivo de reapertura", 
        required=True
    )
    fecha_limite_nueva = fields.Datetime(
        string="Fecha Límite", 
        required=True
    )

    def confirmar_reapertura(self):
        """
        Repertura de Tarea
        """
        tarea = self.env["tareas.lista_tarea"].browse(self.env.context.get("active_id"))
        if tarea and tarea.categoria == "atrasado":
            tarea.write({"categoria": "pendiente"})

        return {"type": "ir.actions.act_window_close"}
