Начало работы
=====

На данной странице есть вся необходимая информация для начала работы с программным обеспечением MRIphantom QA Solution.

Системные требования
--------------------

Программа совместима с современными операционными системами (Windows, MacOS и Linux).

Требования к ОС
__________________________

Windows: Windows 10 и выше.

macOS: macOS Big Sur (11) и выше.

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


Тестирование на удаленном рабочем столе
--------------------------

Для внутреннего пользования.

Установка VPN
________________________

Необходимо cкачать и установить WireGuard VPN по ссылке https://www.wireguard.com/install/

Добавьте файл конфигурации user*.conf в WireGuard VPN и активируйте его.

Подключение через Microsoft Remote Desktop
________________________

Установите Microsoft Remote Desktop

 Windows – https://apps.microsoft.com/detail/9wzdncrfj3ps?ocid=webpdpshare
 macOS – https://apps.apple.com/ru/app/microsoft-remote-desktop/id1295203466?mt=12

в графу “PC name” введите адрес: 172.18.113.2

Введите свой логин и пароль.

Запуск программы
________________________

Подключитесь к удаленному рабочему столу.

Для тестирования программы перейдите в корень диска С:\ и запустите от имени администратора файл MRI_QA_Solution.bat

Файлы для тестирования лежат в папке C:\MRI_QA_Solution\test_images