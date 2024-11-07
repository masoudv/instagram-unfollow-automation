# Instagram Unfollow Automation Script

This Python script automates the process of unfollowing Instagram accounts by sorting the followings list from oldest to newest and unfollowing them in that order. **Please use this script responsibly and be aware of Instagram's limitations to avoid potential restrictions on your account.**

## Features
- Logs in to your Instagram account.
- Extracts and sorts your followings list.
- Automatically unfollows accounts based on the specified order.

## Requirements
- Python 3.x
- Chrome browser
- ChromeDriver (matching your Chrome browser version)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/masoudv/instagram-unfollow-automation.git
   cd instagram-unfollow-automation
   ```

2. **Install dependencies**:
   Make sure you have the necessary Python libraries installed. You can install them using:
   ```bash
   pip install selenium beautifulsoup4
   ```

3. **Download ChromeDriver**:
   - Download the ChromeDriver for your operating system [here](https://chromedriver.chromium.org/downloads).
   - Make sure the version matches your installed Chrome browser version.
   - Place the downloaded `chromedriver` file in the project folder or update the path in the script.

## Usage

1. **Configure your login credentials**:
   Open `instagram_unfollow.py` and replace the following variables with your Instagram login details:
   ```python
   username = "your_username"
   password = "your_password"
   ```

2. **Run the script**:
   ```bash
   python instagram_unfollow.py
   ```

3. **Adjust the unfollow limit**:
   By default, the script will unfollow only the first 10 accounts for testing purposes. You can modify this limit in the code:
   ```python
   for following in followings[:10]:  # Adjust the limit as needed
       unfollow_user(following)
   ```

### Important Notes
- **Rate Limits**: Instagram imposes rate limits, so unfollowing too many users in a short time can result in temporary or permanent restrictions. It’s recommended to keep unfollowing sessions moderate.
- **Responsibility**: This script is for educational purposes only. Use it responsibly and be aware of Instagram's rules.
- **Privacy**: Ensure your login information is stored securely. Avoid sharing sensitive details in public repositories.

## Disclaimer
This project is not affiliated with Instagram and is for educational purposes only. Use at your own risk.

## License
[MIT](https://opensource.org/licenses/MIT)
