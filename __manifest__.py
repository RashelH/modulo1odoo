{
    "name": "Listas de Tarea",
    "sumary": "To-do Gestión de Lista de Tareas",
    "version": "13.0",
    "author": "Rashel Hernandez C. <rashel.oohel@gmail.com",
    "category": "Tareas",
    "depends": ["base", "mail", "base_setup"],
    "description": """
    Description text
    """,
    # data files always loaded at installation
    "data": [
        # 'views/mymodule_view.xml',
        "views/tarea.xml",
        "security/security.xml",
        "security/ir.model.access.csv",
        "wizard/wizard.xml",
        "template/email_tarea_atrasada.xml",
        "data/cron_tarea_atrasada.xml",
    ],
    # data files containing optionally loaded demonstration data
    "demo": [
        # 'demo/demo_data.xml',
    ],
}
