import pytest
from pages.login_page import LoginPage

@pytest.mark.smoke
def test_login_success(driver):
    """Verify that a valid user is able to log in successfully."""

    # Create page object
    login_page = LoginPage(driver)

    # Open login page
    login_page.open()

    # Perform login by entering valid username and password
    login_page.login("standard_user", "secret_sauce")

    #verify that user is redirected to products page
    assert login_page.is_logged_in(), "User should be logged in but is_logged_in() returned False"

@pytest.mark.smoke
@pytest.mark.parametrize(
    "username",
    [
        "standard_user",
        "problem_user",
        "performance_glitch_user",
        "error_user",
        "visual_user",
    ],
)

def test_login_multiple_users(driver,username):
    """
        Data-driven positive test:
        Verify that several valid user accounts can log in successfully.
        """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, "secret_sauce")
    assert login_page.is_logged_in(), (
        f"Login failed for a supposed valid user: username={username!r}"
    )

@pytest.mark.negative
@pytest.mark.parametrize(
    "username, password",
    [
        ("standard_user", "wrong_password"),
        ("wrong_user", "secret_sauce"),
        ("", "secret_sauce"),
        ("standard_user", ""),
    ],
)
def test_invalid_login_combinations(driver, username, password):
    """
        Data-driven negative login test:
        Try multiple invalid username/password combinations and
        verify that login does NOT succeed.
    """
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username,password)

    assert not login_page.is_logged_in(), (
        f"Login Unexpectedly succeeded for username={username!r} and password={password!r}"
    )

