import vk
import telebot


def vk2telegram():
    response = vk.vk_get()
    if response[0]:
        telebot.tbotxt(response[0])
    if response[1]:
        telebot.tbotimg(response[1])
if __name__ == "__main__":
    vk2telegram()
