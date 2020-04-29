from tpblite import TPB


t = TPB()
torrents = input("Search for a torrent: ")
torrentList = t.search(torrents)
for torrent in torrentList:
    print(torrent.magnetlink)

