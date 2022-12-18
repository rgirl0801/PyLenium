import time


def test_carlos_is_on_leadership(py):
    py.visit('https://www.demoblaze.com/index.html')
    py.get('#login2').hover()
    py.get('#login2').click()
    py.get('#loginusername').type('KateFox1')
    py.get('#loginpassword').type('KateFox')
    py.get('[onclick="logIn()"]').click()
    time.sleep(2)
    assert py.get('#nameofuser').should().contain_text('Welcome')