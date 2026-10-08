import tempfile
import unittest
from pathlib import Path

from organizer import get_category, get_unique_destination


class TestOrganizer(unittest.TestCase):

    def test_pdf_category(self):
        file_path = Path("report.pdf")
        self.assertEqual(get_category(file_path), "PDFs")

    def test_image_category(self):
        file_path = Path("photo.jpg")
        self.assertEqual(get_category(file_path), "Images")

    def test_unknown_category(self):
        file_path = Path("file.xyz")
        self.assertEqual(get_category(file_path), "Others")

    def test_duplicate_destination(self):
        with tempfile.TemporaryDirectory() as temp_folder:
            folder = Path(temp_folder)

            original = folder / "report.pdf"
            original.write_text("first file")

            duplicate = folder / "report_1.pdf"

            result = get_unique_destination(original)

            self.assertEqual(result, folder / "report_1.pdf")

    def test_available_destination(self):
        with tempfile.TemporaryDirectory() as temp_folder:
            folder = Path(temp_folder)

            destination = folder / "new_file.pdf"

            result = get_unique_destination(destination)

            self.assertEqual(result, destination)


if __name__ == "__main__":
    unittest.main()