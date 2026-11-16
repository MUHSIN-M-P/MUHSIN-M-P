#!/usr/bin/env python3
"""
Clean, Punchy Asset Generator for MUHSIN-M-P GitHub Profile README.
High-end Obsidian-Coral Tech Cockpit.
- Primary Accent: #FF734D (Coral Orange)
- Accents: #38BDF8 (Sky Cyan), #F59E0B (Amber), #2DD4BF (Teal)
- Dark Backgrounds: #030712 / #080E1E / #0B1120
"""

import os
import html

ASSETS_DIR = "/run/media/ldzbeta/01DBBA8BC63F76B0/portfolio/MUHSIN-M-P/assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. HERO COCKPIT SVG (assets/hero.svg)
# -------------------------------------------------------------
hero_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <!-- Background Gradients -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#030712" />
      <stop offset="50%" stop-color="#080E1E" />
      <stop offset="100%" stop-color="#030712" />
    </linearGradient>

    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF9376" />
      <stop offset="50%" stop-color="#FF734D" />
      <stop offset="100%" stop-color="#FF451A" />
    </linearGradient>

    <radialGradient id="coralGlow" cx="20%" cy="35%" r="55%">
      <stop offset="0%" stop-color="#FF734D" stop-opacity="0.25" />
      <stop offset="60%" stop-color="#FF734D" stop-opacity="0.03" />
      <stop offset="100%" stop-color="#030712" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="cyanGlow" cx="80%" cy="30%" r="55%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.18" />
      <stop offset="55%" stop-color="#38BDF8" stop-opacity="0.02" />
      <stop offset="100%" stop-color="#030712" stop-opacity="0" />
    </radialGradient>

    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF734D" stop-opacity="0.7" />
      <stop offset="35%" stop-color="#38BDF8" stop-opacity="0.3" />
      <stop offset="70%" stop-color="#1E293B" stop-opacity="0.4" />
      <stop offset="100%" stop-color="#FF734D" stop-opacity="0.5" />
    </linearGradient>

    <!-- Grid Pattern -->
    <pattern id="cyberGrid" width="36" height="36" patternUnits="userSpaceOnUse">
      <path d="M 36 0 L 0 0 0 36" fill="none" stroke="#1E293B" stroke-width="0.8" stroke-opacity="0.45" />
      <circle cx="36" cy="36" r="1" fill="#38BDF8" opacity="0.35" />
    </pattern>

    <filter id="subtleGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="16" />
    </filter>
  </defs>

  <style>
    @keyframes pulseLive {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.2; }
    }
    @keyframes shimmerTitle {
      0%, 100% { filter: drop-shadow(0 0 16px rgba(255, 115, 77, 0.4)); }
      50% { filter: drop-shadow(0 0 28px rgba(255, 115, 77, 0.7)); }
    }

    .live-dot { animation: pulseLive 2s ease-in-out infinite; }
    .brand-title { animation: shimmerTitle 4s ease-in-out infinite; }

    .brand-name {
      font-family: 'Syne', 'Anton', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      font-weight: 800;
      letter-spacing: 5px;
    }
    .mono-meta {
      font-family: 'Geist Mono', 'Fira Code', 'JetBrains Mono', monospace;
    }
    .sans-text {
      font-family: 'Geist', 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }
  </style>

  <!-- Background Base -->
  <rect width="1200" height="400" rx="16" fill="url(#bgGrad)" />
  <rect width="1200" height="400" rx="16" fill="url(#cyberGrid)" />

  <!-- Ambient Light Fields -->
  <circle cx="280" cy="160" r="260" fill="url(#coralGlow)" filter="url(#subtleGlow)" />
  <circle cx="960" cy="150" r="240" fill="url(#cyanGlow)" filter="url(#subtleGlow)" />

  <!-- Outer Glass Border -->
  <rect x="1" y="1" width="1198" height="398" rx="15" fill="none" stroke="url(#borderGrad)" stroke-width="1.5" />

  <!-- Top Status HUD -->
  <g transform="translate(56, 40)">
    <!-- Pill 1: Status -->
    <g>
      <rect x="0" y="0" width="230" height="32" rx="16" fill="#0B1120" stroke="#1E293B" stroke-width="1.2" />
      <circle cx="18" cy="16" r="4.5" fill="#22C55E" class="live-dot" />
      <text x="32" y="21" class="mono-meta" font-size="11.5" fill="#E2E8F0" font-weight="700" letter-spacing="1">SYSTEM : ACTIVE</text>
      <text x="175" y="21" class="mono-meta" font-size="11" fill="#38BDF8" font-weight="600">v2.6</text>
    </g>

    <!-- Pill 2: Environment -->
    <g transform="translate(245, 0)">
      <rect x="0" y="0" width="220" height="32" rx="16" fill="#0B1120" stroke="#1E293B" stroke-width="1.2" />
      <text x="16" y="21" class="mono-meta" font-size="11" fill="#94A3B8">OS :</text>
      <text x="48" y="21" class="mono-meta" font-size="11" fill="#F1F5F9" font-weight="600">LINUX / HYPRLAND</text>
    </g>

    <!-- Pill 3: Campus -->
    <g transform="translate(735, 0)">
      <rect x="0" y="0" width="350" height="32" rx="16" fill="#0B1120" stroke="#1E293B" stroke-width="1.2" />
      <text x="16" y="21" class="mono-meta" font-size="11.5" fill="#FF734D" font-weight="700">🎓 NIT CALICUT</text>
      <text x="125" y="21" class="mono-meta" font-size="11" fill="#94A3B8">· B.TECH CSE · CLASS OF '26</text>
    </g>
  </g>

  <!-- Main Hero Brand Content -->
  <g transform="translate(56, 135)">
    <!-- Overline Category -->
    <g transform="translate(4, 0)">
      <rect x="0" y="-11" width="10" height="10" rx="2.5" fill="#38BDF8" />
      <text x="18" y="0" class="mono-meta" font-size="13" fill="#38BDF8" font-weight="700" letter-spacing="2.5">
        FULL-STACK DEVELOPER &amp; SYSTEMS ENTHUSIAST
      </text>
    </g>

    <!-- Primary Title -->
    <text x="0" y="66" class="brand-name brand-title" font-size="76" fill="url(#primaryGrad)">
      MUHSIN M P
    </text>

    <!-- Credo -->
    <g transform="translate(4, 102)">
      <rect x="0" y="-15" width="4" height="20" fill="#FF734D" rx="2" />
      <text x="14" y="0" class="sans-text" font-size="16" fill="#CBD5E1" font-weight="500">
        Tested. Broken. Perfecting. <tspan fill="#FF734D" font-weight="700">Built On Resilience.</tspan>
      </text>
    </g>
  </g>

  <!-- Architectural Pillars Dock (Bottom) -->
  <g transform="translate(56, 320)">
    <!-- Module 1: Web -->
    <g transform="translate(0, 0)">
      <rect x="0" y="0" width="255" height="44" rx="8" fill="#0B1120" stroke="#1E293B" stroke-width="1.2" />
      <rect x="0" y="0" width="4" height="44" rx="2" fill="#FF734D" />
      <text x="16" y="18" class="mono-meta" font-size="10" fill="#FF734D" font-weight="800" letter-spacing="1.5">01 // FULL-STACK</text>
      <text x="16" y="34" class="sans-text" font-size="12" fill="#E2E8F0" font-weight="600">Next.js · TypeScript · Prisma · Postgres</text>
    </g>

    <!-- Module 2: Desktop -->
    <g transform="translate(275, 0)">
      <rect x="0" y="0" width="255" height="44" rx="8" fill="#0B1120" stroke="#1E293B" stroke-width="1.2" />
      <rect x="0" y="0" width="4" height="44" rx="2" fill="#38BDF8" />
      <text x="16" y="18" class="mono-meta" font-size="10" fill="#38BDF8" font-weight="800" letter-spacing="1.5">02 // DESKTOP HUD</text>
      <text x="16" y="34" class="sans-text" font-size="12" fill="#E2E8F0" font-weight="600">QML · C++ · Wayland · Hyprland</text>
    </g>

    <!-- Module 3: Security & Containers -->
    <g transform="translate(550, 0)">
      <rect x="0" y="0" width="255" height="44" rx="8" fill="#0B1120" stroke="#1E293B" stroke-width="1.2" />
      <rect x="0" y="0" width="4" height="44" rx="2" fill="#F59E0B" />
      <text x="16" y="18" class="mono-meta" font-size="10" fill="#F59E0B" font-weight="800" letter-spacing="1.5">03 // DOCKER &amp; CLI</text>
      <text x="16" y="34" class="sans-text" font-size="12" fill="#E2E8F0" font-weight="600">Python CLI · RBAC · Container Audits</text>
    </g>

    <!-- Module 4: Low-Level -->
    <g transform="translate(825, 0)">
      <rect x="0" y="0" width="263" height="44" rx="8" fill="#0B1120" stroke="#1E293B" stroke-width="1.2" />
      <rect x="0" y="0" width="4" height="44" rx="2" fill="#2DD4BF" />
      <text x="16" y="18" class="mono-meta" font-size="10" fill="#2DD4BF" font-weight="800" letter-spacing="1.5">04 // SYSTEMS &amp; LABS</text>
      <text x="16" y="34" class="sans-text" font-size="12" fill="#E2E8F0" font-weight="600">C · POSIX Sockets · CSEA / CSC NITC</text>
    </g>
  </g>

  <!-- Technical Corner Brackets -->
  <g stroke="#FF734D" stroke-width="1.5" opacity="0.7">
    <path d="M 24 34 L 24 24 L 34 24" fill="none" />
    <path d="M 1176 34 L 1176 24 L 1166 24" fill="none" />
    <path d="M 24 366 L 24 376 L 34 376" fill="none" />
    <path d="M 1176 366 L 1176 376 L 1166 376" fill="none" />
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "hero.svg"), "w") as f:
    f.write(hero_svg)
