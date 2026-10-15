"""Generate the SVG assets for the iaski15 GitHub profile README (light + dark)."""
import os, sys
from xml.sax.saxutils import escape

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, monospace"

THEMES = {
    "light": dict(bg="#FFF4E6", card="#FFFFFF", border="#F0D9BC", ink="#2B2B2B",
                  sub="#6B5A48", accent="#E8A55B", accent2="#C97F2E", chip="#FCE8D0",
                  chipInk="#8A5520", cream="#FFF4E6"),
    "dark": dict(bg="#161210", card="#1F1915", border="#3A2E24", ink="#F5ECE1",
                 sub="#BFAE9C", accent="#E8A55B", accent2="#F2BC7E", chip="#33271D",
                 chipInk="#F2BC7E", cream="#FFF4E6"),
}


def shiba(x, y, s, t):
    """The Shiba Lift face, redrawn as vector. (x, y) is top-left, s is the size."""
    k = s / 1024
    def P(px, py):
        return f"{x + px * k:.1f},{y + py * k:.1f}"
    a, c, ink = t["accent"], t["cream"], "#2B2B2B"
    return f"""
  <g>
    <polygon points="{P(240,450)} {P(283,178)} {P(450,318)}" fill="{a}"/>
    <polygon points="{P(784,450)} {P(741,178)} {P(574,318)}" fill="{a}"/>
    <polygon points="{P(302,380)} {P(316,243)} {P(405,326)}" fill="{c}"/>
    <polygon points="{P(722,380)} {P(708,243)} {P(619,326)}" fill="{c}"/>
    <ellipse cx="{x+512*k:.1f}" cy="{y+580*k:.1f}" rx="{311*k:.1f}" ry="{270*k:.1f}" fill="{a}"/>
    <ellipse cx="{x+512*k:.1f}" cy="{y+703*k:.1f}" rx="{222*k:.1f}" ry="{138*k:.1f}" fill="{c}"/>
    <circle cx="{x+405*k:.1f}" cy="{y+465*k:.1f}" r="{25*k:.1f}" fill="{c}"/>
    <circle cx="{x+619*k:.1f}" cy="{y+465*k:.1f}" r="{25*k:.1f}" fill="{c}"/>
    <circle cx="{x+413*k:.1f}" cy="{y+555*k:.1f}" r="{37*k:.1f}" fill="{ink}"/>
    <circle cx="{x+611*k:.1f}" cy="{y+555*k:.1f}" r="{37*k:.1f}" fill="{ink}"/>
    <ellipse cx="{x+348*k:.1f}" cy="{y+645*k:.1f}" rx="{41*k:.1f}" ry="{24*k:.1f}" fill="#F5B5A8"/>
    <ellipse cx="{x+676*k:.1f}" cy="{y+645*k:.1f}" rx="{41*k:.1f}" ry="{24*k:.1f}" fill="#F5B5A8"/>
    <ellipse cx="{x+512*k:.1f}" cy="{y+636*k:.1f}" rx="{37*k:.1f}" ry="{26*k:.1f}" fill="{ink}"/>
    <path d="M{P(462,678)} Q{P(487,705)} {P(512,668)} Q{P(537,705)} {P(562,678)}"
          fill="none" stroke="{ink}" stroke-width="{14*k:.1f}" stroke-linecap="round"/>
  </g>"""


def banner(t, name):
    W, H = 1000, 260
    paws = "".join(
        f'<g fill="{t["accent"]}" opacity="{op}" transform="translate({px},{py}) rotate({r})">'
        f'<ellipse cx="0" cy="8" rx="11" ry="9"/><circle cx="-11" cy="-6" r="4.5"/>'
        f'<circle cx="-4" cy="-12" r="4.5"/><circle cx="4" cy="-12" r="4.5"/><circle cx="11" cy="-6" r="4.5"/></g>'
        for px, py, r, op in [(880, 52, 20, .18), (930, 104, 30, .14), (884, 158, 15, .11), (936, 210, 28, .08)])
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="iaski15">
  <defs>
    <linearGradient id="g" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{t['card']}"/><stop offset="1" stop-color="{t['bg']}"/>
    </linearGradient>
    <style>
      .fade {{ animation: f 0.9s ease-out both; }}
      .d1 {{ animation-delay: .15s }} .d2 {{ animation-delay: .3s }}
      @keyframes f {{ from {{ opacity: 0; transform: translateY(6px) }} to {{ opacity: 1; transform: none }} }}
      .bob {{ animation: b 3.6s ease-in-out infinite; transform-origin: center; transform-box: fill-box; }}
      @keyframes b {{ 0%,100% {{ transform: rotate(0deg) }} 50% {{ transform: rotate(-4deg) }} }}
      @media (prefers-reduced-motion: reduce) {{ .fade, .bob {{ animation: none }} }}
    </style>
  </defs>
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="22" fill="url(#g)" stroke="{t['border']}" stroke-width="2"/>
  <circle cx="160" cy="130" r="92" fill="{t['chip']}"/>
  <g class="bob">{shiba(68, 38, 184, t)}</g>
  {paws}
  <text class="fade" x="300" y="112" font-family="{FONT}" font-size="54" font-weight="800" fill="{t['ink']}">Hi, I'm {escape(name)}</text>
  <text class="fade d1" x="302" y="154" font-family="{FONT}" font-size="21" fill="{t['sub']}">I build small, polished tools for Windows and Android —</text>
  <text class="fade d1" x="302" y="182" font-family="{FONT}" font-size="21" fill="{t['sub']}">mostly in C# and TypeScript, usually with a shiba on them.</text>
  <g class="fade d2" font-family="{MONO}" font-size="14" font-weight="600">
    {chips(t, 302, 208, ["C# / .NET", "WPF", "React Native", "Kotlin", "Win32 / PE"])}
  </g>
