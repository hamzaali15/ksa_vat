import frappe

from ksa_vat.saudi_arabia.setup import make_custom_fields


def execute():
	company = frappe.get_all("Company", filters={"country": "Saudi Arabia"})
	if not company:
		return

	make_custom_fields()