print("✓ Created hero.svg")

# -------------------------------------------------------------
# 2. BESPOKE ACTION BADGES (Portfolio, LinkedIn, GitHub, Email, Resume)
# -------------------------------------------------------------
badges = [
    {
        "filename": "badge-portfolio.svg",
        "width": 160,
        "label": "PORTFOLIO",
        "color": "#FF734D",
        "icon": '''<circle cx="22" cy="18" r="6" fill="none" stroke="#FF734D" stroke-width="1.6"/>
                   <ellipse cx="22" cy="18" rx="3" ry="6" fill="none" stroke="#FF734D" stroke-width="1.3"/>
                   <line x1="16" y1="18" x2="28" y2="18" stroke="#FF734D" stroke-width="1.3"/>'''
    },
    {
        "filename": "badge-linkedin.svg",
        "width": 150,
        "label": "LINKEDIN",
        "color": "#38BDF8",
        "icon": '''<rect x="16" y="12" width="12" height="12" rx="2.5" fill="none" stroke="#38BDF8" stroke-width="1.6"/>
                   <line x1="19.5" y1="17" x2="19.5" y2="21" stroke="#38BDF8" stroke-width="1.4"/>
                   <circle cx="19.5" cy="15" r="0.7" fill="#38BDF8"/>
                   <path d="M 23 21 L 23 18.5 C 23 17.7 24.5 17.7 24.5 18.5 L 24.5 21" fill="none" stroke="#38BDF8" stroke-width="1.4"/>'''
    },
    {
        "filename": "badge-github.svg",
        "width": 140,
        "label": "GITHUB",
        "color": "#94A3B8",
        "icon": '''<path d="M 22 12 C 18.68 12 16 14.68 16 18 C 16 20.65 17.72 22.9 20.11 23.7 C 20.41 23.75 20.52 23.57 20.52 23.41 L 20.52 22.4 C 18.85 22.76 18.5 21.6 18.5 21.6 C 18.23 20.9 17.83 20.71 17.83 20.71 C 17.29 20.34 17.87 20.35 17.87 20.35 C 18.47 20.39 18.79 20.96 18.79 20.96 C 19.32 21.88 20.19 21.61 20.53 21.46 C 20.58 21.08 20.74 20.81 20.91 20.66 C 19.57 20.5 18.18 19.99 18.18 17.68 C 18.18 17.02 18.41 16.48 18.8 16.06 C 18.74 15.91 18.53 15.29 18.85 14.46 C 18.85 14.46 19.36 14.3 20.52 15.09 C 21 14.95 21.5 14.88 22 14.88 C 22.5 14.88 23 14.95 23.48 15.09 C 24.64 14.3 25.15 14.46 25.15 14.46 C 25.47 15.29 25.26 15.91 25.2 16.06 C 25.59 16.48 25.82 17.02 25.82 17.68 C 25.82 20 24.42 20.5 23.08 20.65 C 23.3 20.84 23.5 21.22 23.5 21.8 L 23.5 23.41 C 23.5 23.57 23.61 23.76 23.92 23.7 C 26.3 22.89 28 20.65 28 18 C 28 14.68 25.32 12 22 12 Z" fill="#94A3B8"/>'''
    },
    {
        "filename": "badge-email.svg",
        "width": 135,
        "label": "EMAIL",
        "color": "#F59E0B",
        "icon": '''<rect x="16" y="13" width="12" height="10" rx="1.5" fill="none" stroke="#F59E0B" stroke-width="1.6"/>
                   <path d="M 16 14.5 L 22 18.5 L 28 14.5" fill="none" stroke="#F59E0B" stroke-width="1.4"/>'''
    },
    {
        "filename": "badge-resume.svg",
        "width": 140,
        "label": "RESUME",
        "color": "#2DD4BF",
        "icon": '''<path d="M 17 12 L 23 12 L 27 16 L 27 24 L 17 24 Z" fill="none" stroke="#2DD4BF" stroke-width="1.6"/>
                   <line x1="20" y1="16" x2="22" y2="16" stroke="#2DD4BF" stroke-width="1.3"/>
                   <line x1="20" y1="20" x2="24" y2="20" stroke="#2DD4BF" stroke-width="1.3"/>'''
    }
]

