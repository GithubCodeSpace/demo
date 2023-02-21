const puppeteer = require('puppeteer');
const { PythonShell } = require('python-shell');
const path = require('path');

(async () => {
    // Launch Puppeteer
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto('https://twitter.com/login');

    // Login to Twitter
    await page.waitForSelector('input[name="session[username_or_email]"]');
    await page.type('input[name="session[username_or_email]"]', 'your_username');
    await page.type('input[name="session[password]"]', 'your_password');
    await page.click('div[data-testid="LoginForm_Login_Button"]');

    // Wait for login to complete
    await page.waitForNavigation();
    await page.waitForSelector('a[data-testid="SideNav_NewTweet_Button"]');

    // Call the Python script
    const options = {
        mode: 'text',
        pythonPath: 'python',
        pythonOptions: ['-u'],
        scriptPath: path.join(__dirname, '/'),
        args: ['your_username', 'from:your_username', '2022-02-20', '2022-02-21', '10']
    };
    PythonShell.run('twitter_scraper.py', options, (err, results) => {
        if (err) throw err;
        console.log('Python script completed successfully:', results);
    });

    // Close the browser
    await browser.close();
})();