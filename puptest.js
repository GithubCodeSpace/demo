// const puppeteer = require("puppeteer");

// (async () => {
//   const browser = await puppeteer.launch();
//   const page = await browser.newPage();
//   const tweetUrls = require("./tweets.json");

//   for (let i = 0; i < tweetUrls.length; i++) {
//     const tweetUrl = tweetUrls[i][0];
//     const authorName = tweetUrls[i][1];
//     await page.goto(tweetUrl, { waitUntil: "networkidle0" });

//     // Scroll down 20000 pixels
//     await page.evaluate(() => {
//       window.scrollBy(0, 20000);
//     });

//     // Wait for the tweets to load
//     await page.waitForSelector('[data-testid="tweet"]');

//     // Get the first 40 tweets in the thread that match the author name
//     const authorTweets = [];
//     let numTweets = 0;
//     while (
//       numTweets < 40 &&
//       (await page.$(
//         '[data-testid="tweet"] [data-testid="tweetText"]:last-of-type'
//       ))
//     ) {
//       await page.evaluate(() => {
//         window.scrollBy(0, 20000);
//       });
//       const tweets = await page.$$('[data-testid="tweet"]');
//       for (const tweet of tweets) {
//         const displayName = await tweet.$eval(
//           '[data-testid="tweet"] [data-testid="tweetAuthorName"]',
//           (el) => el.textContent
//         );
//         if (displayName.trim() === authorName) {
//           authorTweets.push(tweet);
//           numTweets++;
//         }
//       }
//     }

//     // Print the author's tweets in the thread
//     for (let j = 0; j < authorTweets.length; j++) {
//       const authorTweet = authorTweets[j];
//       const text = await authorTweet.$eval(
//         '[data-testid="tweet"] [data-testid="tweetText"]',
//         (el) => el.textContent
//       );
//       console.log(text.trim());
//     }
//   }

//   await browser.close();
// })();

// with Try and catch

const puppeteer = require("puppeteer");

(async () => {
  try {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();
    const tweetUrls = require("./tweets.json");

    for (let i = 0; i < tweetUrls.length; i++) {
      const tweetUrl = tweetUrls[i][0];
      const authorName = tweetUrls[i][1];
      await page.goto(tweetUrl, { waitUntil: "networkidle0" });

      
      // Wait for the tweets to load
      await page.waitForSelector('[data-testid="tweet"]');
      // Scroll down 20000 pixels
      await page.evaluate(() => {
        window.scrollBy(0, 20000);
      });


      // Get the first 40 tweets in the thread that match the author name
      const authorTweets = [];
      let numTweets = 0;
      while (
        numTweets < 40 &&
        (await page.$(
          '[data-testid="tweet"] [data-testid="tweetText"]:last-of-type'
        ))
      ) {
        await page.evaluate(() => {
          window.scrollBy(0, 20000);
        });
        const tweets = await page.$$('[data-testid="tweet"]');
        for (const tweet of tweets) {
          const displayName = await tweet.$eval(
            '[data-testid="User-Names"]',
            (el) => el.textContent
          );
          if (displayName.trim() === authorName) {
            authorTweets.push(tweet);
            numTweets++;
          }
        }
      }

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
  } catch (error) {
    console.error(error);
  }
})();
