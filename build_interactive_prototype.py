import os
import re
import base64
from io import BytesIO
from PIL import Image

WORKSPACE_DIR = "/home/jc/Área de trabalho/LP - Evolve/LP EVOLVE ANTIGRAVITY"

def get_base64_image(file_path):
    if not os.path.exists(file_path):
        return ""
    
    ext = os.path.splitext(file_path)[1].lower()
    if ext not in ['.jpg', '.jpeg', '.png', '.svg', '.webp']:
        return ""
        
    if ext == '.svg':
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                svg_data = f.read()
            b64 = base64.b64encode(svg_data.encode('utf-8')).decode('utf-8')
            return f"data:image/svg+xml;base64,{b64}"
        except Exception:
            return ""
    
    try:
        im = Image.open(file_path)
        
        # Check if it's a drive photo or background image to use aggressive optimization
        is_drive_photo = 'drive-download-' in file_path or 'parceria/' in file_path
        is_home_hero = os.path.basename(file_path) in ('foto_palestra_nitida.png', '56-DSC01070.jpg', '46-DSC00995.jpg', 'amanda_palestra_casaco.png')
        max_size = 1800 if is_home_hero else (600 if is_drive_photo else 900)
        
        if im.width > max_size or im.height > max_size:
            im.thumbnail((max_size, max_size), Image.Resampling.LANCZOS)
        
        if im.mode in ('RGBA', 'P') and ext in ['.jpg', '.jpeg']:
            im = im.convert('RGB')
        
        buffer = BytesIO()
        if ext in ['.jpg', '.jpeg']:
            im.save(buffer, format='JPEG', quality=95 if is_home_hero else 75, optimize=True)
            mime = "image/jpeg"
        elif ext == '.png':
            # Convert non-transparent PNGs to JPEG for 10x smaller size, or optimize PNG
            if im.mode == 'RGB' or (im.mode == 'RGBA' and not im.getextrema()[3][0] < 255):
                im = im.convert('RGB')
                im.save(buffer, format='JPEG', quality=95 if is_home_hero else 75, optimize=True)
                mime = "image/jpeg"
            else:
                im.save(buffer, format='PNG', optimize=True)
                mime = "image/png"
        elif ext == '.webp':
            im.save(buffer, format='WEBP', quality=75)
            mime = "image/webp"
        else:
            mime = "application/octet-stream"
        
        b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return f"data:{mime};base64,{b64}"
    except Exception as e:
        print(f"Error processing image {file_path}: {e}")
        return ""

def process_content_assets(content):
    def replace_src(match):
        attr = match.group(1) # src= or href=
        quote = match.group(2)
        path = match.group(3).strip()
        
        if path.startswith('data:') or path.startswith('http') or path.startswith('#') or path.startswith('mailto:') or path.startswith('tel:'):
            return match.group(0)
        
        clean_path = path.startswith('/') and path[1:] or path
        clean_path = clean_path.split('?')[0].split('#')[0]
        
        full_path = os.path.join(WORKSPACE_DIR, clean_path)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            b64_uri = get_base64_image(full_path)
            if b64_uri:
                return f"{attr}{quote}{b64_uri}{quote}"
        
        return match.group(0)

    # Match ONLY image extensions
    pattern_attr = r'(src=|href=)(["\'])(assets/[^"\']+\.(?:jpg|jpeg|png|svg|webp)|drive-download-[^"\']+\.(?:jpg|jpeg|png|svg|webp)|[\w\-\.\/]+\.(?:jpg|jpeg|png|svg|webp))\2'
    content = re.sub(pattern_attr, replace_src, content, flags=re.IGNORECASE)
    
    pattern_url = r'(url\()(["\']?)(assets/[^"\']+\.(?:jpg|jpeg|png|svg|webp)|drive-download-[^"\']+\.(?:jpg|jpeg|png|svg|webp)|[\w\-\.\/]+\.(?:jpg|jpeg|png|svg|webp))\2(\))'
    def replace_css_url(match):
        path = match.group(3).strip()
        if path.startswith('data:') or path.startswith('http'):
            return match.group(0)
        clean_path = path.split('?')[0].split('#')[0]
        full_path = os.path.join(WORKSPACE_DIR, clean_path)
        if os.path.exists(full_path) and os.path.isfile(full_path):
            b64_uri = get_base64_image(full_path)
            if b64_uri:
                return f"url('{b64_uri}')"
        return match.group(0)
        
    content = re.sub(pattern_url, replace_css_url, content, flags=re.IGNORECASE)
    return content

