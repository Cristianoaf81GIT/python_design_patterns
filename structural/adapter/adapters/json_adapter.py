from interfaces import AdapterInterface  # pyright: ignore
import xml.etree.ElementTree as elmTree
from json import dumps


class XmlAdapter(AdapterInterface):

    _xml_path: str

    def __init__(self, xml_path: str) -> None:
        self._xml_path = xml_path

    def exec_operation(self) -> None:
        elements = {}
        tree = elmTree.parse(self._xml_path)
        root = tree.getroot()
        for country in root.findall("country"):
            elements[country.get("name", "")] = {
                "rank": country.find("rank").text or "",  # pyright: ignore
                "year": country.find("year").text or "",  # pyright: ignore
                "neighbor": country.find("neighbor").get(  # pyright: ignore
                    "name", ""
                )  # noqa
                or "",
                "gdppc": country.find("gdppc").text or "",  # pyright: ignore
            }

        print(dumps(elements, ensure_ascii=False).encode("utf8"))
