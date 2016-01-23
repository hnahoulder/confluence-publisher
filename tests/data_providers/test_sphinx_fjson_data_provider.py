from unittest import TestCase
import os

from conf_publisher.data_providers.sphinx_fjson_data_provider import SphinxFJsonDataProvider


class SphinxFJsonDataProviderTestCase(TestCase):

    tests_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_get_source_1(self):
        result = SphinxFJsonDataProvider().get_source('file')
        expected = os.path.join(self.tests_root, 'docs/build/json/file.fjson')

        self.assertEqual(expected, result)

    def test_get_source_2(self):
        result = SphinxFJsonDataProvider(root_dir='./', base_dir='result').get_source('file')
        expected = os.path.join(self.tests_root, 'result/file.fjson')

        self.assertEqual(expected, result)

