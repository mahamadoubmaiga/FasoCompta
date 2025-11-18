# Contributing to FasoCompta

Merci de votre intérêt pour FasoCompta ! / Thank you for your interest in FasoCompta!

## 🌍 À propos / About

FasoCompta est un système de gestion d'entreprise open-source conçu spécialement pour les entreprises ouest-africaines. Toutes les contributions sont les bienvenues !

FasoCompta is an open-source business management system designed specifically for West African businesses. All contributions are welcome!

## 🤝 Comment Contribuer / How to Contribute

### Rapporter des Bugs / Report Bugs

Si vous trouvez un bug :
1. Vérifiez qu'il n'a pas déjà été signalé dans [Issues](https://github.com/mahamadoubmaiga/FasoCompta/issues)
2. Créez une nouvelle issue avec :
   - Description claire du problème
   - Étapes pour reproduire
   - Comportement attendu vs actuel
   - Captures d'écran si applicable
   - Version de FasoCompta

### Proposer des Fonctionnalités / Suggest Features

Pour proposer une nouvelle fonctionnalité :
1. Ouvrez une issue avec le tag `enhancement`
2. Décrivez clairement :
   - Le besoin business
   - La solution proposée
   - Des alternatives possibles
   - Impact sur les utilisateurs existants

### Contribuer du Code / Contribute Code

#### 1. Fork et Clone

```bash
# Fork le repo sur GitHub
# Puis clone votre fork
git clone https://github.com/votre-username/FasoCompta.git
cd FasoCompta
```

#### 2. Créer une Branche / Create a Branch

```bash
git checkout -b feature/ma-fonctionnalite
# ou
git checkout -b fix/mon-correctif
```

#### 3. Faire vos Modifications / Make Changes

- Suivez le style de code existant
- Ajoutez des tests si applicable
- Mettez à jour la documentation si nécessaire
- Commentez votre code en français ou anglais

#### 4. Tester / Test

```bash
# Installer les dépendances
bench get-app .

# Tester l'installation
bench --site test.local install-app erpnext

# Lancer les tests (si disponibles)
bench --site test.local run-tests --app erpnext
```

#### 5. Commit

Utilisez des messages de commit clairs :
```bash
git commit -m "Ajout: Fonctionnalité X pour restaurants"
git commit -m "Correction: Bug Y dans calcul TVA"
git commit -m "Doc: Guide pour boutiques au Sénégal"
```

#### 6. Push et Pull Request

```bash
git push origin feature/ma-fonctionnalite
```

Ensuite, créez une Pull Request sur GitHub avec :
- Description claire des changements
- Références aux issues liées
- Captures d'écran si UI
- Checklist des tests effectués

## 📝 Standards de Code / Code Standards

### Python
- Suivez [PEP 8](https://pep8.org/)
- Utilisez des noms de variables descriptifs
- Ajoutez des docstrings pour les fonctions
- Utilisez les type hints quand possible

```python
def calculate_vat(amount: float, rate: float = 18.0) -> float:
    """
    Calculate VAT for West African countries.
    
    Args:
        amount: Base amount
        rate: VAT rate (default 18% for most countries)
    
    Returns:
        VAT amount
    """
    return amount * (rate / 100)
```

### JavaScript
- Suivez [StandardJS](https://standardjs.com/)
- Utilisez ES6+ features
- Préférez `const` et `let` à `var`

### Documentation
- Documentation en français ET anglais quand possible
- Exemples concrets d'utilisation
- Captures d'écran pour les guides UI
- Maintenez la documentation à jour

## 🎯 Priorités de Contribution / Contribution Priorities

Nous cherchons particulièrement des contributions sur :

### Haute Priorité / High Priority
- 🇲🇱 Support pour pays additionnels (Burkina Faso, Niger, etc.)
- 📱 Amélioration interface mobile
- 🏪 Fonctionnalités pour boutiques et commerces
- 📊 Rapports financiers OHADA
- 🌐 Traductions et localisation

### Moyenne Priorité / Medium Priority
- 📈 Tableaux de bord analytiques
- 🔔 Notifications et alertes
- 📧 Templates d'emails
- 🎨 Thèmes et personnalisation

### Basse Priorité / Low Priority
- 🧪 Tests unitaires supplémentaires
- 📚 Tutoriels vidéo
- 🛠️ Outils de développement

## 🌍 Localisation / Localization

### Ajouter un Pays / Add a Country

Pour ajouter le support d'un nouveau pays ouest-africain :

1. Ajoutez le pays dans `erpnext/regional/west_africa/utils.py`
2. Définissez les taux de TVA et taxes
3. Créez les templates fiscaux
4. Documentez les spécificités réglementaires
5. Ajoutez un guide de configuration

### Traductions / Translations

FasoCompta priorise le français, mais accepte :
- Langues locales (Bambara, Wolof, etc.)
- Arabe
- Anglais

Pour ajouter une traduction :
1. Utilisez l'outil de traduction Frappe
2. Créez les fichiers de traduction
3. Testez l'interface dans la nouvelle langue

## 🏪 Contributions Sectorielles / Industry Contributions

### Restaurants
- Nouvelles fonctionnalités de gestion de cuisine
- Intégrations avec systèmes de commande
- Optimisations POS pour service rapide

### Boutiques
- Gestion de variantes produits
- Intégrations e-commerce
- Programmes de fidélité

### Commerce Général
- Workflows d'import/export
- Gestion documentaire
- Multi-devises et multi-sites

## 🧪 Tests

Si vous ajoutez du code, ajoutez des tests :

```python
# erpnext/regional/west_africa/test_utils.py
import unittest
from erpnext.regional.west_africa.utils import calculate_aib_tax

class TestWestAfricaUtils(unittest.TestCase):
    def test_calculate_aib_mali(self):
        """Test AIB calculation for Mali"""
        amount = 100000
        aib = calculate_aib_tax(amount, rate=1.0)
        self.assertEqual(aib, 1000)
```

## 📄 Licence / License

En contribuant à FasoCompta, vous acceptez que vos contributions soient sous licence GPL-3.0.

By contributing to FasoCompta, you agree that your contributions will be licensed under GPL-3.0.

## 💬 Communication

- **GitHub Issues** : Pour bugs et features
- **Discussions** : Pour questions générales
- **Email** : contact@fasocompta.com

## 🙏 Remerciements / Acknowledgments

Merci à tous les contributeurs qui rendent FasoCompta meilleur !

Thank you to all contributors who make FasoCompta better!

## 📚 Ressources / Resources

- [Documentation FasoCompta](./docs/fr/README.md)
- [Frappe Framework Docs](https://frappeframework.com/docs)
- [ERPNext Developer Guide](https://docs.erpnext.com/docs/user/en/developer)
- [OHADA Accounting Standards](http://www.ohada.org/)

---

**Ensemble, construisons le meilleur système de gestion pour l'Afrique de l'Ouest !**

**Together, let's build the best management system for West Africa!**
