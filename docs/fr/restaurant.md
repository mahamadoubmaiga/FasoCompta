# Guide Restaurant - FasoCompta

## Configuration pour Restaurants et Établissements de Restauration

Ce guide est conçu pour les restaurants, maquis, fast-foods, cafétérias, et tous établissements de restauration en Afrique de l'Ouest.

## 🍽️ Configuration Initiale

### 1. Informations de Base

**Menu > Setup > Company**

- **Nom** : Nom de votre restaurant
- **Type** : Restaurant/Food & Beverage
- **Pays** : Mali, Sénégal, Côte d'Ivoire, etc.
- **Devise** : XOF (Franc CFA)
- **IFU/NIF** : Numéro d'identification fiscale
- **Licence Restaurant** : Numéro de licence sanitaire

### 2. Configuration du Point de Vente

**Menu > Retail > POS Profile > New**

#### Paramètres Restaurant
- **Nom** : "POS Restaurant"
- **Type** : Restaurant
- **Devise** : XOF
- **Entrepôt** : Cuisine/Stock
- **Impression** : Ticket de caisse + Bon de cuisine

#### Modes de Paiement
- ✅ Espèces
- ✅ Orange Money
- ✅ Moov Money
- ✅ Wave
- ✅ Carte Bancaire
- ✅ Chèque Restaurant (si applicable)

#### Options Spéciales
- ✅ Frais de Service (10% standard)
- ✅ Service à Table
- ✅ Impression séparée cuisine/bar
- ✅ Gestion des tables

### 3. Configuration des Tables

**Menu > Restaurant > Tables > New**

Créez vos tables et zones :

#### Zones du Restaurant
- **Intérieur** : Tables 1-20
- **Terrasse** : Tables 21-30
- **VIP/Salon** : Tables 31-35
- **Bar** : Tabourets B1-B10
- **Livraison/Emporter** : Table virtuelle "T-GO"

Pour chaque table :
- Numéro de table
- Zone
- Capacité (nombre de places)
- Statut : Disponible/Occupée/Réservée

## 📋 Le Menu

### Structure du Menu

**Menu > Stock > Item Group**

Organisez votre menu :

#### Catégories Principales
- 🥗 Entrées & Salades
- 🍲 Soupes
- 🍖 Plats Principaux
  - Viandes
  - Poissons
  - Poulet
  - Plats Végétariens
- 🍚 Accompagnements
  - Riz
  - Attiéké
  - Foutou
  - Frites
  - Aloco
- 🍰 Desserts
- ☕ Boissons
  - Boissons Froides
  - Boissons Chaudes
  - Jus Naturels
  - Boissons Alcoolisées

### Créer un Plat

**Menu > Stock > Item > New**

Pour chaque plat du menu :

#### Informations de Base
- **Code** : Ex. PLT001
- **Nom** : Poulet Braisé
- **Catégorie** : Plats Principaux > Poulet
- **Prix de Vente** : 3,500 XOF
- **Unité** : Portion

#### Détails Restaurant
- ✅ **Est un Article du Menu**
- **Catégorie Menu** : Plats Principaux
- **Temps de Préparation** : 20 minutes
- **Disponible** : Déjeuner et Dîner
- **Photo** : Image du plat (pour POS)

#### Options
- **Allergènes** : Arachides, Gluten, etc.
- **Niveau de Piquant** : Doux, Moyen, Fort
- **Options Végétariennes** : Oui/Non
- **Origine** : Malienne, Sénégalaise, Ivoirienne, etc.

### Variantes de Plats

Pour plats avec options :

**Exemple : Poulet Grillé**
- Poulet Entier
- Demi-Poulet
- Quart de Poulet

**Exemple : Boisson**
- Petite (33cl)
- Moyenne (50cl)
- Grande (1L)

## 👨‍🍳 Gestion de la Cuisine

### Nomenclature (Recettes)

**Menu > Stock > BOM (Bill of Materials)**

Pour chaque plat, créez sa recette :

#### Exemple : Riz Gras (10 portions)

