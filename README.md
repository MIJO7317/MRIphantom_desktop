# Десктопное приложение MRIphantom <img alt="project_icon" height="25" src="assets/icons/MRIphantom_icon.ico" width="25"/>

Приложение для анализа геометрических отклонений МРТ изображений для планирования радиохирургии.

## Как запустить?



### Готовые релизы

TODO

### Запуск из источников

_При запуске текущей версии из источников могут возникать баги. Относительно стабильные версии находятся в релизах._

1. Клонировать репозиторий себе на ПК.
2. Установить Python 3.12.
2. В директории проекта создать виртуальное окружение командой

```python
python -m venv venv
```
и активировать его (Linux, MacOS)

```bash
source venv/scripts/activate
```

или (Windows)
```PS
./venv/Scripts/Activate.ps1
```


3. Установить необходимые пакеты с помощью requirements.txt

```python
pip install -r requirements.txt
```
4. Запустить приложение командой

```python
python app.py
```

## Документация

TODO readthedocs+sphinx
