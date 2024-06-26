from environs import Env
from dataclasses import dataclass


@dataclass
class Bots:
    bot_token: str


@dataclass
class Settings:
    bots: Bots


def get_settings(path: str):
    env = Env()
    env.read_env(path)

    return Settings(
        bots=Bots(
            bot_token=env.str("BOT_TOKEN")
        )
    )

settings = get_settings('input')
print(settings)