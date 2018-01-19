import unittest
import os
from  aviatrix3 import Aviatrix

class Aviatrix_Test(unittest.TestCase):
    def test_init(self):
        #Gather Environmental Variables
        controller_ip = os.environ.get("TEST_CONTROLLER_IP")
        username = os.environ.get("TEST_USERNAME")
        private_ip = os.environ.get("TEST_PRIVATE_IP")
        admin_email = os.environ.get("TEST_ADMIN_EMAIL")
        password = os.environ.get("TEST_PASSWORD")
        #Execution
        controller=Aviatrix(controller_ip)
        #Tests
        self.assertIs(type(controller.controller_ip),str)
        self.assertEqual(controller.controller_ip,controller_ip)
        self.assertEqual(controller.CID, "")
    def test_login(self):
        #Gather Environmental Variables
        controller_ip = os.environ.get("TEST_CONTROLLER_IP")
        username = os.environ.get("TEST_USERNAME")
        private_ip = os.environ.get("TEST_PRIVATE_IP")
        admin_email = os.environ.get("TEST_ADMIN_EMAIL")
        password = os.environ.get("TEST_PASSWORD")
        #Execution
        controller=Aviatrix(controller_ip)
        controller.login(username,private_ip)
        #Tests
        self.assertIsNot(controller.result['results'].find('has been authorized successfully'),-1)
        #Negative Tests
        #Execution
        controller=Aviatrix(controller_ip)
        controller.login(username,password)
        self.assertEqual(controller.results,'User name/password does not match')

if __name__ == '__main__':
  unittest.main()
