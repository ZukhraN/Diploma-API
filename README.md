<h1> Проект по тестированию сайта Petstore</h1>

> <a target="_blank" href="https://petstore.swagger.io/">Ссылка на сайт</a>

![Homepage](./resources/screenshots/Homepage.png)

### Список проверок:
* Создание нового питомца
* Получение списка питомцев по статусам (available, pending, sold)
* Удаление питомца

### Особенности проекта:
* Проверки проводятся для неавторизованного пользователя
* В телеграм приходят оповещения о результатах прохождения тестов
* Сборка проекта осуществляется через Jenkins 
* Отчеты в Allure Report
----

### Используемый стэк

<img title="Python" src="./resources/icons/python.png" height="40" width="40"/> <img title="Pytest" src="./resources/icons/pytest.png" height="40" width="40"/> <img title="Pycharm" src="./resources/icons/pycharm.png" height="40" width="40"/> <img title="Jenkins" src="./resources/icons/jenkins.png" height="40" width="40"/> <img title="GitHub" src="./resources/icons/github.png" height="40" width="40"/> <img title="Allure Report" src="./resources/icons/allure_report.png" height="40" width="40"/> <img title="Allure TestOps" src="./resources/icons/allureTestOps.png" height="40" width="40"/>

----

## Проект в Jenkins
> <a target="_blank" href="https://github.com/ZukhraN/Diploma-API/">Ссылка на проект в Jenkins</a>

Наш проект возможно запускать через Jenkins. Доступны следующие параметры сборки:
* `environment` - параметр позволяет выбрать окружение, на котором будут запущены тесты
* `comment` - параметр позволяет выбрать комментарий из предложенных


#### Шаги для запуска автотестов через Jenkins

1. Открыть страницу <a target="_blank" href="https://jenkins.autotests.cloud/job/hdrezka_ui_project/">проекта</a>
2. В меню выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке
4. Выбрать комментарий
5. Нажать кнопку `Build`

После прохождения автотестов в Build History будет доступен отчет

![Jenkins build](./resources/screenshots/Build.png)

----

### Allure отчет
#### Общие результаты

На странице с общими результатами мы можем увидеть общее количество тестов, сколько из них были успешными и сколько не успешными

![Allure_report_example](./resources/screenshots/allure_report_result.png)

#### Отчет прохождения теста

В отчете для каждого кейса есть проверка на статус запроса, проверка jsonschema

![Allure_suites_test](./resources/screenshots/allure_suites.png)


----

### Allure TestOps

Общий список всех кейсов, имеющихся в системе

![Allure_suites_test](./resources/screenshots/allure_testops_results.png)

Пример dashboard с общими результатами тестирования

![Allure_suites_test](./resources/screenshots/dashboard.png)

