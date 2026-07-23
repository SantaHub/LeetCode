from __future__ import annotations

from typing import List

class FSNode:
    def __init__(self, name: str, is_file: bool, children: dict[str,FSNode]) -> None:
        self.name = name
        self.is_file = is_file
        self.children = children
        self.content = ""


class FileSystem:
    root: FSNode
    def __init__(self) -> None:
        self.root = FSNode("/", False, {})

    def traverse(self, path: str) -> FSNode:
        current_node = self.root 
        if path == "/":
            return current_node
        for dir in path.split("/")[1:]:
            if dir in current_node.children:
                current_node = current_node.children[dir]
            else:
                break 
        return current_node

    def ls(self, path: str) -> List[str]:
        target_node = self.traverse(path)
        if target_node.is_file:
            return [target_node.name, target_node.content]
        if target_node.name !='/' and len(target_node.children) == 0:
            return [target_node.name]
        return sorted(target_node.children.keys())

    def mkdir(self, path: str) -> bool:
        parent_node = self.traverse(path)
        if parent_node.is_file :
            return False

        # Create the new directory node
        target_dir_name = path.split("/")[-1]
        end_node=FSNode(target_dir_name, False, {})

        # If parent_node is the same as the target dir, add the new node to parent_node
        # Else, handle parent_node is `/` case and case where name is not the special `/'
        if parent_node.name == target_dir_name:
            parent_node.children[target_dir_name]= end_node
        else:
            # Handle case special `/` case
            # Else, the normal case where parent_node is not a special `/` case
            if parent_node.name =="/" :
                new_path = path
            else :
                new_path = "".join(path.split(parent_node.name)[1:])
            #Create new node along with any parent node.
            for part in new_path.split("/")[1:]:
                if part : 
                    new_node = FSNode(part, False, {})
                    parent_node.children[part] = new_node
                    parent_node = new_node
                else:
                    continue
        return True

    def addContentToFile(self, filePath: str, content: str) -> None:
        # Create the parents if they don't exist
        target_node = self.traverse(filePath)
        if target_node.name != filePath.split(f"/")[-1]:
            self.mkdir(filePath)
            target_node = self.traverse(filePath)

        if target_node.is_file:
            target_node.content += content
        if not target_node.is_file and len(target_node.children) == 0:
            target_node.content = content
            target_node.is_file = True
        
    def readContentFromFile(self, filePath: str) -> str:
        target_node = self.traverse(filePath)
        if target_node.is_file:
            return target_node.content
        else:
            return ""
