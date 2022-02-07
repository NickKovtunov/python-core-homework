def build_roles_tree(mapping):
    """
    :param mapping: маппинг ролей в категории
    :return: дерево ролей
    """
    categories = []
    for cId in mapping["categoryIdsSorted"]:
        category = {
            "id": "category-" + cId,
            "text": mapping["categories"][cId]["name"],
            "items": []
        }
        
        for rId in mapping["categories"][cId]["roleIds"]:
            item = {
                "id": rId,
                "text": mapping["roles"][rId]["name"]
            }
            category["items"].append(item)
            
        categories.append(category)

    res = {"categories": categories}
    return res
    pass
