import pandas as pd
from .scrapers.scrapers import fetch_history

class Ticker:
    def __init__(self, ticker_name: str):
        # ICI : On stocke le nom dans 'symbol'
        self.symbol = ticker_name.upper() 
        self._history = None

    def history(self, length=365) -> pd.DataFrame:
        # ICI : On utilise bien self.symbol
        df = fetch_history(self.symbol, length=length)
        if df is not None:
            self._history = df
        return df

    def __repr__(self):
        return f"brvmfinance.Ticker('{self.symbol}')"