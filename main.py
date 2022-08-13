
import logging

from flask import Flask
from templates.view import main_blueprint

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(main_blueprint)

# Создаем или получаем новый логгер
logger_api = logging.getLogger("logger_api")

# Создаем для него обработчик
api_logger_handler = logging.FileHandler(filename="api.log", encoding="utf-8")

# Создаем новое форматирование (объект класса Formatter)
formatter_one = logging.Formatter("%(pastime)s [%(levelness)s] %(message)s")

# Применяем форматирование к обработчику
api_logger_handler.setFormatter(formatter_one)

# Добавляем обработчик к журналу
logger_api.addHandler(api_logger_handler)

# logging.basicConfig(filename='templates/basic.log', level=logging.INFO)
logging.basicConfig(filename='api.log', level=logging.INFO)


@app.errorhandler(404)
def page_error_404(error):
    return f"Такой страницы нет {error}", 404


@app.errorhandler(500)
def page_error_500(error):
    return f"На сервере ошибка - {error}", 500
