# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'My Farm',
    'version' : '1.1',
    'category': 'Services',
    'installable': True,
    'application': True,
    'depends': ['project'],
    'data': [
        'data/res.country.state.csv',
        'data/seq.xml',
        'security/ir.model.access.csv',        
        'views/farm_configuration_farm_locations.xml',
        'views/farm_configuration_fleets.xml',
        'views/farm_configuration_farmers.xml',
        'views/farm_configuration_farm_locations_detail.xml',
        'views/farm_configuration_stages.xml',
        'views/farm_crops.xml',
        'views/farm_dieases_cure.xml',
        'views/farm_incidents.xml',
        'views/farm_projects.xml',
        'views/farm_tasks.xml',
        'views/farm_crop_requests.xml',
        'views/farm_menu.xml',
    ],
    'asset': {
        'web.assets_backend': [
            'farm/static/src/**/*'
        ]
    },
    'license': 'LGPL-3'
}