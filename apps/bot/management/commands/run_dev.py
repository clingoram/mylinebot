import os
from django.core.management.commands.runserver import Command as RunserverCommand
# from django.core.management import call_command
from apps.bot.utils.update_line_webhook import update_line_webhook

class Command(RunserverCommand):
    def inner_run(self, *args, **options):
        '''
        自動更新line bot webhook url
        在虛擬環境中cmd： python3 manage.py run_dev
        '''
        if os.environ.get("RUN_MAIN") == "true":
            print("🚀 更新LINE Webhook")
            # 自動更新 webhook（只會在啟動時跑一次）
            update_line_webhook()

            # call_command("runserver")

        super().inner_run(*args, **options)
