import re
import shutil
from pathlib import Path
from urllib.parse import quote
from PIL import Image, ImageDraw, ImageFont, ImageOps

root = Path(__file__).resolve().parents[1]
assets = root / 'assets'
assets.mkdir(exist_ok=True)
shots = ['Screenshot 2025-09-28 054905.png', 'Screenshot 2025-09-28 055023.png', 'Screenshot 2025-09-28 055302.png', 'Screenshot 2025-09-28 055349.png', 'Screenshot 2025-09-28 055423.png']
bg, lime, ink = '#111613', '#B9F227', '#F3F5E9'
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
for i in range(40):
    im = Image.new('RGB', (1000, 380), bg)
    d = ImageDraw.Draw(im)
    text(d, (35, 23), 'ANALYST RUSHI / BI STUDIO', 17, lime)
    text(d, (35, 82), 'Read the ride.', 58)
    text(d, (35, 151), 'See the signal.', 58, lime)
    text(d, (38, 244), 'OLA ride operations / independent Power BI portfolio', 19)
    points = [(650, 270), (750, 270), (750, 125), (950, 125)]
    d.line(points, fill='#354237', width=5)
    t = i / 40 * 3
    n = min(int(t), 2)
    u = t-n
    x = points[n][0]*(1-u)+points[n+1][0]*u
    y = points[n][1]*(1-u)+points[n+1][1]*u
    d.ellipse((x-9, y-9, x+9, y+9), fill=lime)
    text(d, (35, 335), 'ILLUSTRATIVE ANIMATION | OLA-INSPIRED, NOT AFFILIATED WITH OLA', 13)
    frames.append(im)
save('analyst-rushi-hero.gif', frames, 125)
frames = []
for i, filename in enumerate(shots):
    im = Image.new('RGB', (1000, 640), bg)
    d = ImageDraw.Draw(im)
    text(d, (25, 17), f'ANALYST RUSHI / ORIGINAL REPORT VIEW {i+1} OF 5', 18, lime)
    with Image.open(root / filename) as source:
        shot = ImageOps.contain(source.convert('RGB'), (960, 530))
    im.paste(shot, ((1000-shot.width)//2, 66+(530-shot.height)//2))
    text(d, (25, 610), 'SCREENSHOT SLIDESHOW | NOT LIVE POWER BI | NO DATA REFRESH', 14)
    frames.append(im)
save('powerbi-report-preview.gif', frames, 2200)
p = root / 'README.md'
s = re.sub(r'<!-- POWERBI_PREVIEWS -->.*?<!-- /POWERBI_PREVIEWS -->\s*', '', p.read_text(), flags=re.S)
s = s.replace('Public Pages deployment is not configured or verified by this update.', 'GitHub Pages publishing is automated; successful public deployment still requires verification.')
block = '<!-- POWERBI_PREVIEWS -->\n![Analyst Rushi animated hero](assets/analyst-rushi-hero.gif)\n\n## Original dashboard walkthrough\n![Original Power BI screenshot slideshow](assets/powerbi-report-preview.gif)\n\n[Open branded website](https://anyalstrushi.github.io/PowerBI/showcase/) · [Deployment status](https://github.com/AnyalstRushi/PowerBI/actions/workflows/publish-showcase.yml)\n\nWebsite availability depends on a successful Pages deployment. This GIF is a screenshot slideshow, not live Power BI.\n\n<!-- /POWERBI_PREVIEWS -->\n\n'
p.write_text(block+s)
site = root / '_site'
if site.exists():
    shutil.rmtree(site)
(site / 'showcase').mkdir(parents=True)
(site / 'themes').mkdir()
(site / 'docs').mkdir()
html = (root / 'showcase/index.html').read_text()
html = html.replace('../OLA%20Project%20DashBOard.pbix', 'https://github.com/AnyalstRushi/PowerBI/raw/refs/heads/main/OLA%20Project%20DashBOard.pbix')
(site / 'showcase/index.html').write_text(html)
for name in shots:
    shutil.copy2(root / name, site / name)
shutil.copy2(root / 'themes/analyst-rushi-mobility.json', site / 'themes/analyst-rushi-mobility.json')
for name in ['PRESENTATION.html', 'PROJECT_PRESENTATION.md', 'PROJECT_REQUIREMENTS.md']:
    shutil.copy2(root / 'docs' / name, site / 'docs' / name)
(site / 'index.html').write_text('<!doctype html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=showcase/"><title>Analyst Rushi</title><a href="showcase/">Open Analyst Rushi showcase</a>')
(site / '.nojekyll').touch()
assert (site / 'showcase/index.html').stat().st_size > 0
for name in shots:
    assert (site / name).is_file()
for name in ['analyst-rushi-hero.gif', 'powerbi-report-preview.gif']:
    assert (assets / name).is_file()
