import pytest


@pytest.fixture(scope="session")
def user():
    print("Тестовый пользователь перед тестом")

    yield
    print("Откатываем тестового пользователя")

#выполняется после теста, например очистка и закрытие браузера (в джаве befo after) yield
#фикстура выполняемая один раз для всех тестов scope="session", так же можно для функции scope="function" или модуля scope="module"
