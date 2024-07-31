# File path: [your_app_name]/[your_app_name]/number_cards.py

import frappe
from frappe.utils import add_to_date, nowdate, flt


@frappe.whitelist()
def get_sales_growth_rate():
    """
    Calculate the sales growth rate comparing current month's sales to previous month's sales.
    """
    end_date = nowdate()
    start_date = add_to_date(end_date, months=-1, days=1)
    previous_start_date = add_to_date(start_date, months=-1)

    current_sales = get_total_sales(start_date, end_date)
    previous_sales = get_total_sales(previous_start_date, start_date)

    if previous_sales:
        growth_rate = ((current_sales - previous_sales) / previous_sales) * 100
    else:
        growth_rate = 100  # If previous sales were 0, we consider it 100% growth

    return {
        "value": flt(growth_rate, 2),
        "fieldtype": "Percent",
        "route_options": {
            "from_date": start_date,
            "to_date": end_date,
        },
        "route": ["query-report", "Sales Analytics"],
    }


def get_total_sales(start_date, end_date):
    """
    Get total sales amount for a given date range.
    """
    sales = frappe.get_all(
        "Sales Invoice",
        filters={"docstatus": 1, "posting_date": ["between", [start_date, end_date]]},
        fields=["sum(grand_total) as total_sales"],
    )
    return sales[0].total_sales if sales else 0
