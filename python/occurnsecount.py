text=input("enter a line ofm text")
word=text.split()
count={}
for w in word:
    if w in count:
        count[w]+=1
    else:
        count[w]=1
for words in count:
        print(words,":",count[words])
