"""
   Module covers iOS screens' elements
"""

all_editfields = 'XCUIElementTypeTextField'
all_buttons = 'XCUIElementTypeButton'
all_textviews = 'XCUIElementTypeStaticText'

# NEW LOGISTRATION SCREEN
new_logistration_logo = 'XCUIElementTypeImage'
new_logistration_discover_courses_button = 'Discover Courses'
new_logistration_sign_in_button = 'Sign In'
new_logistration_register_button = 'Register'
old_logistration__signup_button = 'Sign up and start learning'

# Login Screen
login_title_textview = 'Sign In'
# XCUIElementTypeImage type="XCUIElementTypeImage" name="logo.png"
#  label="edX" enabled="true" visible="true" x="31" y="71"
# width="313" height="175"/>
login_edx_logo = ''
# ==XCUIElementTypeTextField type="XCUIElementTypeTextField"
#  value="User name or e-mail address"name="user-field" label=""
#  enabled="true" visible="true" x="42" y="266" width="291" height="40"/>
login_user_name_editfield = 'XCUIElementTypeTextField'
# XCUIElementTypeSecureTextField type="XCUIElementTypeSecureTextField"
# value="Password" name="password-field" enabled="true" visible="true"
#  x="42" y="314" width="291" height="40"/
login_password_editfield = 'XCUIElementTypeSecureTextField'
login_forget_password_textview = ''
# XCUIElementTypeStaticText type="XCUIElementTypeStaticText"
# value="Or Sign in with" name="Or Sign in with" label="Or Sign
# in with" enabled="true" visible="true" x="134"y="459" width="107"
#  height="20"/
login_signin_divider_textview = 'Or Sign in with'
# XCUIElementTypeButton type="XCUIElementTypeButton" name="Sign In"
#  label="Sign In" enabled="true"visible="true" x="36" y="407"
#  width="303" height="40"/
login_singin_button = 'Sign In'
# XCUIElementTypeButton type="XCUIElementTypeButton"
# name="Register with Facebook" label="Register with Facebook"
#  enabled="true" visible="true" x="204" y="491" width="102"
#  height="30"/
login_facebook_textview = 'Facebook'
# XCUIElementTypeButton type="XCUIElementTypeButton" name="Register
#  with Google" label="Register with Google" enabled="true"
# visible="true" x="69" y="491" width="102" height="30"/>
login_google_textview = 'Google'
# XCUIElementTypeStaticText type="XCUIElementTypeStaticText"
# value="By signing in to this app, you agree to the"
# name="By signing in to this app, you agree to the"
# label="By signing in to this app, you agree to the"
# enabled="true" visible="true" x="88" y="549" width="199" height="13"/
login_agree_textview = 'By signing in to this app, you agree to the'
# XCUIElementTypeLink type="XCUIElementTypeLink"
# name="By signing in to this app, you agree to the,edX Terms of Service and Honor Code"
# label="By signing in to this app, you agree to the,edX Terms of Service and Honor Code"
# enabled="true" visible="true" x="99" y="560" width="177" height="21"/
login_terms_textview = ('By signing in to this app, you agree to the,' 
                            'edX Terms of Service and Honor Code')
# WHATS NEW SCREEN
whats_new_title_textview = 'Version 2.12.1, New Features'
# XCUIElementTypeButton type="XCUIElementTypeButton" name="Close" label="Close" enabled="true"
# visible="true" x="345" y="22" width="30" height="28"/>
whats_new_close_button = 'XCUIElementTypeButton'
# XCUIElementTypeImage type="XCUIElementTypeImage" name="screen_1" enabled="true" visible="true"
#  x="25" y="68" width="325" height="388"/>
whats_new_main_image = 'XCUIElementTypeImage'
# <XCUIElementTypeStaticText type="XCUIElementTypeStaticText" value="Updated Navigation"
#  name="Updated Navigation" label="Updated Navigation" enabled="true" visible="true"
# x="25" y="472" width="325" height="25"/>
whats_new_feature_title_textview = ''
# <XCUIElementTypeStaticText type="XCUIElementTypeStaticText"
# value="A simplified main menu makes it easier to access and discover courses."
# name="A simplified main menu makes it easier to access and discover courses."
# label="A simplified main menu makes it easier to access and discover courses."
# enabled="true" visible="true" x="25" y="505" width="325" height="50"/>
whats_new_feature_details_textview = ''
whats_new_done_button = 'Done'

# MY DASHBOARD SCREEN
main_dashboard_title_textview = 'My Courses'
# <XCUIElementTypeButton type="XCUIElementTypeButton" name="navigation-bar-button"
#  label="Navigation Menu" enabled="true" visible="true" x="5" y="26" width="38"
# height="30"/>
main_dashboard_navigation_icon = 'XCUIElementTypeButton'
main_dashborad_drawer_account_textview = 'ACCOUNT'

# MY ACCOUNT SCREEN
account_logout_option = 'Logout'

# REGISTER SCREEN
register_title_textview = 'Register'

# DISCOVERY SCREEN
discover_courses_title_textview = 'Discover'
