class LivreIndisponibleError(Exception):
    def __init__(self, message="Ce livre est indisponible!"):
        super().__init__(message)

class QuotaEmpruntDepasseError(Exception):
    def __init__(self, message="Le quota des emprunts (3) est depassé!"):
        super().__init__(message)

class MembreInexistantError(Exception):
    def __init__(self, messsage="Ce membre est inexistant!"):
        super().__init__(messsage)

class LivreInexistantError(Exception):
    def __init__(self, message="Ce livre est inexistant!"):
        super().__init__(message)

class SaisieInvalideError(Exception):
    def __init__(self, message="Saisie Invalide!"):
        super().__init__(message)

class LivreDejaExistantError(Exception):
    def __init__(self, message="Un livre avec cet ISBN est déja existant!"):
        super().__init__(message)

class MembreDejaExistantError(Exception):
    def __init__(self, message="Un membre avec cet ID est déja inscrit!"):
        super().__init__(message)