print("Processing CSS files...")
css_files = ['style.css', 'assets/css/system.css']
combined_css = ""
for css in css_files:
    css_path = os.path.join(WORKSPACE_DIR, css)
    if os.path.exists(css_path):
        with open(css_path, 'r', encoding='utf-8') as f:
            css_content = f.read()
            combined_css += process_content_assets(css_content) + "\n"

print("Processing JS files...")
js_files = ['assets/js/app.js', 'assets/js/diagnostico.js']
combined_js = ""
for js in js_files:
    js_path = os.path.join(WORKSPACE_DIR, js)
    if os.path.exists(js_path):
        with open(js_path, 'r', encoding='utf-8') as f:
            combined_js += f.read() + "\n"

# Add SPA Routing JS script
spa_router_js = """
document.addEventListener('DOMContentLoaded', () => {
    const views = document.querySelectorAll('.app-view');
    
    function revealViewElements(view) {
        if (!view) return;
        const targets = view.querySelectorAll('[data-reveal], [data-reveal-rule], .rise, .no-secao, .rotina__step, .pull-frame, .abertura__tile, .equipe-card-vert, .card-metodo');
        targets.forEach(el => {
            el.classList.add('is-in', 'revealed');
        });
    }

    function navigateTo(targetId) {
        if (!targetId) targetId = 'home';
        targetId = targetId.replace('.html', '').replace('#', '').replace('/', '');
        if (targetId === '' || targetId === 'index') targetId = 'home';
        
        let targetView = document.getElementById('view-' + targetId);
        if (!targetView) {
            targetView = document.getElementById('view-home');
        }
        
        views.forEach(v => {
            v.style.display = 'none';
            v.classList.remove('active');
        });
        
        targetView.style.display = 'block';
        targetView.classList.add('active');
        window.scrollTo({ top: 0, behavior: 'smooth' });

        revealViewElements(targetView);
        window.dispatchEvent(new Event('resize'));
        window.dispatchEvent(new Event('scroll'));
    }
    
    document.addEventListener('click', (e) => {
        const link = e.target.closest('a');
        if (!link) return;
        
        const href = link.getAttribute('href');
        if (!href) return;
        
        if (href.endsWith('.html') || href.startsWith('#view-') || href === 'index.html' || href === 'evolve.html' || href === 'carta-aberta.html' || href === 'servicos.html') {
            e.preventDefault();
            const pageName = href.replace('.html', '').replace('#', '');
            navigateTo(pageName);
        }
    });
    
    navigateTo('home');
});
"""

combined_js += "\n" + spa_router_js

pages = [
    ('home', 'index.html'),
    ('evolve', 'evolve.html'),
    ('carta-aberta', 'carta-aberta.html'),
    ('servicos', 'servicos.html'),
    ('servicos-pessoas-relacionamento', 'servicos-pessoas-relacionamento.html'),
    ('servicos-recrutamento-selecao', 'servicos-recrutamento-selecao.html'),
    ('servicos-riscos-saude', 'servicos-riscos-saude.html'),
    ('servicos-lideranca-desenvolvimento', 'servicos-lideranca-desenvolvimento.html')
]

views_html = ""

for view_id, filename in pages:
    filepath = os.path.join(WORKSPACE_DIR, filename)
    if os.path.exists(filepath):
        print(f"Processing page {filename}...")
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        html = process_content_assets(html)
        
        body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL | re.IGNORECASE)
        if body_match:
            body_content = body_match.group(1)
        else:
            body_content = html
            
        views_html += f"""
        <div id="view-{view_id}" class="app-view" style="display: {'block' if view_id == 'home' else 'none'};">
            {body_content}
        </div>
        """

full_interactive_document = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Evolve - Protótipo Interativo</title>
    <style>
        {combined_css}
        .app-view {{
            width: 100%;
            min-height: 100vh;
            animation: fadeInView 0.35s ease-out;
        }}
        @keyframes fadeInView {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body>
    {views_html}
    <script>
        {combined_js}
    </script>
</body>
</html>
"""

output_filename = os.path.join(WORKSPACE_DIR, "Evolve_Prototipo_Interativo.html")
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(full_interactive_document)

print(f"Success! Interactive single-file prototype created: {output_filename}")
print(f"File size: {os.path.getsize(output_filename) / (1024*1024):.2f} MB")
