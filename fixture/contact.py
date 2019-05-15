
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contacts(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add next").click()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # open modification form
        wd.find_element_by_css_selector('img[alt="Details"]').click()
        # select modify
        wd.find_element_by_css_selector('input[name="modifiy"]').click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_css_selector('input[name="update"]').click()

    def edit_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        # select details
        wd.find_element_by_css_selector('img[alt="Details"]').click()
        # select modify
        wd.find_element_by_css_selector('input[name="modifiy"]').click()
        # submit updating
        wd.find_element_by_css_selector('input[name="update"]').click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # edit
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contacts()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.name)
        self.change_field_value("lastname", contact.sname)
        self.change_field_value("address", contact.address)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

