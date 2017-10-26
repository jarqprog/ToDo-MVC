"""Module conatains varied helper functions."""

import time
import sys
import os
import random


# import getch (avoid problem with windows/ubuntu):
try:
    from msvcrt import getwch as getch

except ImportError:
    def getch():
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


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


def animate_string(speed=0.0005, string=None):
    """
    Display string using pseudo-animating technique.

    speed: determine "animating" speed (float), default: 0.005
    string: string text to display
    """
    if string is None:
        string = "\n\nLoading program...\n\n"
    for char in string:
        sys.stdout.write("%s" % char)
        sys.stdout.flush()
        time.sleep(speed)


def display_text_with_asci_graphics(text_1=None, text_2=None, repeat=9):
    """
    Display text and asci graphisc in pseudo-animating form.

    Parameters:
    text_1, text_2: string (text to display)
    repeat: integer (number of repeats in loop)

    Sample output:
    Loading program... (text_1)
    ***************************2....
    *****************************1..
    *******************************0
    Program loaded ^o^ (text_2)
    """
    clear_screen()
    animate_string(string=text_1)
    for counter in range(repeat, -1, -1):
        string = "{: >25}".format(
                                    str(counter) +
                                    (".."*counter) + "\n")
        animate_string(string=string)
    animate_string(string=text_2)


def clear_screen():
    """Clear screen - universal for ubuntu/windows platform."""
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    """Stop program action until user will press any key."""
    print('\n\npress any key..\n')
    getch()



# head = ['id', 'first', 'last']
# body = [['Jarek', 'Kucharczyk'], ['Jelenka', 'Kucharczyk']]
# lista = display_table_from_given_lists(head, body)
# print(lista)
