import requests
import datetime
import os

# 환경변수에서 Webhook URL 가져오기
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK_URL")

if not WEBHOOK_URL:
    print("❌ DISCORD_WEBHOOK_URL 환경 변수가 설정되지 않았습니다.")
    exit(1)

def send_discord_webhook():
    today = datetime.date.today().strftime("%Y-%m-%d")

    data = {
        "content": f"📢 {today}의 새로운 포럼 게시글입니다!",
        "embeds": [
            {
                "title": "오늘의 업데이트 🚀",
                "description": "이곳에 내용을 추가하세요.",
                "color": 5814783
            }
        ]
    }

    response = requests.post(WEBHOOK_URL, json=data)

    if response.status_code == 204:
        print("✅ 메시지가 성공적으로 전송되었습니다.")
    else:
        print(f"❌ 오류 발생: {response.status_code}, 응답 내용: {response.text}")

if __name__ == "__main__":
    send_discord_webhook()
