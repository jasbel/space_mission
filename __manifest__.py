# -*- coding: utf-8 -*-

{
    'name': 'academy',
    'summary': """Odoo Academy""",
    'description': """
        Courses Javascript.
        - Framework JS
        - Typescript
        - Educar al Alex
    """,
    'author': 'Asbel Jhonatan',
    'license': 'LGPL-3',
    'website': 'https://develoop.net',
    'category': 'Education/Javacript',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/space_mission_groups.xml',
        'security/ir.model.access.csv',
        'security/space_mission_security.xml',
        'views/space_mission_menuitems.xml',
        'views/spaceship_views.xml'
    ],
    'demo': [
        'demo/spaceship_demo.xml',
    ],
    'application': True,
}