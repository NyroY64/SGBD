from BPTree import BPTree
from BPTreeNode import BPTreeNode

class Database:

    def __init__(self, name):
        self.name = name
        # Dictionnaire pour stocker les tables
        # Clé : Nom de la table, Valeur : Instance de la classe Relation
        self.tables = {}
        self.indexes = {}  # Stores indexes for each table



     # Getter pour le nom de la base de données
    def get_name(self):
        return self.name

    # Setter pour le nom de la base de données
    def set_name(self, name):
        if not name:
            raise ValueError("Le nom de la base de données ne peut pas être vide.")
        self.name = name

    # Getter pour les tables
    def get_tables(self):
        return self.tables

    # Setter pour les tables (rarement utilisé, mais disponible si nécessaire)
    def set_tables(self, tables):
        if not isinstance(tables, dict):
            raise ValueError("Les tables doivent être un dictionnaire.")
        self.tables = tables
        
        
    def create_index(self, table_name, column_name, order):
       """Crée un index B+Tree pour une table sur une colonne donnée."""
       if table_name not in self.tables:
           raise ValueError(f"La table {table_name} n'existe pas.")
       if table_name not in self.indexes:
           self.indexes[table_name] = {}
       # Créer un B+Tree et insérer toutes les clés existantes
       tree = BPTree(order=order)
       for row_id, record in enumerate(self.tables[table_name]):
           key = record[column_name]
           tree.insert(key, row_id)  # Associer la clé à l'ID du record
       self.indexes[table_name][column_name] = tree
       print(f"Index créé sur {table_name}.{column_name} avec ordre {order}.")
       
    def get_index(self, table_name, column_name):
        if table_name in self.indexes and column_name in self.indexes[table_name]:
            return self.indexes[table_name][column_name]
        raise ValueError(f"Index introuvable pour {table_name}.{column_name}.")