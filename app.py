from tpblite import TPB

t = TPB()
file = open("Torrent List.txt", "w+")
torrents = input("Search for a torrent: ")
torrentList = t.search(torrents)
for torrent in torrentList:
    file.write(str(torrent) + "\n")
    file.write(str(torrent.magnetlink) + "\n\n")
