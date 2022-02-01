import re
n = int(input())
for i in range(n):
    line = input()
    pattern = r"href=\"\S*\""
    pattern2 = r"\>[a-zA-Z][\w\s\.]*\<|\>\s\<"
    link = re.findall(pattern,line)
    name = re.findall(pattern2,line)
    if len(link)>0 and len(name)>0:
        for i in range(len(link)):
            print(link[i].replace("\"","").replace("href=","")+"," + name[i].replace("<","").replace(">",""))


