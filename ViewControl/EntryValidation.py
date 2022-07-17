import re

class EntryValidation:

    # MIN LEN 3, MAX LEN 25#
    LOGIN_PATTERN = '[a-zA-Z]{4,25}?';

    # 4 digits #
    PASSWD_PATTERN = '[0-9]{4,4}?';

    @staticmethod
    def validateField(field_value, regex_expression):

        validity = bool(re.fullmatch(regex_expression, field_value.strip()));

        return validity
