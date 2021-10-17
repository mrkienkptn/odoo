# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Estate',
    'version' : '1.1',
    'category': 'Accounting/Esxxx',
    'installable': True,
    'application': True,
    'data': [
        'data/res.country.state.csv',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',        
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_menu.xml'
    ]
}