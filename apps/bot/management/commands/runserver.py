from django.core.management.commands.runserver import Command as RunserverCommand
import os

from apps.bot.utils.update_line_webhook import update_line_webhook

print(">>> 自訂 runserver 已載入 <<<")

class Command(RunserverCommand):

    def inner_run(self, *args, **options):

        if os.environ.get("RUN_MAIN") == "true":
            update_line_webhook()

        super().inner_run(*args, **options)