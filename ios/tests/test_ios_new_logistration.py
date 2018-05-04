"""
    New Logistration Test Module
"""
import pytest

from common import strings
from ios.pages.ios_new_logistration import IosNewLogistration


@pytest.mark.skip(reason="New Logistration screen is replaced by New Landing Screen")
class TestIosNewLogistration(object):
    """
    New Logistration screen's Test Cases
    """

    def test_start_new_logistration_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify New Logistration screen is loaded successfully
        """

        ios_new_logistration_page = IosNewLogistration(set_capabilities, setup_logging)
        setup_logging.info('-- Starting {} Test Case'.format(TestIosNewLogistration.__name__))
        assert ios_new_logistration_page.load_app().text == strings.NEW_LOGIS_DISCOVER_COURSES

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify "edX logo", "Discover Courses", "Register" & "Sign In"
                      fields are visible on screen 
                Verify all screen contents have their default values
        """

        ios_new_logistration_page = IosNewLogistration(set_capabilities, setup_logging)

        assert ios_new_logistration_page.get_edx_logo().text == strings.NEW_LOGIS_EDX_LOGO
        assert ios_new_logistration_page.get_discover_course_button().text == strings.NEW_LOGIS_DISCOVER_COURSES
        assert ios_new_logistration_page.get_register_button().text == strings.NEW_LOGIS_REGISTER
        assert ios_new_logistration_page.get_signin_button().text == strings.NEW_LOGIS_LOGIN

    def test_back_and_forth_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify tapping "Sign In" loads Sign In screen
                Verify tapping back icon from 'Sign In' screen navigate user
                    back to 'New Logistration' screen.
                Verify tapping "Register" loads Register screen
                Verify tapping back icon from 'Register' screen navigate user
                    back to 'New Logistration' screen. 
                Verify tapping "Discover Courses" loads Discovery screen
                Verify tapping back icon from 'Discover Courses' screen
                    navigate user back to 'New Logistration' screen.
        """

        ios_new_logistration_page = IosNewLogistration(set_capabilities, setup_logging)

        assert ios_new_logistration_page.back_and_forth_login()
        assert ios_new_logistration_page.back_and_forth_register()
        assert ios_new_logistration_page.back_and_forth_discover_courses()
        setup_logging.info('-- Ending {} Test Case'.format(TestIosNewLogistration.__name__))
