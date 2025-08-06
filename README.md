# Проект Marketplace

Проект реализует классы, необходимые для функционирования
интернет-магазина.

## Описание

В проекте в пакете src реализованы классы:
1. Класс Product (модуль product).
2. Класс Category (модуль category).

## Установка

1. Клонируйте репозиторий:
```commandline
git clone https://github.com/aleks-stellar/Marketplace
```
2. Установите зависимости:
```commandline
poetry install
```

## Использование

1. Запустите модуль main в корневой директории.
2. Следуйте инструкциям.

## Тестирование

1. Для тестирования проекта введите команду:
```commandline
pytest --cov src
```
2. Для проверки проекта линтерами введите команду:
```commandline
flake8 src
mypy src
isort src

flake8 tests
mypy tests
isort tests
```
