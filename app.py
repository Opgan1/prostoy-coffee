from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
import asyncio
from aiohttp import web
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message, ReplyKeyboardRemove
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

espresso_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пошаговый рецепт Эспрессо")],
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

americano_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пошаговый рецепт Американо")],
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

latte_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пошаговый рецепт Латте")],
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

cappuccino_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пошаговый рецепт Капучино")],
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

raf_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пошаговый рецепт Раф")],
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

flat_white_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пошаговый рецепт Флэт Уайт")],
        [KeyboardButton(text="Меню")]
    ],
    resize_keyboard=True
)

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Эспрессо"),
            KeyboardButton(text="Американо"),
            KeyboardButton(text="Латте")
        ],
        [
            KeyboardButton(text="Капучино"),
            KeyboardButton(text="Раф"),
            KeyboardButton(text="Флэт Уайт")
        ]

    ],
    resize_keyboard=True
)


@dp.message(lambda message: message.text == "Меню")
async def open_menu(message: Message):
    await message.answer(
        "Выбери нужный тип кофе:",
        reply_markup=menu_keyboard
    )


@dp.message(lambda message: message.text == 'Эспрессо')
async def espresso(message: Message):
    await message.answer(
        "<b>Вы выбрали Эспрессо.</b> Для приготовления 1-ой порции вам понадобится:\n\n"
        "<b>- Кофе:</b> 8 граммов (2 чайные ложки с горкой), сверхтонкий помол - 'в пудру'\n\n"
        "<b>- Вода:</b> 50 мл холодная или комнатная температура\n\n"
        "<b>- Добавки:</b> сахар, щепотка соли/корицы, сироп по вкусу\n\n"
        "Чтобы посмотреть пошаговый рецепт, нажмите на кнопку ниже.",
        reply_markup=espresso_keyboard, parse_mode=ParseMode.HTML
    )


@dp.message(lambda message: message.text == 'Американо')
async def americano(message: Message):
    await message.answer(
        "<b>Вы выбрали Американо.</b> Для приготовления 1-ой порции вам понадобится:\n\n"
        "<b>- Кофе:</b> 8 граммов (2 чайные ложки с горкой), сверхтонкий помол - 'в пудру'\n\n"
        "<b>- Вода холодная:</b> 50 мл\n\n"
        "<b>- Вода горячая:</b> 100 мл с температурой около 90°C\n\n"
        "<b>- Добавки:</b> сахар, щепотка соли/корицы, сироп по вкусу\n\n"
        "Чтобы посмотреть пошаговый рецепт, нажмите на кнопку ниже.",
        reply_markup=americano_keyboard, parse_mode=ParseMode.HTML
    )


@dp.message(lambda message: message.text == 'Латте')
async def latte(message: Message):
    await message.answer(
        "<b>Вы выбрали Латте.</b> Для приготовления 1-ой порции вам понадобится:\n\n"
        "<b>- Кофе:</b> 8 граммов (2 чайные ложки с горкой), сверхтонкий помол - 'в пудру'\n\n"
        "<b>- Вода:</b> 50 мл холодная или комнатная температура\n\n"
        "<b>- Молоко:</b> 150 мл\n\n"
        "<b>- Добавки:</b> сахар, щепотка соли/корицы, сироп по вкусу\n\n"
        "Чтобы посмотреть пошаговый рецепт, нажмите на кнопку ниже.",
        reply_markup=latte_keyboard, parse_mode=ParseMode.HTML
    )


@dp.message(lambda message: message.text == 'Капучино')
async def cappuccino(message: Message):
    await message.answer(
        "<b>Вы выбрали Капучино.</b> Для приготовления 1-ой порции вам понадобится:\n\n"
        "<b>- Кофе:</b> 8 граммов (2 чайные ложки с горкой), сверхтонкий помол - 'в пудру'\n\n"
        "<b>- Вода:</b> 50 мл холодная или комнатная температура\n\n"
        "<b>- Молоко:</b> 120 мл\n\n"
        "<b>- Добавки:</b> сахар, щепотка соли/корицы, сироп по вкусу\n\n"
        "Чтобы посмотреть пошаговый рецепт, нажмите на кнопку ниже.",
        reply_markup=cappuccino_keyboard, parse_mode=ParseMode.HTML
    )


