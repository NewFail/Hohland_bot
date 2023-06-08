import configparser
from dataclasses import dataclass


@dataclass
class DcBot:
    token: str
    api: str

@dataclass
class Config:
    Dc_bot: DcBot


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    Dc_bot = config["Dc_bot"]

    return Config(
        Dc_bot=DcBot(
            token=Dc_bot["token"],
            api=Dc_bot["api"]
        )
    )