
Проект по ООП 

"Создание ядра интернет магазина на основе направления E-commerce"


Установка


		1. Убедитесь, что у вас установлен Python 3.6 или более поздняя версия.


Использование


		1. Скачайте файл данных и поместите его в папку data в корне проекта.


		2. Запустите основную программу:

python src/main.py


		3. После выполнения программа выведет результаты анализа на экран.



Структура проекта


		• 
data/ - расположение products.json

src/ - основной код проекта.

main.py - точка входа в приложение.

utils.py - Созданы классы 
Product и Category с атрибутами, реализована логика анализа файла Json.

		•
tests/test_utils.py - тестовые файлы.

Содержит тесты для всех основных функций проекта.
        
        • 


Тестирование:

Проект покрыт тестами на 94%. Чтобы запустить тесты, выполните команду:


pytest --cov=src --cov-report=html