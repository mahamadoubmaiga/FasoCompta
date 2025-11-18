# Guide Boutique & Commerce de Détail - FasoCompta

## Configuration pour Boutiques et Commerces

Ce guide est spécialement conçu pour les propriétaires de boutiques, magasins de détail, et commerces de vêtements, cosmétiques, alimentation, etc.

## 🏪 Configuration Initiale

### 1. Informations de Base

**Menu > Setup > Company**

- **Nom** : Nom de votre boutique
- **Type** : Retail/Commerce de Détail
- **Pays** : Mali, Sénégal, Côte d'Ivoire, etc.
- **Devise** : XOF (Franc CFA)
- **IFU/NIF** : Votre numéro d'identification fiscale
- **RCCM** : Numéro du registre de commerce

### 2. Configuration des Entrepôts

**Menu > Stock > Warehouse**

Créez vos entrepôts/points de vente :
- **Magasin Principal** : Votre point de vente principal
- **Arrière-boutique** : Zone de stockage
- **Dépôt** : Si vous avez un entrepôt séparé
- **Magasin 2, 3, etc.** : Si vous avez plusieurs points de vente

### 3. Groupes d'Articles

**Menu > Stock > Item Group**

Organisez vos produits par catégories :
- Vêtements Hommes
- Vêtements Femmes
- Vêtements Enfants
- Chaussures
- Accessoires
- Cosmétiques
- Produits alimentaires
- Électronique
- etc.

## 📦 Gestion des Articles

### Créer un Article

**Menu > Stock > Item > New**

Pour chaque produit :

#### Informations de Base
- **Code Article** : SKU ou code unique
- **Nom Article** : Nom du produit
- **Groupe** : Catégorie du produit
- **Unité de Mesure** : Pièce, Boîte, Kg, etc.

#### Codes-Barres
- Ajoutez le(s) code(s)-barres du produit
- Scannez avec votre lecteur ou tapez manuellement
- Support multi-codes-barres pour le même article

#### Prix
- **Prix d'Achat** : Coût d'acquisition
- **Prix de Vente Standard** : Prix public
- **Prix de Gros** : Pour clients grossistes
- **Prix Promotionnel** : Prix en promotion

#### Stock
- **Entrepôt par Défaut** : Où le stock est généralement situé
- **Stock Minimum** : Niveau d'alerte de réapprovisionnement
- **Stock Maximum** : Niveau optimal
- **Valeur du Stock** : Calculée automatiquement

#### Taxes
- **TVA** : Standard 18% ou Exonéré
- **Taxe Produit Spécifique** : Si applicable

### Articles Avec Variantes

Pour les produits avec tailles/couleurs :

**Menu > Stock > Item > Has Variants**

Exemple : T-Shirt
- **Attributs** :
  - Taille : S, M, L, XL, XXL
  - Couleur : Blanc, Noir, Rouge, Bleu

Le système créera automatiquement :
- T-Shirt-S-Blanc
- T-Shirt-S-Noir
- T-Shirt-M-Blanc
- etc.

## 💰 Point de Vente (POS)

### Configuration du POS

**Menu > Retail > POS Profile > New**

#### Paramètres de Base
- **Nom** : "POS Boutique"
- **Devise** : XOF
- **Entrepôt** : Magasin Principal
- **Caisse** : Compte de caisse

#### Modes de Paiement
Activez :
- ✅ Espèces
- ✅ Orange Money
- ✅ Moov Money
- ✅ Wave
- ✅ Carte Bancaire
- ✅ Crédit Client

#### Options
- ✅ Activer Scanner de Codes-Barres
- ✅ Autoriser Remises
- ✅ Imprimer Reçu Automatiquement
- ✅ Vente à Crédit (optionnel)

### Utiliser le POS

**Menu > Retail > POS**

#### Processus de Vente

1. **Sélectionner Client**
   - "Client Comptant" pour vente directe
   - Ou sélectionnez un client enregistré

2. **Ajouter Articles**
   - Scannez le code-barres
   - OU Recherchez par nom
   - OU Cliquez sur l'article

3. **Ajuster Quantité**
   - Cliquez sur "+" ou "-"
   - Ou tapez directement

4. **Appliquer Remise** (si autorisé)
   - Remise en % ou montant fixe
   - Par ligne ou sur le total

5. **Encaissement**
   - Sélectionnez mode de paiement
   - Pour Mobile Money : notez le numéro de transaction
   - Pour Espèces : le système calcule la monnaie à rendre

6. **Imprimer Reçu**
   - Reçu automatique ou sur demande

### Multi-Paiement