**Ingrédients :**
- Riz : 2 kg
- Viande : 1 kg
- Tomates : 500g
- Oignons : 300g
- Huile : 200ml
- Concentré tomate : 100g
- Épices : 50g

**Coût Total** : 8,000 XOF  
**Coût par Portion** : 800 XOF  
**Prix de Vente** : 2,000 XOF  
**Marge** : 1,200 XOF (60%)

### Bons de Cuisine

**Configuration > Print Format > Kitchen Order**

Quand commande est prise :
1. Impression automatique en cuisine
2. Séparation cuisine/bar si nécessaire
3. Affichage temps de préparation
4. Ordre de préparation des plats

### Stations de Travail

Organisez la cuisine :
- **Station Grillade** : Viandes, poulet
- **Station Friture** : Frites, aloco, beignets
- **Station Sauce** : Soupes, sauces
- **Station Froide** : Salades, entrées
- **Bar** : Boissons

## 🎫 Processus de Service

### Service à Table

#### 1. Arrivée des Clients

**Menu > Restaurant > Open Table**

- Sélectionnez table disponible
- Nombre de couverts
- Nom client (optionnel)
- Serveur assigné

#### 2. Prise de Commande

**POS > Select Table**

Le serveur :
1. Sélectionne la table
2. Ajoute les plats commandés
3. Note instructions spéciales
   - "Sans piment"
   - "Bien cuit"
   - "Sauce à part"
4. Envoie en cuisine
   - Bon imprimé automatiquement
   - Notification cuisine si écran

#### 3. Service des Plats

En cuisine :
- Plats préparés selon ordre
- Marqués "Prêts"
- Serveur averti

Serveur :
- Récupère plats prêts
- Sert les clients
- Marque "Servi" dans système

#### 4. Commandes Additionnelles

Client commande dessert/boisson :
- Rouvrir la table dans POS
- Ajouter nouveaux articles
- Envoyer à cuisine/bar

#### 5. Encaissement

**POS > Close Table**

1. Vérifier total
2. Appliquer frais de service (10%)
3. Choisir mode de paiement
4. Imprimer facture
5. Remettre monnaie si espèces
6. Libérer la table

### Service Emporter/Livraison

**POS > Takeaway**

1. Sélectionner "Emporter" ou "Livraison"
2. Nom et téléphone client
3. Adresse (si livraison)
4. Prendre commande
5. Temps de préparation estimé
6. Encaissement
7. Préparer emballage

## 📱 Réservations

### Créer une Réservation

**Menu > Restaurant > Reservation > New**

Informations :
- **Date et Heure**
- **Nombre de Personnes**
- **Nom Client**
- **Téléphone**
- **Table Préférée**
- **Occasion Spéciale** (anniversaire, etc.)
- **Notes** (allergies, préférences)

### Gérer les Réservations

Vue du jour :
- Réservations confirmées
- Tables disponibles
- Planification du service

Rappels :
- SMS/WhatsApp 24h avant
- Confirmation client

## 💰 Tarification Restaurant

### Prix Standard

Menu avec prix fixes :
- Entrée : 1,500 - 3,000 XOF
- Plat Principal : 3,000 - 8,000 XOF
- Dessert : 1,000 - 2,500 XOF
- Boissons : 500 - 3,000 XOF

### Menus Formules

**Menu > Selling > Pricing Rule**

#### Formule Déjeuner
**12h-15h : 5,000 XOF**
- 1 Entrée au choix
- 1 Plat principal au choix
- 1 Boisson incluse

#### Menu Découverte
**8,000 XOF**
- Entrée + Plat + Dessert + Boisson

#### Menu Groupe (10+ personnes)
- Remise 15%
- Réservation obligatoire

### Happy Hour

**Menu > Promotions**

Example : Boissons -30%
- Horaire : 18h-20h
- Jours : Lundi-Jeudi
- Boissons sélectionnées

### Frais de Service

Standard : 10% du total
- Appliqué automatiquement
- Mentionné sur facture
- Optionnel selon pays

## 📦 Gestion des Stocks

### Catégories de Stock

