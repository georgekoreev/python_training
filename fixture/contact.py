from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_contacts(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add next").click()

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # open modification form
        wd.find_elements_by_xpath("(//img[@alt='Details'])")[index].click()
        # select modify
        wd.find_element_by_css_selector('input[name="modifiy"]').click()
        # fill contact form
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element_by_css_selector('input[name="update"]').click()
        self.contact_cache = None

    # взято для отладки с урока
    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        #self.select_contact_by_index(index)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

        #wd.find_elements_by_xpath("(//img[@alt='Details'])")[index].click()
        #wd.find_element_by_css_selector('input[name="modifiy"]').click()
        #self.fill_contact_form(new_contact_data)
        #wd.find_element_by_css_selector('input[name="update"]').click()
        #self.contact_cache = None

    # взято для отладки с урока
    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        #self.select_contact_by_index(index)
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

        #wd = self.app.wd
        #self.open_contacts_page()
        #self.select_contact_by_index(index)
        #wd.find_elements_by_xpath("(//img[@alt='Details'])")[index].click()
        #wd.find_element_by_css_selector('input[name="modifiy"]').click()
        #self.fill_contact_form(new_contact_data)
        #wd.find_element_by_css_selector('input[name="update"]').click()
        #self.contact_cache = None

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, mobilephone=mobilephone,
                       workphone=workphone, secondaryphone=secondaryphone)

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
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # select first contact
        #wd.find_element_by_name("selected[]")[index].click()
        # edit
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        self.contact_cache = None

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_contacts()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
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

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2], secondaryphone=all_phones[3]))
        return list(self.contact_cache)






