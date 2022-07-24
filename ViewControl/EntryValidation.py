import re

class EntryValidation:

    @staticmethod
    def validateField(field_value, regex_expression):

        validity = bool(re.fullmatch(regex_expression, field_value.strip()));

        return validity