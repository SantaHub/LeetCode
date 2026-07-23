# 588. Design In-Memory File System

Design a data structure that simulates an in-memory file system.

Implement the `FileSystem` class:

- `FileSystem()` — Initializes the object of the file system.
- `ls(path)` — If `path` is a **file** path, return a list containing only that file's name. If `path` is a **directory** path, return the list of file and directory names in this directory. The answer should be in **lexicographical order**.
- `mkdir(path)` — Given a directory path that does not exist, make a new directory. If intermediate directories do not exist, create them as well. Return type is void.
- `addContentToFile(filePath, content)` — If the file does not exist, create it. Append the given content to the file. Return type is void.
- `readContentFromFile(filePath)` — Return the content of the file.

You can assume:

- All file contents are strings and file operations are saved in memory.
- Paths use `/` as the directory separator; paths begin with `/` and are absolute.
- You will not receive invalid operations (e.g. read a missing file).

## Example

```
Input:
["FileSystem", "ls", "mkdir", "ls", "mkdir", "ls", "ls", "addContentToFile", "ls", "ls", "addContentToFile", "ls"]
[[], ["/"], ["/a/b/c"], ["/"], ["/a/b/c/d"], ["/a/b/c"], ["/a/b/c/d"], ["/a/b/c/d", "hello"], ["/"], ["/a/b/c/d"], ["/a/b/c/d", " world"], ["/a/b/c/d"]]

Output:
[null, [], null, ["a"], null, ["d"], ["d"], null, ["a"], ["d", "hello"], null, ["d", "hello world"]]
```

## Hints

- Model the filesystem as a **tree** (often a trie): each node is a file or directory.
- Store children in a map keyed by name; sort keys when listing.
- `mkdir` and `addContentToFile` both need to create missing parent directories.
- For `ls` on a file path, return only the file's name (last path component).

## Practice

Edit `solution.py` and run tests:

```bash
pytest
```

Debug in Cursor: open `solution.py`, set breakpoints, run **Debug Tests** or **Debug Current Test File**.
