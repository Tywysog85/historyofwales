const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
const c = await b.newContext({ viewport: { width: 412, height: 800 } }); const p = await c.newPage();
await p.addInitScript(() => { window.__g = []; const iv = setInterval(() => { if (window.HCL3 && HCL3.frame && !HCL3.__w) { HCL3.__w = 1; const f = HCL3.frame; HCL3.frame = function (st) { const k = [st.ground.x, st.ground.y, st.ground.ppm, st.sumX, st.sumY, st.ppm].map(v => v.toFixed(2)).join(','); const g = window.__g; if (!g.length || g[g.length - 1][1] !== k) g.push([Math.round(performance.now()), k, HCL3.shown ? 1 : 0]); return f.call(this, st); }; } }, 5); });
await p.goto('http://localhost:8000/index.html?sky=night'); await p.waitForFunction('window.HCL3 && HCL3.shown', null, { timeout: 90000 }); await p.waitForTimeout(6000);
console.log(JSON.stringify(await p.evaluate('window.__g'), null, 0).replace(/\],\[/g, ']\n[')); await b.close(); })();
