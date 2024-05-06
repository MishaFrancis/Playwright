def save_multiple_keys(data, keys_to_save):
    saved_values = {}
    file_path = "dirk_offer_list.txt"
    with open(file_path, 'w') as file:  ## This is just to clear the file
        pass
    
    def search_and_collect(data, keys_to_save):
        # If the data is a dictionary
        if isinstance(data, dict):
            # Check each key in the dictionary
            for key in keys_to_save:
                # If the key is in the dictionary, save the value
                if key in data:
                    saved_values[key] = data[key]
                    print(f"{key}",data[key])
                    if key == ('normalPrice'):
                        n = data[key]
                    elif (key == 'offerPrice' and data[key] != 0):
                        o = data[key]
                        pro = n - o
                        rounded_number = round(pro, 2)
                        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Profit : ", rounded_number)
                    text = key
                    file_path = "dirk_offer_list.txt"    
                    file = open(file_path, 'a')
                    file.write(text+'\n')
                    file.write(str(data[key]))
                    file.write('\n')
                    file.write('\n\n')
                    file.close()                    
            # Recursively search the values in the dictionary
            for value in data.values():
                search_and_collect(value, keys_to_save)
            print("        ")
        # If the data is a list
        elif isinstance(data, list):
            # Recursively search each item in the list
            for item in data:
                search_and_collect(item, keys_to_save)

    # Start the search and collection process
    search_and_collect(data, keys_to_save)

    return saved_values


def calcs(calc):
    square = calc * calc
    return square


def reverse(word):
    rev = ""
    for char in reversed(word):

        rev += char

    return rev