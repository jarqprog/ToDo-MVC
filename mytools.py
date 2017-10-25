"""Module conatains varied helper functions."""


def display_table_from_given_lists(head, body, bar_mark='-'):
    """
    Return formated strings (from lists: head, body) to display in table form.

    Sample output:
    ---------------------------------------
    id      name    description         # head (list) elements, e.g. head = ["id", "name", "description"]
    ---------------------------------------
    01      apple   nice fruit          # body elements (list of lists), e.g. body = [["apple", "nice fruit"], [...]]
    02      orange  tasty thing         # id numbers from enumerate list elements in loop
    ---------------------------------------
    list (head, body) elements: string type
    """
    # check if arguments are correct
    length_modifier = 1  # head should have 1 element more (e.g. 'id')
    if len(head) != len(body[0]) + length_modifier:
        raise BaseException("Incorrect number of elements in head or body in func:\
                            \ndisplay_table_from_given_lists()")

    # create list of lists (all_elements_to_display)
    all_elements_to_display = []
    all_elements_to_display.append(head)
    for number, elements in enumerate(body):
        tmp_list = [str(number)]
        for element in elements:
            tmp_list.append(element)
        all_elements_to_display.append(tmp_list)

    # take longest elements in lists to display the table correctly
    index = 0
    loop_limiter = len(head)
    longest_elements = []
    while index < loop_limiter:
        tmp_list = []
        for elements in all_elements_to_display:
            tmp_list.append(len(elements[index]))
        longest_element_in_list = max(length for length in tmp_list)
        index += 1
        longest_elements.append(longest_element_in_list)
    table_width = sum(longest_elements)  # calculate width of table

    # create final string to return:
    table_width_modifier = len(head) * 5
    table_bar = bar_mark*(table_width + table_width_modifier)  # table_bar: -------
    output_string = ""
    gap = "    "
    for elements in all_elements_to_display:
        for index, element in enumerate(elements):
            output_string += "".join(element).ljust(longest_elements[index]) + gap
        output_string += "\n" + table_bar + "\n"
    return output_string


# head = ['id', 'first', 'last']
# body = [['Jarek', 'Kucharczyk'], ['Jelenka', 'Kucharczyk']]
# lista = display_table_from_given_lists(head, body)
# print(lista)
