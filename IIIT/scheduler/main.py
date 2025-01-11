import psycopg2
import telebot
from telebot import types
import datetime
from datetime import date, datetime

conn = psycopg2.connect(database="schedular_db",
                                 user="postgres",
                                 password='1',
                                 host="localhost",
                                 port="5432")

cursor = conn.cursor()

token = '0'
bot = telebot.TeleBot(token)

current_date = date.today()
first_week = date(2021, 9, 3)
dellta = current_date - first_week
parity = (dellta.days // 7) % 2
if parity == 0:
    parity = 't'
    parity1 = 'f'
else:
    parity = 'f'
    parity1 = 't'

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Понедельник", "/Вторник", "/Среда", "/Четверг", "/Пятница", "/Расписание_на_текущую_неделю",
                 "/Расписание на следующую неделю")
    bot.send_message(message.chat.id, 'Привет! Хотите узнать расписание?', reply_markup=keyboard)

@bot.message_handler(commands=['Понедельник'])
def monday(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Понедельник", "/Вторник", "/Среда", "/Четверг", "/Пятница", "/Текущая",
                 "/Следующая")
    cursor.execute("SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Понедельник' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;", parity)
    records = list(cursor.fetchall())
    day = 'Понедельник.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(","")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'
    bot.send_message(message.chat.id, (day),reply_markup=keyboard)

@bot.message_handler(commands=['Вторник'])
def tuesday(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Понедельник", "/Вторник", "/Среда", "/Четверг", "/Пятница", "/Текущая",
                 "/Следующая")
    cursor.execute("SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Вторник' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;", parity)
    records = list(cursor.fetchall())
    day = 'Вторник.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(","")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'
    bot.send_message(message.chat.id, (day),reply_markup=keyboard)

@bot.message_handler(commands=['Среда'])
def wednesday(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Понедельник", "/Вторник", "/Среда", "/Четверг", "/Пятница", "/Текущая",
                 "/Следующая")
    cursor.execute("SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Среда' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;", parity)
    records = list(cursor.fetchall())
    day = 'Среда.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(","")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'
    bot.send_message(message.chat.id, (day),reply_markup=keyboard)

@bot.message_handler(commands=['Четверг'])
def thursday(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Понедельник", "/Вторник", "/Среда", "/Четверг", "/Пятница", "/Текущая",
                 "/Следующая")
    cursor.execute("SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Четверг' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;", parity)
    records = list(cursor.fetchall())
    day = 'Четверг.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(","")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'
    bot.send_message(message.chat.id, (day),reply_markup=keyboard)

@bot.message_handler(commands=['Пятница'])
def friday(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Понедельник", "/Вторник", "/Среда", "/Четверг", "/Пятница", "/Текущая",
                 "/Следующая")
    cursor.execute("SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Пятница' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;", parity)
    records = list(cursor.fetchall())
    day = 'Пятница.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(","")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'
    bot.send_message(message.chat.id, day, reply_markup=keyboard)

@bot.message_handler(commands=['Текущая'])
def t_week(message):
    print(parity)
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Понедельник", "/Вторник", "/Среда", "/Четверг", "/Пятница", "/Текущая",
                 "/Следующая")
    cursor.execute("SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Понедельник' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;", parity)
    records = list(cursor.fetchall())
    day = 'Понедельник.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(","")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'
    day += '\n' + '\n'
    cursor.execute("SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Вторник' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",parity)
    records = list(cursor.fetchall())
    day += 'Вторник.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'

    day += '\n' + '\n'
    cursor.execute(
        "SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Среда' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",
        parity)
    records = list(cursor.fetchall())
    day += 'Среда.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'

    day += '\n' + '\n'
    cursor.execute(
        "SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Четверг' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",
        parity)
    records = list(cursor.fetchall())
    day += 'Четверг.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'

    day += '\n' + '\n'
    cursor.execute(
        "SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Пятница' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",
        parity)
    records = list(cursor.fetchall())
    day += 'Пятница.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'
    bot.send_message(message.chat.id, day, reply_markup=keyboard)

@bot.message_handler(commands=['Следующая'])
def n_week(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("/Понедельник", "/Вторник", "/Среда", "/Четверг", "/Пятница", "/Текущая",
                 "/Следующая")
    cursor.execute(
        "SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Понедельник' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",
        parity1)
    records = list(cursor.fetchall())
    day = 'Понедельник.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'

    day += '\n' + '\n'
    cursor.execute(
        "SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Вторник' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",
        parity1)
    records = list(cursor.fetchall())
    day += 'Вторник.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'

    day += '\n' + '\n'
    cursor.execute(
        "SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Среда' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",
        parity1)
    records = list(cursor.fetchall())
    day += 'Среда.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'

    day += '\n' + '\n'
    cursor.execute(
        "SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Четверг' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",
        parity1)
    records = list(cursor.fetchall())
    day += 'Четверг.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'

    day += '\n' + '\n'
    cursor.execute(
        "SELECT timetable.subject, timetable.room_numb, timetable.start_time, teacher.name FROM timetable, teacher WHERE day='Пятница' AND chet=%s AND timetable.subject=teacher.subject ORDER BY timetable.start_time ASC;",
        parity1)
    records = list(cursor.fetchall())
    day += 'Пятница.'
    for i in range(len(records)):
        cl = str(records[i])
        cl = cl.replace("(", "")
        cl = cl.replace(")", "")
        cl = cl.replace("'", "")
        day += '\n' + cl + '.'
    bot.send_message(message.chat.id, (day), reply_markup=keyboard)


bot.polling(non_stop=True)