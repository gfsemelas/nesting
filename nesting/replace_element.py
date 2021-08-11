def replace_element(iterable_object: (list, dict),
                    old_value: (str, int, float, list, tuple, dict),
                    new_value: (str, int, float, list, tuple, dict)
                    ) -> (list, dict):
    '''
    This function takes an iterable object and two values, and returns
    the same object with the first value replaced by the first. It is
    thought for nested iterable and mutable objects.
    
    All arguments must be of equal length.
    :param iterable_object: list or dict to change
    :param old_value: element to be replaced
    :param new_value: element that replaces old_value
    :return: iterable_object with old_value replaced with new_value
    '''
    
    # Creation of a function that finds the element to change and replaces it with the new element.
    # Note: if "old_value" is not in "nested_list", no change is made and no error is raised.
    def change_element_in_pure_list(nested_list, old_value, new_value):
        for index, element in enumerate(nested_list):
            # check if old_value is an element of the primary list
            if element == old_value:
                nested_list[index] = new_value
            
            # if not, then apply recursive search to look for old_value in secondary lists
            elif isinstance(element, list):
                change_element_in_pure_list(element, old_value, new_value)
        
        return nested_list
    
    
    # Creation of a function that finds the element to change and replaces it with the new element.
    # Note: if "old_value" is not in "nested_dict", no change is made and no error is raised.
    def change_element_in_dict(nested_dict, old_value, new_value):
        for key, value in nested_dict.items():
            # check if old_value is a value of the primary dictionary
            if value == old_value:
                nested_dict[key] = new_value
            
            # if any value is a dictionary then apply recursive search to look for old_value in secondary dictionaries
            elif isinstance(value, dict):
                change_element_in_dict(value, old_value, new_value)
            
            # if any value is a list then apply recursive search to look for old_value in its elements
            elif isinstance(value, list):
                for index, element in enumerate(value):
                    # check if old_value is an element of the list
                    if element == old_value:
                        nested_dict[key][index] = new_value
                    
                    # if any element of the list is a dictionary, then apply recursive search by calling the function again
                    elif isinstance(element, dict):
                        change_element_in_dict(element, old_value, new_value)
                    
                    # if any value of the list is a list, apply recursive search by calling the function change_element_in_pure_list
                    elif isinstance(element, list):
                        change_element_in_pure_list(element, old_value, new_value)
        
        return nested_dict
    
    
    # Creation of a function that finds the element to change and replaces it with the new element.
    # Note: if "old_value" is not in "nested_list", no change is made and no error is raised.
    def change_element_in_list(nested_list, old_value, new_value):
        for index, element in enumerate(nested_list):
            # check if old_value is an element of the primary list
            if element == old_value:
                nested_list[index] = new_value
            
            # if not and it is a list, then apply recursive search to look for old_value in secondary lists
            elif isinstance(element, list):
                change_element_in_pure_list(element, old_value, new_value)
            
            # if not and it is a dict, then apply recursive search to look for old_value in secondary dicts or lists
            elif isinstance(element, dict):
                change_element_in_dict(element, old_value, new_value)
        
        return nested_list
    
    
    if isinstance(iterable_object, list):
        return change_element_in_list(iterable_object, old_value, new_value)
    
    elif isinstance(iterable_object, dict):
        return change_element_in_dict(iterable_object, old_value, new_value)
    
    # else:
    #     raise TypeError('Input must be an iterable and mutable object: dictionary or list.')