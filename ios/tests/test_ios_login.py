
"""
    Login Test Module
"""

from common import strings
from common.globals import Globals
from ios.pages.ios_login import IosLogin
from ios.pages.ios_new_landing import IosNewLanding


class TestIosLogin(object):
    """
    Login screen's Test Case
    """

    def test_start_login_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Login screen is loaded successfully
        """

        setup_logging.info('-- Starting {} Test Case'.format(TestIosLogin.__name__))

        ios_new_landing_page = IosNewLanding(set_capabilities, setup_logging)
        assert ios_new_landing_page.load_login_screen().text == strings.LOGIN

        setup_logging.info('Login screen successfully loaded')

    def test_ui_elements(self, set_capabilities, setup_logging):
        """
        Verify following contents are visible on screen, 
            "Back icon", "Sign In" Title, "User name or e-mail address" label, User Name edit-field
            Password edit-field, "Forgot your password?" option, "Sign In" button,
            "Or sing in with" label, "Facebook" button, "Google" button,
            "By signing in to this app, you agree to the" label ,
            "edX Terms of Service and Honor Code" option
        Verify all screen contents have their default values

        """

        ios_login_page = IosLogin(set_capabilities, setup_logging)

        # Commenting it temporarily, it should be fix with LEARNER-4409
        # textview_screen_title = ios_login_page.get_title_textview()
        # assert textview_screen_title
        # assert textview_screen_title.text == strings.LOGIN_SCREEN_TITLE

        assert ios_login_page.get_logo().text == strings.LOGIN_EDX_LOGO
        assert ios_login_page.get_username_editfield().text == strings.LOGIN_USER_NAME_WATER_MARK
        assert ios_login_page.get_password_editfield().text == strings.LOGIN_PASSWORD_WATER_MARK
        assert ios_login_page.get_forget_password_textview().text == strings.LOGIN_FORGOT_PASSWORD
        assert ios_login_page.get_sign_in_button().text == strings.LOGIN
        assert ios_login_page.get_login_with_email_divider_textview().text == strings.LOGIN_IOS_WITH_EMAIL_DIVIDER
        assert ios_login_page.get_facebook_textview().text == strings.LOGIN_FACEBOOK_OPTION
        assert ios_login_page.get_google_textview().text == strings.LOGIN_GOOGLE_OPTION
        assert ios_login_page.get_agree_textview().text == strings.LOGIN_AGREE
        assert ios_login_page.get_terms_textview().text == strings.LOGIN_IOS_TERMS

    def test_login_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can login with valid Username and Password
        """

        global_contents = Globals(setup_logging)
        ios_login_page = IosLogin(set_capabilities, setup_logging)
        login_output = ios_login_page.login(global_contents.login_user_name, global_contents.login_password).text

        assert login_output == strings.WHATS_NEW_IOS_SCREEN_TITLE

        setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))
        setup_logging.info('-- Ending {} Test Case'.format(TestIosLogin.__name__))
