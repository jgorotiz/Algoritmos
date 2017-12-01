def insertsort(array):
    for removed_index in range(1, len(array)):
        removed_value = array[removed_index]
        insert_index = removed_index
        while insert_index > 0 and array[insert_index - 1] > removed_value:
            array[insert_index] = array[insert_index - 1]
            insert_index = insert_index - 1
        array[insert_index] = removed_value