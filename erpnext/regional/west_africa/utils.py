# Copyright (c) 2024, FasoCompta and Contributors
# License: GNU General Public License v3. See license.txt

"""
West Africa Regional Utilities
Helper functions for West African business operations
"""

import frappe
from frappe import _


def get_west_african_countries():
	"""Return list of supported West African countries"""
	return [
		"Mali",
		"Senegal",
		"Côte d'Ivoire",
		"Burkina Faso",
		"Niger",
		"Benin",
		"Togo",
		"Guinea",
		"Guinea-Bissau",
		"Cameroon",
		"Chad",
		"Central African Republic",
		"Congo",
		"Gabon",
		"Equatorial Guinea",
	]


def get_uemoa_countries():
	"""Return list of UEMOA (West African Economic and Monetary Union) countries"""
	return [
		"Benin",
		"Burkina Faso",
		"Côte d'Ivoire",
		"Guinea-Bissau",
		"Mali",
		"Niger",
		"Senegal",
		"Togo",
	]


def get_cemac_countries():
	"""Return list of CEMAC (Central African Economic and Monetary Community) countries"""
	return [
		"Cameroon",
		"Central African Republic",
		"Chad",
		"Congo",
		"Equatorial Guinea",
		"Gabon",
	]


def is_uemoa_country(country):
	"""Check if a country is part of UEMOA"""
	return country in get_uemoa_countries()


def is_cemac_country(country):
	"""Check if a country is part of CEMAC"""
	return country in get_cemac_countries()


def get_cfa_currency(country):
	"""
	Get the appropriate CFA currency for a country
	Returns XOF for UEMOA countries, XAF for CEMAC countries
	"""
	if is_uemoa_country(country):
		return "XOF"  # West African CFA franc
	elif is_cemac_country(country):
		return "XAF"  # Central African CFA franc
	return None


def get_standard_vat_rate(country):
	"""Get standard VAT rate for West African countries"""
	vat_rates = {
		"Mali": 18.0,
		"Senegal": 18.0,
		"Côte d'Ivoire": 18.0,
		"Burkina Faso": 18.0,
		"Niger": 19.0,
		"Benin": 18.0,
		"Togo": 18.0,
		"Guinea": 18.0,
		"Guinea-Bissau": 15.0,
		"Cameroon": 19.25,
		"Chad": 18.0,
		"Central African Republic": 19.0,
		"Congo": 18.0,
		"Gabon": 18.0,
		"Equatorial Guinea": 15.0,
	}
	return vat_rates.get(country, 18.0)


def format_ifu_number(ifu):
	"""Format IFU/NIF number according to West African standards"""
	# Remove any spaces or special characters
	ifu = str(ifu).replace(" ", "").replace("-", "")
	return ifu


def validate_ifu_number(ifu, country):
	"""Validate IFU/NIF number format for specific country"""
	# Basic validation - can be enhanced for specific country requirements
	ifu = format_ifu_number(ifu)
	
	# Mali IFU is typically 13 digits
	if country == "Mali":
		return len(ifu) == 13 and ifu.isdigit()
	
	# Generic validation for other countries
	return len(ifu) >= 10 and ifu.isalnum()


def get_ohada_account_types():
	"""Return OHADA/SYSCOHADA account types"""
	return {
		"1": _("Capital Accounts"),
		"2": _("Fixed Assets"),
		"3": _("Inventory"),
		"4": _("Third Parties"),
		"5": _("Financial Accounts"),
		"6": _("Expenses"),
		"7": _("Revenue"),
		"8": _("Other Accounts"),
	}


def calculate_aib_tax(amount, rate=1.0):
	"""
	Calculate AIB (Acompte sur Impôt sur les Bénéfices)
	Common in Mali and some other West African countries
	Default rate is 1%
	"""
	return amount * (rate / 100)


def calculate_tps_tax(amount, rate=None):
	"""
	Calculate TPS (Taxe sur les Prestations de Services)
	Used in some West African countries
	"""
	if rate is None:
		rate = 5.0  # Default 5%
	return amount * (rate / 100)


def get_restaurant_specific_taxes(country):
	"""Get restaurant-specific tax configurations"""
	# Some countries have specific tax rates for restaurant services
	restaurant_taxes = {
		"Mali": {
			"tva": 18.0,
			"aib": 1.0,
			"service_charge": 10.0,  # Optional service charge
		},
		"Senegal": {
			"tva": 18.0,
			"service_charge": 10.0,
		},
		"Côte d'Ivoire": {
			"tva": 18.0,
			"service_charge": 15.0,
		},
	}
	return restaurant_taxes.get(country, {"tva": 18.0})


def get_retail_tax_exemptions(country):
	"""Get list of tax-exempt goods for retail in West African countries"""
	# Common tax exemptions in West Africa
	exemptions = [
		"Basic Food Items",
		"Medical Supplies",
		"Educational Materials",
		"Agricultural Products",
		"Exported Goods",
	]
	return exemptions
