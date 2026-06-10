'''
未完成


自動更新line bot webhook url
'''
from django.core.management.commands.runserver import Command as RunserverCommand
import os

from apps.bot.utils.update_line_webhook import update_line_webhook


class Command(RunserverCommand):
    def inner_run(self, *args, **options):

        if os.environ.get("RUN_MAIN") == "true":
            print("🚀 更新LINE Webhook")
            update_line_webhook()

        super().inner_run(*args, **options)