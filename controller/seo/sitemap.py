import pathlib
import xml.etree.ElementTree as et

from typing import List


class Sitemap(List[str]):
    def save_to_xml(self, filename: pathlib.Path) -> None:
        root = et.Element('urlset')
        root.set('xmlns', "http://www.sitemaps.org/schemas/sitemap/0.9")

        for url in self:
            url_element = et.SubElement(root, 'url')
            loc_element = et.SubElement(url_element, 'loc')
            loc_element.text = url

        tree = et.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