for b in badges:
    fn = b["filename"]
    w = b["width"]
    c = b["color"]
    badge_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 36" width="{w}" height="36">
  <defs>
    <linearGradient id="bg_{fn}" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#050B18" />
    </linearGradient>
  </defs>
  <rect x="1" y="1" width="{w-2}" height="34" rx="17" fill="url(#bg_{fn})" stroke="{c}" stroke-opacity="0.5" stroke-width="1.2" />
  {b["icon"]}
  <text x="35" y="22" font-family="'Geist Mono', 'Fira Code', monospace" font-size="11" font-weight="700" fill="#F8FAFC" letter-spacing="1">{b["label"]}</text>
  <text x="{w - 18}" y="22" font-family="'Geist Mono', monospace" font-size="12" font-weight="600" fill="{c}">↗</text>
</svg>'''
    with open(os.path.join(ASSETS_DIR, fn), "w") as f:
        f.write(badge_svg)
    print(f"✓ Created {fn}")

# -------------------------------------------------------------
# 3. TAGLINE SVGS (assets/tagline-dark.svg & assets/tagline-light.svg)
# -------------------------------------------------------------
tagline_dark = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 50" width="100%" height="100%">
  <style>
    .t-main {
      font-family: 'Geist', 'Inter', -apple-system, sans-serif;
      font-size: 15px;
      font-weight: 500;
      fill: #E2E8F0;
      letter-spacing: 0.2px;
    }
    .t-glow {
      font-weight: 700;
      fill: #FF734D;
    }
    .t-sub {
      font-family: 'Geist Mono', 'Fira Code', monospace;
      font-size: 11.5px;
      font-weight: 600;
      fill: #94A3B8;
      letter-spacing: 1.5px;
    }
    .dot {
      fill: #38BDF8;
    }
  </style>

  <g transform="translate(450, 20)" text-anchor="middle">
    <text class="t-main" y="0">
      Building resilient software &amp; web architecture <tspan class="t-glow">from the ground up</tspan>.
    </text>
    <text class="t-sub" y="22">
      CAMPUS PORTALS <tspan class="dot">◆</tspan> WAYLAND WORKSPACES <tspan class="dot">◆</tspan> DOCKER TOOLS <tspan class="dot">◆</tspan> NETWORK LABS
    </text>
  </g>
</svg>'''

