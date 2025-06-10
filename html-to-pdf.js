const puppeteer = require('puppeteer');

const [,, url, filename = 'output.pdf'] = process.argv;

if (!url) {
  console.log('Usage: node convert.js <URL> [filename.pdf]');
  process.exit(1);
}

(async () => {
  const browser = await puppeteer.launch({ args: ['--no-sandbox', '--disable-setuid-sandbox'] });
  const page = await browser.newPage();
  await page.goto(url, { waitUntil: 'networkidle2' });
  await page.pdf({
    path: filename,
    format: 'A4',
    printBackground: true,
    margin: { top: '1in', bottom: '1in', left: '0.5in', right: '0.5in' }
  });
  await browser.close();
  console.log(`PDF saved as ${filename}`);
})();
