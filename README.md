sika-python-module
==================

#Usage

import sika_

user = sika_.User(token = "token goes here")

#To create a user
user.create_user(name="", phone="", email="")

#To create an invoice
user.create_invoice(total=23, delivery_cost=23, ref="11134", first_name="Kofi", items=[])

#To get all invoices
user.invoices(ref="ref_id")

#To get a particular invoice
user.invoice_detail(ref="ref_id")
