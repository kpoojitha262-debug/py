#set example
s = {1, 2, 3, 4}
print(s)
#Creation of set
set1 = {10, 20, 30}
set2 = set([1,2,3,4])
print(set1)
print(set2)

#All Set Operations
# Creating two sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print("Set1:", set1)
print("Set2:", set2)

# Add elements
set1.add(9)
print("\nAfter add:", set1)
# Update elements
set1.update([10, 11])
print("After update:", set1)
# Remove elements
set1.remove(3)      # Raises error if not present
set1.discard(100)   # No error if not present
removed_element = set1.pop()  # Removes random element
print("Removed (pop):", removed_element)
print("After remove:", set1)
# Union
union_set = set1 | set2
print("\nUnion:", union_set)
# Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)
# Difference
difference_set = set1 - set2
print("Difference (set1 - set2):", difference_set)
# Symmetric Difference
sym_diff_set = set1 ^ set2
print("Symmetric Difference:", sym_diff_set)
# Subset & Superset
subset_check = {4, 5}.issubset(set2)
superset_check = set2.issuperset({6, 7})
print("\nIs {4,5} subset of set2?", subset_check)
print("Is set2 superset of {6,7}?", superset_check)
# Membership test
print("\nIs 5 in set1?", 5 in set1)
# Loop through set
print("\nElements in set1:")
for item in set1:
    print(item)
# Set length
print("\nLength of set1:", len(set1))
# Clear set
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear:", temp_set)
# Frozen set
frozen = frozenset([1, 2, 3, 4])
print("\nFrozen set:", frozen)
