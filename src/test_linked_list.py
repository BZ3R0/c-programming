from linked_list import LinkedList

# Instaciate variable
linked_list = LinkedList()

# Insert elements on list
linked_list.insert(3)
linked_list.insert(5)
linked_list.insert(7)

# Search for a specific element on list (Return True if find the element and None otherwise)
print('found:', linked_list.search(5))

# Remove element from list (return True if remove element and None otherwise)
print('remove:',linked_list.remove(5))

# Print list
print(linked_list.__str__())