def decide_strategy(layout_types):
    if "Table" in layout_types:
        return "table_heavy"
    if "Form" in layout_types:
        return "form"
    return "mixed"
