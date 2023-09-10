# Not elegant at all
def find_most_frequent(items):
    if len(items) == 0:
        return set([])

    counts = {}
    items_set = set(items)

    for item in items_set:
        counts[item] = items.count(item)

    sorted_dict = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    highest_count = sorted_dict[0][1]
    most_frequent_items = {item[0] for item in sorted_dict if item[1] == highest_count}

    return most_frequent_items
