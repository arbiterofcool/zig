from unittest import TestCase, skip
import python


class pythonTest(TestCase):
	def setUp(self):
		pass

	def tearDown(self):
		pass

	@skip('Tests not implemented')
	def test_something(self):
		self.assertTrue(False)
