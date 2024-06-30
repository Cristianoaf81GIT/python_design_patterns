from adapters import XmlAdapter  # pyright: ignore
from clients import JsonClient  # pyright: ignore


def main() -> None:
    xml_adapter = XmlAdapter(xml_path="./country_data.xml")
    json_client = JsonClient(adapter=xml_adapter)
    json_client.exec_operation()


if __name__ == "__main__":
    main()
