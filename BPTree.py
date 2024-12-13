import BPTreeNode
from BPTreeNode import BPTreeNode


class BPTree:
    def __init__(self, order=3):
        self.racine = BPTreeNode(is_feuille=True)  # L'arbre commence avec une feuille vide
        self.order = order    
        
        
    def insert(self, key, value):
        root = self.racine
        if len(root.keys) == (self.order - 1):  # Split root if full
            new_racine = BPTreeNode(is_feuille=False)
            new_racine.children.append(self.racine)
            self.split_child(new_racine, 0, self.racine)
            self.racine = new_racine
        self.insert_non_full(self.racine, key, value)

    
    def insert_non_full(self, node, key, value):
        """Insert a key into a node that is not full."""
        if node.is_feuille:
            # Insert the key in the correct position
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            node.keys.insert(i, key)
            node.children.insert(i, value)  # Children store the corresponding values for leaves
        else:
            # Find the child to insert the key into
            i = len(node.keys) - 1
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (self.order - 1):  # If the child is full, split it
                self.split_child(node, i, node.children[i])
                # After the split, decide which of the two children to insert into
                if key > node.keys[i]:
                    i += 1
            self.insert_non_full(node.children[i], key, value)
    
    
    def split_child(self, parent, index, child):
        """Split a child node that is too full."""
        if not child.keys:
            raise ValueError("Cannot split a child node with an empty keys list.")
    
        # Create a new node for the split
        new_node = BPTreeNode(is_feuille=child.is_feuille)
        mid = len(child.keys) // 2
    
        # Save the middle key before modifying child.keys
        middle_key = child.keys[mid]
    
        # Move keys and children from the child node to the new node
        new_node.keys = child.keys[mid + 1:]  # Right half keys
        new_node.children = child.children[mid + 1:]  # Right half children
    
        # Adjust the original child node
        child.keys = child.keys[:mid]  # Left half keys
        child.children = child.children[:mid + 1]  # Left half children
    
        # Insert the middle key into the parent
        parent.keys.insert(index, middle_key)
        parent.children.insert(index + 1, new_node)


    
    def search(self, key):
        """Recherche une clé dans le B+Tree et renvoie sa valeur."""
        return self._search(self.racine, key)

    
    def _search(self, node, key):
        """Recherche récursive dans le noeud donné."""
        if node.is_feuille:
            if key in node.keys:
                index = node.keys.index(key)
                return node.children[index]
            return None
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            return self._search(node.children[i], key)