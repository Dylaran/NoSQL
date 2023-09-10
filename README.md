# NoSQL

Implementation of a Document Store, a type of database with no schema

### Collection Class
| Function | Purpose |
| --- | --- |
| \_\_init\_\_(self) | Initializes a collection |
| insert(self, document) | Takes a document as a python dictionary and adds it to the collection |
| find_all(self) | Returns a list of all documents stored in the collection by insertion order |
| delete_all(self) | Removes all the documents stored in the collection |
| find_one(self, where_dict) | Returns the first document (in insertion order) that matches the where_dict |
| find(self, where_dict) | Returns all the documents (in insertion order) that matches the where_dict. Returns empty list if no matches found |
| count(self, where_dict) | Returns the number of documents that matches the where_dict |
| delete(self, where_dict) | Removes the documents that matches the where_dict |
| update(self, where_dict, changes_dict) | Adds/updates the documents that match the where_dict with changes_dict |
| map_reduce(self, map_function, reduce_function) | Takes two arguments that are both functions and applies the map function to each document, saving each result to a list that is passed to the reduce function |

---------------------------------------------------

### Database Class
| Function | Purpose |
| --- | --- |
| \_\_init\_\_(self, filename) | Takes a filename where the database will store its information |
| get_collection(self, name) | Returns a Collection instance associated with the name. If no collection exists, creates an empty one and returns it |
| get_names_of_collections(self) | Returns a list of sorted names of collections in the database |
| drop_collection(self, name) | Removes the collection associated with the name from the database |
| close(self) | Saves the information of the database to the file |