@dp.message(lambda message: message.text == 'Раф')
async def raf(message: Message):
    await message.answer(
        "<b>Вы выбрали Раф.</b> Для приготовления 1-ой порции вам понадобится:\n\n"
        "<b>- Кофе:</b> 10 граммов (3 чайные ложки без горки), сверхтонкий помол - 'в пудру'\n\n"
        "<b>- Вода:</b> 75 мл холодная или комнатная температура\n\n"
        "<b>- Сливки 10-15%:</b> 120 мл\n\n"
        "<b>- Ванильный сахар:</b> 1 чайная ложка\n\n"
        "<b>- Добавки:</b> сахар, щепотка соли/корицы, сироп по вкусу\n\n"
        "Чтобы посмотреть пошаговый рецепт, нажмите на кнопку ниже.",
        reply_markup=raf_keyboard, parse_mode=ParseMode.HTML
    )


@dp.message(lambda message: message.text == 'Флэт Уайт')
async def flat_white(message: Message):
    await message.answer(
        "<b>Вы выбрали Флэт Уайт.</b> Для приготовления 1-ой порции вам понадобится:\n\n"
        "<b>- Кофе:</b> 14 граммов (3 чайные ложки с горкой), сверхтонкий помол - 'в пудру'\n\n"
        "<b>- Вода:</b> 70 мл холодная или комнатная температура\n\n"
        "<b>- Молоко:</b> 120 мл\n\n"
        "<b>- Добавки:</b> сахар, щепотка соли/корицы, сироп по вкусу\n\n"
        "Чтобы посмотреть пошаговый рецепт, нажмите на кнопку ниже.",
        reply_markup=flat_white_keyboard, parse_mode=ParseMode.HTML
    )


@dp.message(lambda message: message.text == "Пошаговый рецепт Эспрессо")
async def espresso_recipe(message: Message):
    await message.answer(
        "<b>Пошаговый рецепт Эспрессо:</b>\n"
        "1. Насыпьте молотый кофе (и по желанию сахар/специи) в сухую турку.\n\n"
        "2. Залейте холодной или чуть теплой отфильтрованной водой. Аккуратно перемешайте один раз, чтобы смочить все частички.\n\n"
        "3. Поставьте турку на самый медленный огонь. Чем медленнее будет нагрев, тем богаче получится вкус.\n\n"
        "4. Внимательно следите за напитком. По мере нагрева на поверхности начнет собираться густая темная пенка (крема́).\n\n"
        "5. Как только шапочка пенки начнет подниматься и светлеть (не доводя до бурления и кипения), снимите турку с плиты.\n\n"
        "6. Дайте напитку постоять 1–2 минуты, чтобы гуща осела на дно, либо воспользуйтесь ситом, чтобы убрать лишние частицы, и наслаждайтесь вашим свежим Эспрессо! ☕",
        reply_markup=main_keyboard, parse_mode=ParseMode.HTML
    )
    await message.answer("Если хотите приготовить другой кофе, нажмите 'Меню' и выберите тип кофе.", reply_markup=main_keyboard)


