import os
import requests
from django.core.management.commands.runserver import Command as RunserverCommand
# from django.core.management import call_command
from apps.bot.utils.update_line_webhook import update_line_webhook
import logging
logger = logging.getLogger(__name__)

class Command(RunserverCommand):
    def inner_run(self, *args, **options):
        '''
        自動更新line bot webhook url
        啟動docker時會一併啟動ngrok並將ngrok網址貼到line webhook
        '''
        # print("👻 RUN_MAIN=", os.environ.get("RUN_MAIN"), flush=True)
        # logger.info("👻 RUN_MAIN=%s",os.environ.get("RUN_MAIN"))

        try:
            if not os.environ.get("WEBHOOK_UPDATED"):
                # print("🚀 更新LINE Webhook", flush=True)
                logger.info("🚀 更新LINE Webhook")

                update_line_webhook()

                os.environ["WEBHOOK_UPDATED"] = "1"

            super().inner_run(*args, **options)

        except requests.RequestException as e:
            # print(f"❌ LINE webhook更新失敗: {e}", flush=True)
            logger.exception(f"❌ LINE webhook更新失敗: {e}")
