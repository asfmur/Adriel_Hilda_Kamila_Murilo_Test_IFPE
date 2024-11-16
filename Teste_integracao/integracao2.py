import unittest
import sqlite3

class Test(unittest.TestCase):

    def setUp(self):

        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()
        self.cursor.execute("CREATE TABLE predios (id INTEGER PRIMARY KEY, enderecos TEXT)")

    def test_inserir_endereco(self):
            
        self.cursor.execute("INSERT INTO predios (enderecos) VALUES ('Rua Sao Pedro')")
        self.conn.commit()

        self.cursor.execute("SELECT enderecos FROM predios WHERE id = 1")
        endereco = self.cursor.fetchone()
        self.assertEqual(endereco[0], 'Rua Sao Pedro')


    def tearDown(self):
        return super().tearDown()

    
if __name__ == '__main__':
    unittest.main()