@dp.message(lambda message: message.text == "Пошаговый рецепт Американо")
async def americano_recipe(message: Message):
    await message.answer(
        "<b>Пошаговый рецепт Американо:</b>\n"
        "1. Насыпьте молотый кофе (и по желанию сахар/специи) в сухую турку.\n\n"
        "2. Залейте холодной или чуть теплой отфильтрованной водой. Аккуратно перемешайте один раз, чтобы смочить все частички.\n\n"
        "3. Поставьте турку на самый медленный огонь. Чем медленнее будет нагрев, тем богаче получится вкус.\n\n"
        "4. Внимательно следите за напитком. По мере нагрева на поверхности начнет собираться густая темная пенка (крема́).\n\n"
        "5. Как только шапочка пенки начнет подниматься и светлеть (не доводя до бурления и кипения), снимите турку с плиты.\n\n"
        "6. Налейте в чашку 100 мл горячей воды с температурой около 90°C.\n\n"
        "7. Аккуратно влейте готовый эспрессо из турки в чашку с водой через сито, чтобы убрать лишние частицы. На поверхности останется плотная ароматная пенка. Наслаждайтесь вашим Американо! ☕\n\n",

        reply_markup=main_keyboard, parse_mode=ParseMode.HTML
    )
    await message.answer("Если хотите приготовить другой кофе, нажмите 'Меню' и выберите тип кофе.", reply_markup=main_keyboard)


@dp.message(lambda message: message.text == "Пошаговый рецепт Латте")
async def latte_recipe(message: Message):
    await message.answer(
        "<b>Пошаговый рецепт Латте:</b>\n"
        "1. Насыпьте молотый кофе (и по желанию сахар/специи) в сухую турку.\n\n"
        "2. Залейте холодной или чуть теплой отфильтрованной водой. Аккуратно перемешайте один раз, чтобы смочить все частички.\n\n"
        "3. Поставьте турку на самый медленный огонь. Чем медленнее будет нагрев, тем богаче получится вкус.\n\n"
        "4. Внимательно следите за напитком. По мере нагрева на поверхности начнет собираться густая темная пенка (крема́).\n\n"
        "5. Как только шапочка пенки начнет подниматься и светлеть (не доводя до бурления и кипения), снимите турку с плиты.\n\n"
        "6. Подогрейте молоко до температуры 60-65°C. Взбейте его с помощью френч-пресса.\n\n"
        "7. Аккуратно влейте готовый эспрессо из турки в чашку через сито, чтобы убрать лишние частицы.\n\n"
        "8. Аккуратно влейте взбитое теплое молоко в чашку с эспрессо. По желанию, вы можете создать рисунок на поверхности. Наслаждайтесь вашим Латте! ☕\n\n",

        reply_markup=main_keyboard, parse_mode=ParseMode.HTML
    )
    await message.answer("Если хотите приготовить другой кофе, нажмите 'Меню' и выберите тип кофе.", reply_markup=main_keyboard)


@dp.message(lambda message: message.text == "Пошаговый рецепт Капучино")
async def cappuccino_recipe(message: Message):
    await message.answer(
        "<b>Пошаговый рецепт Капучино:</b>\n"
        "1. Насыпьте молотый кофе (и по желанию сахар/специи) в сухую турку.\n\n"
        "2. Залейте холодной или чуть теплой отфильтрованной водой. Аккуратно перемешайте один раз, чтобы смочить все частички.\n\n"
        "3. Поставьте турку на самый медленный огонь. Чем медленнее будет нагрев, тем богаче получится вкус.\n\n"
        "4. Внимательно следите за напитком. По мере нагрева на поверхности начнет собираться густая темная пенка (крема́).\n\n"
        "5. Как только шапочка пенки начнет подниматься и светлеть (не доводя до бурления и кипения), снимите турку с плиты.\n\n"
        "6. Подогрейте молоко до температуры 60-65°C. Взбейте его с помощью френч-пресса.\n\n"
        "7. Аккуратно влейте готовый эспрессо из турки в чашку через сито, чтобы убрать лишние частицы.\n\n"
        "8. Аккуратно влейте взбитое теплое молоко в чашку с эспрессо. По желанию, вы можете создать рисунок на поверхности. Наслаждайтесь вашим Капучино! ☕\n\n",

        reply_markup=main_keyboard, parse_mode=ParseMode.HTML
    )
    await message.answer("Если хотите приготовить другой кофе, нажмите 'Меню' и выберите тип кофе.", reply_markup=main_keyboard)


