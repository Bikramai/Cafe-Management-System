import unittest
from application.control.UserProfileController import CreateUserProfileController


class CreateUserProfileTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.controller = CreateUserProfileController(database_path="../application/entity/database.db")

    def test_createUserProfile(self):
        row_id = 7
        job_title = "Resturant Branch 2 Manager"
        desc = "Some desc"

        self.controller.createUserProfile(job_title, desc)

        added_profile = self.controller.entity.getUserProfile(row_id)
        self.assertIsNotNone(added_profile)
        self.assertEqual(added_profile[3], desc)
        self.assertEqual(added_profile[10], job_title)


if __name__ == '__main__':
    unittest.main()