#### Ingrédients Frais
- Viandes, poissons
- Légumes, fruits
- Produits laitiers
- **Rotation** : Quotidienne
- **Contrôle** : Strict (DLC)

#### Ingrédients Secs
- Riz, pâtes, farine
- Conserves
- Épices
- **Rotation** : Hebdomadaire/Mensuelle

#### Boissons
- Boissons gazeuses
- Bières
- Vins et spiritueux
- Jus, eau
- **Rotation** : Hebdomadaire

#### Consommables
- Emballages
- Serviettes
- Couverts jetables
- Sacs

### Réception de Marchandises

**Menu > Stock > Purchase Receipt**

Chaque matin/livraison :
1. Vérifier la commande
2. Contrôler qualité
   - Viandes : fraîcheur, couleur
   - Légumes : état, fermeté
   - Dates d'expiration
3. Peser/Compter
4. Enregistrer réception
5. Stocker selon zones :
   - Frigo : 0-4°C
   - Congélateur : -18°C
   - Sec : Température ambiante

### Inventaire Quotidien

**Menu > Stock > Stock Reconciliation**

#### Matin (Ouverture)
Vérifier :
- Viandes/poissons
- Légumes frais
- Pain
- Boissons froides

Anticiper :
- Besoins du service
- Commandes urgentes

#### Soir (Fermeture)
Compter :
- Restes utilisables
- Produits à écouler rapidement
- Ruptures de stock

### Gaspillage

**Menu > Stock > Stock Entry > Material Issue**

Enregistrer :
- Aliments périmés
- Casse
- Erreurs de préparation

Analyser mensuellement pour réduire pertes.

### Niveau de Stock Optimal

Articles critiques :
- **Stock Mini** : Pour 2 jours
- **Stock Maxi** : Pour 1 semaine (frais)
- **Stock Maxi** : Pour 1 mois (secs)

Alertes automatiques réapprovisionnement.

## 👥 Gestion du Personnel

### Équipe Restaurant

**Menu > HR > Employee**

#### Postes
- Chef de cuisine
- Cuisiniers
- Commis de cuisine
- Serveurs
- Barmans
- Plongeurs
- Caissier
- Gérant

#### Informations Employé
- Données personnelles
- Numéro CNSS
- Poste et département
- Horaires de travail
- Salaire

### Horaires et Présence

**Menu > HR > Attendance**

#### Services
- **Service Déjeuner** : 11h-15h
- **Service Dîner** : 18h-23h
- **Équipe Matin** : 8h-16h
- **Équipe Soir** : 16h-00h

Planning :
- Rotation des équipes
- Jours de repos
- Gestion des congés

### Performance des Serveurs

**Rapports > HR > Employee Performance**

Suivez :
- Nombre de tables servies
- Montant des ventes
- Erreurs de commande
- Satisfaction clients
- Commissions (si applicable)

### Paie

**Menu > HR > Payroll**

Composantes :
- **Salaire de base**
- **Prime de service** (part des frais de service)
- **Heures supplémentaires**
- **Prime de nuit** (si service tardif)
- **Pourboires** (optionnel)
- **Cotisations CNSS** : -3.6%

## 📊 Rapports Restaurant

### Rapports Quotidiens

#### 1. Ventes du Jour
**Selling > Daily Sales Report**
- Total des ventes
- Nombre de couverts
- Ticket moyen
- Répartition déjeuner/dîner

#### 2. Plats Vendus
**Stock > Sales Analytics**
- Plats les plus vendus
- Plats non vendus (à retirer du menu?)
- Tendances

#### 3. Clôture de Caisse
**Retail > Cashier Closing**
- Espèces
- Mobile Money
- Cartes bancaires
- Écarts éventuels

#### 4. Réservations du Lendemain
**Restaurant > Reservations**
- Nombre de couverts prévus
- Tables assignées
- Préparation nécessaire

### Rapports Hebdomadaires

#### Performance du Menu
- Top 10 plats
- Plats à rotation lente
- Analyse des marges

