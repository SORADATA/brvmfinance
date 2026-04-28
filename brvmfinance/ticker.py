# Fichier : brvmfinance/ticker.py

# On importe le "moteur" depuis l'autre fichier
from .brvm_scrapers import fetch_history

class Ticker:
    def __init__(self, symbole):
        """Initialise l'action (ex: Ticker('SNTS'))"""
        self.symbole = symbole.upper()

    def __repr__(self):
        """Comment l'objet s'affiche dans la console"""
        return f'yfinance.Ticker object <{self.symbole}>'

    def history(self, period=365):
        """
        Récupère l'historique des prix.
        period : nombre de jours (par défaut 365 jours = 1 an)
        """
        return fetch_history(self.symbole, length=period)