class LivreIndisponibleError(Exception):
    def __init__(self, message="Ce livre est indisponible!"):
        super().__init__(message)

class QuotaEmpruntDepasseError(Exception):
    def __init__(self, message="Le quota des emprunts est depassé!"):
        super().__init__(message)

class MembreInexistantError(Exception):
    def __init__(self, messsage="Ce membre est inexistant!"):
        super().__init__(messsage)

class LivreInexistantError(Exception):
    def __init__(self, message="Ce livre est inexistant!"):
        super().__init__(message)
