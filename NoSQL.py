"""
Name: Don Nakashima

Comments: 
Simple Document Storage System

Sources: JSON library
"""

import json

class Collection:
    """
    A list of dictionaries (documents) accessible in a DB-like way.
    """

    def __init__(self, documents = None):
        """
        Initialize an empty collection.
        """
        if documents == None:
            documents = []
            
        self.documents = documents

    def insert(self, document):
        """
        Add a new document (a.k.a. python dict) to the collection.
        """
        self.documents.append(document)
        
    def check(self, doc, where_dict):
        """
        Check the list of documents
        """
        for k in where_dict:
            if k not in doc:
                return False
            else:
                if type(doc[k]) == dict:
                    if not self.check(doc[k], where_dict[k]):
                        return False
                elif doc[k] != where_dict[k]:
                    return False

        return True

    def find_all(self):
        """
        Return list of all docs in database.
        """
        return self.documents

    def find_one(self, where_dict):
        """
        Return the first matching doc.
        If none is found, return None.
        """
        for doc in self.documents:
            if self.check(doc, where_dict):
                return doc

    def find(self, where_dict):
        """
        Return matching list of matching doc(s).
        """
        matches = []
        
        for doc in self.documents:
            if self.check(doc, where_dict):
                matches.append(doc)
                
        return matches

    def count(self, where_dict):
        """
        Return the number of matching docs.
        """
        total_count = 0
        
        for doc in self.documents:
            if self.check(doc, where_dict):
                total_count += 1
                
        return total_count
    
    def delete_all(self):
        """
        Truncate the collection.
        """
        self.documents.clear()

    def delete(self, where_dict):
        """
        Delete matching doc(s) from the collection.
        """
        temp_list = self.find(where_dict)
        
        for doc in temp_list:
            self.documents.remove(doc)
        
    def update(self, where_dict, changes_dict):
        """
        Update matching doc(s) with the values provided.
        """
        temp_list = self.find(where_dict)
        c = changes_dict
        
        for doc in temp_list:
            for k in c:
                doc[k] = c[k]
  

    def map_reduce(self, map_function, reduce_function):
        """
        Applies a map_function to each document, collating the results.
        Then applies a reduce function to the set, returning the result.
        """
        map_list = []
        
        for doc in self.documents:
            map_list.append(map_function(doc))
            
        r = reduce_function(map_list)
        
        return r


class Database:
    """
    Dictionary-like object containing one or more named collections.
    """

    def __init__(self, filename):
        """
        Initialize the underlying database. If filename contains data, load it.
        """
        self.collections = {}


        try:
            self.fp = open(filename)
            contents = json.load(self.fp)
            
            for name in contents:
                temp = contents[name]
                self.collections[name] = Collection(temp)

            self.fp.close()
                
        except:
            self.fp = open(filename, "w")
            

    def get_collection(self, name):
        """
        Create a collection (if new) in the DB and return it.
        """
        if name not in self.collections:
            self.collections[name] = Collection()
        
        return self.collections[name]

    def drop_collection(self, name):
        """
        Drop the specified collection from the database.
        """
        if name in self.collections:
            del self.collections[name]

    def get_names_of_collections(self):
        """
        Return a list of the sorted names of the collections in the database.
        """
        sorted_list = sorted(self.collections.keys())
        
        return sorted_list

    def close(self):
        """
        Save and close file.
        """
        contents = {}
        
        for name in self.collections:
            contents[name] = self.collections[name].find_all()
            
        json.dump(contents, self.fp)
        
        self.fp.close()
