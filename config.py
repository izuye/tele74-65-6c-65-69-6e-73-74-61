import os
from instaloader import Instaloader
class Config:
    API_ID = int(os.environ.get("API_ID", "7094855"))
    API_HASH = os.environ.get("API_HASH", "3062e6689983577670405ae0728d65f2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2054711839:AAEMpMIMnRII0yaVG3nwvCUZlC9K4C8UG5M") 
    USER = os.environ.get("INSTAGRAM_USERNAME", "aws_ind")
    OWNER = os.environ.get("OWNER_ID", "1319487019")
    INSTA_SESSIONFILE_ID = os.environ.get("INSTA_SESSIONFILE_ID", None)
    S = "0"
    STATUS = set(int(x) for x in (S).split())
    L=Instaloader()
    HELP="""
You can Download almost anything From your Instagram Account.

<b>What Can Be Downloaded?:</b>

1. Semua posting dari Profil apa pun. (Baik Publik dan Pribadi, untuk profil pribadi Anda harus menjadi pengikut.)
2. Semua Postingan dari feed Anda.
3. Cerita dari profil apa pun (Baik Publik maupun Pribadi, untuk profil pribadi Anda harus menjadi pengikut.)
4. DP profil apa saja (Tidak perlu difollow)
5. Daftar Pengikut dan Pengikut dari Profil apa pun.
6. Daftar pengikut yang mengikuti kembali nama pengguna yang diberikan.
7. Daftar pengikut yang tidak mengikuti kembali nama pengguna yang diberikan.
8. Kisah Pengikut Anda.
9. Tagged posting dari profil apapun.
10. Postingan Anda yang disimpan.
11. video IGTV.
12. Sorotan dari profil apa pun.
13. Setiap Postingan Publik dari Tautan (Post/Reels/IGTV)


<b>How to Download:</b>

Its Easy!!
You Need to login into your account by /login. 

You have two Options:

1. From Username:

Just send any instagram username.

For Example:
<code>samantharuthprabhuoffl</code>
<code>subin_p_s_</code>
<code>_chill_manh_7</code>


2. From URL:

You can also sent a post link to download the post or video.

For Example:
<code>https://www.instagram.com/p/CL4QbUiLRNW/?utm_medium=copy_link</code>


<b>Available Commands and Usage</b>

/start - Check wheather bot alive.
/restart - Restart the bot (If you messed up anything use /restart.)
/help - Shows this menu.
/login - Login into your account.
/logout - Logout of your account.
/account - Shows the details of logged in account.

/posts <username> - Download posts of any username. Use /posts to download own posts or <code> /posts <username> </code>for others.
Example : <code>/posts samantharuthprabhuoffl</code>

/igtv <username> - Download IGTV videos from given username. If no username given, downloads your IGTV.

/feed <number of posts to download> - Downloads posts from your feed.If no number specified all posts from feed will be downloaded.
Example: <code>/feed 10</code> to download latest 10 posts from feed.

/saved <number of posts to download> - Downloads your saved posts. If no number specified all saved posts will be downloaded.
Example: <code>/saved 10</code> to download latest 10 saved posts.

/followers <username> - Get a list of all followers of given username. If no username given, then your list will be retrieved.
Example: <code>/followers samantharuthprabhuoffl</code>

/followees <username> - Get a list of all followees of given username. If no username given, then your list will be retrieved.

/fans <username> - Get a list of of followees who follow back the given username. If no username given, your list will be retrieved.

/notfollowing <username> - Get a list of followees who is not following back the given username.

/tagged <username> - Downloads all posts in which given username is tagged. If nothing given your tagged posts will be downloaded.

/story <username> - Downloads all stories from given username. If nothing given your stories will be downloaded.

/stories - Downloads all the stories of all your followees.

/highlights <username> - Downloads highlights from given username, If nothing given your highlights will be downloaded.


"""
    HOME_TEXT = """
<b>Helo, [{}](tg://user?id={})

This is a bot of [{}](www.instagram.com/{}) to manage his Instagram account. 
I can only work for my master [{}](tg://user?id={}).
But you can Deploy the same bot for your use from the below source code.

Use /help to know What I can Do?</b>
"""
    HOME_TEXT_OWNER = """
<b>Helo, [{}](tg://user?id={})
I am your assistant to manage your Instagram account.

Use /help to know what I can do for you.</b>
"""