@dp.message(lambda message: message.text == "Пошаговый рецепт Раф")
async def raf_recipe(message: Message):
    await message.answer(
        "<b>Пошаговый рецепт Раф:</b>\n"
        "1. Насыпьте молотый кофе (и по желанию сахар/специи) в сухую турку.\n\n"
        "2. Залейте холодной или чуть теплой отфильтрованной водой. Аккуратно перемешайте один раз, чтобы смочить все частички.\n\n"
        "3. Поставьте турку на самый медленный огонь. Чем медленнее будет нагрев, тем богаче получится вкус.\n\n"
        "4. Внимательно следите за напитком. По мере нагрева на поверхности начнет собираться густая темная пенка (крема́).\n\n"
        "5. Как только шапочка пенки начнет подниматься и светлеть (не доводя до бурления и кипения), снимите турку с плиты.\n\n"
        "6. В отдельном сотейнике или кружке соедините сливки и ванильный сахар.\n\n"
        "7. Слегка подогрейте смесь (примерно до 60–65 °C, не доводя до кипения), чтобы сахар полностью растворился.\n\n"
        "8. Аккуратно влейте готовый эспрессо из турки в теплые сливки через сито, чтобы убрать лишние частицы.\n\n"
        "9. Взбейте напиток с помощью френч-пресса, чтобы появилась плотная сливочная пенка.\n\n"
        "10. Перелейте готовый раф в чашку и наслаждайтесь вашим ароматным напитком! ☕\n\n",

        reply_markup=main_keyboard, parse_mode=ParseMode.HTML
    )
    await message.answer("Если хотите приготовить другой кофе, нажмите 'Меню' и выберите тип кофе.", reply_markup=main_keyboard)


@dp.message(lambda message: message.text == "Пошаговый рецепт Флэт Уайт")
async def flat_white_recipe(message: Message):
    await message.answer(
        "<b>Пошаговый рецепт Флэт Уайт:</b>\n"
        "1. Насыпьте молотый кофе (и по желанию сахар/специи) в сухую турку.\n\n"
        "2. Залейте холодной или чуть теплой отфильтрованной водой. Аккуратно перемешайте один раз, чтобы смочить все частички.\n\n"
        "3. Поставьте турку на самый медленный огонь. Чем медленнее будет нагрев, тем богаче получится вкус.\n\n"
        "4. Внимательно следите за напитком. По мере нагрева на поверхности начнет собираться густая темная пенка (крема́).\n\n"
        "5. Как только шапочка пенки начнет подниматься и светлеть (не доводя до бурления и кипения), снимите турку с плиты.\n\n"
        "6. Подогрейте молоко до температуры 60-65°C. Взбейте его с помощью френч-пресса до получения однородной шелковистой текстуры с минимальным количеством пены (около 2–3 мм).\n\n"
        "7. Аккуратно влейте готовый эспрессо из турки в чашку через сито, чтобы убрать лишние частицы.\n\n"
        "8. Аккуратно влейте взбитое теплое молоко в чашку с эспрессо, создавая тонкий слой молочной пены сверху. Наслаждайтесь вашим Флэт Уайт! ☕\n\n",

        reply_markup=main_keyboard, parse_mode=ParseMode.HTML
    )
    await message.answer("Если хотите приготовить другой кофе, нажмите 'Меню' и выберите тип кофе.", reply_markup=main_keyboard)


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Давайте начнем готовить вкусный кофе! Заходите в Меню и выберите тип кофе, который хотите приготовить.', reply_markup=main_keyboard)


async def health(request):
    return web.Response(text="OK")


async def main():
    app = web.Application()
    app.router.add_get("/", health)
    app.router.add_get("/health", health)

    runner = web.AppRunner(app)
    await runner.setup()

    port = int(os.environ.get("PORT", "10000"))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    print(f"HTTP-сервер запущен на порту {port}")

    try:
        await dp.start_polling(bot, drop_pending_updates=True)
    finally:
        await runner.cleanup()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
