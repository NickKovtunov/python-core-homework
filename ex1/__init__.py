def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories = []
    for c_id in mapping["categoryIdsSorted"]:
        category = {
            "id": "category-" + c_id,
            "text": mapping["categories"][c_id]["name"],
            "items": []
        }
        for r_id in mapping["categories"][c_id]["roleIds"]:
            item = {
                "id": r_id,
                "text": mapping["roles"][r_id]["name"]
            }
            category["items"].append(item)
        categories.append(category)

    res = {"categories": categories}
    return res
