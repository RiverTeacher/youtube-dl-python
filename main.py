import requests

def get_video_info(video_url):
    api_url = f"https://youtubedownloader-api.onrender.com/youtube-video/?url={video_url}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        video_info = data['response']
        return video_info
    else:
        return None

def main():
    video_url = input("最初に動画のURLを入力してください: ")
    video_info = get_video_info(video_url)
    
    if video_info:
        print("動画情報:")
        print(f"タイトル: {video_info['title']}")
        print(f"説明: {video_info['description']}")
        print(f"視聴回数: {video_info['viewCount']}")
        print(f"カテゴリ: {video_info['category']}")
        print(f"公開日: {video_info['publishDate']}")
        print(f"チャンネル名: {video_info['channelName']}")
        print(f"チャンネル登録者数: {video_info['subscriberCount']}")
        print("動画URL:")
        for video in video_info['videos']:
            if video['hasAudio']:
                print(video['url'])
    else:
        print("動画情報を取得できませんでした。")

if __name__ == "__main__":
    main()
