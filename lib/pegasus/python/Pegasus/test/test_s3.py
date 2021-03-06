import unittest

from Pegasus import s3

class TestPaths(unittest.TestCase):
    def test_get_path_for_key(self):
        #s3.get_path_for_key(bucket, searchkey, key, output)
        self.assertEquals(s3.get_path_for_key("bucket", None, "foo", "baz"), "baz/foo")
        self.assertEquals(s3.get_path_for_key("bucket", None, "foo", "baz/"), "baz/bucket/foo")
        self.assertEquals(s3.get_path_for_key("bucket", None, "foo/bar", "baz"), "baz/foo/bar")
        self.assertEquals(s3.get_path_for_key("bucket", None, "foo/bar", "baz/"), "baz/bucket/foo/bar")
        self.assertEquals(s3.get_path_for_key("bucket", "foo", "foo/bar", "baz"), "baz/bar")
        self.assertEquals(s3.get_path_for_key("bucket", "foo", "foo/bar", "baz/"), "baz/foo/bar")
        self.assertEquals(s3.get_path_for_key("bucket", "foo", "foo/bar/boo", "baz"), "baz/bar/boo")
        self.assertEquals(s3.get_path_for_key("bucket", "foo/", "foo/bar", "baz"), "baz/bar")
        self.assertEquals(s3.get_path_for_key("bucket", "foo/", "foo/bar", "baz/"), "baz/foo/bar")
        self.assertEquals(s3.get_path_for_key("bucket", "foo/bar", "foo/bar", "baz"), "baz")
        self.assertEquals(s3.get_path_for_key("bucket", "foo/bar", "foo/bar/boo", "baz"), "baz/boo")
        self.assertEquals(s3.get_path_for_key("bucket", "foo/bar", "foo/bar/boo", "baz/"), "baz/bar/boo")
        self.assertEquals(s3.get_path_for_key("bucket", "foo/bar", "foo/bar/boo/moo/choo", "baz/"), "baz/bar/boo/moo/choo")
        self.assertEquals(s3.get_path_for_key("bucket", None, "foo/", "baz"), "baz/foo")
        self.assertEquals(s3.get_path_for_key("bucket", None, "foo", ""), "foo")
        self.assertEquals(s3.get_path_for_key("bucket", None, "foo/", ""), "foo")
        self.assertEquals(s3.get_path_for_key("bucket", None, "foo/bar", ""), "foo/bar")
        self.assertEquals(s3.get_path_for_key("bucket", "foo", "foo/", "baz"), "baz")
        self.assertEquals(s3.get_path_for_key("bucket", "foo/", "foo/", "baz"), "baz")
        self.assertEquals(s3.get_path_for_key("bucket", "foo", "foo/bar/", "baz"), "baz/bar")

    def test_get_key_for_path(self):
        #s3.get_key_for_path(infile, path, outkey):
        self.assertEquals(s3.get_key_for_path("/foo", "/foo", "baz/"), "baz/foo")
        self.assertEquals(s3.get_key_for_path("/foo/", "/foo", "baz/"), "baz/foo")
        self.assertEquals(s3.get_key_for_path("/foo/", "/foo/", "baz/"), "baz/foo")
        self.assertEquals(s3.get_key_for_path("/foo", "/foo/", "baz/"), "baz/foo")
        self.assertEquals(s3.get_key_for_path("/foo", "/foo/bar", "baz"), "baz/bar")
        self.assertEquals(s3.get_key_for_path("/foo", "/foo/bar", "baz/"), "baz/foo/bar")
        self.assertEquals(s3.get_key_for_path("/foo", "/foo/bar/baz", "baz/"), "baz/foo/bar/baz")
        self.assertEquals(s3.get_key_for_path("/foo", "/foo/bar/baz", "baz"), "baz/bar/baz")
        self.assertEquals(s3.get_key_for_path("/foo", "/foo/bar/baz", "baz/boo/"), "baz/boo/foo/bar/baz")
        self.assertRaises(Exception, s3.get_key_for_path, "/foo", "/foo/bar/baz", "")
        self.assertRaises(Exception, s3.get_key_for_path, "foo", "foo", "bar")
        self.assertRaises(Exception, s3.get_key_for_path, "/foo", "/bar", "bar")

if __name__ == '__main__':
    unittest.main()
