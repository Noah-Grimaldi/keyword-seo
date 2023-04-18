# keywordSEO

DESCRIPTION - This is a Python standalone application which uses KeywordSheeter, pytrends, and PySimpleGUI to create a simple GUI app that takes a keyword input and returns [LSI](https://www.wordstream.com/blog/ws/2020/08/27/lsi-keywords "These are keywords that add context to your site so search engines can better categorize your content.") and [Long-Tail](https://www.wordstream.com/long-tail-keywords "These are more specific keywords that target niche demographics.") keywords to the user. The application also mentions where the user should place these keywords inside their website. One challenge I faced was attempting to work around a Google 429 error that would occur because of the mass amount of requests to Google.

INSTALLATION - You can either download the source code above (main.py) or you can download the executable [here](https://github.com/Noah-Grimaldi/keywordSEO/releases/tag/v1.0).

IMPORTANT - After clicking the SUBMIT button the program may take a couple seconds to process the requests and display the keyword results. (pytrends) - If you want to use proxies as you are blocked due to Google rate limit:

```
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), proxies=['https://34.203.233.13:80',], retries=2, backoff_factor=0.1, requests_args={'verify':False})
```

HOW TO USE - Usage of this program is quite simple; download the executable, run the program, enter 2-3 keywords about your current website topic, hit the SUBMIT button, and notice your LSI and Long-Tail keyword results in the multilines below. From there you can also place them in different places on your webpage according to the placements mentioned in the application.

> Long-Tail Keyword Placement: In a title tag, the first 100 words, an image alt text, an h1 tag, an h2 or h3 tag, and the last 100 words of your page.
> LSI Keyword Placement: In several places anywhere throughout the webpage.

CREDITS - Credit to [pytrends](https://pypi.org/project/pytrends/), [PySimpleGUI](https://www.pysimplegui.org/en/latest/), and [Keyword Sheeter](https://keywordsheeter.com/) for making this project extremely easy.
