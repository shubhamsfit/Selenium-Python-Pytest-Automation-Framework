import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize(
    "username,password",
    [
        ("aayush.batra@simplefixit.com", "password"),       # Replace with a valid test account
        ("invalid_user@example.com", "wrong") # Invalid test case
    ]
)
def test_login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)

    if username == "testuser@123":
        assert login_page.is_logged_in(), "Expected login to succeed but it failed"
    else:
        assert not login_page.is_logged_in(), "Expected login to fail but it succeeded"
