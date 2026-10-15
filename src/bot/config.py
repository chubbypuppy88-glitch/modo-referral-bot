import os


class Config(object):
    LOGGER = True

    DATABASE_URI = os.environ["DATABASE_URL"].replace(
        "postgres://", "postgresql://", 1
    )

    LOG_CHANNEL = int(os.environ["LOG_CHANNEL"])

    SUDO_USERS = [
        int(value.strip())
        for value in os.environ["SUDO_USERS"].split(",")
        if value.strip()
    ]

    BOT_TOKEN = os.environ["BOT_TOKEN"]

    WORKERS = 8

    SUPPORT_CHANNEL = (
        os.environ["SUPPORT_CHANNEL"].strip().lstrip("@")
    )

    REFERRAL_LINK = "https://modo.us/?referralCode=WP26NV"
