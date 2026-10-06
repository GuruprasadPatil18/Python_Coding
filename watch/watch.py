"""
Problem:
Ask the user for a line of HTML and, if it has a YouTube iframe, print the short youtu.be link of the video. Example: "https://www.youtube.com/embed/xvFZjo5PgG0"
becomes "https://youtu.be/xvFZjo5PgG0". If there is no YouTube iframe, print None.

Approach:
I made a parse() function that uses re.search to look for an iframe with a src that has youtube.com/embed/ in it. The part after "embed/"
is the video id, which I get from the match group. If there is a match, I return "https://youtu.be/" with the id added. If not, I return None.
In main() I take the input and print the result.
"""

import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    matches = re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([^"]+)"', s)

    if matches:
        video_id = matches.group(1)
        return "https://youtu.be/" + video_id
    else:
        return None

if __name__ == "__main__":
    main()
