import telebot
from telebot import types
import random


answer = 0


def restart():
    global word
    word = {'а':['абдоминальный','абдраган','абдуктор','абдукция','Абдула' ,'абевега','абелевский','абелевый','абелит' ,'абелсонит','Абель','абенакиит-се','аберантный','абергин','абернатит','аберрантный','аберрационный'],'б':['баба',' Бабка', 'бабло', 'бенефит', 'берет', 'блуд', 'блюдо', 'бог',' богатей', 'берет'],
        'в':['вагон', 'валюта', 'вам', 'вампир', 'вариация', 'вас', 'вверх',' власти','вполне', 'восхождение'],'г':['глаза','глазок','гости','гостиная','гость','газировка','галоп','гамак','глухарь','глушь'],'д':['дети','детский','дай','далее','далекий ','дом',' долой ','доминатор ','джунгли',' диалог'],'е':['естественный'
        'европа','ежевика','Ева','евнух','Евразия','Египет','ездок','еда','если'],'ё':['ёж','ёмкость','ёга','ёж-рыба','ёлка','ёкнуть'],'ж':['жар-птица','жасмин','жечь','жилет','жужелица','жюри','желание','женщина','жестокий','жёлтый'],'з':['забор','загадка','закон','запад','зачем','запись','замирать','завтрашний','завтрак','завтра','заря'],
        'и':['Из-за','Извини','Изготовитель','Изумрудный','Индивидуальный','Изображение','Извините','Идеал'],'й':['йога','йеменцы','йод','йо-йо','йог','йорк','йель','йервин','йогуртовый','йоддефицитный','йогин'],'к':['казаться','камыш','кабинет','календарь','капель','калькулятор','капитан','карета','карман'],
        'л':['лабиринт','Лагерь',"Ластик",'лабиринт','лес','леска','ложка','ложь','лом','лето'],'м':['маршрут','машина','мебель','лол','лечение','лайк','лор','лоретка','либо','лаконично'],'н':['навечно','назло','наоборот','направо','например','надолго','на память','назад','налево'],'о':['обаяние','обратно','общество','обман','общество',
        'объект','овраг','огород'],'п':['пакет','паркет','пастух','пассивный','пассажир','пафос','педаль','пенал'],'р':['радио','работа','рабочий','разгадать','разделить','рассвет','рассечённый','рассказ'],'с':['салат','самолёт','салют','сбоку','сбоку','сверху','сегодня','секрет'],'т':['талант','такси','теперь','тогда','телефон','теннис','телёнок','территория'],
        'у':['увеличить','украшать','удалить','узел','универмаг','упорядочить','ураган','участник','учебник'],'ф':['февраль','филология','финиш','футбол','фонарь','фигура','фасад'],'х':['халат','характер','хотеть','хореограф','холодный'],'ц':['целина','цемент','циферблат','цыган','цыпочки','цыган','циклон','цивилизация'],'ч':['часовня','человек','чудесный','чувство','чтобы','четырнадцать',
        'честно'],'ш':['шаблон','шалаш','шестнадцать','шпион','шоссе','Шотландия','шоколад','шёлк','шампунь','шефствовать'],'щ':['щегол','щедроты','щеколда','щенок','щётка','щупальца'],'э':['эвкалипт','эквивалент','эгоист','экскурс','эксплуатация','электрификация','эмблема','эстафета','эпидемия'],'ю':['юг','юмор','юннат','юность','юный'],'я':['яблоко','ягода','язык','яйцо','якорь']}
restart()
def print_12(file,message):
    with open(file + '.txt') as tx:
        global prime
        prime = tx.readlines()
    print_13(prime,message)
def print_13(prime,message):
    T_F = True
    for i in range(5):
        if prime:
            my_bot.send_message(message.chat.id,prime[0])
            prime.remove(prime[0])
        else:
            my_bot.send_message(message.chat.id,f'Сылки закочились')
            T_F = False
            break

    if T_F:
        more = types.ReplyKeyboardMarkup().add('More','❌Exit❌')
        my_bot.send_message(message.chat.id, f'Ещё надо',reply_markup=more)



