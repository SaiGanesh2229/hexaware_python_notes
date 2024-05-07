# sets are changeable like list but only unique
# Mutable, unique, no order, cannot be accessed elements using an index
# {}
tech_gadgets = {"smartphones", "electricals", "electronics", "computers"}
empty_set = set()
print(type(empty_set))
print(type(tech_gadgets))
tech_gadgets.add("Commerce")
print(tech_gadgets)
tech_gadgets.add("computers")
print(tech_gadgets)
