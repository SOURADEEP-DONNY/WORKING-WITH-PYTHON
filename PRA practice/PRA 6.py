class Chapter:
    def __init__(self,Subject,Pages,Marks,Name):
        self.Subject=Subject
        self.Pages=Pages
        self.Marks=Marks
        self.Name=Name

class Exam:
    def __init__(self,examName,chapterList):
        self.examName=examName
        self.chapterList=chapterList

    def findMaximumChapterByPage(self):
        l=[]
        l2=[]
        for i in chapterList:
            l.append(i.Pages)
        maxi=max(l)
        for i in chapterList:
            if maxi==i.Pages:
                l2.append(i.Subject)
                l2.append(i.Pages)
                l2.append(i.Marks)
                l2.append(i.Name)
        return l2
    def sortChapterByMarks(self):
        l=[]
        for i in chapterList:
            l.append(i.Marks)
        l.sort()
        if l:
            return l
        else:
            return None
if __name__=='__main__':
    n=int(input())
    chapterList=[]
    for i in range(n):
        Subject=input()
        Pages=int(input())
        Marks=int(input())
        Name=input()
        o=Chapter(Subject,Pages,Marks,Name)
        chapterList.append(o)
    obj=Exam("EXAM",chapterList)
    res1=obj.findMaximumChapterByPage()
    res2=obj.sortChapterByMarks()
    if res1:
        for i in res1:
            print(i)
    else:
        print("No  Chapter Found")
    if res2:
        for i in res2:
            print(i)
    else:
        print("Not Found")
        