</svg>"""
    return svg


def chips(t, x, y, labels, size=14):
    out, cx = [], x
    for l in labels:
        w = len(l) * size * 0.62 + 22
        out.append(f'<rect x="{cx:.0f}" y="{y}" width="{w:.0f}" height="28" rx="14" fill="{t["chip"]}"/>'
                   f'<text x="{cx + w/2:.0f}" y="{y+19}" text-anchor="middle" fill="{t["chipInk"]}">{escape(l)}</text>')
        cx += w + 8
    return "".join(out)


def card(t, title, emoji_shape, lines, tags, foot):
    W, H = 480, 200
    body = "".join(
        f'<text x="28" y="{98 + i*24}" font-family="{FONT}" font-size="15.5" fill="{t["sub"]}">{escape(l)}</text>'
        for i, l in enumerate(lines))
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{escape(title)}">
  <rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16" fill="{t['card']}" stroke="{t['border']}" stroke-width="2"/>
  <clipPath id="c"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="16"/></clipPath>
  <rect x="0" y="0" width="7" height="{H}" fill="{t['accent']}" clip-path="url(#c)"/>
  <circle cx="44" cy="46" r="18" fill="{t['chip']}"/>
  <g transform="translate(44,46)" fill="none" stroke="{t['accent2']}" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{emoji_shape}</g>
  <text x="74" y="54" font-family="{FONT}" font-size="23" font-weight="750" fill="{t['ink']}">{escape(title)}</text>
  <text x="{W-26}" y="53" text-anchor="end" font-family="{MONO}" font-size="12.5" fill="{t['sub']}">{escape(foot)}</text>
  {body}
  <g font-family="{MONO}" font-size="12.5" font-weight="600">{chips(t, 28, 152, tags, 12.5)}</g>
</svg>"""


# Small line icons, drawn around (0,0) within ~±10px.
ICON = {
    "lift": '<path d="M-10 0h20M-7 -6v12M-4 -4v8M7 -6v12M4 -4v8"/>',
    "patch": '<path d="M-8 -3l5 -5 11 11 -5 5z"/><path d="M-3 2l-5 5M2 -3l5 -5"/>',
    "tag": '<path d="M-9 -9h8l9 9 -8 8 -9 -9z"/><circle cx="-5" cy="-5" r="1.4"/>',
    "music": '<path d="M-4 6v-14l11 -2v13"/><circle cx="-7" cy="6" r="3"/><circle cx="4" cy="4" r="3"/>',
    "scan": '<circle cx="-2" cy="-2" r="6.5"/><path d="M3 3l6 6"/>',
    "play": '<rect x="-10" y="-7" width="20" height="14" rx="4"/><path d="M-2 -3l5 3 -5 3z"/>',
}

CARDS = [
    ("shiba-lift", "Shiba Lift", "lift",
     ["Workout tracker with real progressive overload,",
      "a Wear OS companion app, Hevy sync & a social feed."],
     ["React Native", "Expo", "Kotlin", "Supabase"], "Android"),
    ("shibaberg", "Shibaberg", "patch",
     ["One-click Goldberg emulator patcher: PE analysis,",
      "in-process SteamStub unpacking, journalled undo."],
     ["C#", ".NET 4.8", "WinForms", "PE parsing"], "Windows"),
    ("shibatag", "ShibaTag", "tag",
     ["Cleans up music folders: fills missing tags from",
      "file names, finds covers, groups duplicates."],
     ["C#", "WPF", "iTunes API", "Installer"], "Windows"),
    ("spotify", "Spotify to MP3", "music",
     ["Turns Spotify tracks, albums & playlists into local",
      "audio, with its own YouTube InnerTube client."],
     ["C#", ".NET 10", "WPF", "NAudio"], "Windows"),
    ("drm", "DRM Detector", "scan",
     ["Scans game executables for DRM & packer",
      "signatures. GUI plus a scriptable --scan CLI."],
     ["C#", ".NET 8", "WPF", "CLI"], "Windows"),
    ("youtube", "YouTube to MP3", "play",
     ["Paste a link, get an MP3 or 1080p MP4.",
      "Preview card, live progress, friendly errors."],
     ["C#", "WPF", "yt-dlp", "ffmpeg"], "Windows"),
]

for theme, t in THEMES.items():
    open(f"{OUT}/banner-{theme}.svg", "w").write(banner(t, "iaski"))
    for slug, title, icon, lines, tags, foot in CARDS:
        open(f"{OUT}/card-{slug}-{theme}.svg", "w").write(card(t, title, ICON[icon], lines, tags, foot))
print("ok", sorted(os.listdir(OUT)))
