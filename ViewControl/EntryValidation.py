import re


class EntryValidation:

    @staticmethod
    def validateField(field_value, regex_expression):

        validity = bool(re.fullmatch(regex_expression, field_value.strip()));

        return validity

    @staticmethod
    def input_integer(message):
        while True:
            try:
                input_value = int(input(message))
            except ValueError:
                print("Invalid type, try again!")
                continue
            else:
                return input_value

    @staticmethod
    def choose_option(length, message):
        option = EntryValidation.input_integer(message)
        while option > length:
            print('Invalid value. Choose again')
            option = EntryValidation.input_integer(message)

        return option
