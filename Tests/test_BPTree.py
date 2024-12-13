import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from BPTree import BPTree
from DatabasePrime import Database

db = Database("children.db")
db.tables["MaTable"] = [
    {"Nom": "Alice", "Age": 25},
    {"Nom": "Bob", "Age": 30},
    {"Nom": "Charlie", "Age": 20}
]

db.create_index("MaTable", "Nom", order=3)


