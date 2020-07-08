import unittest
from pprint import pprint
import NoSQL

class TestMethods(unittest.TestCase):
    # Test 1
    def test_Empty_Collection(self):
        c = NoSQL.Collection()
        assert c.find_all() == []

    # Test 2
    def test_First_Insertion(self):
        c = NoSQL.Collection()
        assert c.find_all() == []

        doc_1 = {"First": "Josh", "Last": "Nahum"}
        c.insert(doc_1)
        assert c.find_all() == [doc_1]

    # Test 3
    def test_Insertion_Order(self):
        c = NoSQL.Collection()
        assert c.find_all() == []

        doc_1 = {"First": "Josh", "Last": "Nahum"}
        c.insert(doc_1)

        doc_2 = {"First": "Emily", "Last": "Dolson"}
        c.insert(doc_2)

        doc_3 = {"Pet_1": "RaceTrack", "Pet_2": "CrashDown", "happiness": True}
        c.insert(doc_3)

        assert c.find_all() == [doc_1, doc_2, doc_3]

    # Test 4
    def test_First_Find(self):
        c = NoSQL.Collection()
        
        docs = [
            {"First": "Josh", "Last": "Nahum"},
            {"First": "Emily", "Last": "Dolson"},
            {"First": "RaceTrack", "Last": "Nahum"},
            {"First": "CrashDown", "Last": "Dolson"},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        expected = [
            {"First": "Josh", "Last": "Nahum"},
            {"First": "RaceTrack", "Last": "Nahum"},
        ]

        assert c.find({"Last": "Nahum"}) == expected

    # Test 5
    def test_Find_with_Irregular_Documents(self):
        c = NoSQL.Collection()

        docs = [
            {"First": "Josh", "Last": "Nahum"},
            {"First": "Emily", "Last": "Dolson"},
            {"age": 5, "Last": "Nahum"},
            {},
            {"other": "data"},
            {"First": "RaceTrack", "Last": "Nahum"},
            {"First": "RaceTrack", "Last": "Nahum"},
            {"First": "CrashDown", "Last": "Dolson"},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        expected = [
            {"First": "Josh", "Last": "Nahum"},
            {"age": 5, "Last": "Nahum"},
            {"First": "RaceTrack", "Last": "Nahum"},
            {"First": "RaceTrack", "Last": "Nahum"},
        ]

        assert c.find({"Last": "Nahum"}) == expected

    # Test 6
    def test_Find_With_Empty_Search(self):
        c = NoSQL.Collection()

        docs = [
            {"First": "Josh", "Last": "Nahum"},
            {"First": "Emily", "Last": "Dolson"},
            {"age": 5, "Last": "Nahum"},
            {},
            {"other": "data"},
            {"First": "RaceTrack", "Last": "Nahum"},
            {"First": "RaceTrack", "Last": "Nahum"},
            {"First": "CrashDown", "Last": "Dolson"},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find({}) == docs

    # Test 7
    def test_Multiple_Collections(self):
        names = NoSQL.Collection()
        quotes = NoSQL.Collection()

        name_docs = [
        {"First": "Josh", "Last":"Nahum"},
        {"First": "Emily", "Last":"Dolson"},
        {"age": 5, "Last": "Nahum"},
        {},
        {"other": "data"},
        {"First": "RaceTrack", "Last": "Nahum"},
        {"First": "RaceTrack", "Last": "Nahum"},
        {"First": "CrashDown", "Last": "Dolson"},
        ]

        quote_docs = [
        {"Name": "Josh", "Quote":"Hello Class"},
        {"Name": "Archon", "Quote":"Power Overwhelming"},
        {"Quote":"Hello World!"},
        ]

        for doc in name_docs:
            names.insert(doc)

        for doc in quote_docs:
            quotes.insert(doc)

        assert names.find_all() == name_docs
        assert quotes.find_all() == quote_docs

    # Test 8
    def test_Nested_Documents(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "grades": {"hw1": 2, "hw2": 1.5}},
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}},
            {"student": "Charles", "grades": {}},
            {"student": "Tyler"},
            {"student": "Grant", "grades": {"hw1": 2, "hw3": 1.5}},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        expected = [
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}},
        ]

        assert c.find({"grades": {"hw2": 2}}) == expected

    # Test 9
    def test_Multiple_Criteria(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "grades": {"hw1": 2, "hw2": 1.5}, "class": 450},
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Charles", "grades": {}, "class": 480},
            {"student": "Lena", "grades": {"hw2": 2, "hw3": 1}, "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "grades": {"hw1": 2, "hw3": 1.5}, "class": 480},
            {"student": "Jane", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}, "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        expected = [
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Jane", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}, "class": 480},
        ]

        actual = c.find({"grades": {"hw2": 2}, "class": 480})

        assert actual == expected, actual

    # Test 10
    def test_No_Matches(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "grades": {"hw1": 2, "hw2": 1.5}, "class": 450},
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Charles", "grades": {}, "class": 480},
            {"student": "Lena", "grades": {"hw2": 2, "hw3": 1}, "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "grades": {"hw1": 2, "hw3": 1.5}, "class": 480},
            {"student": "Jane", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}, "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        actual = c.find({"student": "Janis"})

        assert actual == [], actual

    # Test 11
    def test_Find_One_No_Matches(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "grades": {"hw1": 2, "hw2": 1.5}, "class": 450},
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Charles", "grades": {}, "class": 480},
            {"student": "Lena", "grades": {"hw2": 2, "hw3": 1}, "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "grades": {"hw1": 2, "hw3": 1.5}, "class": 480},
            {"student": "Jane", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}, "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        actual = c.find({"student": "Janis"})

        assert actual == [], actual

    # Test 12
    def test_Find_One_Is_One(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "grades": {"hw1": 2, "hw2": 1.5}, "class": 450},
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Charles", "grades": {}, "class": 480},
            {"student": "Lena", "grades": {"hw2": 2, "hw3": 1}, "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "grades": {"hw1": 2, "hw3": 1.5}, "class": 480},
            {"student": "Jane", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}, "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        actual = c.find({"student": "Janis"})

        assert actual == [], actual

    # Test 13
    def test_Find_One_Of_Many(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "grades": {"hw1": 2, "hw2": 1.5}, "class": 480},
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Charles", "grades": {}, "class": 480},
            {"student": "Lena", "grades": {"hw2": 2, "hw3": 1}, "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "grades": {"hw1": 2, "hw3": 1.5}, "class": 480},
            {"student": "Jane", "grades": {"hw2": 2, "hw3": 1.5}, "class": 450},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}, "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        actual = c.find_one({"class": 450})

        expected = {"student": "Lena", "grades": {"hw2": 2, "hw3": 1}, "class": 450}
        assert actual == expected, actual

    # Test 14
    def test_Count(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "grades": {"hw1": 2, "hw2": 1.5}, "class": 480},
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}, "class": 480},
            {"student": "Charles", "grades": {}, "class": 480},
            {"student": "Lena", "grades": {"hw2": 2, "hw3": 1}, "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "grades": {"hw1": 2, "hw3": 1.5}, "class": 480},
            {"student": "Jane", "grades": {"hw2": 2, "hw3": 1.5}, "class": 450},
            {"student": "Chuck"},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}, "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs

        assert c.count({"class": 450}) == 2, c.count({"class": 450})
        assert c.count({"class": 480}) == 6, c.count({"class": 480})

    # Test 15
    def test_Delete_All(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "class": 480},
            {"student": "Emily", "class": 480},
            {"student": "Charles", "class": 480},
            {"student": "Lena", "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "class": 480},
            {"student": "Jane", "class": 450},
            {"student": "Chuck"},
            {"student": "Rich", "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs
        c.delete_all()
        assert c.find_all() == [], c.find_all()

    # Test 16
    def test_Delete_One(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "class": 480},
            {"student": "Emily", "class": 480},
            {"student": "Charles", "class": 480},
            {"student": "Lena", "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "class": 480},
            {"student": "Jane", "class": 450},
            {"student": "Chuck"},
            {"student": "Rich", "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs
        c.delete({"student": "Tyler"})
        expected = [
            {"student": "Josh", "class": 480},
            {"student": "Emily", "class": 480},
            {"student": "Charles", "class": 480},
            {"student": "Lena", "class": 450},
            {"student": "Grant", "class": 480},
            {"student": "Jane", "class": 450},
            {"student": "Chuck"},
            {"student": "Rich", "class": 480},
        ]

        assert c.find_all() == expected, c.find_all()

    # Test 17
    def test_Delete_Many(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "class": 480},
            {"student": "Emily", "class": 480},
            {"student": "Charles", "class": 480},
            {"student": "Lena", "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "class": 480},
            {"student": "Jane", "class": 450},
            {"student": "Chuck"},
            {"student": "Rich", "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs
        c.delete({"class": 450})
        expected = [
            {"student": "Josh", "class": 480},
            {"student": "Emily", "class": 480},
            {"student": "Charles", "class": 480},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "class": 480},
            {"student": "Chuck"},
            {"student": "Rich", "class": 480},
        ]

        assert c.find_all() == expected, c.find_all()

    # Test 18
    def test_Delete_Empty_Where(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "class": 480},
            {"student": "Emily", "class": 480},
            {"student": "Charles", "class": 480},
            {"student": "Lena", "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "class": 480},
            {"student": "Jane", "class": 450},
            {"student": "Chuck"},
            {"student": "Rich", "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs
        c.delete({})

        assert c.find_all() == [], c.find_all()

    # Test 19
    def test_Update(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "class": 480},
            {"student": "Emily", "class": 480},
            {"student": "Charles", "class": 480},
            {"student": "Lena", "class": 450},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "class": 480},
            {"student": "Jane", "class": 450},
            {"student": "Chuck"},
            {"student": "Rich", "class": 480},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs
        c.update({"class": 450}, {"cool": True})

        expected = [
            {"student": "Josh", "class": 480},
            {"student": "Emily", "class": 480},
            {"student": "Charles", "class": 480},
            {"student": "Lena", "class": 450, "cool": True},
            {"student": "Tyler", "class": 480},
            {"student": "Grant", "class": 480},
            {"student": "Jane", "class": 450, "cool": True},
            {"student": "Chuck"},
            {"student": "Rich", "class": 480},
        ]

        assert c.find_all() == expected, c.find_all()
    
    # Test 20
    def test_Map_Reduce(self):
        c = NoSQL.Collection()

        docs = [
            {'age': 4},
            {'name': 'Jim', 'age': 2},
            {'happy': 'go lucky'},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs


        def find_age(doc):
            if 'age' in doc:
                return doc['age']
            return 0


        c.map_reduce(find_age, sum)

        assert c.map_reduce(find_age, sum) == 6, c.map_reduce(find_age, sum)

    # Test 21
    def test_Map_Reduce2(self):
        c = NoSQL.Collection()

        docs = [
            {"student": "Josh", "grades": {"hw1": 2, "hw2": 1.5}},
            {"student": "Emily", "grades": {"hw2": 2, "hw3": 1.5}},
            {"student": "Charles", "grades": {}},
            {"student": "Tyler"},
            {"student": "Grant", "grades": {"hw1": 2, "hw3": 1.5}},
            {"student": "Rich", "grades": {"hw2": 2, "hw3": 1}},
        ]

        for doc in docs:
            c.insert(doc)

        assert c.find_all() == docs


        def get_total_scores(doc):
            if 'grades' in doc:
                return sum(doc["grades"].values())
            return 0


        def avg_points_awarded(total_scores):
            total_scores_list = list(total_scores)
            return sum(total_scores_list) / len(total_scores_list)


        assert c.map_reduce(get_total_scores, avg_points_awarded) == 2.25, c.map_reduce(
            get_total_scores, avg_points_awarded)
            
    
if __name__ == "__main__":
    unittest.main()
