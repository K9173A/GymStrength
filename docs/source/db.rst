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

Создание БД
-----------
Если процесс активен, то создать пустую БД. Для удобства создаём из скрипта ``create_db.sql``. В этом скрипте также
создаётся и пользователь, которому будет открыт доступ к БД. В скрипт необходимо передать пароль пользователя. Запомните
его, он может потребоваться в дальнейшей работе!

.. code-block:: bash

    cd backend
    sudo -u postgres psql -f scripts/create_db.sql -v v1="my_password"

Необходимо пояснить, что для работы с БД создаются два пользователя, специфика которых на первый взгляд может показаться
похожей, но на деле они предназначены для разных целей:

* Пользователь, который создаётся через PostgreSQL, необходим для доступа к БД от лица приложения Django. Поэтому данные пользователя и прописываются в `settings.py` в `DATABASES`. Вместе с созданием данного пользователя мы устанавливаем его права по отношению к БД.
* Пользователь, который создаётся через Django, необходим для доступа внутрь самой БД, чтобы работать с данными. Права, связанные с данным пользователем позволяют получить доступ к админке Django (`django.admin.site`).

Далее необходимо выполнить миграции моделей из приложений Django:

.. code-block:: bash

    python manage.py makemigrations authapp
    python manage.py makemigrations gymapp
    python manage.py migrate

Создать суперпользователя Django. Можно указать параметр ``--database gymstrength``, если в настройках в ``DATABASES``
несколько БД. По умолчанию выбирается БД по ключу ``default``. Запомните свой пароль, он понадобится ещё не раз!

.. code-block:: bash

    python manage.py createsuperuser --username gymadmin --email gymstrength@gmail.com

Пересоздание БД
---------------
Сделать дамп данных. Флаг ``-e`` позволяет исключить данные из дампа:

.. code-block:: bash

    python manage.py dumpdata -e=sessions -e=contenttypes -e=auth -e=authapp -e=admin -o dump.json

Удалить БД:

.. code-block:: bash

    cd backend
    sudo -u postgres psql -f scripts/delete_db.sql

Пересоздать БД по алгоритму из предыдущего раздела. Залить нужные дампы в БД:

.. code-block:: bash

    python manage.py loaddata dumps/my_dump.json.

