import pytest
#фекстуры как пред условия в тесте setup
@pytest.fixture
def browser():
    print("Выполняюсь перед тестом, например открываю браузер")

    yield
    print("Выполняюсь после теста")

@pytest.fixture
def main_page(browser):
    pass


def test_first(browser, user, main_page):
    assert 1 == 1
    assert 1 == 2, "Ожидалось другое значение"



def test_second():
    pass

from selene.support.shared import browser
from selene import be, have

#время на прогрузку 8 секунд
browser.config.timeout = 8

#чтоб закрывался после каждого теста
def teardown_function():
    browser.quit()

def test_valid_login():
    browser.open('https://demoqa.com/text-box')
    browser.element('[id="userName"]').should(be.blank).type('Andy').press_enter()
    browser.element('[id="userEmail"]').should(be.blank).type('123@mail.ru').press_enter()
    browser.element('[id="currentAddress"]').should(be.blank).type('Vladivostok Vatutina 4').press_enter()
    browser.element('[id="submit"]').press_enter()
    browser.element('[id="output"]').should(
        have.text('Name:Andy\nEmail:123@mail.ru\nCurrent Address:Vladivostok Vatutina 4'))

   # test_valid_login()

def test_invalid_login():
    browser.open('https://demoqa.com/text-box')
    browser.element('[id="userName"]').should(be.blank).type('Elvi').press_enter()
    browser.element('[id="userEmail"]').should(be.blank).type('124@mail.ru').press_enter()
    browser.element('[id="currentAddress"]').should(be.blank).type('Vladivostok Vatutina 5').press_enter()
    browser.element('[id="submit"]').press_enter()
    browser.element('[id="output"]').should(
        have.text('Name:Andy\nEmail:123@mail.ru\nCurrent Address:Vladivostok Vatutina 4'))
