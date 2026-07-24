#!/usr/bin/env python3
"""Add remaining visual enhancements to index.html"""

import re

# Read the file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add layup diagram after the "Request a Quote" button in vacuum-infusion section
layup_diagram = '''          <a href="#contact" class="btn btn-primary mt-lg">Request a Quote</a>

          <div class="layup-diagram" aria-label="Diagram showing the layers of a vacuum infusion composite layup">
            <div class="layup-title">Vacuum Infusion Stack</div>
            <div class="layup-layers">
              <div class="layup-layer" style="--layer-color: rgba(39,154,173,0.15); --layer-border: #279aad;">
                <div class="layer-swatch"></div>
                <div class="layer-label">Vacuum Bag</div>
                <div class="layer-desc">Sealed envelope drawing vacuum</div>
              </div>
              <div class="layup-layer" style="--layer-color: rgba(255,255,255,0.06); --layer-border: rgba(255,255,255,0.2);">
                <div class="layer-swatch"></div>
                <div class="layer-label">Flow Mesh</div>
                <div class="layer-desc">Distributes resin across laminate</div>
              </div>
              <div class="layup-layer" style="--layer-color: rgba(193,89,43,0.15); --layer-border: #c1592b;">
                <div class="layer-swatch"></div>
                <div class="layer-label">Peel Ply</div>
                <div class="layer-desc">Release layer for clean surface</div>
              </div>
              <div class="layup-layer" style="--layer-color: rgba(39,154,173,0.25); --layer-border: #279aad;">
                <div class="layer-swatch"></div>
                <div class="layer-label">Fibreglass Laminate</div>
                <div class="layer-desc">Structural fibre layers</div>
              </div>
              <div class="layup-layer" style="--layer-color: rgba(255,255,255,0.04); --layer-border: rgba(255,255,255,0.15);">
                <div class="layer-swatch"></div>
                <div class="layer-label">Release Film</div>
                <div class="layer-desc">Separates part from mold</div>
              </div>
              <div class="layup-layer" style="--layer-color: rgba(10,34,51,0.8); --layer-border: rgba(39,154,173,0.4);">
                <div class="layer-swatch"></div>
                <div class="layer-label">Mold Surface</div>
                <div class="layer-desc">Defines final part geometry</div>
              </div>
            </div>
            <div class="layup-resin-bar">
              <div class="layup-resin-fill"></div>
              <span>Resin infusion direction →</span>
            </div>
          </div>'''

old_vacuum = r'<a href="#contact" class="btn btn-primary mt-lg">Request a Quote</a>\n        </div>'
new_vacuum = layup_diagram + '\n        </div>'
content = re.sub(old_vacuum, new_vacuum, content, count=1)

# 2. Add hull watermark to marine section
hull_watermark = '''  <section id="marine" style="background: var(--sand-100);">
    <div class="hull-watermark" aria-hidden="true">
      <svg viewBox="0 0 1200 400" preserveAspectRatio="xMidYMid meet" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M100,80 L250,80 C350,80 400,100 450,140 C500,180 520,220 600,260 C680,220 700,180 750,140 C800,100 850,80 950,80 L1100,80" stroke="rgba(39,154,173,0.06)" stroke-width="2" fill="none"/>
        <path d="M560,240 C575,285 590,320 600,340 C610,320 625,285 640,240" stroke="rgba(39,154,173,0.05)" stroke-width="2" fill="none"/>
        <line x1="50" y1="80" x2="1150" y2="80" stroke="rgba(193,89,43,0.06)" stroke-width="1" stroke-dasharray="8 6"/>
        <line x1="400" y1="80" x2="470" y2="200" stroke="rgba(39,154,173,0.04)" stroke-width="1"/>
        <line x1="500" y1="80" x2="540" y2="240" stroke="rgba(39,154,173,0.04)" stroke-width="1"/>
        <line x1="600" y1="80" x2="600" y2="340" stroke="rgba(39,154,173,0.04)" stroke-width="1"/>
        <line x1="700" y1="80" x2="660" y2="240" stroke="rgba(39,154,173,0.04)" stroke-width="1"/>
        <line x1="800" y1="80" x2="730" y2="200" stroke="rgba(39,154,173,0.04)" stroke-width="1"/>
      </svg>
    </div>
    <div class="container">'''

