const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  const tweetUrls = require("./tweets.json");

  for (let i = 0; i < tweetUrls.length; i++) {
    const tweetUrl = tweetUrls[i][0];
    const authorName = tweetUrls[i][1];
    await page.goto(tweetUrl, { waitUntil: "networkidle0" });

    // Wait for the tweets to load
    await page.waitForSelector('[data-testid="tweet"]');

    // Get all the tweets in the thread
    const tweets = await page.$$('[data-testid="tweet"]');

    // Filter out the replies made by other users
    const authorTweets = tweets.filter(async (tweet) => {
      const displayName = await tweet.$eval(
        '[data-testid="tweet"] [data-testid="tweetAuthorName"]',
        (el) => el.textContent
      );
      return displayName.trim() === authorName;
    });

    // Print the author's tweets in the thread
    for (let j = 0; j < authorTweets.length; j++) {
      const authorTweet = authorTweets[j];
      const text = await authorTweet.$eval(
        '[data-testid="tweet"] [data-testid="tweetText"]',
        (el) => el.textContent
      );
      console.log(text.trim());
    }
  }

  await browser.close();
})();
