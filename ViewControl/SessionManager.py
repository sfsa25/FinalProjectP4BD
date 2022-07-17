import PersistencyDML
from User import User


class SessionManager:

    def __init__(self, persistencycontrol):
        self.persistency = persistencycontrol
        self.logged_user = None

    def auth_user(self, login, passwd):
        query_result = self.persistency.execute_select(
            PersistencyDML.select_all_user + " WHERE LOGIN='" + login + "' AND CRYPTOGRAPHIC_PASSWD='" + passwd + "'")

        if not query_result:
            return False

        self.logged_user = User(query_result[0][1], query_result[0][2])
        return True