def example_answer(message):
    global answer
    sign = signs[random.randint(0,3)]
    first_nemaber = random.randint(0, 150)
    second_nemaber = random.randint(0, 150)
    if first_nemaber == 0 and sign == '/':
        return example(message)
    else:
        example_neamder.append(str(first_nemaber)  + sign + str(second_nemaber))
        answer = example_neamder[0]
        for i in range(3): example_neamder.append(str(random.randint(0, 150)) + signs[random.randint(0,3)] + str(random.randint(0, 150)))
        random.shuffle(example_neamder)
        button = types.ReplyKeyboardMarkup().add(str(example_neamder[0]),str(example_neamder[1]),str(example_neamder[2]),str(example_neamder[3]), '🚫Stop game🚫')
        my_bot.send_message(message.chat.id, f'Ответ будет = {round(eval(answer), 2)}\n Чтобы ответить нажмите на кнопку',reply_markup=button)



def example(message):
    global answer
    sign = signs[random.randint(0,3)]
    first_nemaber = random.randint(0, 150)
    second_nemaber = random.randint(0, 150)
    if first_nemaber == 0 and sign == '/':
        return example(message)
    else:
        my_bot.send_message(message.chat.id,
        f'Пример будет {first_nemaber} {sign} {second_nemaber} = \n Чтобы ответить отправте ответ боту')
        answer = round(eval(str(first_nemaber) + sign + str(second_nemaber)),2)


def wriet(file,message,text):
    count = 0
    with open(file+'.txt') as tx:
        prime = tx.readlines()
    for i in prime:
        i.replace('\n', '')
        if text[0] not in i:
            count = count + 1
        else:
            break
    if count == len(prime):
        with open(file +'.txt', 'a') as tx:
            tx.write(str(text[0]) + '\n')
        my_bot.send_message(message.chat.id, 'Сохранено')
    else:
        my_bot.send_message(message.chat.id, 'Такая слыка есть')

capitals = {'Япония':'Токио','Украина':'Киев','Польша': 'Варшава', 'Германия': 'Берлин', 'Франция': 'Париж', 'Италия': 'Рим', 'Беларусь': 'Минск', 'Чехия': 'Прага', 'Дания': 'Копенгаген', 'Аргентина': 'Буэнос-Айрес', 'США': 'Вашингтон', 'Канада': 'Оттава', 'Бразилия': 'Бразилиа', 'Колумбия': 'Богота'}
game_city = False
game_examples = False
game_R_P_S = False
save_on = False
game_world = False
game_Eagle_or_tails = False
game_answe_examples = False
my_bot = telebot.TeleBot('5752290598:AAEsAum3utqdIxoFLoGdxDrcgjCkDrSDMqU')
start_kb = types.ReplyKeyboardMarkup().add('🎮Menu game🎮','💾Save💾','Print',)
exit = types.ReplyKeyboardMarkup().add('❌Exit❌')
stop_game = types.ReplyKeyboardMarkup().add('🚫Stop game🚫')
game_kb = types.ReplyKeyboardMarkup().add('🏢City🏢', '🔢Examples🔢','Rock Paper Scissors','🆎Words🆎','💰Eagle or tails💰','⬅Back➡')
print_1 = types.ReplyKeyboardMarkup().add('TikTok','Youtube','Other','⬅Back➡')
Eagle_and_tails = types.ReplyKeyboardMarkup().add('Eagle','Tails')
example_kb =  types.ReplyKeyboardMarkup().add('Examples - answer','Answer - examples','⬅Back➡')
signs = ['*','/' ,'+','-']
R_P_S = ['🗿Rock🗿','📄Parser📄','✂Scissors✂']
my_bot = telebot.TeleBot('5116218178:AAETJx1pTB6O22oWxCk5JBft3cmTBwRxXWc')
Correct, no_board = 0,0
point_player,point_bot = 0,0
word_del = []
end_bot = 'а'
example_neamder =[]
Idnt =  types.ReplyKeyboardMarkup().add('I do not know')
word_were = []

@my_bot.message_handler(commands=['start'])
def start(message):
    my_bot.send_message(message.chat.id, 'menu', reply_markup=start_kb)
