# -*- coding: utf-8 -*-

{
    'name': 'Space Mission',
    'summary': """Odoo va al espacio""",
    'description': """
        Organiza la logística para viejar a la luna.
        - Nave Espacial
        - Tripulación Espacial
    """,
    'author': 'Franz Montealegre',
    'license': 'LGPL-3',
    'website': 'https://develoop.net',
    'category': 'Organisation/Trip',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/space_mission_groups.xml',
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml'
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'application': True,
}