tagline_light = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 50" width="100%" height="100%">
  <style>
    .t-main-l {
      font-family: 'Geist', 'Inter', -apple-system, sans-serif;
      font-size: 15px;
      font-weight: 500;
      fill: #0F172A;
      letter-spacing: 0.2px;
    }
    .t-glow-l {
      font-weight: 700;
      fill: #EA580C;
    }
    .t-sub-l {
      font-family: 'Geist Mono', 'Fira Code', monospace;
      font-size: 11.5px;
      font-weight: 600;
      fill: #64748B;
      letter-spacing: 1.5px;
    }
    .dot-l {
      fill: #0284C7;
    }
  </style>

  <g transform="translate(450, 20)" text-anchor="middle">
    <text class="t-main-l" y="0">
      Building resilient software &amp; web architecture <tspan class="t-glow-l">from the ground up</tspan>.
    </text>
    <text class="t-sub-l" y="22">
      CAMPUS PORTALS <tspan class="dot-l">◆</tspan> WAYLAND WORKSPACES <tspan class="dot-l">◆</tspan> DOCKER TOOLS <tspan class="dot-l">◆</tspan> NETWORK LABS
    </text>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "tagline-dark.svg"), "w") as f:
    f.write(tagline_dark)
with open(os.path.join(ASSETS_DIR, "tagline-light.svg"), "w") as f:
    f.write(tagline_light)
