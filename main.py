from os import getenv

from dotenv import load_dotenv

from utils.client import MyBot

load_dotenv(override=True)


if __name__ == "__main__":
    client: MyBot = MyBot()
    client.run(getenv("TOKEN"))
