# Guide de Démarrage Rapide - FasoCompta

## Qu'est-ce que FasoCompta ?

FasoCompta est une application web complète de gestion d'entreprise conçue spécialement pour les restaurants, boutiques, commerces et entrepreneurs d'Afrique de l'Ouest.

## Fonctionnalités Principales

✅ **Comptabilité** : Plan comptable OHADA/SYSCOHADA  
✅ **Facturation** : Devis, factures, avoirs  
✅ **Point de Vente** : POS rapide pour restaurants et boutiques  
✅ **Gestion de Stock** : Inventaire en temps réel  
✅ **RH** : Gestion du personnel et paie  
✅ **Multi-devises** : Support Franc CFA (XOF/XAF)  
✅ **Mobile-friendly** : Utilisable sur smartphone et tablette  

## Installation Rapide

### Option 1 : Installation avec Frappe Bench (Recommandée)

```bash
# Installer bench
pip install frappe-bench

# Créer un nouveau site
bench init fasocompta-bench
cd fasocompta-bench
bench new-site monsite.local

# Obtenir FasoCompta
bench get-app https://github.com/mahamadoubmaiga/FasoCompta

# Installer l'application
bench --site monsite.local install-app erpnext

# Démarrer le serveur
bench start
```

### Option 2 : Installation Docker

```bash
git clone https://github.com/frappe/frappe_docker
cd frappe_docker
docker compose -f pwd.yml up -d
```

Accédez à `http://localhost:8000` dans votre navigateur.

## Premier Démarrage

### 1. Connexion Initiale

Lors de la première connexion :
- **Utilisateur** : Administrator
- **Mot de passe** : Celui défini lors de l'installation

### 2. Configuration de Base (Assistant de Configuration)

L'assistant vous guidera à travers :

#### Étape 1 : Région et Langue
- **Pays** : Mali, Sénégal, Côte d'Ivoire, etc.
- **Langue** : Français
- **Fuseau horaire** : GMT

#### Étape 2 : Informations de l'Entreprise
- Nom de votre entreprise
- Type d'activité : Restaurant / Boutique / Commerce Général
- Devise : XOF (Franc CFA)

#### Étape 3 : Configuration Fiscale
- Numéro IFU/NIF
- Numéro RCCM
- TVA : 18% (standard Mali)

#### Étape 4 : Plan Comptable
- Sélectionnez : "OHADA/SYSCOHADA"

## Cas d'Usage par Secteur

### 🍽️ Restaurant

#### Configuration Rapide
1. Créez votre menu dans **Stock > Items**
2. Configurez les tables dans **Restaurant > Tables**
3. Créez un profil POS dans **Retail > POS Profile**
4. Commencez à prendre des commandes !

#### Processus de Vente
```
Client arrive → Assigner table → Prendre commande → 
Envoyer en cuisine → Servir → Encaisser (POS)
```

### 🏪 Boutique/Commerce

#### Configuration Rapide
1. Créez vos articles dans **Stock > Items**
2. Configurez votre entrepôt dans **Stock > Warehouse**
3. Créez un profil POS dans **Retail > POS Profile**
4. Commencez à vendre !

#### Processus de Vente
```
Client achète → Scanner article → Ajouter au panier → 
Paiement (Espèces/Mobile Money) → Imprimer reçu
```

### 📊 Commerce Général

#### Processus Complet
```
Devis → Bon de Commande → Livraison → Facture → Paiement
```

## Modules Principaux

### 💰 Comptabilité
- **Accès** : Menu > Accounting
- **Fonctions** :
  - Plan comptable OHADA
  - Écritures comptables
  - Rapprochement bancaire
  - Rapports financiers

### 📦 Stock
- **Accès** : Menu > Stock
- **Fonctions** :
  - Gestion articles
  - Mouvements de stock
  - Inventaires
  - Valorisation

### 💵 Ventes
- **Accès** : Menu > Selling
- **Fonctions** :
  - Devis
  - Bons de commande
  - Livraisons
  - Factures

### 🛒 Achats
- **Accès** : Menu > Buying
- **Fonctions** :
  - Demandes d'achat
  - Bons de commande fournisseurs
  - Réceptions
  - Factures fournisseurs

### 👥 Ressources Humaines
- **Accès** : Menu > HR
- **Fonctions** :
  - Gestion employés
  - Paie
  - Congés
  - Présence

### 🏪 Point de Vente (POS)
- **Accès** : Menu > Retail > POS
- **Fonctions** :
  - Vente rapide
  - Multi-modes de paiement
  - Gestion tables (restaurant)
  - Impression tickets

## Opérations Quotidiennes