Pour un paiement mixte :
1. 50,000 XOF en espèces
2. 30,000 XOF Orange Money
3. Total : 80,000 XOF

Le système accepte plusieurs modes de paiement pour une même vente.

## 📊 Gestion des Stocks

### Réception de Marchandises

**Menu > Stock > Purchase Receipt**

Quand vous recevez des produits d'un fournisseur :

1. Créez un Bon de Réception
2. Sélectionnez le Fournisseur
3. Ajoutez les articles reçus avec quantités
4. Vérifiez les articles physiquement
5. Soumettez le document
6. Le stock est mis à jour automatiquement

### Mouvement de Stock

**Menu > Stock > Stock Entry**

Pour les transferts internes :
- **Magasin → Arrière-boutique**
- **Dépôt → Magasin**
- **Ajustement de Stock** : Corrections d'inventaire

### Inventaire Physique

**Menu > Stock > Stock Reconciliation**

Processus mensuel recommandé :

1. Comptez physiquement vos articles
2. Créez une réconciliation de stock
3. Entrez les quantités réelles
4. Le système calcule les différences
5. Soumettez pour ajuster les stocks

### Alertes de Stock

**Menu > Stock > Stock Reports > Stock Level**

Le système vous alerte quand :
- ⚠️ Stock en dessous du minimum
- ✅ Stock optimal
- 🔴 Article en rupture de stock

### Valorisation du Stock

**Menu > Stock > Stock Balance**

Consultez :
- Quantité en stock par article
- Valeur totale du stock
- Valeur par entrepôt
- Analyse par groupe d'articles

## 💳 Gestion des Prix

### Listes de Prix

**Menu > Stock > Price List**

Créez différentes listes :

#### Prix Standard
- Prix de détail normal
- Pour ventes au comptant

#### Prix de Gros
- Remise 10-15% sur prix standard
- Pour clients grossistes
- Minimum d'achat requis

#### Prix Promotionnel
- Prix spécial pendant promotions
- Définissez période de validité
- Appliquez à certains articles

#### Prix VIP
- Pour clients fidèles/VIP
- Remise permanente 5-10%

### Règles de Tarification

**Menu > Selling > Pricing Rule**

Automatisez les remises :
- "Achetez 3, payez 2"
- "10% de remise sur achat > 50,000 XOF"
- "5% de remise sur catégorie X"
- Promotions à durée limitée

## 👥 Gestion des Clients

### Créer un Client

**Menu > Selling > Customer > New**

#### Types de Clients

1. **Client Comptant**
   - Ventes au comptoir
   - Paiement immédiat
   - Pas de crédit

2. **Client à Crédit**
   - Factures avec délai de paiement
   - Limite de crédit définie
   - Conditions de paiement : Net 30 jours

3. **Client Grossiste**
   - Achats en volume
   - Prix de gros appliqués
   - Paiement : 50% avance, solde à livraison

#### Informations Client
- Nom et prénom
- Téléphone (important pour Mobile Money)
- Adresse
- IFU/NIF (pour entreprises)
- Limite de crédit
- Groupe de clients (Détail, Gros, VIP)

### Programme de Fidélité

**Menu > Selling > Loyalty Program**

Récompensez vos clients fidèles :
- Points par achat
- 1 point = 100 XOF dépensés
- Réduction ou cadeaux selon points

## 🛍️ Processus de Vente

### Vente Comptant (POS)

```
Client arrive → Scanner articles → Encaissement → Reçu
```
Le plus rapide pour boutique.

### Vente avec Facture

**Menu > Selling > Sales Invoice**

Pour clients professionnels ou à crédit :

1. **Devis** (optionnel)
   - Client demande prix
   - Créez devis avec validité 7 jours

2. **Facture Proforma** (optionnel)
   - Client veut confirmation avant paiement

3. **Facture Définitive**
   - Créez facture
   - Incluez articles, quantités, prix
   - TVA calculée automatiquement
   - Générez et imprimez

4. **Livraison** (si nécessaire)
   - Créez bon de livraison
   - Mettez à jour le stock

5. **Encaissement**
   - Immédiat ou à crédit
   - Enregistrez paiement partiel ou total

## 🔄 Gestion des Retours

### Retour Client (Avoir)

**Menu > Selling > Sales Invoice > Return**

Si client retourne produit :

1. Trouvez facture originale
2. Cliquez "Create Return/Credit Note"
3. Sélectionnez articles retournés
4. Motif du retour
5. Remboursement :
   - Espèces
   - Crédit pour prochain achat
   - Échange contre autre produit

### Retour Fournisseur

**Menu > Stock > Delivery Note > Return**

Si vous retournez marchandise défectueuse :
1. Créez note de retour
2. Stock est ajusté
3. Demandez avoir au fournisseur

