class MySQLRouter:
    """
        Valida de o model é do MySQL
    """
    def IsMySQLModel(self, model_name):
        return  model_name == 'agendamento' or \
                model_name == 'cliente' or \
                model_name == 'forma_contato' or \
                model_name == 'servico_forma_contato' or \
                model_name == 'servico' or \
                model_name == 'tiposervico' or \
                model_name == 'tipoveiculo'

    """
        Valida de o model é do MongoDB
    """
    def IsMongoDBModel(self, model_name):
        return False

    """
        Valida se é um dos projetos proprietário
    """
    def IsOwnerProject(self, app_label):
        return  app_label == 'private_site' or \
                app_label == 'public_site'

    """
        Um roteador para direcionar operações de alguns modelos para o banco MySQL.
    """
    def db_for_read(self, model, **hints):
        """Direciona as leituras de certos modelos para o banco MySQL."""
        if self.IsOwnerProject(model._meta.app_label):
            if self.IsMySQLModel(model._meta.model_name):
                return 'mysql_db'
            elif self.IsMongoDBModel(model._meta.model_name):
                return 'mongo_db'
        return 'default'

    def db_for_write(self, model, **hints):
        """Direciona as gravações de certos modelos para o banco MySQL."""
        if self.IsOwnerProject(model._meta.app_label):
            if self.IsMySQLModel(model._meta.model_name):
                return 'mysql_db'
            elif self.IsMongoDBModel(model._meta.model_name):
                return 'mongo_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._state.db == 'mysql_db' and obj2._state.db == 'mysql_db':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Permite migrações somente no banco de dados adequado."""
        if self.IsOwnerProject(app_label):
            if self.IsMySQLModel(model_name):
                return 'mysql_db'
            elif self.IsMongoDBModel(model_name):
                return 'mongo_db'
        return 'default'