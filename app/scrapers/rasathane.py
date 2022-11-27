import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import json
from datetime import datetime

SOURCE_URL = "http://www.koeri.boun.edu.tr/scripts/lst9.asp"


def get_json_data():
    """Return a list of JSON objects

    Returns:
        list: List of JSON objects
    """
    ###### get data ######
    res = requests.get(SOURCE_URL)

    bs = BeautifulSoup(res.text, "html.parser")

    ###### clean response text ######
    pre = bs.find("pre").text

    table_content = pre.split("Büyüklük")[1]

    table_content = BeautifulSoup(table_content, "html.parser").text
    table_content = str(table_content).strip().split("--------------")[2]

    table_content = table_content.split("\n")
    table_content.pop(0)
    table_content.pop()
    table_content.pop()

    scraped_data = []

    for index in range(len(table_content)):
        element = str(table_content[index].rstrip())
        element = re.sub(r"\s\s\s", " ", element)
        element = re.sub(r"\s\s\s\s", " ", element)
        element = re.sub(r"\s\s", " ", element)
        element = re.sub(r"\s\s", " ", element)
        Args = element.split(" ")
        location = (
            Args[8]
            + element.split(Args[8])[len(element.split(Args[8])) - 1]
            .split("İlksel")[0]
            .split("REVIZE")[0]
        )
        json_table_content = json.dumps(
            {
                "id": index + 1,
                "date": Args[0],
                "time": Args[1],
                "datetime": Args[0] + " " + Args[1],
                "timestamp": int(
                    datetime.strptime(
                        Args[0] + " " + Args[1], "%Y.%m.%d %H:%M:%S"
                    ).timestamp()
                ),
                "latitude": float(Args[2]),
                "longitude": float(Args[3]),
                "depth": float(Args[4]),
                "size_md": float(Args[5].replace("-.-", "0")),
                "size_ml": float(Args[6].replace("-.-", "0")),
                "size_mw": float(Args[7].replace("-.-", "0")),
                "location": location.strip(),
            },
            sort_keys=False,
        )

        scraped_data.append(json.loads(json_table_content))
    return scraped_data