## 📈 Rapports Essentiels

### Rapports Quotidiens

#### Ventes du Jour
**Selling > Sales Analytics**
- Total des ventes
- Nombre de transactions
- Ticket moyen
- Meilleures ventes

#### Encaissements
**Accounts > Payment Entry Report**
- Espèces reçues
- Mobile Money reçu
- Détail par mode de paiement

#### Clôture de Caisse
**Retail > Cashier Closing**
- Compter l'argent en caisse
- Comparer avec système
- Identifier écarts éventuels

### Rapports Hebdomadaires

#### Articles les Plus Vendus
**Stock > Stock Analytics**
- Top 20 produits
- Tendances de vente
- Prévision de réapprovisionnement

#### Stock Faible
**Stock > Stock Level**
- Articles à réapprovisionner
- Articles en rupture
- Générer bons de commande

### Rapports Mensuels

#### Analyse des Ventes
- Ventes par catégorie
- Ventes par vendeur
- Comparaison mois précédent

#### Inventaire Mensuel
- Valorisation du stock
- Rotation du stock
- Articles à faible rotation

#### Rentabilité
- Marge brute par produit
- Produits les plus rentables
- Analyse des remises accordées

## 💡 Bonnes Pratiques

### Quotidiennes
- ✅ Clôturer la caisse chaque soir
- ✅ Vérifier les paiements Mobile Money
- ✅ Sauvegarder les données
- ✅ Vérifier stock des articles populaires

### Hebdomadaires
- ✅ Réapprovisionner articles en stock faible
- ✅ Analyser les ventes de la semaine
- ✅ Vérifier les créances clients
- ✅ Nettoyer et organiser le magasin

### Mensuelles
- ✅ Inventaire physique complet
- ✅ Réconciliation bancaire
- ✅ Déclaration et paiement TVA
- ✅ Analyse de rentabilité
- ✅ Révision des prix si nécessaire

### Conseils de Gestion

1. **Rotation du Stock**
   - Méthode FIFO (Premier Entré, Premier Sorti)
   - Placez produits récents derrière
   - Surveillez dates d'expiration

2. **Merchandising**
   - Produits populaires à hauteur des yeux
   - Articles complémentaires ensemble
   - Promotions en vitrine

3. **Contrôle des Prix**
   - Vérifiez prix concurrents régulièrement
   - Ajustez selon marché
   - Promotions sur articles à rotation lente

4. **Service Client**
   - Formez vendeurs à utiliser POS
   - Rapidité de service
   - Politesse et sourire

5. **Sécurité**
   - Caméras de surveillance
   - Comptage régulier de caisse
   - Vérification quotidienne des stocks

## 🚀 Fonctionnalités Avancées

### Multi-Magasins

Si vous avez plusieurs boutiques :
- Créez un entrepôt par magasin
- Transférez stock entre magasins
- Rapports consolidés ou par magasin

### E-Commerce

Intégration possible avec :
- Boutique en ligne (WooCommerce, Shopify)
- Ventes Facebook/Instagram
- WhatsApp Business

### Programme de Parrainage

Récompensez clients qui amènent nouveaux clients :
- Bonus de parrainage
- Remise pour les deux parties

### Gestion des Employés

**Menu > HR**
- Fiches employés/vendeurs
- Horaires de travail
- Commissions sur ventes
- Évaluation des performances

## 📱 Utilisation Mobile

FasoCompta fonctionne sur :
- ✅ Smartphones Android
- ✅ Tablets
- ✅ iOS (iPhone/iPad)

Idéal pour :
- Ventes en extérieur (événements, marchés)
- Inventaire avec tablette
- Consultation des stocks

## 🆘 Problèmes Courants

### "Article non trouvé avec code-barres"
→ Vérifiez que code-barres est enregistré dans fiche article

### "Stock insuffisant"
→ Vérifiez stock disponible dans bon entrepôt
→ Faites transfert de stock si nécessaire

### "Paiement Mobile Money non confirmé"
→ Notez numéro de transaction
→ Vérifiez avec client/opérateur

### "Erreur de clôture de caisse"
→ Comptez à nouveau espèces
→ Vérifiez toutes transactions du jour
→ Identifiez transaction manquante

## 📞 Support

**Besoin d'aide ?**
- Email : contact@fasocompta.com
- Téléphone : [À compléter]
- WhatsApp : [À compléter]
- Documentation : https://github.com/mahamadoubmaiga/FasoCompta/wiki

---

**Succès à votre boutique avec FasoCompta ! 🏪**

*Fait avec ❤️ pour les commerçants ouest-africains*
