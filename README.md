# GeekStreak-Twitter-bot
Automate your GeekStreak tweeting workflow with this command-line tool. After tackling a #gfg160 challenge, instantly share your achievement from the terminal by providing the image path. The script handles hashtagging, counting days and tagging @geeksforgeeks, making posting seamless.

[Know more about gfg160](https://x.com/geeksforgeeks/status/1857321074993549547)
## Features
- ✏️ Tags users and adds hashtags automatically
- 🕒 Track day progression using a local JSON file

## Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/ArujAnand/GeekStreak-Twitter-bot
cd GeekStreak-Twitter-bot
````
### 2. Install Dependencies
```bash
pip install tweepy python-dotenv
```
### 3. Create .env File
Create a file named .env in the root directory and add your Twitter API credentials:
```basb
CONSUMER_KEY=your_consumer_key
CONSUMER_SECRET=your_consumer_secret
ACCESS_TOKEN=your_access_token
ACCESS_TOKEN_SECRET=your_access_token_secret
```
How to Get These Keys:
1. Go to [Twitter/X Developer Portal](https://developer.x.com/en)
2. Create a project and an app (u might also get one by default)
3. Under User Authentication Settings enable:
   - App Type: ```bash Web App```
   - Callback URL: ```bash http://localhost/``` or any dummy URL
   - Permissions: ```bash Read and Write```
