from biz.web import EBPortal
import pytest
from config import Web_Config



@pytest.mark.parametrize("username,password",
    [
        ("Invalid User","Invalid Password"),
    ]
)
def test_login(username,password):
    
    eb=EBPortal()
    eb.pg_home.navigate()
    eb.pg_home.lnk_login.click()
    
    eb.pg_login.txt_username=username
    eb.pg_login.txt_password=password
    
    eb.pg_login.btn_login.click()
    
    assert Web_Config.WEB_LOGIN_URL in eb.pg_login.page.url,"Page has navigated away from the login page"
    assert eb.pg_login.lbl_message.text_content() in ("Your login attempt was not successful. Please try again." ,"Your account has been locked.\nContact your administrator or unlock your account.")
    
