import frappe


@frappe.whitelist()
def get_doctypes_with_numeric_fields(
    doctype, txt, searchfield, start, page_len, filters
):
    doctypes = frappe.get_all("DocType", filters={"istable": 0})
    valid_doctypes = []

    for dt in doctypes:
        meta = frappe.get_meta(dt.name)
        has_numeric_field = any(df.fieldtype in ["Int", "Float"] for df in meta.fields)

        if has_numeric_field:
            valid_doctypes.append((dt.name, dt.name))  # (value, label)

    return valid_doctypes
