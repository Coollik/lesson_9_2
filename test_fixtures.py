import pytest


@pytest.fixture()
def browser():
    print('Выполнено перед тестом (setup)')

    yield "browser"

    print('Выполнено после теста (teardown)')


@pytest.fixture()
def login_page(browser):
    pass


@pytest.fixture()
def credentials():
    return "admin", "12345"


def test_login(login_page, credentials):
    assert credentials == ('admin', '12345'), "Ошибка в логине или пароле"
