from typing import List


def array1_has_all_array2_elements(array1: List, array2: List) -> bool:
    for element in set(array2):
        if array1.count(element) < array2.count(element):
            return False

    return True


def build_or_buy(actual_resources: str) -> List[str]:
    possible_purchases = []

    purchases = {
        "road": "bw",
        "settlement": "bwsg",
        "city": "ooogg",
        "development": "osg"
    }

    for purchase, purchases_required_resources in purchases.items():
        if array1_has_all_array2_elements(list(actual_resources), list(purchases_required_resources)):
            possible_purchases.append(purchase)

    return possible_purchases
