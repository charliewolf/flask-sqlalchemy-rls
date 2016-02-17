import sqlalchemy
import flask_sqlalchemy
import flask_login

SET_ROLE_SQL = sqlalchemy.sql.text("SET LOCAL ROLE :role_name;")

class AnonymousUser(flask_login.AnonymousUserMixin):
    def get_sql_role(self):
        return 'anonymous'

class RowLevelAuthSession(flask_sqlalchemy.SignallingSession):

    def __init__(self, *args, **kwargs):
        super(RowLevelAuthSession, self).__init__(*args, **kwargs)
        sqlalchemy.event.listen(self, 'after_begin', self.set_local_role)

    def set_local_role(self, session, txn, connection):
        connection.execute(SET_ROLE_SQL, role_name=flask_login.current_user.get_sql_role())


class SQLAlchemy(flask_sqlalchemy.SQLAlchemy):
    def create_session(self, options):
        return RowLevelAuthSession(self, **options)
