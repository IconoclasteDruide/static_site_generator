import unittest

from src.extract_markdown_links import extract_markdown_images, extract_markdown_links

class TestMDExtract(unittest.TestCase):
    def test_image_extract(self):
        test_text = "Super cool ![image](mypng.png)"
        links = extract_markdown_images(test_text)
        self.assertEqual(links, [('image', 'mypng.png')])

    def test_link_extract(self):
        test_text = "Super cool ![link](accordancebible.com)"
        links = extract_markdown_images(test_text)
        self.assertEqual(links, [('link', 'accordancebible.com')])

    def test_multi_image_extract(self):
        test_text = "Super cool ![image](mypng.png) and here’s another ![one](myotherpng.png)"
        links = extract_markdown_images(test_text)
        self.assertEqual(links, [('image', 'mypng.png'), ('one', 'myotherpng.png')])

    def test_multi_link_extract(self):
        test_text = "Super cool [link](accordancebible.com) and here’s another [one](bible.disciple)"
        links = extract_markdown_links(test_text)
        self.assertEqual(links, [('link', 'accordancebible.com'), ('one', 'bible.disciple')])

    def test_not_link_extract(self):
        test_text = "This is actually an ![image](image.png)"
        links = extract_markdown_links(test_text)
        self.assertEqual(links, [])



if __name__ == "__main__":
    unittest.main()