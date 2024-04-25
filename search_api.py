def search_multiple_values(data, keys_to_search):
    found_values = {}
    def search(data, key_to_search):
        # Check if the data is a dictionary
        if isinstance(data, dict):
            # If the key is in the dictionary, return the associated value
            if key_to_search in data:
                return data[key_to_search]
            # Otherwise, recursively search the values in the dictionary
            for value in data.values():
                result = search(value, key_to_search)
                if result is not None:
                    return result
        # Check if the data is a list
        elif isinstance(data, list):
            # Loop through each item in the list and recursively search
            for item in data:
                result = search(item, key_to_search)
                if result is not None:
                    return result
        # Return None if the key was not found
        return None
    
    # Search for each key in the keys_to_search list
    for key in keys_to_search:
        found_values[key] = search(data, key)
    
    return found_values
