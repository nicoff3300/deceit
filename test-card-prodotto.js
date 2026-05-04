const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext();
  const page = await context.newPage();

  const errors = [];
  const networkLogs = [];
  const consoleLogs = [];
  let canvasInfo = null;

  // Capture console logs
  page.on('console', msg => {
    const type = msg.type();
    const text = msg.text();
    consoleLogs.push({ type, text });
    if (type === 'error') {
      errors.push({ type, text });
    }
  });

  // Capture page errors
  page.on('pageerror', error => {
    errors.push({ type: 'pageerror', text: error.message });
  });

  // Capture network requests
  page.on('request', request => {
    networkLogs.push({
      type: 'request',
      url: request.url(),
      method: request.method()
    });
  });

  // Capture network responses
  page.on('response', response => {
    const url = response.url();
    if (url.includes('shopify') || url.includes('/collections/') || url.includes('api')) {
      networkLogs.push({
        type: 'response',
        url: url,
        status: response.status(),
        ok: response.ok()
      });
    }
  });

  console.log('🌐 Navigating to card-prodotto page...');
  try {
    await page.goto('https://deceitdeceit.com/pages/card-prodotto', {
      waitUntil: 'networkidle',
      timeout: 30000
    });
  } catch (e) {
    console.log('Navigation error:', e.message);
  }

  // Wait for page to settle
  await page.waitForTimeout(3000);

  console.log('\n📊 PAGE INFO:');
  console.log('Title:', await page.title());
  console.log('URL:', page.url());

  // Check canvas
  console.log('\n🎨 CANVAS CHECK:');
  try {
    const canvas = await page.$('canvas');
    if (canvas) {
      const canvasData = await canvas.evaluate(el => ({
        width: el.width,
        height: el.height,
        hasContext: !!el.getContext('2d'),
        parentId: el.parentElement?.id || 'none'
      }));
      canvasInfo = canvasData;
      console.log('✅ Canvas found:', canvasData);
    } else {
      console.log('❌ No canvas element found');
    }
  } catch (e) {
    console.log('Canvas check error:', e.message);
  }

  // Check for product loading
  console.log('\n📦 PRODUCT LOADING CHECK:');
  try {
    // Check if any product-related elements exist
    const productElements = await page.$$eval('[data-product], .product, [class*="product"], [class*="prodotto"]', els => els.length);
    console.log(`Found ${productElements} product-related elements`);

    // Check page HTML for collection references
    const html = await page.content();
    if (html.includes('SS26')) {
      console.log('✅ SS26 reference found in HTML');
    }
    if (html.includes('collections')) {
      console.log('✅ Collections reference found in HTML');
    }
    if (html.includes('shopify')) {
      console.log('✅ Shopify reference found in HTML');
    }
  } catch (e) {
    console.log('Product check error:', e.message);
  }

  // Take screenshot
  console.log('\n📸 Taking screenshot...');
  await page.screenshot({ path: '/Users/nicoskolp/Desktop/DECĒIT_MARKETING_AI/card-prodotto-screenshot.png', fullPage: true });
  console.log('Screenshot saved to card-prodotto-screenshot.png');

  // Output collected data
  console.log('\n📋 CONSOLE LOGS:');
  if (consoleLogs.length > 0) {
    consoleLogs.forEach(log => {
      console.log(`[${log.type}] ${log.text.substring(0, 200)}`);
    });
  } else {
    console.log('No console logs captured');
  }

  console.log('\n🔴 ERRORS:');
  if (errors.length > 0) {
    errors.forEach(err => console.log(`[${err.type}] ${err.text.substring(0, 200)}`));
  } else {
    console.log('No errors detected');
  }

  console.log('\n🌐 NETWORK ACTIVITY:');
  const relevantNetwork = networkLogs.filter(n =>
    n.url?.includes('shopify') ||
    n.url?.includes('/collections/') ||
    n.url?.includes('/api/') ||
    n.url?.includes('myshopify')
  );
  if (relevantNetwork.length > 0) {
    relevantNetwork.forEach(n => {
      console.log(`[${n.type}] ${n.method || ''} ${n.url?.substring(0, 100)} - ${n.status || 'OK'}`);
    });
  } else {
    console.log('No relevant Shopify API network activity found');
  }

  // Final JSON report
  console.log('\n🎯 FINAL REPORT JSON:');
  const report = {
    url: page.url(),
    title: await page.title(),
    canvasFound: !!canvasInfo,
    canvasInfo: canvasInfo,
    errorCount: errors.length,
    errors: errors.map(e => ({ type: e.type, text: e.text.substring(0, 200) })),
    consoleLogCount: consoleLogs.length,
    relevantNetworkRequests: relevantNetwork.length,
    screenshot: 'card-prodotto-screenshot.png'
  };
  console.log(JSON.stringify(report, null, 2));

  await browser.close();
})();
