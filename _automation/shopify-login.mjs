import { chromium } from 'playwright';

const browser = await chromium.launch({ headless: false });
const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
const page = await context.newPage();

await page.goto('https://admin.shopify.com/store/deceitdeceit', { waitUntil: 'domcontentloaded', timeout: 30000 });
console.log(`URL: ${page.url()}`);

// If redirected to login, user needs to log in
if (page.url().includes('accounts.shopify.com')) {
  console.log('');
  console.log('==============================================');
  console.log('Fai il LOGIN su Shopify nel browser che si è appena aperto.');
  console.log('Se non ti fa andare avanti dopo la mail, compila manualmente.');
  console.log('Dopo aver completato il login, torna qui e premi INVIO.');
  console.log('==============================================');
  await new Promise(resolve => process.stdin.once('data', resolve));
}

console.log('Sei dentro! URL:', page.url());
await context.storageState({ path: '/Users/nicoskolp/Desktop/DECĒIT_MARKETING_AI/_automation/shopify-auth.json' });
console.log('Sessione salvata!');

// Go to themes page to show we're in
await page.goto('https://admin.shopify.com/store/deceitdeceit/online-store/themes', { waitUntil: 'domcontentloaded' });
console.log('Tema aperto! URL:', page.url());

console.log('');
console.log('Browser resta aperto. Fammi sapere cosa vuoi fare.');
await new Promise(() => {});
