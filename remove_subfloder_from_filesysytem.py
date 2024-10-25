# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result=[]
        for i in folder:
            if not result or not i.startswith(result[-1]+'/'):
                result.append(i)

        return result


