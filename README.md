# my-addons
A practical ground for odoo concepts

It is a simple folder contains odoo addons intended to be integrated with odoo.
You should put it with odoo main folder into a common folder, let us call this folder `common`.
To run it you need to add its path to the addons-path parameter:
```
--addons-path="my-addons,odoo/addons" -r db_user -w db_pass -d db 
```
assuming that you have the common folder as your root path.
And if you want to install it immediately during the first database initialization you can add `-i "base,practice"` , for now we only have practice module.
 

