class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        def pallindrom(y):
            str1=y[::-1]
            if(str1==y):
                return True
            else:
                return False
        def dfs(s,j,path,ans):
            if j==len(s):
                ans.append(path)
                return
            for i in range(j,len(s)):
                if pallindrom(s[j:i+1]):
                    dfs(s,i+1,path+[s[j:i+1]],ans)
        dfs(s,0,[],ans)
        return ans
