import unittest
from logic.controls import title, subtitle, text
from logic.styles import admonitions_color_scheme
import flet as ft


class FletTest(unittest.TestCase):
    def test_title(self):
        result = title("Hello World")
        self.assertIsInstance(result, ft.Text)
        self.assertEqual(result.value, "Hello World")
        self.assertEqual(result.size, 21)
        self.assertEqual(result.weight, "bold")

    def test_subtitle(self):
        result = subtitle("Welcome", key="subtitle1")
        self.assertIsInstance(result, ft.Text)
        self.assertEqual(result.value, "Welcome")
        self.assertEqual(result.size, 17)
        self.assertEqual(result.weight, "w700")
        self.assertEqual(result.key, "subtitle1")

    def test_text(self):
        result = text("Lorem ipsum")
        self.assertIsInstance(result, ft.Text)
        self.assertEqual(result.value, "Lorem ipsum")
        self.assertEqual(result.size, 12)
        self.assertEqual(result.weight, "w400")


if __name__ == "__main__":
    unittest.main()
