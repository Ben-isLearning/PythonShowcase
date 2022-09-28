# more_frequent_item  has three parameters - lst, item1, and item2.
# Return either item1 or item2 depending on which
# item appears more often in lst.

# If the two items appear the same number of times, return item1.

def more_frequent_item(list_one, item_one, item_two):
    if list_one.count(item_one) >= list_one.count(item_two):
        return item_one
    return item_two


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