print("✓ Created tagline SVGs")

# -------------------------------------------------------------
# 4. SECTION HEADINGS (01 Now, 02 Toolkit, 03 Activity)
# -------------------------------------------------------------
sections = [
    ("now", "01 // RIGHT NOW", 260),
    ("toolkit", "02 // TECH STACK", 260),
    ("activity", "03 // RECENT ACTIVITY", 310)
]

for key, title, width in sections:
    svg_dark = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 44" width="{width}" height="44">
  <defs>
    <linearGradient id="hG_{key}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FF9376" />
      <stop offset="100%" stop-color="#FF734D" />
    </linearGradient>
  </defs>
  <style>
    .h-title {{
      font-family: 'Geist Mono', 'Fira Code', monospace;
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 2px;
      fill: #F8FAFC;
    }}
  </style>
  <g transform="translate(10, 28)">
    <rect x="0" y="-17" width="5" height="22" rx="2.5" fill="url(#hG_{key})" />
    <circle cx="16" cy="-6" r="3" fill="#38BDF8" />
    <text x="28" y="0" class="h-title">{title}</text>
  </g>
</svg>'''

    svg_light = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 44" width="{width}" height="44">
  <defs>
    <linearGradient id="hGL_{key}" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#EA580C" />
      <stop offset="100%" stop-color="#FF734D" />
    </linearGradient>
  </defs>
  <style>
    .h-title-l {{
      font-family: 'Geist Mono', 'Fira Code', monospace;
      font-size: 15px;
      font-weight: 800;
      letter-spacing: 2px;
      fill: #0F172A;
    }}
  </style>
  <g transform="translate(10, 28)">
    <rect x="0" y="-17" width="5" height="22" rx="2.5" fill="url(#hGL_{key})" />
    <circle cx="16" cy="-6" r="3" fill="#0284C7" />
    <text x="28" y="0" class="h-title-l">{title}</text>
  </g>
</svg>'''

    with open(os.path.join(ASSETS_DIR, f"heading-{key}-dark.svg"), "w") as f:
        f.write(svg_dark)
    with open(os.path.join(ASSETS_DIR, f"heading-{key}-light.svg"), "w") as f:
        f.write(svg_light)

print("✓ Created Section Headings")

# -------------------------------------------------------------
# 5. SKILLS MARQUEE (assets/skills-marquee.svg)
# -------------------------------------------------------------
skills_data = [
    {"cat": "LANGUAGES", "color": "#FF734D"},
    {"name": "C++", "tech": "cplusplus"},
    {"name": "C", "tech": "c"},
    {"name": "TypeScript", "tech": "typescript"},
    {"name": "JavaScript", "tech": "javascript"},
    {"name": "Python", "tech": "python"},
    {"name": "SQL", "tech": "postgresql"},
    {"name": "QML", "tech": "qt"},

    {"cat": "FRONTEND & UI", "color": "#38BDF8"},
    {"name": "Next.js", "tech": "nextdotjs"},
    {"name": "React", "tech": "react"},
    {"name": "Tailwind CSS", "tech": "tailwindcss"},
    {"name": "HTML5 / CSS3", "tech": "html5"},

    {"cat": "BACKEND & DB", "color": "#F59E0B"},
    {"name": "Node.js", "tech": "nodedotjs"},
    {"name": "Express.js", "tech": "express"},
    {"name": "FastAPI", "tech": "fastapi"},
    {"name": "Flask", "tech": "flask"},
    {"name": "PostgreSQL", "tech": "postgresql"},
    {"name": "Prisma", "tech": "prisma"},

    {"cat": "SYSTEMS & TOOLS", "color": "#2DD4BF"},
    {"name": "Linux / Hyprland", "tech": "linux"},
    {"name": "Docker", "tech": "docker"},
    {"name": "Git & GitHub", "tech": "git"},
    {"name": "Socket Programming", "tech": "network"},
    {"name": "Postman", "tech": "postman"},
    {"name": "VS Code", "tech": "vscode"},
]

