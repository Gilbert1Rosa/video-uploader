import unittest
import upload


class MyTestCase(unittest.TestCase):

    def test_upload_video(self):
        upload.upload_video("C:\\Users\\Gilbert\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\qp71cu4y.Selenium",
                            'Some title', '/my/path')
        self.assertEqual(True, True)  # Test upload video


if __name__ == '__main__':
    unittest.main()
