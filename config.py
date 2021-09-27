from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")

FILES = {
    'Учебники': {
        'Вышмат': {

        },
        'Инженерная графика': {
            'BQACAgIAAxkBAAICg2FQ2VHS-Mz4STLhivqB87mCLxtgAAK_DgACuleISqboquvJI457IQQ': 'Короев - Начертательная геометрия',
            'BQACAgIAAxkBAAIChGFQ2WlymPoYxZSCCiaOswid_juPAALADgACuleIStMUyzif_91XIQQ': 'Инженерная и компьютерная графика, часть 1',
        },
        'Физика': {

        },
        'Химия': {
            'BQACAgIAAxkBAAIELGFSI27BNhzIGrJGJHo9lJHHcmhAAAKCFQACSnCQSswxIJ-iwVdOIQQ': 'Сидоров - Общая Химия',
            'BQACAgIAAxkBAAIELWFSI5Bot3SaevC_U9busZoETbGGAAKDFQACSnCQSptVIDntsetBIQQ': 'Помощник по химии',
        },
        'История': {

        },
        'Экология': {

        },
        'Английский язык': {
            'BQACAgIAAxkBAAIEKmFSIyYL-kcozDvQfwrODg0NHUw8AAJrEgACuleQSjgXiqX2pxp3IQQ': 'Гарагуля - Английский язык',
        },
    },
    'Тетради': {
        'Вышмат': {

        },
        'Инженерная графика': {
            'BQACAgIAAxkBAAIDK2FQ5-cpg6xET4VTJVzsz9VHo4dhAALLDgACuleISnRHLRs6sHY8IQQ': 'Теория построения проекционного чертежа',
            'BQACAgIAAxkBAAIEKGFSIkofCULTqJxeA7Flx3ZE_wL_AAJjEgACuleQSgFCZTrJ5bigIQQ': 'Рабочая тетрадь',
        },
        'Физика': {

        },
        'Химия': {
            'BQACAgIAAxkBAAIEK2FSI0n3xxLIE-Hfk9FXtyWqispwAAJsEgACuleQSuQr07tP5FjAIQQ': 'Журнал Лаб.работ по Химии',
        },
        'История': {

        },
        'Экология': {

        },
        'Английский язык': {

        },
    },
    'Презентации': {
        'Вышмат': {

        },
        'Инженерная графика': {
            
        },
        'Физика': {

        },
        'Химия': {
            'BQACAgIAAxkBAAID5WFSHdw8lDs5jFB6WGX86vFzfuyDAAJREgACuleQShrEbTaPzUIlIQQ': 'Лекция 1 - Закон термодинамики',
        },
        'История': {

        },
        'Экология': {

        },
        'Английский язык': {

        },
    },
    'Задания': {
        'Вышмат': {
            'BQACAgIAAxkBAAIEh2FSJbKDWxz3TXRivVCRej2yOqRAAAKNFQACSnCQSqdJoyShWVqSIQQ': 'Клетеник - Сборник задач по ан. геом.',
        },
        'Инженерная графика': {
            'BQACAgIAAxkBAAIEKWFSIqsIyLTlh9A174YHThVtwvTgAAJmEgACuleQSlx64qQRYWtcIQQ': 'Задание на семестр',
        },
        'Физика': {

        },
        'Химия': {

        },
        'История': {

        },
        'Экология': {

        },
        'Английский язык': {

        },
    },
    'ГДЗ': {
        'Вышмат': {

        },
        'Инженерная графика': {
            
        },
        'Физика': {

        },
        'Химия': {

        },
        'История': {

        },
        'Экология': {

        },
        'Английский язык': {

        },
    },
}
