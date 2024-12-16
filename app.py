from flask import Flask, jsonify
import requests

app = Flask(__name__)

def get_follower_count():
    url = "https://tiktok.livecounts.io/user/search/dux.a_"
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'dnt': '1',
        'origin': 'https://tokcounter.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://tokcounter.com/',
        'sec-ch-ua': '"Chromium";v="130", "Opera";v="115", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 OPR/115.0.0.0'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            user_data = response.json().get('userData', [])[0]
            return {"number": user_data['stats']['followers']}
        else:
            return {"error": "Failed to fetch data", "status_code": response.status_code}
    except (KeyError, IndexError):
        return {"error": "Data Not Found"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/u1-follower-count', methods=['GET'])
def follower_count():
    """Endpoint to return follower count as JSON"""
    return jsonify(get_follower_count())

if __name__ == "__main__":
    app.run(debug=True)