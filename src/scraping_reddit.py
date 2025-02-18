# -*- coding: utf-8 -*-
"""scraping_reddit.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cJHOuENR-xtWi3erlfNM6vOginA4rY6-
"""

if 'google.colab' in str(get_ipython()):
  from google.colab import drive
  drive.mount('/content/drive')
  basepath = '/content/drive/MyDrive/MY_WEBSITE/Reddit-Complexity-LLM'
else:
  basepath = '/Users/prachidalal/Desktop/MY\ WEBSITE/Reddit-Complexity-LLM'

pip install asyncpraw

pip install --upgrade asyncpraw

import asyncpraw
import asyncio

CLIENT_ID = "JvY7agmByFJ92ES5tIq2bA"
CLIENT_SECRET = "x0B3d-JzpPPPLhh51bpq-vQd_jCSJw"
USER_AGENT = "MyScraper by u/WayReasonable3297"
PASSWORD = "DDDaanceDance!123"
USERNAME = "WayReasonable3297"

# Initialize asyncpraw with client ID and secret
reddit = asyncpraw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    password=PASSWORD,
    user_agent=USER_AGENT,
    username=USERNAME,
)

print(await reddit.user.me())
reddit.read_only = True

# This function fetches subreddit info and post titles
async def fetch_subreddit_info():
    # Access the subreddit
    subreddit = await reddit.subreddit("dallas")

    await subreddit.load()

    # Print the subreddit info
    print(f"Subreddit Display Name: {subreddit.display_name}")
    print(f"Subreddit Title: {subreddit.title}")
    print(f"Subreddit Description: {subreddit.description}\n")

    # Fetch the hottest 10 submissions
    async for submission in subreddit.hot(limit=10):
        print(f"Submission Title: {submission.title}")
        print(f"Submitted by: {submission.author.name if submission.author else 'Deleted'}\n")

# Running the asyncio event loop to execute the function
await fetch_subreddit_info()

# Async function to scrape submissions and comments
async def scrape_subreddit(subreddit_name, max_submissions=10):
    # Create an async PRAW Reddit instance
    reddit = asyncpraw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT
    )

    # Get the subreddit
    subreddit = await reddit.subreddit("dallas")

    print(f"Scraping the top {max_submissions} submissions from r/{subreddit_name}...\n")
    async for submission in subreddit.top(limit=max_submissions):
        print(f"Title: {submission.title}")
        print(f"Author: {submission.author}")
        print(f"Score: {submission.score}")
        print(f"URL: {submission.url}")
        print("Comments:")

        # Fetch comments from the submission
        await submission.load()  # Ensure the submission's comments are loaded
        submission.comments.replace_more(limit=0)

        for comment in submission.comments.list():
          if isinstance(comment, asyncpraw.models.Comment):  # Ensure it's a Comment object
              print(f"  - {comment.body[:100]}...")  # Display the first 100 characters of the comment

        print("\n" + "-" * 50 + "\n")

   # Close the Reddit instance
    await reddit.close()

# The `main` function to call the scraper
async def main(subreddit_name, max_submissions):
    await scrape_subreddit(subreddit_name, max_submissions)

await main("learnpython", 5)