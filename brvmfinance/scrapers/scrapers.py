import requests
import pandas as pd
# Importation depuis le dossier utils
from brvmfinance.utils.client_http import BASE_URL, HEADERS, get_faux_guid

def fetch_history(symbole, length=365):
    """
    Récupère l'historique EOD d'un titre via l'API Sika Finance.
    """
    s = symbole.upper()
    
    # Paramètres de la requête
    parametres = {
        'symbol': s, 
        'length': length, 
        'period': '1',        # '1' pour tenter d'avoir du quotidien
        'guid': get_faux_guid()
    }

    try:
        # Exécution de la requête HTTP
        reponse = requests.get(BASE_URL, params=parametres, headers=HEADERS, timeout=10)
        reponse.raise_for_status()
        
        donnees = reponse.json()

        # Sécurité si aucune donnée n'est renvoyée
        if not donnees or 'QuoteTab' not in donnees:
            print(f"❌ Aucune donnée ou format invalide pour {s}")
            return None

        # Transformation du JSON en DataFrame Pandas
        df_propre = pd.json_normalize(donnees, record_path=['QuoteTab'])
        
        # Renommage des colonnes Sika vers format financier standard
        colonnes_noms = {
            'd': 'Date', 
            'o': 'Open', 
            'h': 'High', 
            'l': 'Low', 
            'c': 'Close', 
            'v': 'Volume'
        }
        df_propre = df_propre.rename(columns=colonnes_noms)
        
        if 'Date' in df_propre.columns:
            # Conversion des dates (Origine Unix 1970 avec unité Jours)
            df_propre['Date'] = pd.to_datetime(df_propre['Date'], unit='D', origin='1970-01-01')
            
            # Suppression des heures pour ne garder que la date YYYY-MM-DD
            df_propre['Date'] = df_propre['Date'].dt.normalize()
            
            # Tri chronologique (Ancien -> Récent)
            df_propre = df_propre.sort_values('Date')
            df_propre.set_index('Date', inplace=True)
            
            # Conversion forcée des colonnes de prix en nombres (float/int)
            cols_finance = ['Open', 'High', 'Low', 'Close', 'Volume']
            df_propre[cols_finance] = df_propre[cols_finance].apply(pd.to_numeric, errors='coerce')
        
        return df_propre

    except Exception as e:
        print(f"⚠️ Erreur lors de la récupération de {s} : {e}")
        return None