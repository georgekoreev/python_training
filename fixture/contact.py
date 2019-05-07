
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contacts(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add next").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # edit
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()


    def create_contact(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.sname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contacts()

