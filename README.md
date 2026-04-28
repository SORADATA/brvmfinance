
```markdown
<img src="https://raw.githubusercontent.com/votre-username/brvmfinance/main/doc/logo.png" height="100">

# Données du marché de la BRVM avec Python

<a target="new" href="https://pypi.python.org/pypi/brvmfinance"><img border=0 src="https://img.shields.io/badge/python-3.7+-blue.svg?style=flat" alt="Python version"></a>
<a target="new" href="https://pypi.python.org/pypi/brvmfinance"><img border=0 src="https://img.shields.io/pypi/v/brvmfinance.svg?maxAge=60%" alt="PyPi version"></a>
<a target="new" href="https://pypi.python.org/pypi/brvmfinance"><img border=0 src="https://img.shields.io/pypi/status/brvmfinance.svg?maxAge=60" alt="PyPi status"></a>
<a target="new" href="https://pypi.python.org/pypi/brvmfinance"><img border=0 src="https://img.shields.io/pypi/dm/brvmfinance.svg?maxAge=86400&label=installs&color=%2327B1FF" alt="PyPi downloads"></a>
<a target="new" href="https://github.com/votre-username/brvmfinance"><img border=0 src="https://img.shields.io/github/stars/votre-username/brvmfinance.svg?style=social&label=Star&maxAge=60" alt="Star this repo"></a>

**brvmfinance** offre une solution Pythonic pour récupérer des données financières et boursières de la [BRVM (Bourse Régionale des Valeurs Mobilières)](https://www.brvm.org).

---

> [!IMPORTANT]  
> **brvmfinance** est un outil open-source destiné à la recherche et à l'éducation. Il n'est **pas** affilié, approuvé ou validé par la BRVM. 
> 
> Il s'agit d'un outil communautaire qui utilise des données accessibles publiquement. Vous devez vous référer aux conditions d'utilisation des sources de données concernant vos droits d'utilisation des données téléchargées.

---

## Composants principaux

- `Ticker`: Données d'un titre individuel (ex: SNTS, ETIT).
- `Tickers`: Données pour plusieurs titres simultanément.
- `download`: Téléchargement de données historiques en masse.
- `Market`: Informations sur l'état du marché et les indices (BRVM 30, Composite).
- `CorporateActions`: Récupération des dividendes et fractionnements d'actions.
- `Screener`: Outil pour filtrer et trier les actions du marché selon des critères.

## Installation

Installez `brvmfinance` depuis PyPI en utilisant `pip` :

```bash
$ pip install brvmfinance
```

## Exemple d'utilisation

```python
import brvmfinance as brvm

# Initialiser un titre (ex: Sonatel)
snts = brvm.Ticker("SNTS")

# Récupérer l'historique du dernier mois
hist = snts.history(period="1mo")

# Voir les dividendes
print(snts.dividends)
```

---

## Contribution

**brvmfinance** compte sur la communauté pour corriger les bugs et améliorer les fonctionnalités. Toute aide est la bienvenue !

---

### Mentions Légales

**brvmfinance** est distribué sous la licence **Apache Software License**. Consultez le fichier `LICENSE.txt` pour plus de détails.

Encore une fois — **brvmfinance** n'est **pas** affilié à la BRVM. C'est un outil open-source destiné à faciliter l'analyse financière sur le marché régional de l'UEMOA. L'utilisateur est seul responsable de l'usage qu'il fait des données obtenues.

---

### P.S.

N'hésitez pas à me contacter ou à ouvrir une issue pour toute suggestion ou retour.

```