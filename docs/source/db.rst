Работа с БД
===========

В проекте используется СУБД PostgreSQL. Для неё необходимо установить пакеты:

.. code-block:: bash

    sudo apt-get install postgresql postgresql-contrib

Для работы с PostgreSQL в  Python потребуется также и пакет. Данную команду лучше не выполнять, а установит все пакеты
из файлов в папке `requirements/`.

.. code-block:: bash

    pip install psycopg2-binary

После установки необходимых пакетов можно проверить активность PostgreSQL:

.. code-block:: bash

    sudo service postgresql status


Если процесс активен, то создать пустую БД. Для удобства создаём из скрипта ``create_db.sql``.

.. code-block:: bash

    cd backend
    sudo -u postgres psql
    \i create_db.sql

Далее создать пользователя, который будет root'ом в проекте. Можно также указать параметр ``--database gymstrength``,
если в настройках в ``DATABASES`` несколько БД. По умолчанию выбирается БД по ключу ``default``. Запомните свой пароль,
он понадобится ещё не раз!

.. code-block:: bash

    python manage.py createsuperuser --username admin --email gymstrength@gmail.com