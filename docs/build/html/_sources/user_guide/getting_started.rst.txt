Начало работы
=====

На данной странице есть вся необходимая информация для начала работы с программным обеспечением MRIphantom QA Solution.

Системные требования
--------------------

Программа совместима с современными операционными системами (Windows, MacOS и Linux).

Требования к ОС
__________________________

Windows: Windows 10 и выше.

macOS: macOS Big Sur (11) и выше (поддерживаются Apple Silicon (процессоры серии M-) и Intel).

Linux: любой поддерживаемый LTS дистрибутив, например, Ubuntu 18.04 и старше.

Требования к аппаратной части
________________________

ОЗУ: 4GB минимум.

Установка из источников
--------------------------

Клонируйте репозиторий MRIphantom на свою локальную машину:

.. code-block:: console

   $ git clone git@gitlab.com:bzavolovich/MRIphantom_desktop.git

Убедитесь, что у вас установлена версия Python 3.9 или выше.

Создайте виртуальное окружение в директории проекта, выполнив следующую команду в консоли:

.. code-block:: console

    $ python -m venv venv

Активируйте виртуальное окружение (Linux, macOS):

.. code-block:: console

    $ source venv/scripts/activate

или (Windows):

.. code-block:: console

    ./venv/Scripts/Activate.ps1

Установите необходимые пакеты, используя файл requirements.txt:

.. code-block:: console

    $ pip install -r requirements.txt

Запустите приложение:

.. code-block:: console

    $ python app.py

