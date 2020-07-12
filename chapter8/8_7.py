def make_album(输入歌手名字,输入专辑名字,输入歌曲数=0):
    """创建一个音乐专辑字典"""
    album_dic = {
        '歌手名': 输入歌手名字,
        '专辑名': 输入专辑名字,
    }

    if 输入歌曲数:
        album_dic['歌曲数'] = 输入歌曲数
    
    return album_dic

message1 = "\n请输入'结束'来终止程序"
message2 = '请输入歌手名字: '
message3 = '请输入专辑名字: '
active = True

while active:
    print(message1)
    artist_name = input(message2)
    if artist_name == '结束':
        break
    album_name = input(message3)
    if album_name == '结束':
        break
    
    album_dic1 = make_album(artist_name,album_name)
    print(album_dic1)