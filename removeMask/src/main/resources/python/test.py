import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3904.108 Safari/537.36",
}


def get_share_url(url):
    try:
        r = requests.get(url, headers=headers, allow_redirects=False)
        return r.headers['location']
    except Exception as e:
        print("解析失败")
        print(e)


def get_video_url(url):
    if not url:
        return

    try:
        vid = url.split("/?")[0].split("video/")[1]
        xhr_url = f'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids={vid}'

        r = requests.get(xhr_url, headers=headers).json()
        video_url = r['item_list'][0]['video']['play_addr']['url_list'][0]
        return video_url

    except Exception as e:
        print("解析失败")
        print(e)


def download_video(url, name):
    if not url:
        return

    try:
        r = requests.get(url, headers=headers)
        with open(name + '.mp4', 'wb') as f:
            f.write(r.content)
        print("下载完成")

    except Exception as e:
        print("下载失败")
        print(e)


if __name__ == "__main__":
    while 1 < 2:
        # 抖音APP分享的短链接
        url = input("请输入抖音视频链接: ")
        # url = "https://v.douyin.com/R4tKg6C/"
        name = input("请给视频起个名字吧: ")
        share_url = get_share_url(url)
        video_url = get_video_url(share_url)
        download_video(video_url, name)
        print("去除水印完成!")
