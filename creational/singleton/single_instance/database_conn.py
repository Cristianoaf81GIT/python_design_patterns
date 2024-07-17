from typing import Self


class DatabaseConn:

    _user: str
    _pass: str
    _url: str
    _instance: Self | None = None

    def __new__(cls, user: str, password: str, url: str) -> Self:
        if cls._instance is None:
            cls._user = user
            cls._pass = password
            cls._url = url
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_connection_info(self) -> None:
        print(f"connect to server: {self._url}")