old_marine = r'  <section id="marine" style="background: var\(--sand-100\);">\n    <div class="container">'
new_marine = hull_watermark
content = re.sub(old_marine, new_marine, content, count=1)

# 3. Add material bars to about section  
material_bars = '''        </div>
      </div>
    </div>

    <div class="material-bars reveal">
      <div class="material-bars-title">Process comparison</div>
      <div class="material-bar-row">
        <div class="bar-label">Strength-to-weight</div>
        <div class="bar-track"><div class="bar-fill" data-width="92" style="--bar-color: #279aad;"></div></div>
        <div class="bar-method">Vacuum infusion</div>
      </div>
      <div class="material-bar-row">
        <div class="bar-label">Strength-to-weight</div>
        <div class="bar-track"><div class="bar-fill" data-width="68" style="--bar-color: #c1592b;"></div></div>
        <div class="bar-method">Hand layup</div>
      </div>
      <div class="material-bar-row">
        <div class="bar-label">Resin consistency</div>
        <div class="bar-track"><div class="bar-fill" data-width="96" style="--bar-color: #279aad;"></div></div>
        <div class="bar-method">Vacuum infusion</div>
      </div>
      <div class="material-bar-row">
        <div class="bar-label">Resin consistency</div>
        <div class="bar-track"><div class="bar-fill" data-width="72" style="--bar-color: #c1592b;"></div></div>
        <div class="bar-method">Hand layup</div>
      </div>
      <div class="material-bar-row">
        <div class="bar-label">Geometric flexibility</div>
        <div class="bar-track"><div class="bar-fill" data-width="74" style="--bar-color: #279aad;"></div></div>
        <div class="bar-method">Vacuum infusion</div>
      </div>
      <div class="material-bar-row">
        <div class="bar-label">Geometric flexibility</div>
        <div class="bar-track"><div class="bar-fill" data-width="95" style="--bar-color: #c1592b;"></div></div>
        <div class="bar-method">Hand layup</div>
      </div>
      <div class="material-bar-row">
        <div class="bar-label">Repair suitability</div>
        <div class="bar-track"><div class="bar-fill" data-width="55" style="--bar-color: #279aad;"></div></div>
        <div class="bar-method">Vacuum infusion</div>
      </div>
      <div class="material-bar-row">
        <div class="bar-label">Repair suitability</div>
        <div class="bar-track"><div class="bar-fill" data-width="94" style="--bar-color: #c1592b;"></div></div>
        <div class="bar-method">Hand layup</div>
      </div>
    </div>'''

old_about = r'        </div>\n      </div>\n    </div>\n\n    <div class="grid cols-3 mt-lg">'
new_about = material_bars + '\n\n    <div class="grid cols-3 mt-lg">'
content = re.sub(old_about, new_about, content, count=1)

# 4. Add JavaScript before closing body
js_code = '''<script>
// ========== Enhancement 2: Resin Flow Divider Animation ==========
document.querySelectorAll('.resin-line').forEach(line => {
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('flowing');
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.5 });
  obs.observe(line);
});

// ========== Enhancement 6: Material Property Bars Animation ==========
const barFills = document.querySelectorAll('.bar-fill');
barFills.forEach(bar => {
  bar.style.setProperty('--target-width', bar.dataset.width + '%');
});
const barObs = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('animated');
      barObs.unobserve(e.target);
    }
  });
}, { threshold: 0.3 });
barFills.forEach(bar => barObs.observe(bar));
</script>

<script src="js/main.js"></script>'''

old_js = r'<script src="js/main.js"></script>'
new_js = js_code
content = re.sub(old_js, new_js, content, count=1)

# Write the file
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ Enhancements added successfully!")
