import PersistencyDML
from User import User


class SessionManager:

    def __init__(self, persistencycontrol):
        self.persistency = persistencycontrol
        self.logged_user = None

    def auth_user(self, login, passwd):
        query_result = self.persistency.execute_select_pandas(PersistencyDML.select_all_user + " WHERE LOGIN='" + login + "' AND CRYPTOGRAPHIC_PASSWD='" + passwd+"'")
        if query_result:
            self.logged_user = User(query_result[0], query_result[1])
            return True

        return False
