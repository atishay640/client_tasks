# Intialize the empty list for appending other lists
list2 = []

# Returns the flat hierarchy from hierarchy
def ungroup(hierachy):
    def nested_dict_pairs_iterator(dict_obj):
        ''' This function accepts a nested dictionary as argument
            and iterate over all values of nested dictionaries
        '''
        # Iterate over all key-value pairs of dict argument
        for key, value in dict_obj.items():
            # Check if value is of dict type
            if isinstance(value, dict):
                # If value is dict then iterate over all its values
                for pair in nested_dict_pairs_iterator(value):
                    yield (key, *pair)
            else:
                # If value is not dict type then yield the value
                yield (key, value)
   
    # Loop through all key-value pairs of a nested dictionary
    for pair in nested_dict_pairs_iterator(hierachy): 
        list1 = []
        # Get the list
        for i in range(len(pair)):
            # Appending only the last element of item
            if i == (len(pair)-1):
                # Iterate further elements of last item
                for j in range (i):
                    list1.append(pair[i][j])
                    a = tuple(list1)
                    list2.append(a) 
                    # Remove the last element              
                    list1.pop()
                    if len(pair)==2:
                        list1.append(pair[i][j+1])
                        a = tuple(list1)
                        list2.append(a)
            else :
                # Appending the list till last second element  
                list1.append(pair[i])

    # Coverting list of tuple to list of list
    new_list = [list(x) for x in list2]
    # Get the final list
    return new_list

current_list =  []
def group(flat_hierarchy):
    for item in flat_hierarchy:

        new_dict = current = {}
        for name in item[::]:
            current[name] = {}
            current = current[name]
        current_list.append(new_dict)


        # Create the new list using list concatenation
    for i in range(len(current_list)-1):
        a = current_list[i]
        b = current_list[i+1]
        def merge(a , b, path=None):
        #"merges b into a"
            if path is None: path = []
            for key in b:
                if key in a:
                    if isinstance(a[key], dict) and isinstance(b[key], dict):
                        merge(a[key], b[key], path + [str(key)])
                    elif a[key] == b[key]:
                        pass # same leaf value
                    else:
                        raise Exception('Conflict at %s' % '.'.join(path + [str(key)]))
                else:
                    a[key] = b[key]
            return a

        merge_dict = merge(a, b)
        current_list[i+1] = merge_dict

    old_dict = merge_dict

    for key, val in old_dict.items():

        for key2, val2 in val.items():
            for key3, val3 in val2.items():
                if len(val3) != 1 :
                    dict_keys  = val3.keys()
                    final_list = list(dict_keys)
                    old_dict[key][key2][key3] = final_list
                    print(key3, final_list, "key3")
                else : 
                    for key4, val4 in val3.items():
                            dict_keys  = val4.keys()
                            final_list = list(dict_keys)
                            old_dict[key][key2][key3][key4] = final_list
                            print(key4, final_list, "key4") 
            if final_list ==[] :
                dict_keys = val2.keys()
                final_list = list(dict_keys)
                old_dict[key][key2] = final_list
                print(key2, final_list, "key2") 

        if len(val) == 2 and val2 =={}:
            dict_keys = val.keys()
            final_list = list(dict_keys)
            old_dict[key] = final_list
            print(key, final_list, "key") 

    # print(old_dict, "old_dict")
    return old_dict