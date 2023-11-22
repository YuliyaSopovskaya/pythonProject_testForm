## Ссылка на страницу Text Box: [https://demoqa.com/text-box](https://demoqa.com/text-box)

## Форма: Text Box 
## Задание: Написать фреймворк для тестирования этой формы с использованием шаблона проектирования PageObject.

## План: 
1. Заполнить все поля рандомными данными (можно использовать дополнительные библиотеки).
2. Нажать кнопку Submit.
3. Сравнить введенные данные с полученными данными из поля, в котором будут все заполненные данные.

## Инструкции по установке зависимостей:
```bash
pip install selenium
pip install faker

Selenium WebDriver ChromeDriver  #установка драйвера для Chrome
pip install -r requirements.txt #создать зависимости


pytest main.py # запуск
