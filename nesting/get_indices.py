def get_indices(iterable_object: (list, dict),
                feature: (str, int, float, list, tuple, dict)
                ) -> list:
    ''''
    This function takes an iterable object and one value, and returns
    a list with the subsequent indices that define the position of the
    value. If the value is not found, it does not return anything.
    
    All arguments must be of equal length.
    :param iterable_object: list or dict to be searched in
    :param feature: element to be searched
    :return: indices of feature
    '''
    
    # Find for list or tuple that has no dictionaries in it
    def find_in_pure_nested_list(nested_list, char):
        for index, element in enumerate(nested_list):
            # check if char is an element of the primary list
            if element == char:
                return [index]
            
            # if an element is a list, then apply recursive search by calling the function again
            elif isinstance(element, (list, tuple)):
                next_indices = find_in_pure_nested_list(element, char)
                # when recursive search is done, return all accumulated indices
                if next_indices:
                    return [index] + next_indices
    
    
    # Find for dictionary
    def find_in_nested_dict(nested_dict, char):
        for key, value in nested_dict.items():
            # check if char is an element of the primary dictionary
            if value == char:
                return [key]
            
            # if any value of the dictionary is another dictionary, then apply recursive search by calling the function again
            elif isinstance(value, dict):
                next_keys = find_in_nested_dict(value, char)
                if next_keys:
                    return [key] + next_keys
            
            # if any value of the dictionary is a list, then loop over its elements
            elif isinstance(value, (list, tuple)):
                for index, element in enumerate(value):
                    # check if char is an element of the list
                    if element == char:
                        return [key] + [index]
                    
                    # if any value of the list is a dictionary, then apply recursive search by calling the function again
                    elif isinstance(element, dict):
                        next_indices = find_in_nested_dict(element, char)
                        # when recursive search is done, return all accumulated indices
                        if next_indices:
                            return [key] + [index] + next_indices
                    
                    # if any value of the list is a list, apply recursive search by calling the function find_in_pure_nested_list
                    elif isinstance(element, (list, tuple)):
                        next_indices = find_in_pure_nested_list(element, char)
                        # when recursive search is done, return all accumulated indices
                        if next_indices:
                            return [key] + [index] + next_indices
    
    
    # Find for list or tuple of dictionaries
    def find_in_nested_list(nested_list, char):
        for index, element in enumerate(nested_list):
            # check if char is an element of the primary list
            if element == char:
                return [index]
            
            # if an element is a list, then apply recursive search by calling the function again
            elif isinstance(element, (list, tuple)):
                next_indices = find_in_pure_nested_list(element, char)
                # when recursive search is done, return all accumulated indices
                if next_indices:
                    return [index] + next_indices
            
            # if an element is a dict, then apply recursive search by calling the function find_in_nested_dict
            elif isinstance(element, dict):
                next_indices = find_in_nested_dict(element, char)
                # when recursive search is done, return all accumulated indices
                if next_indices:
                    return [index] + next_indices
    
    
    if isinstance(iterable_object, (list, tuple)):
        return find_in_nested_list(iterable_object, feature)
    
    elif isinstance(iterable_object, dict):
        return find_in_nested_dict(iterable_object, feature)
    
    else:
        raise TypeError('Input must be an ordered iterable object: dictionary, list or tuple.')