import pathlib
import os
import logging

from .say import Say
from .sentry import Sentry

from redbot.core.data_manager import cog_data_path
from redbot.core import Config


def create_cache(path: pathlib.Path):
    if not path.exists():
        return
    directories = [x for x in path.iterdir() if x.is_dir()]
    if (path / "cache") not in directories:
        (path / "cache").mkdir()


def setup(bot):
    n = Say(bot)
    create_cache(cog_data_path(n))
    bot.add_cog(n)
