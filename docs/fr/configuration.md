# Guide de Configuration FasoCompta

## Bienvenue dans FasoCompta

FasoCompta est un système de gestion complet conçu spécialement pour les entreprises ouest-africaines. Ce guide vous aidera à configurer votre système.

## Configuration Initiale

### 1. Informations de l'Entreprise

Après l'installation, configurez les informations de votre entreprise :

1. Allez dans **Setup > Company**
2. Remplissez les informations suivantes :
   - **Nom de l'entreprise**
   - **Pays** : Sélectionnez votre pays (Mali, Sénégal, Côte d'Ivoire, etc.)
   - **Devise par défaut** : XOF (Franc CFA UEMOA) ou XAF (Franc CFA CEMAC)
   - **Numéro IFU/NIF** : Votre identifiant fiscal unique
   - **Numéro RCCM** : Registre de Commerce et du Crédit Mobilier
   - **Numéro CNSS** : Pour les contributions sociales

### 2. Configuration Fiscale

#### Pour le Mali :
- **TVA Standard** : 18%
- **AIB (Acompte sur Impôt sur les Bénéfices)** : 1%
- **TPS (Taxe sur Prestations de Services)** : 5%

#### Configuration dans FasoCompta :
1. Allez dans **Accounting > Setup > Tax Templates**
2. Créez les modèles suivants :
   - TVA 18%
   - TVA + AIB (18% + 1%)
   - Exonéré de TVA

### 3. Plan Comptable OHADA

FasoCompta utilise le système comptable OHADA/SYSCOHADA :

- **Classe 1** : Comptes de capitaux
- **Classe 2** : Comptes d'immobilisations
- **Classe 3** : Comptes de stocks
- **Classe 4** : Comptes de tiers
- **Classe 5** : Comptes de trésorerie
- **Classe 6** : Comptes de charges
- **Classe 7** : Comptes de produits
- **Classe 8** : Comptes spéciaux

Pour importer le plan comptable :
1. Allez dans **Accounting > Chart of Accounts**
2. Sélectionnez "OHADA - Système Comptable OHADA"

## Configuration par Secteur

### Configuration Restaurant

#### 1. Configuration du Point de Vente (POS)

1. Allez dans **Retail > POS Profile**
2. Créez un nouveau profil :
   - **Nom** : "Restaurant POS"
   - **Devise** : XOF
   - **Entrepôt** : Sélectionnez votre entrepôt principal
   - **Mode de paiement** : Espèces, Mobile Money, Carte bancaire
   
#### 2. Configuration des Tables

1. Créez vos tables dans **Restaurant > Tables**
2. Attribuez les numéros de table
3. Configurez les zones (Intérieur, Terrasse, VIP, etc.)

#### 3. Configuration du Menu

1. Allez dans **Stock > Item**
2. Pour chaque plat :
   - Cochez "Is Menu Item"
   - Sélectionnez la catégorie (Entrées, Plats Principaux, Desserts, etc.)
   - Indiquez le temps de préparation
   - Définissez le prix de vente

#### 4. Gestion des Recettes

1. Créez une nomenclature (BOM) pour chaque plat
2. Listez tous les ingrédients et quantités
3. Le système calculera automatiquement le coût de revient

#### 5. Frais de Service

- Configurez le pourcentage de frais de service (généralement 10%)
- Activez l'option dans le profil POS

### Configuration Boutique/Commerce

#### 1. Configuration des Stocks

1. Allez dans **Stock > Warehouse**
2. Créez vos entrepôts/magasins :
   - Magasin principal
   - Dépôt
   - Magasin secondaire (si multi-points de vente)

#### 2. Configuration des Articles

1. Allez dans **Stock > Item**
2. Pour chaque article :
   - Code article (ou code-barres)
   - Nom de l'article
   - Groupe d'articles
   - Unité de mesure
   - Prix d'achat et de vente
   - Niveau de stock minimum

#### 3. Configuration du Point de Vente

1. Créez un profil POS pour votre boutique
2. Activez le scanner de codes-barres
3. Configurez les modes de paiement :
   - Espèces
   - Orange Money
   - Moov Money
   - Carte bancaire

#### 4. Gestion Multi-Prix

Créez des listes de prix pour :
- Prix de détail
- Prix de gros
- Prix promotionnels
- Prix VIP

### Configuration Commerce Général

#### 1. Gestion des Clients

1. Allez dans **Selling > Customer**
2. Pour chaque client professionnel :
   - Nom et coordonnées
   - Numéro IFU/NIF
   - Conditions de paiement
   - Limite de crédit

#### 2. Gestion des Fournisseurs

1. Allez dans **Buying > Supplier**
2. Enregistrez vos fournisseurs avec :
   - Coordonnées complètes
   - Numéro IFU/NIF
   - Conditions de paiement
   - Devise de transaction

#### 3. Processus de Vente

Le processus standard :
1. **Devis** → 2. **Bon de Commande** → 3. **Bon de Livraison** → 4. **Facture**

#### 4. Processus d'Achat

Le processus standard :
1. **Demande d'Achat** → 2. **Bon de Commande Fournisseur** → 3. **Réception** → 4. **Facture Fournisseur**

## Configuration RH (Gestion des Ressources Humaines)

### 1. Structure de l'Entreprise

1. Allez dans **HR > Company Structure**
2. Créez vos départements :
   - Direction
   - Comptabilité
   - Commercial
   - Production/Cuisine (pour restaurants)
   - etc.

### 2. Configuration des Employés

Pour chaque employé :
1. Allez dans **HR > Employee**
2. Remplissez :
   - Informations personnelles
   - **Numéro CNSS**
   - **Carte de Travail**
   - Poste et département
   - Salaire de base

### 3. Configuration de la Paie

1. Allez dans **HR > Payroll**
2. Configurez :
   - **Composantes de salaire** :
     - Salaire de base
     - Prime de transport
     - Prime d'ancienneté
     - Heures supplémentaires
   - **Déductions** :
     - Cotisations CNSS (employé : 3,6%, employeur : 16%)
     - IPTS (Impôt sur les Traitements et Salaires)
     - Avances sur salaire

### 4. Gestion des Congés

1. Configurez les types de congés :
   - Congés annuels (30 jours/an au Mali)
   - Congés maladie
   - Congés maternité
   - Congés sans solde

## Modes de Paiement Mobile

### Configuration Mobile Money

FasoCompta supporte les principaux services de mobile money :

1. **Orange Money**
2. **Moov Money**
3. **Wave**
4. **MTN Mobile Money**

Configuration :
1. Allez dans **Accounting > Mode of Payment**
2. Créez chaque mode de paiement
3. Associez au compte bancaire correspondant

## Rapports Importants

### Rapports Comptables
- Bilan
- Compte de Résultat
- Grand Livre
- Balance Générale
- Journal des Ventes
- Journal des Achats

### Rapports Fiscaux
- Déclaration TVA mensuelle
- État des retenues à la source
- Rapport AIB

### Rapports de Gestion
- Tableau de bord quotidien
- Analyse des ventes par produit
- Analyse de la rentabilité
- État des stocks
- Âge des créances clients

## Support et Assistance

Pour toute question ou assistance :
- Email : contact@fasocompta.com
- Documentation : https://github.com/mahamadoubmaiga/FasoCompta/wiki
- Issues : https://github.com/mahamadoubmaiga/FasoCompta/issues

## Bonnes Pratiques

1. **Sauvegardez régulièrement** vos données
2. **Formez votre personnel** à l'utilisation du système
3. **Tenez à jour** les informations fiscales
4. **Réconciliez** vos comptes bancaires mensuellement
5. **Effectuez des inventaires** réguliers des stocks
6. **Archivez** les documents importants

---

**Fait avec ❤️ pour les entrepreneurs ouest-africains**
