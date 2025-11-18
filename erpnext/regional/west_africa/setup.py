# Copyright (c) 2024, FasoCompta and Contributors
# License: GNU General Public License v3. See license.txt

"""
West Africa Regional Setup
Provides support for Mali, Senegal, Ivory Coast, and other UEMOA/CEMAC countries
Includes OHADA/SYSCOHADA chart of accounts support
"""

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields
from frappe.permissions import add_permission, update_permission_property


def setup(company=None, patch=True):
	"""Setup West African regional customizations"""
	make_custom_fields()
	setup_ohada_chart_of_accounts()
	add_west_african_taxes()


def make_custom_fields():
	"""Create custom fields for West African business requirements"""
	
	# Fields for OHADA compliance
	invoice_fields = [
		dict(
			fieldname="syscohada_section",
			label="SYSCOHADA Details",
			fieldtype="Section Break",
			insert_after="language",
			print_hide=1,
			collapsible=1,
		),
		dict(
			fieldname="dfe_number",
			label="DFE Number",
			fieldtype="Data",
			insert_after="syscohada_section",
			print_hide=1,
		),
		dict(
			fieldname="ifu_number",
			label="IFU/NIF Number",
			fieldtype="Data",
			insert_after="dfe_number",
			print_hide=1,
		),
	]
	
	# Tax fields for West African countries
	tax_fields = [
		dict(
			fieldname="tva_type",
			label="Type de TVA",
			fieldtype="Select",
			insert_after="ifu_number",
			options="\nTVA Standard 18%\nTVA Réduite 5%\nExonéré\nHors Champ",
			print_hide=1,
		),
		dict(
			fieldname="aib_applicable",
			label="AIB Applicable",
			fieldtype="Check",
			insert_after="tva_type",
			print_hide=1,
		),
	]
	
	# Company fields
	company_fields = [
		dict(
			fieldname="ifu_number",
			label="IFU/NIF Number",
			fieldtype="Data",
			insert_after="tax_id",
		),
		dict(
			fieldname="rccm_number",
			label="RCCM Number",
			fieldtype="Data",
			insert_after="ifu_number",
		),
		dict(
			fieldname="cnss_number",
			label="CNSS Number",
			fieldtype="Data",
			insert_after="rccm_number",
		),
	]
	
	# Customer/Supplier fields
	party_fields = [
		dict(
			fieldname="ifu_number",
			label="IFU/NIF Number",
			fieldtype="Data",
			insert_after="tax_id",
		),
		dict(
			fieldname="rccm_number",
			label="RCCM Number",
			fieldtype="Data",
			insert_after="ifu_number",
		),
	]
	
	# Employee fields for West African HR
	employee_fields = [
		dict(
			fieldname="cnss_number",
			label="Numéro CNSS",
			fieldtype="Data",
			insert_after="employment_type",
		),
		dict(
			fieldname="carte_travail",
			label="Carte de Travail",
			fieldtype="Data",
			insert_after="cnss_number",
		),
	]
	
	custom_fields = {
		"Company": company_fields,
		"Customer": party_fields,
		"Supplier": party_fields,
		"Sales Invoice": invoice_fields + tax_fields,
		"Purchase Invoice": invoice_fields + tax_fields,
		"Sales Order": invoice_fields + tax_fields,
		"Purchase Order": invoice_fields + tax_fields,
		"Quotation": invoice_fields + tax_fields,
		"Employee": employee_fields,
	}
	
	create_custom_fields(custom_fields, ignore_validate=frappe.flags.in_patch)


def setup_ohada_chart_of_accounts():
	"""Setup OHADA/SYSCOHADA chart of accounts"""
	# This would typically load a predefined chart of accounts
	# For now, we'll just add a note that it should be configured
	pass


def add_west_african_taxes():
	"""Add common West African tax templates"""
	# Mali: TVA 18%, AIB 1%
	# Senegal: TVA 18%
	# Côte d'Ivoire: TVA 18%
	# This would create tax templates for these countries
	pass
