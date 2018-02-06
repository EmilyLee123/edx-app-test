"""
    Whats New Test Module
"""

from input_data import InputData
from common.globals import Globals
from android.pages.android_whats_new import AndroidWhatsNew


class TestAndroidWhatsNew:
    """
    Whats New screen's Test Case
    """

    def test_start_whats_new_smoke(self, login, setup_logging):
        """
        Scenarios:
            Verify Whats New screen is loaded successfully
        """

        log = setup_logging
        log.info('-- Starting {} Test Case'.format(TestAndroidWhatsNew.__name__))
        if login:
            log.info('{} is successfully logged in'.format(InputData.login_user_name))

    def test_validate_ui_elements(self, set_capabilities, setup_logging):
        """
        Scenarios:
                Verify following contents are visible on screen, 
                    "Screen Title", "Cross Icon", "Main Feature Image",
                     "Feature Title", "Feature Details", "Done"
                Verify all screen contents have their default values
        """

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)

        textview_screen_title = android_whats_new_page.get_title_textview()
        assert textview_screen_title is not None

        assert android_whats_new_page.get_cross_icon() is not None

        assert android_whats_new_page.get_main_image() is not None

        textview_feature_title = android_whats_new_page.get_feature_title_textview()
        assert textview_feature_title is not None

        textview_feature_details = android_whats_new_page.get_feature_details()
        assert textview_feature_details is not None

        button_done = android_whats_new_page.get_done_button()
        assert button_done is not None

    def test_close_features_screen_smoke(self, set_capabilities, setup_logging):
        """
        Verifies that user can close New Feature screen and move to Main Dashboard screen
        """
        log = setup_logging

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        assert android_whats_new_page.exit_features() == Globals.VIEW_MY_COURSES_ACTIVITY_NAME

        log.info('-- Ending {} Test Case'.format(TestAndroidWhatsNew.__name__))
