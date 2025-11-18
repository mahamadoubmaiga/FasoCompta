<div align="center">
    <h1>FasoCompta</h1>
    <p align="center">
        <p>Système de Gestion Financière, Comptable et RH pour l'Afrique de l'Ouest</p>
        <p>Financial Management, Accounting and HR System for West Africa</p>
    </p>

</div>

## À Propos / About

**FasoCompta** est une application web complète de gestion d'entreprise spécialement conçue pour les restaurants, boutiques, commerces généraux et entrepreneurs maliens et ouest-africains. Basé sur ERPNext, FasoCompta offre une solution adaptée aux réalités du marché ouest-africain.

**FasoCompta** is a comprehensive business management web application specifically designed for restaurants, shops, general commerce, and Malian and West African entrepreneurs. Based on ERPNext, FasoCompta offers a solution adapted to the realities of the West African market.

## Fonctionnalités Principales / Key Features

### 💰 Gestion Financière et Comptable / Financial & Accounting Management
- **Comptabilité Générale** : Plan comptable OHADA/SYSCOHADA adapté
- **Facturation** : Création et gestion des factures de vente et d'achat
- **Trésorerie** : Suivi des flux de trésorerie et rapprochements bancaires
- **Fiscalité** : Gestion TVA, impôts et taxes locales (Mali, Sénégal, Côte d'Ivoire, etc.)
- **Rapports Financiers** : Bilan, compte de résultat, grand livre, balance

### 👥 Gestion des Ressources Humaines (GRH) / HR Management
- **Gestion du Personnel** : Dossiers employés, contrats, congés
- **Paie** : Calcul des salaires selon les réglementations locales
- **Présence** : Pointage et gestion des horaires
- **Formation** : Suivi des formations et compétences

### 🍽️ Spécial Restaurants / Restaurant Features
- **Point de Vente (POS)** : Caisse rapide et intuitive
- **Gestion des Tables** : Réservations et suivi des commandes
- **Gestion des Stocks** : Ingrédients et approvisionnements
- **Gestion des Recettes** : Fiches techniques et coûts de revient
- **Inventaire** : Suivi en temps réel des stocks

### 🏪 Spécial Boutiques / Retail Features
- **Gestion des Stocks** : Suivi multi-magasin et multi-dépôt
- **Point de Vente** : Ventes rapides avec scanner de codes-barres
- **Gestion des Prix** : Tarifs multiples, promotions, remises
- **Gestion des Fournisseurs** : Commandes et réceptions
- **Inventaire Périodique** : Outils de comptage et ajustement

### 📊 Commerce Général / General Commerce
- **Gestion Commerciale** : Devis, bons de commande, livraisons
- **CRM** : Gestion de la relation client
- **Achats** : Gestion des fournisseurs et approvisionnements
- **Projets** : Suivi de projets et tâches
- **Rapports** : Tableaux de bord et analyses personnalisables

## Spécificités Ouest-Africaines / West African Specifics

- ✅ **Monnaie** : Franc CFA (XOF/XAF) et autres devises locales
- ✅ **Fiscalité** : Système fiscal malien et autres pays UEMOA/CEMAC
- ✅ **Plan Comptable** : OHADA/SYSCOHADA
- ✅ **Langues** : Français (interface et documentation)
- ✅ **Réglementations** : Conformité aux normes locales
- ✅ **Support Mobile** : Application responsive pour une utilisation sur mobile

## Installation / Setup

### Prérequis / Prerequisites

- Python 3.10+
- Node.js 18+
- MariaDB 10.6+
- Redis

### Installation avec Frappe Bench / Installation with Frappe Bench

```bash
# Installer bench
pip install frappe-bench

# Créer un nouveau site
bench init fasocompta-bench
cd fasocompta-bench

# Créer un nouveau site
bench new-site fasocompta.local

# Obtenir l'application FasoCompta
bench get-app https://github.com/mahamadoubmaiga/FasoCompta

# Installer l'application
bench --site fasocompta.local install-app erpnext

# Démarrer
bench start
```

Accédez à votre site sur `http://fasocompta.local:8000`

### Installation avec Docker / Docker Installation

```bash
git clone https://github.com/frappe/frappe_docker
cd frappe_docker
docker compose -f pwd.yml up -d
```

## Configuration Initiale / Initial Setup

Après l'installation, configurez votre système :

1. **Sélectionnez votre pays** : Mali, Sénégal, Côte d'Ivoire, etc.
2. **Choisissez votre secteur** : Restaurant, Boutique, Commerce Général
3. **Configurez votre devise** : XOF (Franc CFA) ou autre
4. **Importez le plan comptable** : OHADA/SYSCOHADA
5. **Configurez les taxes** : TVA et autres taxes locales

## Documentation

- [Guide d'Utilisation (Français)](/docs/fr/README.md)
- [Guide de Configuration](/docs/fr/configuration.md)
- [Guide Restaurant](/docs/fr/restaurant.md)
- [Guide Boutique](/docs/fr/boutique.md)
- [Documentation Frappe](https://frappeframework.com/docs)
- [Documentation ERPNext](https://docs.erpnext.com/)

## Support et Communauté / Support & Community

- **Email** : contact@fasocompta.com
- **Issues** : [GitHub Issues](https://github.com/mahamadoubmaiga/FasoCompta/issues)
- **Documentation** : [Wiki](https://github.com/mahamadoubmaiga/FasoCompta/wiki)

## Technologies Utilisées / Technologies Used

- **Backend** : Python (Frappe Framework)
- **Frontend** : JavaScript, Vue.js (Frappe UI)
- **Base de Données** : MariaDB
- **Cache** : Redis
- **Architecture** : Application Web Progressive (PWA)

## Contribution

Les contributions sont les bienvenues ! Consultez notre [Guide de Contribution](CONTRIBUTING.md).

## Licence / License

GNU General Public License v3.0 - Voir [LICENSE](license.txt)

## Remerciements / Acknowledgments

Ce projet est basé sur [ERPNext](https://github.com/frappe/erpnext) et [Frappe Framework](https://github.com/frappe/frappe), développés par Frappe Technologies. Nous remercions la communauté open-source pour leur excellent travail.

---

<div align="center">
    <p>Fait avec ❤️ pour les entrepreneurs ouest-africains</p>
    <p>Made with ❤️ for West African entrepreneurs</p>
</div>
