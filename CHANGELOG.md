# Changelog FasoCompta

Tous les changements notables de ce projet seront documentés dans ce fichier.

## [1.0.0] - 2024-11-18

### 🎉 Version Initiale - Transformation en FasoCompta

Cette version marque la transformation du repository ERPNext en **FasoCompta**, un système de gestion complet pour les entreprises ouest-africaines.

### ✨ Ajouts Majeurs

#### Branding et Identité
- Rebranding complet en "FasoCompta"
- Nouvelle identité visuelle adaptée à l'Afrique de l'Ouest
- Description en français : "Système de gestion financière, comptable et RH"
- Couleur principale : Vert (#00B050)
- Mise à jour de tous les fichiers de configuration (hooks.py, package.json, pyproject.toml)

#### Support Régional Ouest-Africain
- **Module régional** : `/erpnext/regional/west_africa/`
- Support de **15 pays** ouest-africains :
  - UEMOA : Mali, Sénégal, Côte d'Ivoire, Burkina Faso, Niger, Benin, Togo, Guinée
  - CEMAC : Cameroun, Tchad, RCA, Congo, Gabon, Guinée Équatoriale
- **Devises** : XOF (Franc CFA UEMOA), XAF (Franc CFA CEMAC)
- **Système comptable** : OHADA/SYSCOHADA
- **Identifiants fiscaux** :
  - IFU/NIF (Identifiant Fiscal Unique)
  - RCCM (Registre de Commerce et du Crédit Mobilier)
  - CNSS (Caisse Nationale de Sécurité Sociale)

#### Fiscalité Ouest-Africaine
- **Mali** : TVA 18%, AIB 1%, TPS 5%
- **Sénégal** : TVA 18%
- **Côte d'Ivoire** : TVA 18%
- Taux de TVA configurés pour les 15 pays
- Validation des numéros IFU/NIF
- Calcul automatique des taxes locales

#### Module Gestion de Restaurant
- **Nouveau module** : `/erpnext/restaurant_management/`
- Gestion des tables et zones (Intérieur, Terrasse, VIP, Bar)
- Attribution de serveurs/waiters
- Catégories de menu :
  - Entrées, Plats Principaux, Desserts
  - Boissons (Froides, Chaudes, Alcoolisées)
  - Accompagnements
- Calcul des frais de service (10% standard)
- Temps de préparation par plat
- Coût de revient par recette (BOM)
- Bons de cuisine automatiques
- Réservations de tables

#### Fonctionnalités Retail/Boutique
- Gestion des variantes produits (tailles, couleurs)
- Support des codes-barres
- Listes de prix multiples (Standard, Gros, Promotionnel, VIP)
- Programmes de fidélité
- Gestion multi-magasins
- Règles de tarification automatiques

#### Modes de Paiement Mobile Money
- Orange Money
- Moov Money
- Wave
- MTN Mobile Money
- Configuration prête à l'emploi pour l'Afrique de l'Ouest

### 📚 Documentation Complète (Français)

#### Guide de Démarrage Rapide
- **Fichier** : `docs/fr/README.md` (7.7 KB)
- Installation (Bench et Docker)
- Configuration initiale en 5 étapes
- Processus de vente par secteur
- Opérations quotidiennes
- Raccourcis clavier
- FAQ

#### Guide de Configuration
- **Fichier** : `docs/fr/configuration.md` (6.8 KB)
- Configuration entreprise et fiscalité
- Plan comptable OHADA
- Configuration par secteur :
  - Restaurants
  - Boutiques
  - Commerce général
- Configuration RH et paie
- Mobile Money
- Rapports essentiels
- Bonnes pratiques

#### Guide Restaurant Complet
- **Fichier** : `docs/fr/restaurant.md` (12.9 KB)
- Configuration complète pour restaurants
- Gestion du menu et des recettes
- Service à table et POS
- Gestion des tables et réservations
- Cuisine et stocks alimentaires
- Gestion du personnel
- Rapports spécifiques restaurants
- Hygiène et sécurité alimentaire
- Best practices quotidiennes

#### Guide Boutique/Commerce Complet
- **Fichier** : `docs/fr/boutique.md` (11.7 KB)
- Configuration pour boutiques et commerces
- Gestion des articles et variantes
- Point de Vente (POS) avec scanner
- Gestion des stocks et inventaires
- Listes de prix et promotions
- Gestion clients et fidélité
- Rapports retail
- Multi-magasins
- Processus de vente et retours

#### Guide de Contribution
- **Fichier** : `CONTRIBUTING.md` (6.4 KB)
- Comment contribuer au projet
- Standards de code (Python, JavaScript)
- Process de Pull Request
- Priorités de contribution
- Localisation et traductions
- Tests

### 🔧 Scripts d'Installation

#### Script Setup Automatisé
- **Fichier** : `erpnext/setup_fasocompta.py`
- Configuration automatique par pays
- Configuration par secteur d'activité
- Création des templates fiscaux
- Setup Mobile Money
- Création de données de démonstration

### 🌍 Fonctionnalités Régionales

#### Utilitaires West Africa
- Détection automatique UEMOA/CEMAC
- Conversion devise CFA appropriée
- Taux de TVA par pays
- Validation IFU/NIF
- Types de comptes OHADA
- Calcul AIB et TPS
- Taxes spécifiques restaurants
- Exemptions fiscales retail

### 📊 Rapports et Analyses

#### Rapports Configurés
- Ventes quotidiennes
- Déclaration TVA
- Valorisation stock
- Tableau de flux de trésorerie
- Compte de résultat OHADA
- Bilan OHADA
- Performance par serveur (restaurants)
- Articles populaires
- Analyse de rentabilité

### 🎨 Interface et Expérience

- Interface responsive (mobile, tablette, desktop)
- Support français complet
- Icônes et couleurs adaptées
- Navigation optimisée pour les secteurs ciblés
- POS rapide et intuitif

### 🔐 Sécurité

- Aucune vulnérabilité détectée (CodeQL)
- Validation des entrées utilisateur
- Protection des données sensibles
- Conformité GPL-3.0

### 📈 Statistiques

- **14 fichiers modifiés**
- **+2,707 lignes ajoutées**
- **-128 lignes supprimées**
- **33+ KB de documentation**
- **15 pays supportés**
- **3 secteurs d'activité configurés**

## 🎯 Prochaines Versions Prévues

### [1.1.0] - À venir
- [ ] Templates de rapports fiscaux par pays
- [ ] Intégration WhatsApp Business
- [ ] Module e-commerce
- [ ] Application mobile dédiée
- [ ] Support langues locales (Bambara, Wolof)
- [ ] Tutoriels vidéo en français

### [1.2.0] - À venir
- [ ] Intelligence artificielle pour prévisions
- [ ] Intégration services bancaires locaux
- [ ] Module de gestion agricole
- [ ] Support Bitcoin/Crypto pour paiements
- [ ] Tableau de bord analytique avancé

## 🤝 Contributeurs

- **Transformation FasoCompta** : GitHub Copilot & mahamadoubmaiga
- **Base ERPNext** : Frappe Technologies & Community

## 📝 Notes

Ce projet est basé sur ERPNext v15 et Frappe Framework v15. Il maintient la compatibilité avec l'écosystème Frappe tout en ajoutant des fonctionnalités spécifiques à l'Afrique de l'Ouest.

---

**Format**: Le changelog suit le format [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/)

**Versions**: Le projet utilise [Semantic Versioning](https://semver.org/lang/fr/)
