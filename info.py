help_message = \
    """Вот, что я умею:
/start - запустить бота
/quest - начать проходить квест
/about - о квесте
/help - узнать, что может бот"""

about_message = \
    """Сюжет квеста «Тайны затерянного артефакта» полностью сгенерирован нейросетью. 
Главный герой просыпается в неизвестом помещении, ничего не помня. Перед ним лишь письмо и ключи. Игрок должен сделать правильный выбор от которого зависит его дальнейшая судьба, а не правильный повлечёт за собой ужасные последствия."""

start_message = [
    "Ты посыпаешься в неизвестной комнате без памяти о том, как сюда попал и что произошло. В комнате есть стол на котором лежит письмо. Письмо гласит, что ты находишься в забытом замке, где храниться древний артефакт. Чтобы выбраться, тебе необходимо разгадать загаки и найти древний артефакт. \n"
    "Согласишься ли ты на такие правила и начнёшь игру?"]

# добавить фото
N1_Text = ["К сожалению, выбор оказался не правильным и вы проиграли, оставшись в замке навсегда :(\n"
           "Чтобы начать заново нажмите /start"]

# добавить загадку
level_1_text = ["На столе перед тобой лежат 3 ключа с разными изображениями, тебе необходимо выбрать 1 из них."
                " Определиться с выбором тебе поможет простая загадка.\n"
                "«Как называется светящийся объект на небе, который состоит из горящего газа?»\n"
                "Ответом на загадку будет являться символ на ключе, который выбирать НЕ стоит."]

answers = ["Луна", "Звезда", "Солнце", "Слева", "Справа", "Сны", "Свет"]
Answers_1 = ["", ["Свет", "-", "Забрать"], ["Справа", "Забрать"]]
Answers_2 = ["", ["Сны", "-", "Оставить"], ["Слева", "Оставить"]]

# добавить описание + фото
sun = ("Дверь открылась, ты попал на светлую поляну."
       " Перед тобой ещё одна дверь, она открывается, если решить простую загадку.\n"
       "«Что можно увидеть с закрытыми глазами?»")

sleep = ("Поздравляю!\n"
         "Ты разгадал загадку и дверь открылась."
         " За ней находится дверний артефакт. Теперь перед тобой стоит важный выбор."
         " Забрать артефакт с собой или же оставить его в замке."
         " Хорошо подумай, этот выбор повлияет на твою судьбу!")

moon = ("Дверь открылась, ты попал в тёмный коридор."
        " Фонариком ты освещаешь путь и видишь две дверей. За одной находится ловушка, а за другой следующий ключ."
        " Тебе необходимо выбрать правильную дверь, рассчитывая только на свою интуицию.\n"
        "Какую дверь выберешь?")

# добавить описание
left = ("Поздравляю!\n"
        "Ты выбрал правильную дверь."
        " За ней находится дверний артефакт. Теперь перед тобой стоит важный выбор."
        " Забрать артефакт с собой или же оставить его в замке."
        " Хорошо подумай, этот выбор повлияет на твою судьбу!")

star = ["Дверь не открылась, ты остаёшься в комнате :( "

        "Нажмите /start , чтобы попробовать пройти ещё раз"]

# добавить фото + описание
location2 = ("-")

Answer_all = ["", [sun, location2, sleep], [moon, left], [star]]

# добавить фото
finals3 = ["Дверь оказалась неверной и ты упал в ловушку из которой не смог выбраться :("]

final1 = ["Ты победил и выходишь из замка..\n"
          "Но ты забрал чужую вещь и теперь всю жизнь тебя будут преследовать беды, твоя жизнь больше никогда не станет прежней. Всю оставшуюся жизнь ты проведёщь в бегстве от последствий.\n"
          "Стоит задуматься, а победил ли ты?"]

# добавить описание
final2 = ["Ты победил!!!\n"
          "И выходишь из замка без последствий!"]

quest2 = ["Ответ не верный, дверь не открывается, а ты навсегда остаёшься в этом замке :("]