#### Stock Utilisé
- Consommation ingrédients
- Coût matières par jour
- Ratio coût matières/ventes (idéal : 30-35%)

#### Performance Serveurs
- Ventes par serveur
- Nombre de tables
- Satisfaction clients

### Rapports Mensuels

#### Compte d'Exploitation
- Chiffre d'affaires
- Coût matières
- Coût personnel
- Charges diverses
- Résultat net

#### Analyse Financière
- **Ratio Coût Matières** : 30-35%
- **Ratio Personnel** : 25-30%
- **Autres Charges** : 20-25%
- **Bénéfice Net** : 15-20%

#### Inventaire Complet
- Valeur du stock
- Rotation du stock
- Gaspillage
- Optimisations possibles

## 💡 Bonnes Pratiques

### Gestion Quotidienne

✅ **Matin**
- Vérifier réservations du jour
- Contrôler stocks et livraisons
- Préparer mise en place
- Brief avec l'équipe

✅ **Service**
- Accueil chaleureux
- Service rapide et efficace
- Communication cuisine-salle
- Gestion des réclamations

✅ **Soir**
- Clôture caisse
- Nettoyage complet
- Inventaire rapide
- Préparation lendemain

### Qualité et Hygiène

✅ **Cuisine**
- Respect chaîne du froid
- Lavage des mains fréquent
- Désinfection surfaces
- Contrôle températures
- Séparation cru/cuit

✅ **Salle**
- Tables propres
- Vaisselle impeccable
- Toilettes propres
- Climatisation fonctionnelle

✅ **Contrôles**
- Dates de péremption
- Température frigos
- Hygiène du personnel
- État des équipements

### Service Client

✅ **Accueil**
- Sourire et politesse
- Temps d'attente raisonnable
- Information sur attente si nécessaire

✅ **Pendant le Repas**
- Vérifier satisfaction
- Réactivité aux demandes
- Discrétion

✅ **Départ**
- Remerciements
- Invitation à revenir
- Gestion des remarques

### Gestion Financière

✅ **Quotidien**
- Suivre trésorerie
- Vérifier paiements Mobile Money
- Contrôler caisse

✅ **Hebdomadaire**
- Payer fournisseurs
- Analyser marges
- Ajuster achats

✅ **Mensuel**
- Déclaration TVA
- Paie du personnel
- Analyse de rentabilité
- Révision des prix si nécessaire

## 🚀 Fonctionnalités Avancées

### Commande en Ligne

Intégration possible :
- Site web restaurant
- Application mobile
- WhatsApp Business
- Commande par téléphone enregistrée

### Livraison à Domicile

**Menu > Delivery Management**
- Zone de livraison
- Frais de livraison
- Livreurs assignés
- Suivi GPS (optionnel)
- Temps de livraison estimé

### Programme Fidélité

**Menu > Loyalty Program**
- Carte de fidélité
- Points par visite
- Réductions fidélité
- Menu anniversaire offert

### Carte Digital

Affichage sur écran :
- Menu du jour
- Prix
- Photos des plats
- Mise à jour en temps réel

### WiFi Gratuit

Pour clients :
- Code WiFi sur ticket
- Récupération emails (marketing)

## 🆘 Problèmes Courants

### "Plat non disponible"
→ Mettre à jour menu en temps réel
→ Former serveurs à proposer alternatives

### "Commande en retard"
→ Vérifier organisation cuisine
→ Améliorer communication
→ S'excuser auprès du client

### "Erreur dans commande"
→ Relecture avant envoi cuisine
→ Formation serveurs
→ Correction immédiate et excuses

### "Réclamation client"
→ Écouter attentivement
→ S'excuser sincèrement
→ Proposer solution (remise, plat offert)
→ Enregistrer pour éviter répétition

## 📞 Support

**Besoin d'aide ?**
- Email : contact@fasocompta.com
- Documentation : https://github.com/mahamadoubmaiga/FasoCompta/wiki

---

**Succès à votre restaurant avec FasoCompta ! 🍽️**

*Fait avec ❤️ pour les restaurateurs ouest-africains*
