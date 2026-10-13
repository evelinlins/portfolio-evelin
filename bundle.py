import base64
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(base_dir, 'assets/img/evelin_hero.jpg'), 'rb') as f:
    hero_b64 = base64.b64encode(f.read()).decode('utf-8')

with open(os.path.join(base_dir, 'assets/img/evelin_about.jpg'), 'rb') as f:
    about_b64 = base64.b64encode(f.read()).decode('utf-8')

with open(os.path.join(base_dir, 'assets/img/aerometrics_preview.png'), 'rb') as f:
    preview_b64 = base64.b64encode(f.read()).decode('utf-8')

with open(os.path.join(base_dir, 'css/style.css'), 'r', encoding='utf-8') as f:
    css_content = f.read()

with open(os.path.join(base_dir, 'js/main.js'), 'r', encoding='utf-8') as f:
    js_content = f.read()

# Source of truth is index.modular.html
with open(os.path.join(base_dir, 'index.modular.html'), 'r', encoding='utf-8') as f:
    html = f.read()

bundled_html = html
bundled_html = bundled_html.replace('<link rel="stylesheet" href="css/style.css">', f'<style>\n{css_content}\n</style>')
bundled_html = bundled_html.replace('<script src="js/main.js"></script>', f'<script>\n{js_content}\n</script>')
bundled_html = bundled_html.replace('assets/img/evelin_hero.jpg', f'data:image/jpeg;base64,{hero_b64}')
bundled_html = bundled_html.replace('assets/img/evelin_about.jpg', f'data:image/jpeg;base64,{about_b64}')
bundled_html = bundled_html.replace('assets/img/aerometrics_preview.png', f'data:image/png;base64,{preview_b64}')

# Save to index.html (primary for Vercel/GitHub upload)
with open(os.path.join(base_dir, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(bundled_html)

# Save to index.bundle.html (backup copy)
with open(os.path.join(base_dir, 'index.bundle.html'), 'w', encoding='utf-8') as f:
    f.write(bundled_html)

print("BUNDLE_READY: index.html and index.bundle.html generated successfully.")
