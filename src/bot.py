import praw
import time
import config
import database
from random import randint

r = praw.Reddit(username=config.username,
                password=config.password,
                client_id=config.client_id,
                client_secret=config.client_secret,
                user_agent="me3thx Bot by /u/BadAthMOFO v0.1")

phrases_to_match = ['me too thanks', 'me too thx',
                    'me 2 thanks', 'me 2 thx', 'me2thx']

phrases_to_say = ['me three thanks', 'me 3 thanks',
                  'me three thx', 'me 3 thanks']


def run_bot():
    subreddit = r.subreddit('all')
    comments = subreddit.comments(limit=15)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = \
            any(string in comment_text for string in phrases_to_match)
        checkDatabase = database.checkDatabase(comment.id)
        if isMatch and checkDatabase is False:
            rand_int = randint(0, len(phrases_to_say) - 1)
            comment.reply(phrases_to_say[rand_int])
            database.addID(comment.id)
            print(comment.id)


while True:
    try:
        run_bot()
        time.sleep(10)
    except:
        print("Caught error")
        time.sleep(60 * 9)
