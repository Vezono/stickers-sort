from modules.BotUtil import BotUtil
import config
bot = BotUtil('1149367015:AAF-Uy_-2JMYhUDYZCPndAtNAUv-NsvXvq4', creator=config.creator)
bot.report('Инициализация...')

from timeit import default_timer as timer
start_time = timer()
from modules.BotRunner import BotsRunner

from modules.heroku import Heroku
app = Heroku(bot).app

from bot import bot as stickerbot

bots = {
    'Stickerbot': stickerbot
}

@bot.message_handler(commands=['reboot'])
def reboot(m):
    if not m.from_user.id == config.creator:
        return
    bot.report('Перезагрузка...')
    app.restart()


@bot.message_handler(commands=['logs'])
def reboot(m):
    if not m.from_user.id == config.creator:
        return
    count = 20
    if m.text.count(' '):
        count = int(m.text.split()[1])
    logs = ''
    for log in app.get_log(lines=count).split('\n'):
        logs += '\n' + log[33:]
    bot.reply_to(m, logs)


runner = BotsRunner(retries=3, show_traceback=True)
runner.add_bots(bots)
runner.set_main_bot(bot, 'status')
bot.report('Готово! Боты запущены и готовы к работе.\nВремени использовано: {} секунд.'.format(timer() - start_time))
runner.run()
