import os
import django
from flask import Flask, render_template_string

# Настройка Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_django.settings")
django.setup()

# Импорт модели из Django
from app.models import NewsModel

app = Flask(__name__)

@app.route('/')
def index():
    news = NewsModel.objects.all()  # Получаем все новости из Django ORM
    return render_template_string("""
    <h1>Новости</h1>
    <ul>
      {% for item in news %}
        <li><b>{{ item.title }}</b>: {{ item.description }}</li>
      {% endfor %}
    </ul>
    """, news=news)

if __name__ == '__main__':
    # Запуск Flask-сервера с доступом для других пользователей в сети
    app.run(host='0.0.0.0', port=5000)
