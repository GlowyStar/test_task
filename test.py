import unittest
from main import Directory

class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.directory = Directory('test_directory.json')
        self.directory.entries = []

    def test_load_entries(self):
        entries = self.directory.load_entries()
        self.assertIsInstance(entries, list)

    def test_add_entry(self):
        entry = {
            'last_name': 'Иванов',
            'first_name': 'Иван',
            'patronymic': 'Иванович',
            'organization': 'ООО "Рога и копыта"',
            'work_phone': '8(999) 999-99-99',
            'personal_phone': '8(888) 888-88-88'
        }
        self.directory.add_entry(entry)
        self.assertEqual(self.directory.entries[-1], entry)

    def test_edit_entry(self):
        entry = {
            'last_name': 'Иванов',
            'first_name': 'Иван',
            'patronymic': 'Иванович',
            'organization': 'ООО "Рога и копыта"',
            'work_phone': '8(999) 999-99-99',
            'personal_phone': '8(888) 888-88-88'
        }
        self.directory.add_entry(entry)
        id_of_added_entry = self.directory.entries[-1]['id']
        new_entry = {
            'last_name': 'Петров',
            'first_name': 'Петр',
            'patronymic': 'Петрович',
            'organization': 'ООО "Копыта и рога"',
            'work_phone': '8(777) 777-77-77',
            'personal_phone': '8(666) 666-66-66'
        }
        new_entry['id'] = id_of_added_entry
        self.directory.edit_entry(id_of_added_entry, new_entry)
        self.assertEqual(self.directory.entries[-1], new_entry)

    def test_search_entries(self):
        entry = {
            'last_name': 'Петров',
            'first_name': 'Петр',
            'patronymic': 'Петрович',
            'organization': 'ООО "Копыта и рога"',
            'work_phone': '8(777) 777-77-77',
            'personal_phone': '8(666) 666-66-66'
        }
        self.directory.add_entry(entry)
        search_terms = {'last_name': 'Петров'}
        results = self.directory.search_entries(search_terms)
        self.assertEqual(results, [self.directory.entries[0]])

    def test_save_entries(self):
        entries = self.directory.entries
        self.directory.save_entries()
        self.directory.entries = []
        self.directory.load_entries()
        self.assertEqual(entries, self.directory.entries)

if __name__ == '__main__':
    unittest.main()
