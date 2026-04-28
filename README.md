<p align="center">
  <img src="doc/logo.png" width="450" alt="brvmfinance logo">
</p>

# brvmfinance

**brvmfinance** est une bibliothèque Python conçue pour faciliter l'accès aux données boursières de la **BRVM** (Bourse Régionale des Valeurs Mobilières).

<p align="left">
  <a href="https://pypi.org/project/brvmfinance/"><img src="https://img.shields.io/badge/python-3.7+-blue.svg" alt="Python Version"></a>
  <a href="https://pypi.org/project/brvmfinance/"><img src="https://img.shields.io/pypi/v/brvmfinance.svg" alt="PyPi Version"></a>
  <a href="https://pypi.org/project/brvmfinance/"><img src="https://img.shields.io/pypi/dm/brvmfinance.svg?label=installs&color=%2327B1FF" alt="Downloads"></a>
  <a href="https://github.com/SORADATA/brvmfinance"><img src="https://img.shields.io/github/stars/SORADATA/brvmfinance.svg?style=social" alt="Stars"></a>
</p>

---

## 🚀 Présentation

Inspiré par `yfinance`, ce package permet aux analystes et développeurs de récupérer facilement les cotations, les historiques et les informations sur les sociétés cotées à la BRVM.

> [!IMPORTANT]
> Ce projet est open-source et n'est pas affilié officiellement à la BRVM. Les données sont récupérées à des fins éducatives et de recherche.

---

## 🛠 Composants principaux

* **`Ticker`** : Accéder aux données d'un titre spécifique (ex: `SNTS`, `ETIT`).
* **`Tickers`** : Gérer plusieurs titres à la fois.
* **`download`** : Télécharger des séries historiques massives.
* **`Market`** : Obtenir un résumé de l'état du marché et des indices.

## 📦 Installation

```bash
pip install brvmfinance
