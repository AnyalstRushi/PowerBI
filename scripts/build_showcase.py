import re
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

root = Path(__file__).resolve().parents[1]
assets = root / 'assets'
assets.mkdir(exist_ok=True)
shots = ['Screenshot 2025-09-28 054905.png', 'Screenshot 2025-09-28 055023.png', 'Screenshot 2025-09-28 055302.png', 'Screenshot 2025-09-28 055349.png', 'Screenshot 2025-09-28 055423.png']
bg, lime, ink = '#0B110D', '#C6FF32', '#F5F3E8'
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def text(d, xy, value, size=20, color=ink):
    d.text(xy, value, fill=color, font=ImageFont.truetype(font_path, size))
def save(name, frames, duration):
    p = assets / name
    frames[0].save(p, save_all=True, append_images=frames[1:], duration=duration, loop=0, optimize=True, disposal=2)
    with Image.open(p) as check:
        assert check.n_frames > 1
    assert p.stat().st_size < 10_000_000
frames = []
for i in range(48):
    im = Image.new('RGB', (1200, 520), bg)
    d = ImageDraw.Draw(im)
    for x in range(760, 1180, 40):
        d.line((x, 90, x, 390), fill='#1D2A20')
    for y in range(90, 410, 40):
        d.line((750, y, 1180, y), fill='#1D2A20')
    text(d, (42, 28), 'ANALYST RUSHI / THE MOBILITY ATLAS', 18, lime)
    text(d, (40, 110), 'Every booking', 68)
    text(d, (40, 190), 'has a story.', 68, lime)
    text(d, (44, 299), 'From ride records to decision-ready insights.', 22)
    text(d, (44, 340), 'A Power BI case study by Analyst Rushi.', 19, '#AEBBAC')
    points = [(790, 355), (900, 355), (900, 150), (1150, 150)]
    d.line(points, fill='#47604B', width=3)
    for k in range(3):
        t = ((i/48+k/3) % 1)*3
        n = min(int(t), 2)
        u = t-n
        x = points[n][0]*(1-u)+points[n+1][0]*u
        y = points[n][1]*(1-u)+points[n+1][1]*u
        d.ellipse((x-7, y-7, x+7, y+7), fill=lime if k == 0 else '#83CDB4')
    for j, label in enumerate(['RECORD', 'MODEL', 'REPORT']):
        x = 770+j*140
        text(d, (x, 410), label, 14, lime if i//16 == j else '#AEBBAC')
    d.line((42, 460, 1158, 460), fill='#354237')
    text(d, (44, 481), 'INDEPENDENT PORTFOLIO / ILLUSTRATIVE FLOW / NOT LIVE GPS OR POWER BI', 14)
    frames.append(im)
save('analyst-rushi-hero.gif', frames, 125)
frames = []
for i, filename in enumerate(shots):
    im = Image.new('RGB', (1200, 760), bg)
    d = ImageDraw.Draw(im)
    text(d, (30, 20), 'THE MOBILITY ATLAS / ORIGINAL REPORT', 20, lime)
    text(d, (1025, 22), f'0{i+1} / 05', 20)
    with Image.open(root / filename) as source:
        shot = ImageOps.contain(source.convert('RGB'), (1140, 620))
    im.paste(shot, ((1200-shot.width)//2, 75+(620-shot.height)//2))
    for j in range(5):
        x = 32+j*230
        d.rectangle((x, 708, x+208, 712), fill=lime if j == i else '#354237')
    text(d, (30, 730), 'Original screenshots. No altered metrics. Slideshow, not live Power BI.', 15)
    frames.append(im)
save('powerbi-report-preview.gif', frames, 2600)
p = root / 'README.md'
s = re.sub(r'<!-- POWERBI_PREVIEWS -->.*?<!-- /POWERBI_PREVIEWS -->\s*', '', p.read_text(), flags=re.S)
s = s.replace('Public Pages deployment is not configured or verified by this update.', 'GitHub Pages publishing is automated; successful public deployment still requires verification.')
s = s.replace('Main palette: charcoal #111613, electric lime #B9F227, ivory #F3F5E9.', 'Main palette: graphite #0B110D, acid lime #C6FF32, ivory #F5F3E8; mint #83CDB4 and amber #F2B65B accents.')
block = '<!-- POWERBI_PREVIEWS -->\n![Analyst Rushi — The Mobility Atlas animated hero](assets/analyst-rushi-hero.gif)\n\n## The report, in its original form\n![Original report views with Analyst Rushi framing](assets/powerbi-report-preview.gif)\n\n[Explore the Mobility Atlas](https://anyalstrushi.github.io/PowerBI/showcase/) · [Build and deployment status](https://github.com/AnyalstRushi/PowerBI/actions/workflows/publish-showcase.yml)\n\nAvailability requires a successful Pages deployment. Hero motion is illustrative; the report preview is a screenshot slideshow, not an interactive Power BI embed.\n\n<!-- /POWERBI_PREVIEWS -->\n\n'
p.write_text(block+s)
site = root / '_site'
if site.exists():
    shutil.rmtree(site)
(site / 'showcase').mkdir(parents=True)
(site / 'themes').mkdir()
(site / 'docs').mkdir()
html = (root / 'showcase/index.html').read_text()
html = html.replace('../OLA%20Project%20DashBOard.pbix', 'https://github.com/AnyalstRushi/PowerBI/raw/refs/heads/main/OLA%20Project%20DashBOard.pbix')
html = html.replace('Analyst Rushi / Mobility Intelligence', 'Analyst Rushi / The Mobility Atlas')
html = html.replace('Read the ride.<br><span class="lime">See the signal.</span>', 'Every booking<br>has a <span class="lime">story.</span>')
html = html.replace('ANALYST RUSHI / BI STUDIO', 'ANALYST RUSHI / THE MOBILITY ATLAS')
html = html.replace('Power BI storytelling for ride operations: inspect the original report views, understand the analytical workflow, and explore the downloadable project.', 'From ride records to decision-ready insights. A Power BI case study by Analyst Rushi, presented through the original report and a guided analytical story.')
style = '''<style id="mobility-atlas-design">
:root{--bg:#0B110D;--ink:#F5F3E8;--muted:#AEBBAC;--lime:#C6FF32;--line:#314136}
body{background:radial-gradient(ellipse at 90% 5%,#1B2A18,transparent 45%),var(--bg)}
nav{padding-top:25px;padding-bottom:25px}nav strong{font-size:12px;letter-spacing:2px}
.hero{grid-template-columns:1.15fr 1fr;padding-top:90px;padding-bottom:90px}
h1{font-size:clamp(48px,7vw,104px);font-weight:650;letter-spacing:-.055em;line-height:1.04}
h2{font-weight:550;letter-spacing:-.04em}.eyebrow{letter-spacing:3px}
.signal{background:linear-gradient(150deg,#1A281B,#0B110D);border-radius:0;border-color:#496043;position:relative}
.signal:before{content:'ATLAS / 001';display:block;color:#83CDB4;font:11px monospace;letter-spacing:3px;margin-bottom:18px}
.signal .route{stroke:#C6FF32}.signal svg circle{fill:#83CDB4}
.button,button{border-radius:2px}.button:hover,button:hover{filter:brightness(1.08)}
#report{padding-top:60px;padding-bottom:75px}.viewer{background:#111C14;padding:10px;border-color:#496043}
.viewer img{aspect-ratio:auto;min-height:160px;background:#0B110D}
.thumbs{gap:12px}.thumbs button{background:#111C14}.thumbs img{height:100px}
.step{background:linear-gradient(150deg,#17231A,#0B110D);border-top:2px solid #83CDB4;position:relative}
.step span{color:#83CDB4}.step.atlas-active{border-top-color:#C6FF32;background:#1C2D1D}
.steps{gap:18px}.atlas-key{font:12px monospace;color:#AEBBAC}
@media(max-width:800px){.hero{grid-template-columns:1fr;padding:45px 6vw}.thumbs img{height:48px}.steps{grid-template-columns:1fr}.viewer{padding:4px}nav div{flex-wrap:wrap}}
@media(prefers-reduced-motion:reduce){.route{animation:none!important}}
@media print{body,.signal,.step,.viewer{background:white!important}.step span{color:black}nav,.atlas-key{display:none}}
</style>'''
html = html.replace('</head>', style+'</head>')
script = '''<script>
(()=>{const reduced=matchMedia('(prefers-reduced-motion: reduce)');const image=document.getElementById('mainShot');const report=document.getElementById('report');if(image){image.addEventListener('load',()=>{if(!reduced.matches&&image.animate)image.animate([{opacity:.3},{opacity:1}],{duration:420,easing:'ease-out'})});const controls=report.querySelector('.controls');const original=document.createElement('a');original.textContent='Open original image';original.target='_blank';original.rel='noopener';const sync=()=>original.href=image.src;image.addEventListener('load',sync);sync();controls.append(original);report.tabIndex=0;const hint=document.createElement('p');hint.className='atlas-key';hint.textContent='Focus this section and use left / right arrow keys. Playback is optional.';controls.after(hint);report.addEventListener('keydown',e=>{if(e.target!==report)return;if(e.key==='ArrowRight'){e.preventDefault();document.getElementById('next').click()}if(e.key==='ArrowLeft'){e.preventDefault();document.getElementById('prev').click()}})}const stages=[...document.querySelectorAll('.step')];let stage=0;const focusStage=()=>{stages.forEach((n,i)=>n.classList.toggle('atlas-active',!reduced.matches&&i===stage));stage=(stage+1)%Math.max(stages.length,1)};let timer=null;const toggle=document.createElement('button');toggle.textContent='Play conceptual workflow';toggle.setAttribute('aria-pressed','false');const architecture=document.getElementById('architecture');architecture.append(toggle);const stop=()=>{clearInterval(timer);timer=null;toggle.textContent='Play conceptual workflow';toggle.setAttribute('aria-pressed','false');stages.forEach(n=>n.classList.remove('atlas-active'))};toggle.onclick=()=>{if(timer){stop();return}if(reduced.matches){stages[0]?.classList.add('atlas-active');return}focusStage();timer=setInterval(focusStage,1600);toggle.textContent='Pause conceptual workflow';toggle.setAttribute('aria-pressed','true')};document.addEventListener('visibilitychange',()=>{if(document.hidden)stop()});reduced.addEventListener('change',stop)})();
</script>'''
html = html.replace('</body>', script+'</body>')
(site / 'showcase/index.html').write_text(html)
for name in shots:
    shutil.copy2(root / name, site / name)
shutil.copy2(root / 'themes/analyst-rushi-mobility.json', site / 'themes/analyst-rushi-mobility.json')
for name in ['PRESENTATION.html', 'PROJECT_PRESENTATION.md', 'PROJECT_REQUIREMENTS.md']:
    shutil.copy2(root / 'docs' / name, site / 'docs' / name)
(site / 'index.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=showcase/"><title>Analyst Rushi — Mobility Atlas</title><a href="showcase/">Explore the Mobility Atlas</a>')
(site / '.nojekyll').touch()
assert 'mobility-atlas-design' in html and 'Every booking' in html
assert (site / 'showcase/index.html').stat().st_size > 0
for name in shots:
    assert (site / name).is_file()
for name in ['analyst-rushi-hero.gif', 'powerbi-report-preview.gif']:
    assert (assets / name).is_file()
