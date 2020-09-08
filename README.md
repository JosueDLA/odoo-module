# Create a custom Odoo Module

Odoo (previously known as OpenERP) is business management software including ERP, CRM, e-commerce, billing, accounting, manufacturing, warehouse, project management, and inventory management. It has an open source “community” version under the LGPLv3 license and an enterprise version under commercial license.

## Prerequisites
- [Odoo](https://www.odoo.com/page/download)
- [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)

## PyCharm Configuration

After downloading and installing Odoo and PyCharm we need to create our new virtual environment. With this virtual environment we can see reflected the changes on the code instantly, otherwise we will need to restart the service off Odoo on every change we perform.

We start creating a new project on PyCharm. By default, PyCharm will create a new Virtual environment to the project.

![PyCharm New Project](/Images/PyCharm-1.png)

After creating the project, we need to setup the Run/Debug configurations with the following information: 

__Script Path:__ [PATH to odoo-bin]

__Parameters:__ --conf [PATH to odoo.conf]

![PyCharm New Project](/Images/PyCharm-2.png)

Now we need to install all the modules that Odoo needs to run, these modules are:

- PyPDF2
- babel
- passlib
- werkzeug
- lxml
- polib
- decorator
- win32service
- pypiwin32
- psycopg2
- python-dateutil
- werkzeug
- requests
- psutil
- jinja2
- reportlab
- html2text
- docutils

You can install these modules via Pip, whl files, requirements.txt or by using the pipfile

Install from requirements.txt

```bash
pip install -r [PATH to requirements.txt]
```

Install from Pipfile

```bash
pipenv install
```

## Custom Module

A Odoo module is a set of business logic which helps to enhance the existing functionality or add some new functionality in Odoo.

### Odoo.conf

To add our custom module to Odoo first we need to make a few changes to the odoo.conf file.

1. Firs we need to specify where our custom module will be stored.

```
addons_path: [Default PATH], [Custom PATH]
```

2. Next, we need to set a new port for the http port

```
http_port = 8070
```

### Module Structure

An Odoo [module](https://www.odoo.com/documentation/13.0/howtos/backend.html) can contain a number of elements:

__Manifest:___ The manifest file serves to declare a python package as an Odoo module and to specify the module metadata. This file is called __manifest\__.py and contains a single python dictionary. Learn more about the manifest file [here](https://www.odoo.com/documentation/10.0/reference/module.html).

__Business objects:__ Declared as Python classes, these resources are automatically persisted by Odoo based on their configuration.

__Data files:__ XML or CSV files declaring metadata (views or workflows), configuration data, demonstration data and more.

__Web controllers:__ Handle requests from web browser.

__Static web data:__ Images, CSS or JavaScript files used b the web interface or website.

### Basic Example

__Manifest__

```python
# -*- coding: utf-8 -*-
{
    'name': 'Res Partner Services',
    'version': '1.0',
    'description': 'Custom module for Odoo ERP',
    'summary': 'Custom module for Odoo ERP',
    'author': 'Jhon Doe',
    'category': 'Generic Modules/Inventory Control',
    'website': 'http://example.net/',
    'license': 'GPL-2',
    'depends': ['base'],
    'init_xml': [],
    'demo_xml': [],
    'data': ['respartner.xml'],
    'installable': True,
    'active': True
}
```

__respartner.xml__

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="resPartnerId" model="ir.ui.view">
        <field name="name">partner.partner.inherit</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form" />
        <field name="arch" type="xml">
            <notebook position="inside">
                <page string="Sessions">
                    <group>
                        <field name="service"/>
                        <field name="url"/>
                        <field name="user"/>
                        <field name="password" password="True"/>
                    </group>
                </page>
            </notebook>
        </field>
    </record>
</odoo> 
```

__respartner.py__

```python
from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    service = fields.Char(required=False, string="Service")
    url = fields.Char(required=False, string="URL")
    user = fields.Char(required=True, string="User")
    password = fields.Char(required=True, string="Password")
```

This code should output 4 custom inputs on the contacts view.

![Custom Module Odoo](/Images/Odoo-1.png)

### Tree Input Example
__respartner.xml__

```xml
<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="resPartnerId" model="ir.ui.view">
        <field name="name">res.partner.inherit</field>
        <field name="model">res.partner</field>
        <field name="inherit_id" ref="base.view_partner_form" />
        <field name="arch" type="xml">
            <notebook position="inside">

                 <page string="Sessions">
                    <field name="partners">
                        <tree>
                             <field name="partner_id" invisible="1" />
                             <field name="service"/>
                             <field name="url"/>
                             <field name="user"/>
                             <field name="password" password="True"/>
                         </tree>
                    </field>

                 </page>

            </notebook>
        </field>
    </record>
</odoo> 
```

__respartner.py__

```
# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    partners = fields.One2many('res.partner.services.list', 'partner_id', string='Partners')


class PartnerList(models.Model):
    _name = 'res.partner.services.list'
    _description = 'Service List'

    partner_id = fields.Many2one('res.partner.services', strin='Partner')
    service = fields.Char(required=False, string="Service")
    url = fields.Char(required=False, string="URL")
    user = fields.Char(required=True, string="User")
    password = fields.Char(required=True, string="Password")
```

Now you should be able to add multiple Services to the contacts view.

![Services Table](/Images/Odoo-2.png)

![Services Input](/Images/Odoo-3.png)