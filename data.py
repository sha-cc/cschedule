from dataclasses import dataclass
from pathlib import PosixPath
from json import load


@dataclass
class Data:
    GROUP: str
    url = "736572766963652e617669616b61742e7275"  # hex to prevent searching
    port = 4256
    group_codes_path = PosixPath("group_codes.json")

    @property
    def group_code(self):
        with open(self.group_codes_path, "r") as file:
            self.groups = load(file)
        for key, value in self.groups.items():
            if key.upper() == self.GROUP.upper():
                return value
        raise ValueError(f'"{self.GROUP}" is not a valid group')

    @property
    def URL(self):
        decoded_url = bytes.fromhex(self.url).decode("utf-8")
        return f"http://{decoded_url}:{self.port}/{self.group_code}.htm"
