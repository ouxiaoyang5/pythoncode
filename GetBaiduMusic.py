'''
Created on 2015年6月13日

@author: harry
'''
from urllib.request import urlopen, urlretrieve

def getUrl(url):
    divurl=url.split('/')
    musicnum=divurl[4]
    if not str.isdigit(musicnum):
        print("error")
        exit()
    codeurl="http://music.baidu.com/data/music/fmlink?songIds="+musicnum+"&type=flac"
    responsecode=urlopen(codeurl).read().decode('unicode-escape')
    last=".flac"
    if "flac" not in responsecode:
        codeurl="http://music.baidu.com/data/music/fmlink?songIds="+musicnum+"&type=mp3"
        responsecode=urlopen(codeurl).read().decode('unicode-escape')
        last=".mp3"
    cur1=responsecode.find("songLink")
    cur2=responsecode.find("?",cur1)
    httpurl=responsecode[cur1+11:cur2]
    divhttpurl=httpurl.split("\/")
    downloadnum=divhttpurl[5]
    downloadurl="http://musicdata.baidu.com/data2/music/"+downloadnum+"/"+downloadnum+last
    cur1=responsecode.find("songName")
    cur2=responsecode.find('"',cur1+11)

    name=responsecode[cur1+11:cur2]#.decode("unicode-escape")
#     http://musicdata.baidu.com/data2/music/124809493/124809493.flac
    print(downloadurl)
    return [downloadurl,name+last]

def downloadMusic(downloadurl,name):
    musicdata=urlretrieve(downloadurl,"C:\\Users\\harry\\Downloads\\"+name)
if __name__=='__main__':
    url=input("input the download url:")
    [downloadurl,name]=getUrl(url)#"http://music.baidu.com/song/40135172/download?fm=altg3"
    downloadMusic(downloadurl,name)
