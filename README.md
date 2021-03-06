# WEB_project_2
A web resource where you can save links to interesting sites and group them by topic

Веб-ресурс, где можно сохранять ссылки на интересные сайты и группировать их по темам

Лучшие сайты, отобранные вручную!

Цель проекта. Создать веб – ресурс в котором можно сохранять ссылки на интересные сайты, группировать их по темам.
Идея. В настоящее время в интернете существует огромного количество разнообразных сайтов. Для поиска нужной нам информации мы привыкли пользоваться поиском или использовать каталоги ссылок на разные сайты, например, Яндекс Радар - https://radar.yandex.ru/. Иногда мы находим действительно интересные и полезные сайты, ссылки на которые хотим сохранить.  Пользоваться для этого закладками в браузере не очень удобно. Можно использовать специализированные ресурсы или сделать такой ресурс самому. Дополнительно на таком ресурсе можно выложить отобранные вручную ссылки на интересные и полезные сайты.

Реализованный функционал:

* Показ ссылок на сайты, разбитые на темы неавторизованным пользователям с возможностью фильтрации сайтов по темам.

* Регистрация пользователей.

* Администратор сайта (пользователь с id = 1) может добавлять темы и описание ссылок на сайты в базу данных используя веб интерфейс. Добавленные им темы и ссылки будут видны всем пользователям ресурса (авторизованным и не авторизованным). Может редактировать описание ссылок на сайты и темы групп сайтов. Может удалять сайты и темы. Реализована защита удаления темы группы сайтов – если есть хоть один сайт с такой темой, то тему удалить не получится. 

* Авторизованные пользователи также могут добавлять, редактировать и удалять свои темы и сайты, группировать сайты по своему усмотрению. Темы и сайты, добавленные пользователями не видны другим пользователям (в текущей версии, через веб-интерфейс, они не видны и администратору). Пользователи могут редактировать и удалять только свои темы и сайты. Они могут скрывать сайты, добавленные администратором.

* Сайты могут дублироваться. Это сделано с учётом того что в личных сборниках ссылок пользователей будут одинаковые сайты.
Темы сайтов сортируются в лексикографическом порядке во всех используемых формах. При добавление новых тем порядок автоматически меняется.

* Добавлена статистика и лозунг сайта, который виден только неавторизованным пользователям.

Лозунг сайта. Сохрани лучшие сайты для себя! Создавай свои темы, сохраняй ссылки на интересные сайты. Ваши темы и ссылки на сайты видны только вам! Для создания и управления своей коллекцией ссылок необходима регистрация.
Проект получился вполне рабочим. В дальнейшем планирую развивать этот проект. Идей для развития проекта много.

Доступ при локальном запуске: http://127.0.0.1:5000/0/0
Пользователи № 1: admin почта: admin@mail.ru, пароль: 12345, пользователь № 2: user_1 почта: user_1@mail.ru, пароль: 12345
Ссылка на сайт в интернете: https://best-sites-selected-manually.herokuapp.com/ (на момент сдачи не работает, буду исправлять)

Реализован запуск с адреса: http://127.0.0.1:5000
