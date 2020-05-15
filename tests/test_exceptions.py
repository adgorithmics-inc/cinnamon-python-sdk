import unittest

from cinnamon_sdk import CinnamonException


class TestExceptions(unittest.TestCase):
    def test_error_code_functionality(self):
        class FakeResponse:
            def json(self):
                return {"errors": [{"extensions": { "code": "hello"}}]}
        err = CinnamonException(message="test",query="test",variables={},headers={},token="", response=FakeResponse())
        self.assertEqual(err.error_codes, ["hello"])


    def test_error_code_functionality_does_not_crash_on_bad_return(self):
        class FakeResponse:
            def json(self):
                return {"errors": "nerp"}
        err = CinnamonException(message="test",query="test",variables={},headers={},token="", response=FakeResponse())
        self.assertEqual(err.error_codes, [])

    def test_error_code_functionality_does_not_crash_on_bad_errors(self):
        class FakeResponse:
            def json(self):
                return {"errors": [{"extensions": "burp"}]}
        err = CinnamonException(message="test",query="test",variables={},headers={},token="", response=FakeResponse())
        self.assertEqual(err.error_codes, [])
