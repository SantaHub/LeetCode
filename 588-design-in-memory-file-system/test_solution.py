import pytest

from solution import FileSystem


def test_empty_root():
    fs = FileSystem()
    assert fs.ls("/") == []


def test_leetcode_example():
    fs = FileSystem()
    assert fs.ls("/") == []

    fs.mkdir("/a/b/c")
    assert fs.ls("/") == ["a"]

    fs.mkdir("/a/b/c/d")
    assert fs.ls("/a/b/c") == ["d"]
    assert fs.ls("/a/b/c/d") == ["d"]

    fs.addContentToFile("/a/b/c/d", "hello")
    assert fs.ls("/") == ["a"]
    assert fs.ls("/a/b/c/d") == ["d", "hello"]

    fs.addContentToFile("/a/b/c/d", " world")
    assert fs.ls("/a/b/c/d") == ["d", "hello world"]
    assert fs.readContentFromFile("/a/b/c/d") == "hello world"


def test_mkdir_creates_intermediate_dirs():
    fs = FileSystem()
    fs.mkdir("/x/y/z")
    assert fs.ls("/") == ["x"]
    assert fs.ls("/x") == ["y"]
    assert fs.ls("/x/y") == ["z"]


def test_lexicographical_order():
    fs = FileSystem()
    fs.mkdir("/dir/z")
    fs.mkdir("/dir/a")
    fs.addContentToFile("/dir/m.txt", "m")
    assert fs.ls("/dir") == ["a", "m.txt", "z"]


def test_append_content():
    fs = FileSystem()
    fs.addContentToFile("/f", "a")
    fs.addContentToFile("/f", "b")
    fs.addContentToFile("/f", "c")
    assert fs.readContentFromFile("/f") == "abc"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
