from single_instance import DatabaseConn  # pyright: ignore


def main() -> None:
    database_instance1 = DatabaseConn(
        user="jhon", password="123", url="https://localhost:5432"
    )

    database_instance2 = DatabaseConn(
        # try overwrites the parameters, but not works
        user="francis",
        password="123",
        url="https://localhost:5432",
    )

    print(f"{database_instance1.get_connection_info()}")
    print(f"{database_instance2.get_connection_info()}")

    if id(database_instance1) == id(database_instance2):
        print("the instances are the same")
    else:
        print("the instances are different")


if __name__ == "__main__":
    main()
