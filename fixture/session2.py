class SessionHelper:

    def __init__(self, kon):
        self.kon = kon


    def login(self, username, password):
        wd = self.kon.wd
        self.kon.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()


    def logout(self):
        wd = self.kon.wd
        wd.find_element_by_link_text("Logout").click()