import re
import shutil
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageOps

root = Path(__file__).resolve().parents[1]
assets = root / 'assets'
assets.mkdir(exist_ok=True)
shots = ['Screenshot 2025-09-28 054905.png', 'Screenshot 2025-09-28 055023.png', 'Screenshot 2025-09-28 055302.png', 'Screenshot 2025-09-28 055349.png', 'Screenshot 2025-09-28 055423.png']
font_path = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def text(d, xy, value, size=20, color='#101510'):
    d.text(xy, value, fill=color, font=ImageFont.truetype(font_path, size))
def save(name, frames, duration):
    p = assets / name
    frames[0].save(p, save_all=True, append_images=frames[1:], duration=duration, loop=0, optimize=True, disposal=2)
    with Image.open(p) as check:
        assert check.n_frames == len(frames)
    assert p.stat().st_size < 10_000_000
hero, preview = [], []
for i, filename in enumerate(shots):
    with Image.open(root / filename) as source:
        original = source.convert('RGB')
    im = Image.new('RGB', (1200, 720), '#101510')
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 1200, 65), fill='#F4F3EC')
    text(d, (32, 20), 'ANALYST RUSHI / OLA RIDE INTELLIGENCE', 20)
    text(d, (32, 92), 'The story behind the ride.', 48, '#F4F3EC')
    text(d, (35, 157), 'ORIGINAL POWER BI WORK / INDEPENDENT PORTFOLIO', 15, '#C6F43B')
    shot = ImageOps.contain(original, (1120, 440))
    im.paste(shot, ((1200-shot.width)//2, 210+(440-shot.height)//2))
    for j in range(5):
        x = 35+j*230
        d.rectangle((x, 673, x+210, 677), fill='#C6F43B' if j==i else '#35402F')
    text(d, (35, 691), 'CAPTURED VIEW 0'+str(i+1)+' / 05 - SCREENSHOT PLAYBACK, NOT LIVE POWER BI', 13, '#C5CFBC')
    hero.append(im)
    im = Image.new('RGB', (1200, 760), '#F4F3EC')
    d = ImageDraw.Draw(im)
    text(d, (30, 18), 'ANALYST RUSHI / REPORT GALLERY', 20)
    text(d, (1030, 20), '0'+str(i+1)+' / 05', 18)
    shot = ImageOps.contain(original, (1140, 620))
    im.paste(shot, ((1200-shot.width)//2, 75+(620-shot.height)//2))
    text(d, (30, 724), 'Original report captures. No invented metrics. Not a live report.', 16)
    preview.append(im)
save('analyst-rushi-hero.gif', hero, 2800)
save('powerbi-report-preview.gif', preview, 3200)
p = root / 'README.md'
s = re.sub(r'<!-- POWERBI_PREVIEWS -->.*?<!-- /POWERBI_PREVIEWS -->\s*', '', p.read_text(), flags=re.S)
block = '<!-- POWERBI_PREVIEWS -->\n![Analyst Rushi / OLA Ride Intelligence](assets/analyst-rushi-hero.gif)\n\n## Original report walkthrough\n![Original dashboard capture gallery](assets/powerbi-report-preview.gif)\n\n[Explore the case study website](https://anyalstrushi.github.io/PowerBI/showcase/) · [Build and deployment](https://github.com/AnyalstRushi/PowerBI/actions/workflows/publish-showcase.yml)\n\nAvailability requires successful deployment. Animated previews use original screenshots; they are not live Power BI. Independent portfolio, not affiliated with Ola.\n\n<!-- /POWERBI_PREVIEWS -->\n\n'
p.write_text(block+s)
site = root / '_site'
if site.exists():
    shutil.rmtree(site)
(site / 'showcase').mkdir(parents=True)
(site / 'themes').mkdir()
(site / 'docs').mkdir()
html = (root / 'showcase/index.html').read_text()
html = html.replace('../OLA%20Project%20DashBOard.pbix', 'https://github.com/AnyalstRushi/PowerBI/raw/refs/heads/main/OLA%20Project%20DashBOard.pbix')
assert 'OLA Ride Intelligence / Analyst Rushi' in html
assert 'id="mainShot"' in html and 'id="flow"' in html
(site / 'showcase/index.html').write_text(html)
for name in shots:
    shutil.copy2(root / name, site / name)
shutil.copy2(root / 'themes/analyst-rushi-mobility.json', site / 'themes/analyst-rushi-mobility.json')
for name in ['PRESENTATION.html', 'PROJECT_PRESENTATION.md', 'PROJECT_REQUIREMENTS.md']:
    shutil.copy2(root / 'docs' / name, site / 'docs' / name)
(site / 'index.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=showcase/"><title>OLA Ride Intelligence / Analyst Rushi</title><a href="showcase/">Explore the case study</a>')
(site / '.nojekyll').touch()
for name in shots:
    assert (site / name).is_file()
