# mz-addons
# A practical ground for odoo concepts

It is a simple folder contains odoo addons intended to be integrated with odoo.
You should put it with odoo main folder into a common folder, let us call this folder `common`.
To use these addons you need to add its path to the addons-path parameter. the running command can take the following form:
```
python3 odoo/odoo-bin --addons-path="mz-addons,odoo/addons" -r db_user -w db_pass -d db 
```
assuming that you have the common folder as the source_path of your application. And then the addons will be available to be installed from odoo apps. 

And if you want to install all of them(or you can select the ones you want) immediately during the first database initialization you can add `-i "base,mail_ext,practice"` to the command above.
 

