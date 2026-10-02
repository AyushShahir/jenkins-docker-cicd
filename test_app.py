import unittest

class TestApplication(unittest.TestCase):

    def test_application_message(self):
        message = "Hello from Jenkins + Docker!"
        self.assertIn("Jenkins", message)
        self.assertIn("Docker", message)

if __name__ == "__main__":
    unittest.main()