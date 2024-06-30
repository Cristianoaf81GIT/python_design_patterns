from clients import Forest  # pyright: ignore


def main() -> None:
    forest: Forest = Forest()
    forest.plant_tree(
        x=8, y=8, name="apple_tree", color="red", texture="apple_tree.png"
    )
    forest.plant_tree(
        x=12, y=12, name="banana_tree", color="yellow", texture="banana_tree.png"
    )
    forest.plant_tree(
        x=24, y=24, name="common_tree", color="brown", texture="common_tree.png"
    )
    forest.plant_tree(
        x=16, y=16, name="apple_tree", color="red", texture="apple_tree.png"
    )
    forest.plant_tree(
        x=32, y=32, name="banana_tree", color="yellow", texture="banana_tree.png"
    )
    forest.plant_tree(
        x=64, y=64, name="common_tree", color="brown", texture="common_tree.png"
    )


if __name__ == "__main__":
    main()
