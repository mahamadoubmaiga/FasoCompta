# Copyright (c) 2024, FasoCompta and Contributors
# License: GNU General Public License v3. See license.txt

"""
Restaurant Management Configuration
Provides setup and configuration for restaurant operations
"""

import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


def setup_restaurant_module():
	"""Setup restaurant management features"""
	create_restaurant_custom_fields()
	create_restaurant_item_groups()
	create_restaurant_pos_profile()


def create_restaurant_custom_fields():
	"""Create custom fields for restaurant operations"""
	
	# POS Invoice fields for restaurants
	pos_fields = [
		dict(
			fieldname="table_number",
			label="Table Number",
			fieldtype="Data",
			insert_after="customer",
			print_hide=0,
		),
		dict(
			fieldname="waiter",
			label="Waiter/Server",
			fieldtype="Link",
			options="Employee",
			insert_after="table_number",
			print_hide=0,
		),
		dict(
			fieldname="service_charge_rate",
			label="Service Charge (%)",
			fieldtype="Float",
			insert_after="waiter",
			default=10.0,
		),
		dict(
			fieldname="service_charge_amount",
			label="Service Charge Amount",
			fieldtype="Currency",
			insert_after="service_charge_rate",
			read_only=1,
		),
	]
	
	# Item fields for menu items
	item_fields = [
		dict(
			fieldname="is_menu_item",
			label="Is Menu Item",
			fieldtype="Check",
			insert_after="item_group",
			default=0,
		),
		dict(
			fieldname="menu_category",
			label="Menu Category",
			fieldtype="Select",
			insert_after="is_menu_item",
			options="\nEntrées\nPlats Principaux\nDesserts\nBoissons\nBoissons Alcoolisées\nCafé & Thé\nAutres",
			depends_on="eval:doc.is_menu_item==1",
		),
		dict(
			fieldname="preparation_time",
			label="Preparation Time (minutes)",
			fieldtype="Int",
			insert_after="menu_category",
			depends_on="eval:doc.is_menu_item==1",
		),
		dict(
			fieldname="recipe_cost",
			label="Recipe Cost",
			fieldtype="Currency",
			insert_after="preparation_time",
			depends_on="eval:doc.is_menu_item==1",
			read_only=1,
		),
	]
	
	# Sales Invoice fields
	invoice_fields = [
		dict(
			fieldname="restaurant_details",
			label="Restaurant Details",
			fieldtype="Section Break",
			insert_after="customer",
			collapsible=1,
		),
		dict(
			fieldname="table_number",
			label="Table Number",
			fieldtype="Data",
			insert_after="restaurant_details",
		),
		dict(
			fieldname="reservation_name",
			label="Reservation",
			fieldtype="Link",
			options="Restaurant Reservation",
			insert_after="table_number",
		),
		dict(
			fieldname="number_of_guests",
			label="Number of Guests",
			fieldtype="Int",
			insert_after="reservation_name",
		),
	]
	
	custom_fields = {
		"Item": item_fields,
		"POS Invoice": pos_fields,
		"Sales Invoice": invoice_fields,
	}
	
	create_custom_fields(custom_fields, ignore_validate=True)


def create_restaurant_item_groups():
	"""Create standard item groups for restaurants"""
	item_groups = [
		"Menu Items",
		"Entrées",
		"Plats Principaux",
		"Desserts",
		"Boissons",
		"Boissons Alcoolisées",
		"Ingrédients",
		"Condiments",
	]
	
	for group in item_groups:
		if not frappe.db.exists("Item Group", group):
			doc = frappe.get_doc({
				"doctype": "Item Group",
				"item_group_name": group,
				"parent_item_group": "All Item Groups",
				"is_group": 0
			})
			doc.insert(ignore_permissions=True)


def create_restaurant_pos_profile():
	"""Create default POS profile for restaurants"""
	# This would create a POS profile optimized for restaurant operations
	pass


def get_restaurant_reports():
	"""Return list of restaurant-specific reports"""
	return [
		"Daily Sales by Table",
		"Menu Item Performance",
		"Waiter Performance",
		"Peak Hours Analysis",
		"Inventory Usage by Recipe",
		"Food Cost Analysis",
	]


def calculate_recipe_cost(item_code):
	"""Calculate the cost of a recipe based on ingredients"""
	# This would calculate the cost of all ingredients in a recipe
	# To be implemented with BOM (Bill of Materials) integration
	return 0.0


def calculate_service_charge(subtotal, rate=10.0):
	"""Calculate service charge for restaurant bills"""
	return subtotal * (rate / 100)


def get_popular_menu_items(from_date, to_date, limit=10):
	"""Get most popular menu items in a date range"""
	# Query to get best-selling items
	return frappe.db.sql("""
		SELECT 
			item_code,
			item_name,
			SUM(qty) as total_qty,
			SUM(amount) as total_amount
		FROM `tabSales Invoice Item`
		WHERE parent IN (
			SELECT name FROM `tabSales Invoice`
			WHERE posting_date BETWEEN %s AND %s
			AND docstatus = 1
		)
		GROUP BY item_code
		ORDER BY total_qty DESC
		LIMIT %s
	""", (from_date, to_date, limit), as_dict=1)
