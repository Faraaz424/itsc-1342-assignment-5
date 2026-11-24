
# Faraaz Syed / Assignment 5

import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "code"))

from solution import sanitize_ip_list


class TestSanitizeIPList(unittest.TestCase):

    def test_remove_blocked_ip(self):
        ip_list = ["192.168.1.1", "10.0.0.1", "192.168.1.1"]
        result = sanitize_ip_list(ip_list, "192.168.1.1")
        self.assertEqual(result, ["10.0.0.1"])

    def test_remove_consecutive_blocked_ips(self):
        ip_list = ["1.1.1.1", "2.2.2.2", "2.2.2.2", "3.3.3.3"]
        result = sanitize_ip_list(ip_list, "2.2.2.2")
        self.assertEqual(result, ["1.1.1.1", "3.3.3.3"])

    def test_replace_invalid_ip(self):
        ip_list = ["192.168.1.1", "invalid_ip", "10.0.0.5"]
        result = sanitize_ip_list(ip_list, "8.8.8.8")
        self.assertEqual(result, ["192.168.1.1", "0.0.0.0", "10.0.0.5"])

    def test_keep_valid_ips(self):
        ip_list = ["8.8.8.8", "1.1.1.1"]
        result = sanitize_ip_list(ip_list, "9.9.9.9")
        self.assertEqual(result, ["8.8.8.8", "1.1.1.1"])

    def test_original_list_unchanged(self):
        ip_list = ["invalid_ip", "2.2.2.2", "2.2.2.2"]
        original = ip_list.copy()
        sanitize_ip_list(ip_list, "2.2.2.2")
        self.assertEqual(ip_list, original)


if __name__ == "__main__":
    unittest.main()