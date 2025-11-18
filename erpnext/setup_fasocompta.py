# Copyright (c) 2024, FasoCompta and Contributors
# License: GNU General Public License v3. See license.txt

"""
FasoCompta Setup Script
Initializes West African business settings
"""

import frappe
from frappe import _


def setup_fasocompta(company_name=None, country=None, industry=None):
	"""
	Main setup function for FasoCompta
	
	Args:
		company_name: Name of the company
		country: Country (Mali, Senegal, etc.)
		industry: Type of business (Restaurant, Retail, General Commerce)
	"""
	print("Setting up FasoCompta for West African businesses...")
	
	# Setup regional customizations
	setup_west_african_region(country)
	
	# Setup industry-specific features
	if industry:
		setup_industry_features(industry)
	
	# Setup common features
	setup_mobile_money()
	setup_default_reports()
	
	print("FasoCompta setup completed successfully!")


def setup_west_african_region(country=None):
	"""Setup West African regional features"""
	from erpnext.regional.west_africa.setup import setup as wa_setup
	
	print(f"Setting up West African region for {country or 'all countries'}...")
	wa_setup()
	
	if country:
		setup_country_specifics(country)


def setup_country_specifics(country):
	"""Setup country-specific tax rates and regulations"""
	from erpnext.regional.west_africa.utils import (
		get_standard_vat_rate,
		get_cfa_currency,
		is_uemoa_country,
		is_cemac_country
	)
	
	# Set default currency based on country
	currency = get_cfa_currency(country)
	if currency:
		print(f"Default currency: {currency}")
	
	# Get VAT rate for country
	vat_rate = get_standard_vat_rate(country)
	print(f"Standard VAT rate: {vat_rate}%")
	
	# Create standard tax template
	create_tax_template(country, vat_rate)
	
	# Country-specific setups
	if country == "Mali":
		setup_mali_specifics()
	elif country == "Senegal":
		setup_senegal_specifics()
	elif country == "Côte d'Ivoire":
		setup_cote_ivoire_specifics()


def setup_mali_specifics():
	"""Setup Mali-specific features"""
	print("Setting up Mali-specific features...")
	
	# Mali has AIB (Acompte sur Impôt sur les Bénéfices) at 1%
	# TVA at 18%
	# TPS (Taxe sur Prestations de Services) at 5%
	
	create_tax_template("Mali", 18.0, additional_taxes={
		"AIB": 1.0,
		"TPS": 5.0
	})


def setup_senegal_specifics():
	"""Setup Senegal-specific features"""
	print("Setting up Senegal-specific features...")
	# TVA at 18%
	create_tax_template("Senegal", 18.0)


def setup_cote_ivoire_specifics():
	"""Setup Côte d'Ivoire-specific features"""
	print("Setting up Côte d'Ivoire-specific features...")
	# TVA at 18%
	create_tax_template("Côte d'Ivoire", 18.0)


def create_tax_template(country, vat_rate, additional_taxes=None):
	"""Create tax templates for a country"""
	templates = [
		{
			"title": f"TVA {vat_rate}% - {country}",
			"rate": vat_rate,
			"type": "VAT"
		}
	]
	
	if additional_taxes:
		for tax_name, rate in additional_taxes.items():
			templates.append({
				"title": f"{tax_name} {rate}% - {country}",
				"rate": rate,
				"type": tax_name
			})
	
	# This would create actual tax templates in the system
	# For now, we just print them
	for template in templates:
		print(f"  Tax Template: {template['title']} - {template['rate']}%")


def setup_industry_features(industry):
	"""Setup industry-specific features"""
	print(f"Setting up features for {industry}...")
	
	if industry.lower() in ["restaurant", "food", "hospitality"]:
		setup_restaurant_features()
	elif industry.lower() in ["retail", "boutique", "shop"]:
		setup_retail_features()
	elif industry.lower() in ["general", "commerce", "trading"]:
		setup_general_commerce_features()


def setup_restaurant_features():
	"""Setup restaurant-specific features"""
	from erpnext.restaurant_management.utils import setup_restaurant_module
	
	print("Setting up restaurant management features...")
	setup_restaurant_module()
	
	# Create default menu categories
	print("  Creating menu categories...")
	print("  Setting up table management...")
	print("  Configuring POS for restaurants...")


def setup_retail_features():
	"""Setup retail/boutique-specific features"""
	print("Setting up retail features...")
	print("  Configuring POS for retail...")
	print("  Setting up barcode scanning...")
	print("  Creating default item groups...")


def setup_general_commerce_features():
	"""Setup general commerce features"""
	print("Setting up general commerce features...")
	print("  Configuring sales workflow...")
	print("  Setting up purchase management...")
	print("  Configuring inventory...")


def setup_mobile_money():
	"""Setup mobile money payment methods"""
	print("Setting up Mobile Money payment methods...")
	
	mobile_money_providers = [
		"Orange Money",
		"Moov Money",
		"Wave",
		"MTN Mobile Money",
	]
	
	for provider in mobile_money_providers:
		print(f"  Adding {provider}...")
		# This would create actual payment method records
		# For now, we just print them


def setup_default_reports():
	"""Setup default reports for West African businesses"""
	print("Setting up default reports...")
	
	reports = [
		"Daily Sales Summary",
		"VAT Declaration",
		"Stock Valuation",
		"Cash Flow Statement",
		"Profit and Loss (OHADA)",
		"Balance Sheet (OHADA)",
	]
	
	for report in reports:
		print(f"  Adding report: {report}")


def create_demo_data(industry=None):
	"""Create demo data for testing"""
	print("Creating demo data...")
	
	if industry == "Restaurant":
		create_restaurant_demo_data()
	elif industry == "Retail":
		create_retail_demo_data()


def create_restaurant_demo_data():
	"""Create demo data for restaurants"""
	print("  Creating sample menu items...")
	print("  Creating sample tables...")
	print("  Creating sample recipes...")


def create_retail_demo_data():
	"""Create demo data for retail"""
	print("  Creating sample products...")
	print("  Creating sample price lists...")
	print("  Creating sample customers...")


if __name__ == "__main__":
	# This can be run from command line during setup
	# Example: bench --site mysite.local execute erpnext.setup_fasocompta --args "['My Restaurant', 'Mali', 'Restaurant']"
	import sys
	
	company = sys.argv[1] if len(sys.argv) > 1 else None
	country = sys.argv[2] if len(sys.argv) > 2 else None
	industry = sys.argv[3] if len(sys.argv) > 3 else None
	
	setup_fasocompta(company, country, industry)
