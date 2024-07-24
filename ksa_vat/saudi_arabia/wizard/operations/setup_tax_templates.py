import frappe
import json
import os

from erpnext.setup.setup_wizard.operations.taxes_setup import from_detailed_data, simple_to_detailed


def setup_templates(doc, method=None):
	if doc.country == "Saudi Arabia":
		file_path = os.path.join(
			os.path.dirname(__file__), "..", "data", "ksa_template.json"
		)
		with open(file_path, "r") as json_file:
			template = simple_to_detailed(json.load(json_file))

			root_account = frappe.new_doc("Account")
			root_account.is_group = 1
			root_account.root_type = "Liability"
			root_account.company = doc.name
			root_account.account_name = "Source of Funds (Liabilities)"
			root_account.report_type = "Balance Sheet"
			# root_account.parent_account = "Source of Funds (Liabilities) - OMFC2"
			# root_account.account_number = ""

			root_account.flags.ignore_links = True
			root_account.flags.ignore_validate = True
			root_account.flags.ignore_mandatory = True
			root_account.insert(ignore_permissions=True)
			from_detailed_data(doc.name, template)
