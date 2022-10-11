import requests
import re
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup
from data import Data

GROUP = "ИП-31"  # remove this


def connect(group: str):
    url = Data(group).URL

    try:
        request = requests.get(url)
        request.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception:
        raise ConnectionError(f"Cannot connect to {url}")

    soup = BeautifulSoup(request.content, "html.parser")

    return soup


def date_check(returned_date: str):
    if Data.date("today") == returned_date:
        print(f"{returned_date} (today) - ok")
    elif Data.date("tomorrow") == returned_date:
        print(f"{returned_date} (tomorrow) - ok")


def main(group: str):

    soup = connect(group)  # returned bs class instance (assuming there was no error)

    for element in soup.find_all(class_="hd"):
        result = re.search("[0-9]{2}.[0-9]{2}.[0-9]{4}", element.text)
        if bool(result):
            date_payload = result.group()
            break

    date_check(date_payload)  # check if the first date is today or tomorrow


if __name__ == "__main__":
    main(GROUP)
