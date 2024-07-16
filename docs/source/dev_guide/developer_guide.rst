Руководство разработчика
=================

Обзор модулей ПО
----------------

entrance
_________

.. automodule:: MRIphantom_desktop.src.entrance.entrance
    :members:

preprocess
____________

.. automodule:: MRIphantom_desktop.src.preprocess.registration
    :members:

.. automodule:: MRIphantom_desktop.src.preprocess.unpack
    :members:

segmentation
_____________

.. automodule:: MRIphantom_desktop.src.segmentation.process
    :members:

visualization
______________

.. automodule:: MRIphantom_desktop.src.visualization.histogram
    :members:

.. automodule:: MRIphantom_desktop.src.visualization.plots
    :members:

.. automodule:: MRIphantom_desktop.src.visualization.scatter2d
    :members:

.. automodule:: MRIphantom_desktop.src.visualization.scatter3d
    :members:

.. automodule:: MRIphantom_desktop.src.visualization.table
    :members:

.. automodule:: MRIphantom_desktop.src.visualization.viewer
    :members:

Инструкции по сборке ПО
-------------------

Для сборки приложения используется пакет PyInstaller и файл конфигурации app.spec (можно найти в корне репозитория).

Установка пакета PyInstaller:

.. code-block:: console

    $ pip install pyinstaller

Используйте файл конфигурации app.spec (можно найти в корне репозитория).
Файл app.spec используется пакетом PyInstaller для конфигурации процесса сборки приложения.

Начать процесс сборки:

.. code-block:: console

    $ pyinstaller app.spec


После завершения процесса сборки вы сможете найти исполняемые файлы программы в директории dist в корне проекта.
Точное расположения исполняемого файла может отличаться в зависимости от вашей операционной системы, а так же от сожержания файла app.spec.

Перед использованием приложения убедитесь, что оно функционирует без ошибок.

Отладка
----------

Специальный отладочный режим приложения запускается при указании системной переменной DEBUG=2.

.. code-block:: console

    $ export DEBUG=2

Отладочный режим отключает экран загрузки и другие излишние компоненты приложения.

Стайлгайд проекта
-------------

Основное
__________

Длина строки:
Желательно придерживаться длин строк менее 120 символов.

Линтеры
__________
Pylint
Flake8

Python
___________

Импорты:
- Standard library imports
- Related third party imports
- Local library specific imports

Docstring
____________

Необходимо написание докстрингов для основных классов, методов и функций приложения.
Обновляйте документацию.