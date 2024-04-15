# -*- coding: utf8 -*-
import requests  # 数据请求库第三方库
import re  # 正则模块
import json
import sys

# 伪装请求头方式/请求头参数
headers = {
    'cookie': 'douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; bd_ticket_guard_client_web_domain=2; xgplayer_user_id=192062668567; my_rd=2; passport_csrf_token=77f06fedd46c41abf499fc03864da20d; passport_csrf_token_default=77f06fedd46c41abf499fc03864da20d; odin_tt=f267d144efc7f3794e3604b8b96b59c751b44259bd7590b22858da836648216af8570b314728236f1ef1255732f5d224b4cf9e64071177cb5b1395eda14123d0998281206792f512ff4897419b974652; _tea_utm_cache_6383={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22}; dy_swidth=1920; dy_sheight=1080; strategyABtestKey=%221710244827.962%22; csrf_session_id=b54618ad921b0a5bf59d200a29478170; _tea_utm_cache_1300={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22android%22%2C%22utm_campaign%22:%22client_share%22}; ttcid=d624853a1f3d43eb949df7714969717a12; FORCE_LOGIN=%7B%22videoConsumedRemainSeconds%22%3A180%2C%22isForcePopClose%22%3A1%7D; download_guide=%223%2F20240312%2F0%22; pwa2=%220%7C0%7C3%7C0%22; __live_version__=%221.1.1.8649%22; webcast_local_quality=null; live_use_vvc=%22false%22; live_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCQk5DcFBaMnRRTEJieWpkVnh0ZE9zbEhTVVFicWt3TEV5cWVMTWQ1S25SYmRhTk90L0F4WTRzZGxjUWpJMFE0MUlPZlFzNFpGaXNxWUhqa3ptYTNVRk09IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoxfQ%3D%3D; douyin.com; device_web_cpu_core=4; device_web_memory_size=8; architecture=amd64; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Atrue%2C%22volume%22%3A0.7%7D; ttwid=1%7C7bQmTeECs9_Ob2Izwp-OIquMl1NkDKuTmkKrBskOjNc%7C1710246235%7Cf6aa32fc5f68e0784bca21a2f49de9929970794098b361bf2fba23a8d84a7f18; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A1%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A4%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; home_can_add_dy_2_desktop=%221%22; msToken=BgRJ-Ie8IqTH9CFQrubjNl1CQzCBRaWZBZ3wxc5YHRR2be0IuqdwpGeCXMJxmAZwej932SQYC2BzGeo8VApJW5w7LouFGFy_Puvmmm6Kww_LuZ9OG4IbNoboAiA=; tt_scid=o7B45EQEai7Ugd-GBw8MpkjXvcNFu.k1gI5ZxG92aimfn5fb4Ok7v4sIQ2s75lexbe9e; msToken=3K3CYASH_Zc2ekOSdfAn02AWr5zuAl8at33Gxk1-UAtZgXUilsAus2lWiiWsSpcNt-uoxQ3tj8Ui_J7Cdv6OLE9QKka63nGytu0AfBvOR4uwL5M85LFJyFNvOoY=; IsDouyinActive=false; __ac_nonce=065f10fc500d709a2f577; __ac_signature=_02B4Z6wo00f01tTrMnQAAIDB6UIo6xB2owrUyzbAANDYAkMXlTOe1N-pHBOn1dOsI8VXY0xvh-r1rPVhwMjeLvAJJ22MR7WqBYxipaV3cRbzDG77ymXbcAvWjGhDfY48CbH-ZQJ793Ew3lyb53; __ac_referer=https://www.douyin.com/video/7341755601363406107/?app=aweme&did=MS4wLjABAAAAAEc27NQ8hRuPEdbRetpI1WXFEZlDzO7Rr3HeMlOY-9HSVrB4EFygdzx331iaT2xe&from_aid=1128&from_ssr=1&iid=MS4wLjABAAAALn1lFXk2wSzII1Ct8APLFwvEtY44m5YYPAT5i5kYLhEFYjFhHQK8eq_rlF6ZD4mb&mid=7341757252635757322&region=CN&share_sign=nF4.ewgPyD_h6YciFkh2jMqus2vKN1uGmOYV4lhoRdI-&share_version=290000&titleType=title&ts=1710243786&u_code=1488mi817&utm_campaign=client_share&utm_medium=android&utm_source=copy&with_sec_did=1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70 '
}


def DyVideoCraw(url):
    response = requests.get(url=url, headers=headers)
    # 获取网页源代码
    # print(response.text)
    try:
        html_date = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', response.text)[0]
        html_date = requests.utils.unquote(html_date)
        # print(html_date)
        # 解析出标题
        title_data = re.findall('"desc":"(.*?)","', html_date)[0]
        # print(title_date)
        # 解析出封面
        cover_data = 'https:' + re.findall('originCover":"(.*?)","', html_date)[0]
        # print(cover_date)
        # 解析出视频地址
        date1 = re.findall('playAddr(.*?),', html_date)[0]
        video_url = 'https:' + re.findall('"src":"(.*?)"}', date1)[0]
        # print(video_url)
        video_obj = {
            "type": "video",
            "video": video_url,
            "title": title_data,
            "cover": cover_data
        }
        r_data = json.dumps(video_obj)
        print(r_data)
    except IndexError:
        print("1")




def DyImageCraw(url):
    response = requests.get(url=url, headers=headers)
    # 获取网页源代码
    # print(response.text)
    try:
        html_date = re.findall('<script id="RENDER_DATA" type="application/json">(.*?)</script', response.text)[0]
        html_date = requests.utils.unquote(html_date)
        # print(html_date)
        # 解析出标题
        title_date = re.findall('"desc":"(.*?)","', html_date)[0]
        # print(title_date)
        # 解析出图片地址
        date1 = re.findall('"images":\[(.*?)],"imageInfos"', html_date)[0]
        date1 = re.findall('"urlList":\["(.*?)"],"downloadUrlList', date1)
        images_list = []
        for i in date1:
            images_list.append(i.split('","')[0])
        images_obj = {
            "type": "image",
            "images": images_list,
            "title": title_date
        }
        r_data = json.dumps(images_obj)
        print(r_data)
    except IndexError:
        print("1")


if __name__ == '__main__':
    a = ["https://www.douyin.com/video/7318178603940760859/?region=CN&mid=7318179380683918089&u_code=0&did=MS4wLjABAAAAO7zp5lRhHMYEzaXATjAEQGUCMV1tqqs1YCYoasf0yF_GsrzWERSPb0JQuBciayRY&iid=MS4wLjABAAAANwkJuWIRFOzg5uCpDRpMj4OX-QryoDgn-yYlXQnRwQQ&with_sec_did=1&titleType=title&share_sign=nT_T2Ucui.hiFZWOqM.xCDC1AnwcbS7pp5hrFzUr_zY-&share_version=170400&ts=1711288180&from_aid=6383&from_ssr=1&from=web_code_link"]
    for i in range(1, len(sys.argv)):
        a.append(sys.argv[i])
        # print(a[0])
    if a[0][23:28]=='video':
        DyVideoCraw(a[0])
    else:
        DyImageCraw(a[0])
