from pytube import YouTube

while True:
    print("\n Çıkış yapmak için Q tuşuna basabilirsin.")
    link = input("İndirilecek video url adresi: ")

    if "https://www.youtube.com/" in link.lower():
        yt = YouTube(link)

        yd = yt.streams.get_highest_resolution()

        yd.download('./video')
    elif link.upper() == "Q":
        break
    else:
        print("hatalı giriş, tekrar dene")
