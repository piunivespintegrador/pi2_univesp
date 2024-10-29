class MySQLRouter:
    """
    Um roteador para direcionar operações de alguns modelos para o banco MySQL.
    """
    def db_for_read(self, model, **hints):
        """Direciona as leituras de certos modelos para o banco MySQL."""
        if model._meta.app_label == 'mysql':
            return 'mysql_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """Direciona as gravações de certos modelos para o banco MySQL."""
        if model._meta.app_label == 'mysql':
            return 'mysql_db'
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Permite migrações somente no banco de dados adequado."""
        if app_label == 'mysql':
            return db == 'mysql_db'
        return db == 'default'