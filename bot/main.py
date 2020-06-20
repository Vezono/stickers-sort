from modules.BotUtil import BotUtil
import config
bot = BotUtil(config.token, creator=config.creator)
bot.report('Инициализация...')

from timeit import default_timer as timer
start_time = timer()
from modules.BotRunner import BotsRunner

from bot import bot as stickerbot

bots = {
    'Stickerbot': stickerbot
}

runner = BotsRunner(retries=3, show_traceback=True)
runner.add_bots(bots)
runner.set_main_bot(bot, 'status')
bot.report('Готово! Боты запущены и готовы к работе.\nВремени использовано: {} секунд.'.format(timer() - start_time))
runner.run()