@my_bot.message_handler(content_types='text')
def command(message):
    global game_kb
    global game_city
    global game_examples
    global game_R_P_S
    global save_on
    global point_bot
    global point_player
    global game_world
    global game_kb_R_P_S_True
    global end_bot
    global game_Eagle_or_tails
    global Correct
    global no_board
    global answer
    global  game_answe_examples
    global Correct
    global no_board
    global word_were
    text = list(message.text.split())
    if message.text == 'Close':
        types.ReplyKeyboardRemove()
    elif message.text == 'Print':
        my_bot.send_message(message.chat.id, 'Print', reply_markup=print_1)
    elif message.text == '🎮Menu game🎮':
        my_bot.send_message(message.chat.id,'Game menu' ,reply_markup=game_kb)
    elif message.text == '⬅Back➡':
        my_bot.send_message(message.chat.id, 'Menu', reply_markup=start_kb)
    elif message.text == '❌Exit❌':
        game_city = False
        game_examples = False
        game_R_P_S = False
        game_world = False
        game_Eagle_or_tails = False
        game_answe_examples = False
        my_bot.send_message(message.chat.id, 'Menu', reply_markup=start_kb)
    elif message.text == '💰Eagle or tails💰' or game_Eagle_or_tails:
        my_bot.send_message(message.chat.id, 'Eagle or tails', reply_markup=Eagle_and_tails)
        list_game = ['Eagle','Tails']
        random_bot = list_game[random.randint(0,1)]
        game_Eagle_or_tails = True
        if random_bot == message.text:
            my_bot.send_message(message.chat.id, 'Ты выйграл)',reply_markup=Eagle_and_tails)
            my_bot.send_message(message.chat.id, 'Menu', reply_markup=game_kb)
            game_Eagle_or_tails = False
        elif message.text != '💰Eagle or tails💰':
            my_bot.send_message(message.chat.id, 'Ты проиграл(',reply_markup=Eagle_and_tails)
            my_bot.send_message(message.chat.id, 'Menu', reply_markup=game_kb)
            game_Eagle_or_tails = False

    elif message.text == '🏢City🏢' or game_city == True:
        game_city = True
        if message.text.lower in capitals:
            my_bot.send_message(message.chat.id, f'{capitals.get(message.text)}')
        elif message.text != '🏢City🏢':
            my_bot.send_message(message.chat.id, 'Вы ввели несуществующую страну или её нет в списке')
        my_bot.send_message(message.chat.id, 'В ведите страну', reply_markup=exit)
    elif message.text == '🔢Examples🔢':
        my_bot.send_message(message.chat.id, 'Menu', reply_markup=example_kb)
    elif message.text == 'Answer - examples' or game_answe_examples:
        game_answe_examples = True
        if message.text == '🚫Stop game🚫':
            global Correct
            global no_board
            my_bot.send_message(message.chat.id, f'Правельные = {Correct}. Неправельные = {no_board}')
            if Correct == no_board:
                my_bot.send_message(message.chat.id, f'Одинаковое количество непраельных и праевельных', reply_markup=game_kb)
            elif Correct < no_board:
                my_bot.send_message(message.chat.id, f'Больше не правельных 😔', reply_markup=game_kb)
            else:
                my_bot.send_message(message.chat.id, f'Больше правельных 😇', reply_markup=game_kb)
            Correct, no_board = 0, 0
        else:

            answer_user = list(message.text.split())
            if answer_user[0] == str(answer):
                Correct += 1
                my_bot.send_message(message.chat.id, f'Правельный ответ вы получили 1 балл')
            elif message.text != 'Answer - examples':
                no_board += 1
                my_bot.send_message(message.chat.id, f'Неправельно вы потеряли 1 балл')
            my_bot.send_message(message.chat.id, f'Следуеший ')
            example_neamder.clear()
            example_answer(message)

    elif message.text == 'Examples - answer' or game_examples:
        game_examples = True
        my_bot.send_message(message.chat.id, 'Игра началась', reply_markup=stop_game)
        if message.text == '🚫Stop game🚫':
            my_bot.send_message(message.chat.id, f'Правельные = {Correct}. Неправельные = {no_board}')
            if Correct == no_board:
                my_bot.send_message(message.chat.id, f'Одинаковое количество непраельных и праевельных', reply_markup=game_kb)
            elif Correct < no_board:
                my_bot.send_message(message.chat.id, f'Больше не правельных 😔', reply_markup=game_kb)
            else:
                my_bot.send_message(message.chat.id, f'Больше правельных 😇', reply_markup=game_kb)
            Correct, no_board = 0, 0
            game_examples = False
        else:
            answer_user = list(message.text.split())
            if answer_user[0] == str(answer) and message.text != 'Examples - answer':
                Correct += 1
                my_bot.send_message(message.chat.id, f'Правельный ответ вы получили 1 балл')
            elif message.text != 'Examples - answer':
                no_board += 1
                my_bot.send_message(message.chat.id, f'Неправельно вы потеряли 1 балл')
            example(message)
    elif message.text == 'Rock Paper Scissors' or game_R_P_S:
        game_R_P_S = True
        game_kb_R_P_S = types.ReplyKeyboardMarkup().add('🗿Rock🗿',"📄Parser📄",'✂Scissors✂','🚫Stop game🚫')
        my_bot.send_message(message.chat.id, 'Игра началась', reply_markup=game_kb_R_P_S)
        if message.text != 'Rock Paper Scissors' and message.text != '🚫Stop game🚫':
            bot = R_P_S[random.randint(0,2)]
            if message.text == '🗿Rock🗿' and bot == '✂Scissors✂' or message.text =='✂Scissors✂' and bot =='📄Parser📄' or message.text ==  '📄Parser📄' and bot == '🗿Rock🗿':
                my_bot.send_message(message.chat.id,f'Выграл игрок. Бот выбрал {bot}')
                point_player += 1
            elif message.text == '✂Scissors✂' and bot == '🗿Rock🗿'or message.text =='📄Parser📄' and bot =='✂Scissors✂' or message.text == '🗿Rock🗿' and bot == '📄Parser📄':
                my_bot.send_message(message.chat.id, f'Выграл бот он выбрал {bot}')
                point_bot += 1
            else:
                my_bot.send_message(message.chat.id, f'Нечья Бот выбрал {bot}')
        elif message.text == '🚫Stop game🚫':
            if point_bot > point_player:
                my_bot.send_message(message.chat.id, f'Выйграл бот балы равны бот -  {point_bot} балы игрока - {point_player}',reply_markup=game_kb)
            elif point_bot == point_player:
                my_bot.send_message(message.chat.id,
                                    f'Нечья балы = бот -  {point_bot} балы игрока - {point_player}',reply_markup=game_kb)
            else:
                my_bot.send_message(message.chat.id,f'Выйграл игрок балы = бот -  {point_bot} балы игрока - {point_player}',reply_markup=game_kb)
            point_player = 0
            point_bot = 0
            game_R_P_S = False
    elif  message.text == '💾Save💾':
        save_on = True
        my_bot.send_message(message.chat.id, 'Жду сылку')
    elif message.text == '🆎Words🆎' or game_world:
        if message.text == 'I do not know':
            my_bot.send_message(message.chat.id, f'Печально(', reply_markup=game_kb)
            end_bot = 'a'
            word_were = []
            game_world = False

            restart()
        if message.text == '🆎Words🆎':
            my_bot.send_message(message.chat.id, f'Первая буквва будет - {end_bot}',reply_markup=Idnt)
            game_world = True
        elif message.text not in ('🆎Words🆎','I do not know'):
            end_word = message.text.lower()
            text_1 = message.text.lower()
            if ord(text_1[0]) >= 1072 and ord(text_1[0]) <= 1103:
                if ord(end_bot) == ord(text_1[0]):
                    if message.text.lower() not in word_were:
                        if end_word[-1] in ('ь', ' ъ'):
                            end_word = end_word[-2]
                        else:
                            end_word = end_word[-1]
                        if word.get(end_word) != None:
                            word_bot = random.choice(word.get(end_word))
                            if word_bot[-1] in ('ь', ' ъ'):
                                end_bot = word_bot[-2]
                            else:
                                end_bot = word_bot[-1]
                            word_were.append(message.text.lower())
                            word_were.append(word_bot.lower())
                            my_bot.send_message(message.chat.id, f'Моё слово будет "{word_bot}" следушее слово на  {end_bot} ')
                            word.get(end_word).remove(word_bot)
                        else:
                            my_bot.send_message(message.chat.id, f'У меня нет больше слов, Ты выйграл',reply_markup=game_kb)
                    else:
                        my_bot.send_message(message.chat.id, f'Это слово было')
                        print(word_were)
                else:
                    my_bot.send_message(message.chat.id, f'Не та буква надо на {end_bot}')
            else:
                my_bot.send_message(message.chat.id, 'Не тот язык')

    elif message.text == 'Youtube':
        print_12('Ютуб',message)
    elif message.text == 'Other':
        print_12('Другое',message)
    elif message.text =='TikTok':
        print_12('ТикТок', message)
    elif message.text == 'More':
        print_13(prime,message)

    else:
        if save_on:
            save_on = False
            if 'tiktok' in message.text and 'https://' in text[0]:
                wriet('ТикТок', message, text)
            elif 'youtube' in message.text and 'https://' in text[0]:
                wriet('Ютуб', message, text)
            elif 'https://' in text[0]:
                wriet('Другое', message, text)
            else:
                my_bot.send_message(message.chat.id, f'Это не сылка')










my_bot.polling()