### Créer une Facture de Vente

1. Menu > Selling > Sales Invoice > Nouveau
2. Sélectionnez le client
3. Ajoutez les articles
4. Le système calcule automatiquement :
   - TVA (18%)
   - Total TTC
5. Enregistrez et soumettez
6. Imprimez la facture

### Utiliser le Point de Vente

1. Menu > Retail > POS
2. Sélectionnez votre profil POS
3. Sélectionnez le client (ou "Client Comptant")
4. Ajoutez les articles :
   - Scannez le code-barres OU
   - Cliquez sur l'article
5. Choisissez le mode de paiement :
   - Espèces
   - Orange Money
   - Moov Money
   - Carte bancaire
6. Validez et imprimez le reçu

### Faire un Encaissement

1. Menu > Accounting > Payment Entry
2. Type : "Receive"
3. Sélectionnez le client
4. Montant reçu
5. Mode de paiement
6. Enregistrez

### Consulter le Tableau de Bord

1. Menu > Home > Dashboard
2. Visualisez :
   - Ventes du jour
   - Encaissements
   - Stocks faibles
   - Factures en attente

## Modes de Paiement Populaires

### Mobile Money

FasoCompta supporte :
- 📱 Orange Money
- 📱 Moov Money
- 📱 Wave
- 📱 MTN Mobile Money

Configuration : **Accounting > Mode of Payment**

## Rapports Essentiels

### Rapports Quotidiens
1. **Ventes du Jour** : Selling > Reports > Sales Analytics
2. **Encaissements** : Accounts > Reports > Payment Entry Report
3. **Stock Disponible** : Stock > Reports > Stock Balance

### Rapports Mensuels
1. **Compte de Résultat** : Accounting > Reports > Profit and Loss
2. **Bilan** : Accounting > Reports > Balance Sheet
3. **Déclaration TVA** : Accounting > Reports > Tax Summary

## Conseils Pratiques

### ✅ À Faire
- Sauvegardez vos données régulièrement
- Effectuez un inventaire mensuel
- Réconciliez vos comptes bancaires
- Formez votre personnel au système
- Tenez vos informations fiscales à jour

### ❌ À Éviter
- Ne partagez pas le mot de passe administrateur
- N'annulez pas les factures déjà payées
- Ne modifiez pas le plan comptable sans formation
- N'oubliez pas de faire les clôtures mensuelles

## Raccourcis Clavier

- `Ctrl + K` : Recherche rapide
- `Ctrl + G` : Aller à un module
- `Ctrl + S` : Enregistrer
- `Ctrl + P` : Imprimer

## Ressources Utiles

### Documentation
- [Guide de Configuration Complet](./configuration.md)
- [Guide Restaurant](./restaurant.md)
- [Guide Boutique](./boutique.md)

### Support
- Email : contact@fasocompta.com
- GitHub : https://github.com/mahamadoubmaiga/FasoCompta
- Wiki : https://github.com/mahamadoubmaiga/FasoCompta/wiki

### Communauté
- Forum de discussion
- Groupe Telegram
- Tutoriels vidéo (à venir)

## Vidéos de Formation

*(À venir)*
- Configuration initiale (10 min)
- Première vente avec POS (5 min)
- Gestion des stocks (15 min)
- Paie des employés (20 min)

## FAQ

**Q : FasoCompta fonctionne-t-il hors ligne ?**  
R : Le POS peut fonctionner en mode hors ligne limité. Une synchronisation est nécessaire quand la connexion revient.

**Q : Combien d'utilisateurs peuvent se connecter ?**  
R : Illimité. Vous pouvez créer autant d'utilisateurs que nécessaire.

**Q : Les données sont-elles sécurisées ?**  
R : Oui, FasoCompta utilise les meilleures pratiques de sécurité. Pensez à faire des sauvegardes régulières.

**Q : Puis-je utiliser FasoCompta sur mobile ?**  
R : Oui, l'interface est responsive et fonctionne sur smartphone et tablette.

**Q : Comment mettre à jour FasoCompta ?**  
R : Utilisez `bench update` pour obtenir les dernières fonctionnalités.

---

## Prochaines Étapes

Maintenant que vous avez configuré FasoCompta :

1. ✅ Créez vos premiers articles/produits
2. ✅ Enregistrez vos clients principaux
3. ✅ Créez votre première facture
4. ✅ Explorez les rapports
5. ✅ Formez votre équipe

**Besoin d'aide ?** N'hésitez pas à consulter la documentation complète ou à contacter le support.

---

**Bonne gestion avec FasoCompta ! 🚀**

*Fait avec ❤️ pour les entrepreneurs ouest-africains*
