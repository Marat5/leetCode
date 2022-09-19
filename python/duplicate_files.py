from collections import defaultdict
from typing import List


class Solution:
    # def getDirectoryPath(self, pathWithContent: str):
    #     separatorIndex = pathWithContent.find(" ")
    #     return pathWithContent[:separatorIndex]

    # def getFiles(self, pathWithContent: str):
    #     separatorIndex = pathWithContent.find(" ")
    #     return pathWithContent[separatorIndex + 1:]

    # def readFiles(self, directory, files: str, contentHashMap):
    #     i = 0
    #     currentName = ""
    #     currentContent = ""
    #     isWritingName = True
    #     while i < len(files):
    #         if files[i] == "(":
    #             isWritingName = False
    #             i += 1
    #             continue
    #         elif files[i] == ")":
    #             isWritingName = True
    #             fullPath = self.getFullPathToFile(directory, currentName)
    #             if currentContent in contentHashMap:
    #                 contentHashMap[currentContent].append(fullPath)
    #             else:
    #                 contentHashMap[currentContent] = [fullPath]
    #             currentName = ""
    #             currentContent = ""
    #             i += 2
    #             continue

    #         if isWritingName:
    #             currentName += files[i]
    #         else:
    #             currentContent += files[i]

    #         i += 1

    # def getFullPathToFile(self, directory, name):
    #     return f"{directory}/{name}"

    # def findDuplicate(self, paths: List[str]) -> List[List[str]]:
    #     # key is content value is array of paths
    #     contentHashMap = {}
    #     for p in paths:
    #         currentDirectory = self.getDirectoryPath(p)
    #         files = self.getFiles(p)
    #         self.readFiles(currentDirectory, files, contentHashMap)

    #     result = []
    #     for key in contentHashMap:
    #         if len(contentHashMap[key]) > 1:
    #             result.append(contentHashMap[key])

    #     return result

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentHashMap = defaultdict(list)
        result = []
        for p in paths:
            splitP = p.split(" ")
            directoryName = splitP[0]
            for i in range(1, len(splitP)):
                name, content = splitP[i].split("(")
                contentHashMap[content].append(f"{directoryName}/{name}")

        for key in contentHashMap:
            if len(contentHashMap[key]) > 1:
                result.append(contentHashMap[key])

        return result


# MORAL OF THE COMMENTED CODE - .split() works faster than iteration through the string

paths = ["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)",
         "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
print(Solution().findDuplicate(paths))
