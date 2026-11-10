// Renders the share image and app icons. Run: node tools/make_images.js (needs Playwright)
const { chromium } = require('playwright');
const path = require('path');
const out = path.join(__dirname, '..', 'src', 'static');
const og = `<html><head><link href="https://fonts.googleapis.com/css2?family=Gloock&family=Figtree:wght@500&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
<style>body{margin:0;width:1200px;height:630px;overflow:hidden;background:#0e1118;font-family:Figtree,sans-serif}canvas{position:absolute;inset:0}
.t{position:absolute;left:72px;top:118px;color:#ece9e1}.e{font:500 20px 'JetBrains Mono',monospace;letter-spacing:.16em;color:#9ba2b0}
h1{font:400 220px/0.86 Gloock,serif;margin:18px 0 0;letter-spacing:-4px}h1 span{color:#e2453d}p{font:400 40px Gloock,serif;margin:64px 0 0}</style></head>
<body><canvas id=c width=1200 height=630></canvas><div class=t><div class=e>HISTORY OF WALES · 230,000 YEARS</div><h1>C<span>y</span>mru</h1><p>A land of poets, castles and coal.</p></div>
<script>const c=document.getElementById('c').getContext('2d'),W=1200,H=630;let s=1282;const r=()=>{s=s*16807%2147483647;return(s-1)/2147483646};
const g=c.createLinearGradient(0,0,0,H);g.addColorStop(0,'#0b0e16');g.addColorStop(.55,'#1a2032');g.addColorStop(.8,'#3a2a35');g.addColorStop(1,'#0e1118');c.fillStyle=g;c.fillRect(0,0,W,H);
for(let i=0;i<120;i++){c.fillStyle='rgba(236,233,225,'+(.2+r()*.5)+')';c.fillRect(r()*W,r()*H*.6,1.5,1.5)}
const mx=930,my=170,mr=62;const mg=c.createRadialGradient(mx,my,mr*.6,mx,my,mr*4.5);mg.addColorStop(0,'rgba(226,69,61,.25)');mg.addColorStop(1,'rgba(226,69,61,0)');c.fillStyle=mg;c.fillRect(0,0,W,H);c.fillStyle='#e9d9c6';c.beginPath();c.arc(mx,my,mr,0,7);c.fill();
[[.62,.16,'#232a3d'],[.7,.14,'#1d2433'],[.8,.12,'#171d2a'],[.9,.09,'#121722']].forEach(([y,a,col])=>{const w=[];for(let k=0;k<6;k++)w.push([r()*6.28,.6+r()*(k+1)*1.7,1/(k+1.2)*(.6+r()*.6)]);c.beginPath();c.moveTo(0,H);for(let x=0;x<=W;x+=6){let v=0;for(const q of w)v+=Math.sin(x/900*3*q[1]+q[0])*q[2];v=Math.abs(v)*.6+v*.4;c.lineTo(x,H*y-v*H*a)}c.lineTo(W,H);c.fillStyle=col;c.fill()});
</script></body></html>`;
const icon = (size, pad) => `<html><body style="margin:0;background:#0e1118"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="${size}" height="${size}" style="display:block"><rect width="64" height="64" fill="#0e1118"/><g transform="translate(${pad} ${pad}) scale(${(64 - 2 * pad) / 64})"><circle cx="46" cy="18" r="7" fill="#e9d9c6"/><path d="M6 50 24 20l9 14 6-8 19 24z" fill="#e2453d"/></g></svg></body></html>`;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await p.setContent(og, { waitUntil: 'networkidle' }); await p.waitForTimeout(500);
  await p.screenshot({ path: path.join(out, 'og.png') });
  for (const [n, s, pad] of [['icon-192.png', 192, 6], ['icon-512.png', 512, 6], ['apple-touch-icon.png', 180, 8], ['icon-maskable-512.png', 512, 14]]) {
    const q = await b.newPage({ viewport: { width: s, height: s } });
    await q.setContent(icon(s, pad)); await q.screenshot({ path: path.join(out, n) }); await q.close();
  }
  await b.close();
})();
