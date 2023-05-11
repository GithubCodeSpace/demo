const puppeteer = require('puppeteer');
const tweetUrls = require('./tweets.json');

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();
  
  for (let i = 0; i < tweetUrls.length; i++) {
    const tweetUrl = tweetUrls[i][0];
    await page.goto(tweetUrl, { waitUntil: 'networkidle0' });
    await page.waitForSelector('[data-testid="reply"]');
    await page.click('[data-testid="reply"]');
    await page.waitForSelector('.public-DraftStyleDefault-block');
    await page.type('.public-DraftStyleDefault-block', 'Your reply text here', { delay: 25 });
    await page.waitForTimeout(5000);
    await page.keyboard.press('Enter');
    await page.waitForTimeout(60000);
  }
  
  await browser.close();
})();