row_elements = []
current_x = 0
spacing = 12

for item in skills_data:
    if "cat" in item:
        raw_label = item["cat"]
        label = html.escape(raw_label)
        color = item["color"]
        w = len(raw_label) * 9 + 28
        row_elements.append(
            f'<rect x="{current_x}" y="8" width="{w}" height="32" rx="16" fill="{color}" />'
            f'<text x="{current_x + w/2}" y="28" text-anchor="middle" font-family="\'Geist Mono\', monospace" font-size="11" font-weight="800" fill="#030712" letter-spacing="1.2">{label}</text>'
        )
        current_x += w + spacing
    else:
        raw_name = item["name"]
        name = html.escape(raw_name)
        w = len(raw_name) * 8 + 34
        row_elements.append(
            f'<rect x="{current_x}" y="8" width="{w}" height="32" rx="16" fill="#0B1120" stroke="#1E293B" stroke-width="1.2" />'
            f'<circle cx="{current_x + 16}" cy="24" r="3" fill="#FF734D" />'
            f'<text x="{current_x + 26}" y="28" font-family="\'Geist\', sans-serif" font-size="12" font-weight="600" fill="#E2E8F0">{name}</text>'
        )
        current_x += w + spacing

total_width = current_x

skills_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 48" width="100%" height="48">
  <defs>
    <style>
      @keyframes scrollRibbon {{
        0% {{ transform: translateX(0px); }}
        100% {{ transform: translateX(-{total_width}px); }}
      }}
      .track {{
        animation: scrollRibbon 36s linear infinite;
      }}
      .track:hover {{
        animation-play-state: paused;
      }}
    </style>

    <linearGradient id="fadeEdge" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#000" stop-opacity="0" />
      <stop offset="5%" stop-color="#000" stop-opacity="1" />
      <stop offset="95%" stop-color="#000" stop-opacity="1" />
      <stop offset="100%" stop-color="#000" stop-opacity="0" />
    </linearGradient>

    <mask id="edgeMask">
      <rect x="0" y="0" width="960" height="48" fill="url(#fadeEdge)" />
    </mask>

    <g id="skillSet">
      {"".join(row_elements)}
    </g>
  </defs>

  <g mask="url(#edgeMask)">
    <g class="track">
      <use href="#skillSet" x="0" />
      <use href="#skillSet" x="{total_width}" />
    </g>
  </g>
</svg>'''

with open(os.path.join(ASSETS_DIR, "skills-marquee.svg"), "w") as f:
    f.write(skills_svg)
print(f"✓ Created skills-marquee.svg")

# -------------------------------------------------------------
# 6. TERMINAL HEADER HUD (assets/terminal-header.svg)
# -------------------------------------------------------------
terminal_header_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 38" width="100%" height="38">
  <defs>
    <linearGradient id="termGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0F172A" />
      <stop offset="100%" stop-color="#090D16" />
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="960" height="38" rx="8" fill="url(#termGrad)" stroke="#1E293B" stroke-width="1.2" />
  
  <!-- Window Controls -->
  <circle cx="20" cy="19" r="5" fill="#EF4444" />
  <circle cx="35" cy="19" r="5" fill="#F59E0B" />
  <circle cx="50" cy="19" r="5" fill="#10B981" />

  <!-- Terminal Title -->
  <text x="480" y="24" text-anchor="middle" font-family="'Geist Mono', monospace" font-size="11.5" fill="#94A3B8" font-weight="600">
    <tspan fill="#FF734D">muhsin@nitc</tspan> : ~/recent-commits <tspan fill="#38BDF8">(git log --oneline)</tspan>
  </text>
  
  <circle cx="940" cy="19" r="4" fill="#22C55E" />
</svg>'''

with open(os.path.join(ASSETS_DIR, "terminal-header.svg"), "w") as f:
    f.write(terminal_header_svg)
print("✓ Created terminal-header.svg")

print("\n🚀 All assets refreshed!")
