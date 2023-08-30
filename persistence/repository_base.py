class RepositoryBase:
    def __init__(self, database_uri: str):
        self.database = database_uri
