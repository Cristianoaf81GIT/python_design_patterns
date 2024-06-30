from typing import List
from imageeditor import ImageEditor  # pyright: ignore
from interfaces import Graphic  # pyright: ignore
from implementations import Circle, Dot  # pyright:ignore


def main() -> None:
    editor = ImageEditor()
    editor.load()

    components: List[Graphic] = []

    dot_component = Dot(x=2, y=4)
    circle_component = Circle(x=3, y=5, radius=15.2)

    components.extend([dot_component, circle_component])

    editor.group_selected(components=components)


if __name__ == "__main__":
    main()
