from selenium import webdriver
import unittest

class UdacityJobsHiringPartners(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_udacity_hiring_partners(self):
        driver = self.driver
        driver.get("https://career-resource-center.udacity.com/")
        self.assertIn("Career Resource Center", driver.title)
        driver.find_element_by_link_text("Jobs with Udacity Hiring Partners").click()


    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
