#!/usr/bin/env python3
"""
RAUPULUS MUSIC — build.py
Generador estático para la web oficial (music.raupulus.dev).
Lee data/songs.json, compila dist/index.html, dist/canciones/*.html, sitemap.xml y robots.txt.
"""

import os
import json
import shutil
import html
from datetime import datetime

SITE_URL = "https://music.raupulus.dev"
YT_CHANNEL = "https://www.youtube.com/@RaupulusMusic"
YT_PERSONAL = "https://www.youtube.com/@raupulus"
PUBLIC_EMAIL = "public@raupulus.dev"
ALBUM_TITLE = "CD 1 — Nunca venderé mi alma de Metal"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "data", "songs.json")
DIST_DIR = os.path.join(BASE_DIR, "dist")
SRC_DIR = os.path.join(BASE_DIR, "src")

def ensure_dirs():
    os.makedirs(os.path.join(DIST_DIR, "assets", "css"), exist_ok=True)
    os.makedirs(os.path.join(DIST_DIR, "assets", "js"), exist_ok=True)
    os.makedirs(os.path.join(DIST_DIR, "assets", "images", "covers"), exist_ok=True)
    os.makedirs(os.path.join(DIST_DIR, "canciones"), exist_ok=True)

def copy_assets():
    # CSS
    shutil.copy2(os.path.join(SRC_DIR, "css", "style.css"), os.path.join(DIST_DIR, "assets", "css", "style.css"))
    # JS
    shutil.copy2(os.path.join(SRC_DIR, "js", "main.js"), os.path.join(DIST_DIR, "assets", "js", "main.js"))
    alpine_src = os.path.join(SRC_DIR, "js", "alpine.min.js")
    if os.path.exists(alpine_src):
        shutil.copy2(alpine_src, os.path.join(DIST_DIR, "assets", "js", "alpine.min.js"))

def load_songs():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_index(songs):
    first_song = songs[0] if songs else {}

    cards_html = []
    for s in songs:
        synopsis_short = html.escape(s.get('synopsis', ''))
        title_esc = html.escape(s['title'])
        card = f"""
        <article class="song-card" data-title="{title_esc.lower()}" data-slug="{s['slug']}">
          <div class="card-media">
            <span class="card-badge-num">#{s['number']:02d}</span>
            <span class="card-badge-dur">{s['duration']}</span>
            <img src="assets/images/covers/{s['cover_file']}" alt="Portada {title_esc} — Raupulus Music" loading="lazy" width="640" height="360">
          </div>
          <div class="card-body">
            <div>
              <h3 class="card-title">{title_esc}</h3>
              <p class="card-synopsis">{synopsis_short}</p>
            </div>
            <div class="card-footer">
              <a href="canciones/{s['slug']}.html" class="btn btn-outline btn-sm">Ver Vídeo y Letra</a>
              <button type="button" class="btn btn-purple btn-sm" 
                      data-spotlight-switch 
                      data-num="{s['number']}"
                      data-title="{title_esc}"
                      data-duration="{s['duration']}"
                      data-synopsis="{synopsis_short}"
                      data-cover="assets/images/covers/{s['cover_file']}"
                      data-slug="{s['slug']}"
                      data-ytid="{s.get('youtube_id', '')}">
                Vista Previa
              </button>
            </div>
          </div>
        </article>
        """
        cards_html.append(card)

    songs_grid_str = "\n".join(cards_html)

    # Schema JSON-LD for Album
    tracks_ld = []
    for s in songs:
        tracks_ld.append({
            "@type": "MusicRecording",
            "name": s['title'],
            "url": f"{SITE_URL}/canciones/{s['slug']}.html",
            "duration": f"PT{s['duration'].replace(':', 'M')}S",
            "position": s['number']
        })

    schema_ld = {
        "@context": "https://schema.org",
        "@type": "MusicAlbum",
        "name": ALBUM_TITLE,
        "byArtist": {
            "@type": "MusicGroup",
            "name": "Raupulus Music",
            "url": YT_CHANNEL
        },
        "genre": ["Industrial Metal", "Cyber Hardcore", "Metal IA"],
        "numTracks": len(songs),
        "track": tracks_ld
    }

    index_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Raupulus Music — Metal Industrial, Cyberpunk & Videoclips con IA</title>
  <meta name="description" content="Sitio oficial de Raupulus Music. Descubre el álbum 'CD 1: Nunca venderé mi alma de Metal', 23 videoclips cinematográficos, letras oficiales y el universo visual de R-Avatar.">
  <link rel="canonical" href="{SITE_URL}/">

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="{SITE_URL}/">
  <meta property="og:title" content="Raupulus Music — CD 1: Nunca venderé mi alma de Metal">
  <meta property="og:description" content="23 canciones de puro Metal Industrial y Cyber Hardcore con 570 clips generados por IA cinematográfica. Explora los vídeos y las letras oficiales.">
  <meta property="og:image" content="{SITE_URL}/assets/images/banner.jpg">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{SITE_URL}/">
  <meta name="twitter:title" content="Raupulus Music — Álbum Oficial CD 1">
  <meta name="twitter:description" content="Metal Industrial y Videoclips Cinematográficos de R-Avatar. Letras, historias y vídeos en YouTube.">
  <meta name="twitter:image" content="{SITE_URL}/assets/images/banner.jpg">

  <link rel="icon" type="image/png" href="assets/images/avatar-circular.png">
  <link rel="stylesheet" href="assets/css/style.css">

  <script type="application/ld+json">
  {json.dumps(schema_ld, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>

  <!-- Siluetas de R-Avatar de fondo -->
  <div class="bg-watermark"></div>
  <div class="bg-watermark-left"></div>

  <!-- Barra de Navegación -->
  <nav class="site-nav" aria-label="Navegación principal">
    <div class="container">
      <a href="{SITE_URL}/" class="nav-brand">
        <img src="assets/images/logo.png" alt="Logo Oficial Raupulus Music">
        <div class="nav-brand-text">
          <span class="nav-brand-title">RAUPULUS</span>
          <span class="nav-brand-sub">MUSIC</span>
        </div>
      </a>

      <ul class="nav-links">
        <li><a href="#inicio" class="active">Inicio</a></li>
        <li><a href="#spotlight">Destacado</a></li>
        <li><a href="#canciones">Canciones ({len(songs)})</a></li>
        <li><a href="#universo">Universo R-Avatar</a></li>
        <li><a href="#proyecto">El Proyecto</a></li>
      </ul>

      <div class="nav-cta">
        <a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="btn btn-yt btn-sm">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          Canal YouTube
        </a>
      </div>

      <button class="mobile-menu-btn" aria-label="Abrir menú de navegación">☰</button>
    </div>
  </nav>

  <!-- Hero Section -->
  <header id="inicio" class="hero">
    <div class="container hero-grid">
      <div class="hero-content">
        <div class="badge badge-cyan">⚡ LANZAMIENTO OFICIAL • CD 1</div>
        <h1 class="hero-title">NUNCA VENDERÉ MI ALMA DE <span class="highlight-purple">METAL</span></h1>
        <p class="hero-subtitle">Metal Industrial • Cyber Hardcore • Inteligencia Artificial</p>
        <p class="hero-desc">
          Sumérgete en la odisea visceral de <strong>R-Avatar</strong>: 23 composiciones brutales y 570 clips cinematográficos generados por IA que desafían el horizonte sonoro y visual.
        </p>

        <div class="hero-actions">
          <a href="#canciones" class="btn btn-purple btn-lg">Explorar las 23 Canciones</a>
          <a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="btn btn-yt btn-lg">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
            Ver en YouTube
          </a>
          <a href="#universo" class="btn btn-outline btn-lg">Conocer a R-Avatar</a>
        </div>

        <div class="hero-stats">
          <div class="stat-item">
            <span class="stat-num highlight-purple">23</span>
            <span class="stat-label">Canciones y Capítulos</span>
          </div>
          <div class="stat-item">
            <span class="stat-num highlight-cyan">570</span>
            <span class="stat-label">Clips Cinematográficos (10s)</span>
          </div>
          <div class="stat-item">
            <span class="stat-num">100%</span>
            <span class="stat-label">Pasión y Arte Conceptual</span>
          </div>
        </div>
      </div>

      <div class="hero-media">
        <div class="hero-avatar-frame">
          <img src="assets/images/r-avatar-portrait.jpg" alt="R-Avatar — Soberano de la corteza y plasma violeta" width="440" height="550">
          <div class="hero-avatar-overlay">
            <span class="hero-avatar-name">R-Avatar</span>
            <span class="hero-avatar-role">Protagonista Canónico del Álbum</span>
          </div>
        </div>
      </div>
    </div>
  </header>

  <!-- Spotlight Player -->
  <section id="spotlight" class="section">
    <div class="container">
      <div class="section-header">
        <div class="badge">VISTA PREVIA INTERACTIVA</div>
        <h2>REPRODUCTOR DESTACADO</h2>
        <p>Selecciona cualquier pista del álbum para explorar su ambientación, sinopsis y enlace oficial de YouTube.</p>
      </div>

      <div class="spotlight-card">
        <div class="spotlight-video-wrap">
          <div class="spotlight-poster">
            <img id="spotlight-img" src="assets/images/covers/{first_song.get('cover_file', 'cover-01.jpg')}" alt="Portada {first_song.get('title', '')}">
            <div class="spotlight-play-overlay">
              <a id="spotlight-yt" href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="play-circle" aria-label="Reproducir en YouTube">
                <svg width="34" height="34" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
              </a>
              <span class="badge badge-yt">🔴 Reproducir en YouTube</span>
            </div>
          </div>
        </div>

        <div class="spotlight-info">
          <div class="spotlight-top">
            <div style="display: flex; gap: 10px; align-items: center;">
              <span id="spotlight-num" class="badge">#01</span>
              <span id="spotlight-dur" class="badge badge-cyan">{first_song.get('duration', '03:31')}</span>
              <span class="badge">CD 1</span>
            </div>
            <h3 id="spotlight-title" class="spotlight-title">{html.escape(first_song.get('title', 'Corona de Hierro'))}</h3>
            <p id="spotlight-synopsis" class="spotlight-synopsis">{html.escape(first_song.get('synopsis', ''))}</p>
          </div>

          <div class="spotlight-actions">
            <a id="spotlight-link" href="canciones/{first_song.get('slug', '01-corona-de-hierro')}.html" class="btn btn-purple">
              Ver Letra Completa & Vídeo
            </a>
            <a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="btn btn-yt">
              Suscribirse al Canal
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Album Tracks Grid -->
  <section id="canciones" class="section">
    <div class="container">
      <div class="section-header">
        <div class="badge badge-cyan">REPERTORIO COMPLETO</div>
        <h2>LAS 23 CANCIONES DEL DISCO</h2>
        <p>Cada canción cuenta con su propia historia cinematográfica sincronizada a 10 segundos por clip, letra oficial protegida y arte conceptual único.</p>
      </div>

      <!-- Buscador y filtro -->
      <div class="toolbar">
        <div class="search-box">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
          <input type="text" id="song-search" placeholder="Buscar por título o temática (ej: Corona, Lobo, Máquina, Mar)..." aria-label="Buscador de canciones">
        </div>
        <div class="filter-count" id="search-count">
          Mostrando {len(songs)} de {len(songs)} canciones
        </div>
      </div>

      <div id="no-results" style="display: none; text-align: center; padding: 40px 0; color: var(--text-dim);">
        <p>No se encontraron canciones con ese criterio de búsqueda.</p>
      </div>

      <div class="songs-grid">
        {songs_grid_str}
      </div>
    </div>
  </section>

  <!-- Universo Visual R-Avatar -->
  <section id="universo" class="section">
    <div class="container">
      <div class="section-header">
        <div class="badge">LORE & CONCEPT ART</div>
        <h2>EL UNIVERSO VISUAL DE R-AVATAR</h2>
        <p>Un cosmos donde la madera de ébano viva, la bioelectricidad violeta y el poder industrial colisionan.</p>
      </div>

      <div class="universe-grid">
        <div class="lore-card">
          <div class="badge">PROTAGONISTA PRINCIPAL</div>
          <h3 class="lore-title">R-Avatar</h3>
          <p>Entidad humanoide atlética (~1.95 m) esculpida en haces de músculo de ébano oscuro, sin piel pero con cero aspecto esquelético. Recorrido por venas bioluminiscentes violetas/magenta (#9b4dff).</p>
          <ul class="lore-list">
            <li><span class="bullet">✦</span> <strong>Cabeza:</strong> Cuernos curvados de madera orgánica y calavera de madera con sonrisa afilada.</li>
            <li><span class="bullet">✦</span> <strong>Cerebro Expuesto:</strong> Tejido neural pulsante con fisuras bioeléctricas violetas y cian.</li>
            <li><span class="bullet">✦</span> <strong>Mirada:</strong> Exactamente 8 ojos violetas sin pupilas (2 orbitales, 2 frontales, 4 temporales).</li>
            <li><span class="bullet">✦</span> <strong>Extremidades:</strong> Zarpas afiladas violetas y pies tridáctilos de velociraptor.</li>
          </ul>
        </div>

        <div class="lore-card">
          <div class="badge badge-cyan">EL HERMANO Y LEAL ALIADO</div>
          <h3 class="lore-title">Wolf-Avatar</h3>
          <p>Lobo titánico de pelaje negro carbón y musculatura de madera orgánica viva. Es el protagonista del capítulo 10 ("Mi mejor amigo Ladra"), representando la fidelidad inquebrantable que cura el aislamiento del alma.</p>
          <ul class="lore-list">
            <li><span class="bullet">✦</span> Furia salvaje en combate y ternura protectora junto a R-Avatar.</li>
            <li><span class="bullet">✦</span> Colmillos de marfil negro y ojos fulgurantes que detectan el peligro en la niebla.</li>
          </ul>
        </div>

        <div class="lore-card">
          <div class="badge">LA MUSA TRÁGICA</div>
          <h3 class="lore-title">M-Love-Avatar</h3>
          <p>Figura femenina etérea esculpida en madera de cerezo oscura y zafiro, protagonista del desgarrador capítulo 18 ("Mi amada tiene fecha de caducidad"). Representa la belleza de lo efímero y la despedida de un amor inmortal.</p>
          <ul class="lore-list">
            <li><span class="bullet">✦</span> Danza sobre las cumbres donde la muerte se convierte en ascensión cósmica.</li>
            <li><span class="bullet">✦</span> Líneas bioeléctricas doradas y púrpuras que se apagan con dulzura al amanecer.</li>
          </ul>
        </div>
      </div>

      <div style="margin-top: 50px; text-align: center;">
        <div style="position: relative; max-width: 1100px; margin: 0 auto; border-radius: var(--radius-lg); overflow: hidden; border: 1px solid var(--border-accent); box-shadow: var(--shadow-card), var(--shadow-glow);">
          <img src="assets/images/r-avatar-triptych.jpg" alt="R-Avatar — Tríptico de Poses Épicas: Riff de Guitarra, Alas Demoníacas y Soberano del Trono" style="width: 100%; height: auto; display: block;" loading="lazy">
        </div>
        <p style="margin-top: 14px; font-size: 0.9rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.08em;">
          Furia Sonora • Ascensión de Plasma • Trono de los Sesenta Mares
        </p>
      </div>
    </div>
  </section>

  <!-- Sobre el Proyecto & SEO -->
  <section id="proyecto" class="section">
    <div class="container">
      <div class="content-box" style="background: linear-gradient(135deg, #0d0a17 0%, #151022 100%);">
        <div class="badge badge-cyan">MANIFIESTO CREATIVO</div>
        <h2 style="font-size: 2rem; margin: 14px 0 16px;">Vanguardia Sonora y Dirección Cinematográfica con IA</h2>
        <p style="font-size: 1.05rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 20px;">
          <strong>Raupulus Music</strong> nace como una visión artística integral donde el metal extremo (Industrial Metal, Cyber Hardcore, Djent y Dark Synth) se fusiona con la potencia de la Inteligencia Artificial generativa para construir películas sonoras compás a compás.
        </p>
        <p style="font-size: 1.02rem; line-height: 1.8; color: var(--text-muted); margin-bottom: 24px;">
          Lejos de ser experimentos aleatorios, cada videoclip de <em>Nunca venderé mi alma de Metal</em> ha sido planeado con un guion técnico matemático: 570 planos de 10 segundos sincronizados al milisegundo con la rítmica y la lírica, con Foley diegético de entorno (viento, chispas, cadenas, agua hirviente) que expande la experiencia auditiva sin interferir con la contundencia del metal.
        </p>
        <div style="display: flex; gap: 16px; flex-wrap: wrap;">
          <a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="btn btn-yt">
            🔴 Suscribirse en YouTube (@RaupulusMusic)
          </a>
          <a href="{YT_PERSONAL}" target="_blank" rel="noopener noreferrer" class="btn btn-outline">
            Canal de Tecnología & Código (@raupulus)
          </a>
          <a href="mailto:{PUBLIC_EMAIL}" class="btn btn-outline">
            Contacto: {PUBLIC_EMAIL}
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="assets/images/logo.png" alt="Raupulus Music">
          <p>
            Proyecto musical y cinematográfico oficial de <strong>Raúl Caro Pastorino (@raupulus)</strong>. Metal Industrial y universos de fantasía oscura generados con Inteligencia Artificial.
          </p>
          <div style="margin-top: 8px;">
            <a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="btn btn-yt btn-sm">
              YouTube @RaupulusMusic
            </a>
          </div>
        </div>

        <div class="footer-col">
          <h4>Navegación</h4>
          <ul class="footer-links">
            <li><a href="#inicio">Inicio</a></li>
            <li><a href="#canciones">Listado de Canciones</a></li>
            <li><a href="#universo">Universo R-Avatar</a></li>
            <li><a href="#proyecto">Sobre el Proyecto</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Contacto & Legal</h4>
          <ul class="footer-links">
            <li><a href="mailto:{PUBLIC_EMAIL}">Email: {PUBLIC_EMAIL}</a></li>
            <li><a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer">YouTube Oficial</a></li>
            <li><a href="{YT_PERSONAL}" target="_blank" rel="noopener noreferrer">Canal Personal / Tech</a></li>
            <li><span style="color: var(--text-dim);">Todos los derechos reservados © {datetime.now().year}</span></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          © {datetime.now().year} <strong>Raupulus Music</strong>. Música, letras y concepto creados por Raúl Caro Pastorino (@raupulus).
        </div>
        <div>
          Dominio oficial: <a href="{SITE_URL}" style="color: var(--accent-purple);">music.raupulus.dev</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="assets/js/main.js"></script>
</body>
</html>
"""
    with open(os.path.join(DIST_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(index_html)
    print(f"Generated {os.path.join(DIST_DIR, 'index.html')}")

def generate_song_pages(songs):
    for s in songs:
        title_esc = html.escape(s['title'])
        synopsis_esc = html.escape(s.get('synopsis', ''))
        lyrics_esc = html.escape(s.get('lyrics', ''))
        slug = s['slug']
        num_str = f"#{s['number']:02d}"

        canonical_url = f"{SITE_URL}/canciones/{slug}.html"
        cover_url = f"{SITE_URL}/assets/images/covers/{s['cover_file']}"
        yt_id = s.get('youtube_id', '')

        # Player Embed or Interactive Poster
        if yt_id:
            player_html = f"""
            <div class="video-player-container">
              <iframe src="https://www.youtube.com/embed/{yt_id}?autoplay=0&rel=0&modestbranding=1" 
                      title="{title_esc} — Raupulus Music" 
                      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                      allowfullscreen 
                      loading="lazy"></iframe>
            </div>
            """
            yt_watch_url = f"https://www.youtube.com/watch?v={yt_id}"
        else:
            player_html = f"""
            <div class="video-player-container">
              <div class="video-poster-placeholder">
                <img src="../assets/images/covers/{s['cover_file']}" alt="Portada {title_esc} — Raupulus Music" width="1280" height="720">
                <div class="spotlight-play-overlay">
                  <a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="play-circle" aria-label="Ver en YouTube">
                    <svg width="40" height="40" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
                  </a>
                  <span class="badge badge-yt">🔴 Estreno en @RaupulusMusic</span>
                </div>
              </div>
            </div>
            """
            yt_watch_url = YT_CHANNEL

        # Track Nav
        prev_html = ""
        if s.get('prev_slug'):
            prev_html = f"""
            <a href="{s['prev_slug']}.html" class="track-nav-card prev">
              <span class="nav-direction">← Pista Anterior</span>
              <span class="nav-song-name">{html.escape(s['prev_title'])}</span>
            </a>
            """
        else:
            prev_html = f"""
            <a href="../index.html#canciones" class="track-nav-card prev">
              <span class="nav-direction">← Álbum Completo</span>
              <span class="nav-song-name">Índice del CD 1</span>
            </a>
            """

        next_html = ""
        if s.get('next_slug'):
            next_html = f"""
            <a href="{s['next_slug']}.html" class="track-nav-card next">
              <span class="nav-direction">Siguiente Pista →</span>
              <span class="nav-song-name">{html.escape(s['next_title'])}</span>
            </a>
            """
        else:
            next_html = f"""
            <a href="../index.html#canciones" class="track-nav-card next">
              <span class="nav-direction">Fin del Disco →</span>
              <span class="nav-song-name">Volver al Inicio</span>
            </a>
            """

        # Schema LD
        schema_ld = {
            "@context": "https://schema.org",
            "@type": "MusicRecording",
            "name": s['title'],
            "url": canonical_url,
            "duration": f"PT{s['duration'].replace(':', 'M')}S",
            "position": s['number'],
            "inAlbum": {
                "@type": "MusicAlbum",
                "name": ALBUM_TITLE,
                "url": f"{SITE_URL}/"
            },
            "byArtist": {
                "@type": "MusicGroup",
                "name": "Raupulus Music",
                "url": YT_CHANNEL
            },
            "description": s.get('synopsis', '')
        }

        song_page_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_esc} — Raupulus Music | Vídeo Oficial y Letra</title>
  <meta name="description" content="Videoclip y letra oficial de '{title_esc}' por Raupulus Music. Pista {s['number']} del álbum 'Nunca venderé mi alma de Metal'.">
  <link rel="canonical" href="{canonical_url}">

  <!-- Open Graph -->
  <meta property="og:type" content="music.song">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:title" content="{title_esc} — Raupulus Music (Vídeo y Letra)">
  <meta property="og:description" content="{synopsis_esc}">
  <meta property="og:image" content="{cover_url}">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:url" content="{canonical_url}">
  <meta name="twitter:title" content="{title_esc} — Raupulus Music">
  <meta name="twitter:description" content="{synopsis_esc}">
  <meta name="twitter:image" content="{cover_url}">

  <link rel="icon" type="image/png" href="../assets/images/avatar-circular.png">
  <link rel="stylesheet" href="../assets/css/style.css">

  <script type="application/ld+json">
  {json.dumps(schema_ld, indent=2, ensure_ascii=False)}
  </script>
</head>
<body>

  <div class="bg-watermark"></div>

  <!-- Navbar -->
  <nav class="site-nav" aria-label="Navegación">
    <div class="container">
      <a href="../index.html" class="nav-brand">
        <img src="../assets/images/logo.png" alt="Logo Raupulus Music">
        <div class="nav-brand-text">
          <span class="nav-brand-title">RAUPULUS</span>
          <span class="nav-brand-sub">MUSIC</span>
        </div>
      </a>

      <ul class="nav-links">
        <li><a href="../index.html">Inicio</a></li>
        <li><a href="../index.html#canciones">Todas las Canciones</a></li>
        <li><a href="../index.html#universo">R-Avatar</a></li>
      </ul>

      <div class="nav-cta">
        <a href="{yt_watch_url}" target="_blank" rel="noopener noreferrer" class="btn btn-yt btn-sm">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          Ver en YouTube
        </a>
      </div>

      <button class="mobile-menu-btn" aria-label="Abrir menú">☰</button>
    </div>
  </nav>

  <main class="container">
    <!-- Header -->
    <header class="song-header">
      <nav class="breadcrumb" aria-label="Miga de pan">
        <a href="../index.html">Inicio</a>
        <span>/</span>
        <a href="../index.html#canciones">CD 1: Nunca venderé mi alma de Metal</a>
        <span>/</span>
        <span style="color: var(--text-bright);">{title_esc}</span>
      </nav>

      <h1 class="song-main-title">{title_esc}</h1>

      <div class="song-meta-bar">
        <span class="badge">{num_str} de 23</span>
        <span class="badge badge-cyan">Duración: {s['duration']}</span>
        <span class="badge">{s['clips_count']} Clips IA (10s)</span>
        <span class="badge">CD 1 — Metal Industrial</span>
      </div>
    </header>

    <!-- Reproductor Embebido de YouTube -->
    {player_html}

    <!-- Banner Visible CTA hacia YouTube -->
    <section class="video-cta-banner" aria-label="Acciones en YouTube">
      <div class="video-cta-info">
        <h3 class="video-cta-title">¿Te gusta este tema? Apoya el proyecto en YouTube</h3>
        <p class="video-cta-text">Dale like, comparte y déjanos tu parte favorita en la caja de comentarios.</p>
      </div>
      <div style="display: flex; gap: 12px; flex-wrap: wrap;">
        <a href="{yt_watch_url}" target="_blank" rel="noopener noreferrer" class="btn btn-yt">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/></svg>
          Ver en YouTube
        </a>
        <a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="btn btn-outline">
          🔔 Suscribirse al Canal
        </a>
      </div>
    </section>

    <!-- Detalles: Historia y Letra -->
    <div class="song-details-grid">
      <!-- Letra Oficial -->
      <article class="content-box">
        <div class="content-box-title">
          <span>📜 Letra Oficial</span>
          <button type="button" id="btn-copy-lyrics" class="btn btn-outline btn-sm">
            📋 Copiar Letra
          </button>
        </div>
        <div class="lyrics-content">{lyrics_esc}</div>

        <div style="margin-top: 36px; padding-top: 20px; border-top: 1px solid var(--border-subtle); font-size: 0.85rem; color: var(--text-dim);">
          <p>© {datetime.now().year} <strong>Raupulus Music</strong>. Letra y música originales registradas. Todos los derechos reservados.</p>
        </div>
      </article>

      <!-- Historia y Ficha Técnica -->
      <aside class="content-box">
        <div class="content-box-title">
          <span>🎬 Universo Cinematográfico</span>
        </div>

        <p class="synopsis-text">{synopsis_esc}</p>

        <h4 style="margin-bottom: 14px; font-size: 1.1rem; color: var(--text-bright);">Ficha de Producción</h4>
        <div class="specs-grid">
          <div class="spec-item">
            <span class="spec-label">Pista</span>
            <div class="spec-val">#{s['number']:02d} de 23</div>
          </div>
          <div class="spec-item">
            <span class="spec-label">Duración</span>
            <div class="spec-val">{s['duration']}</div>
          </div>
          <div class="spec-item">
            <span class="spec-label">Clips de Vídeo</span>
            <div class="spec-val">{s['clips_count']} clips (10s)</div>
          </div>
          <div class="spec-item">
            <span class="spec-label">Protagonista</span>
            <div class="spec-val">R-Avatar</div>
          </div>
          <div class="spec-item">
            <span class="spec-label">Género</span>
            <div class="spec-val">Metal Industrial</div>
          </div>
          <div class="spec-item">
            <span class="spec-label">Dirección</span>
            <div class="spec-val">Raupulus</div>
          </div>
        </div>

        <h4 style="margin: 24px 0 14px; font-size: 1.1rem; color: var(--text-bright);">Arte de Portada</h4>
        <div style="border-radius: var(--radius-md); overflow: hidden; border: 1px solid var(--border-subtle);">
          <img src="../assets/images/covers/{s['cover_file']}" alt="Portada {title_esc}" style="width: 100%; height: auto; display: block;" loading="lazy">
        </div>

        <div style="margin-top: 24px;">
          <a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer" class="btn btn-yt" style="width: 100%;">
            Ver Canal de YouTube
          </a>
        </div>
      </aside>
    </div>

    <!-- Navegación entre Pistas -->
    <nav class="track-nav" aria-label="Navegación entre canciones">
      {prev_html}
      {next_html}
    </nav>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <img src="../assets/images/logo.png" alt="Raupulus Music">
          <p>
            Proyecto musical y cinematográfico oficial de <strong>Raúl Caro Pastorino (@raupulus)</strong>. Metal Industrial y universos de fantasía oscura generados con Inteligencia Artificial.
          </p>
        </div>

        <div class="footer-col">
          <h4>Navegación</h4>
          <ul class="footer-links">
            <li><a href="../index.html">Página Principal</a></li>
            <li><a href="../index.html#canciones">Índice del CD 1 (23 Canciones)</a></li>
            <li><a href="../index.html#universo">Universo R-Avatar</a></li>
          </ul>
        </div>

        <div class="footer-col">
          <h4>Contacto & Legal</h4>
          <ul class="footer-links">
            <li><a href="mailto:{PUBLIC_EMAIL}">Email: {PUBLIC_EMAIL}</a></li>
            <li><a href="{YT_CHANNEL}" target="_blank" rel="noopener noreferrer">YouTube Oficial</a></li>
            <li><a href="{YT_PERSONAL}" target="_blank" rel="noopener noreferrer">Canal Personal / Tech</a></li>
          </ul>
        </div>
      </div>

      <div class="footer-bottom">
        <div>
          © {datetime.now().year} <strong>Raupulus Music</strong>. Letra y música compuestas por Raúl Caro Pastorino (@raupulus).
        </div>
        <div>
          Dominio oficial: <a href="{SITE_URL}" style="color: var(--accent-purple);">music.raupulus.dev</a>
        </div>
      </div>
    </div>
  </footer>

  <script src="../assets/js/main.js"></script>
</body>
</html>
"""
        page_path = os.path.join(DIST_DIR, "canciones", f"{slug}.html")
        with open(page_path, "w", encoding="utf-8") as f:
            f.write(song_page_html)

    print(f"Generated {len(songs)} song pages in {os.path.join(DIST_DIR, 'canciones')}")

def generate_sitemap(songs):
    today = datetime.now().strftime("%Y-%m-%d")
    urls = [
        f"""  <url>
    <loc>{SITE_URL}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>"""
    ]

    for s in songs:
        url_xml = f"""  <url>
    <loc>{SITE_URL}/canciones/{s['slug']}.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""
        urls.append(url_xml)

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(urls)}
</urlset>
"""
    with open(os.path.join(DIST_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap_xml)
    print(f"Generated {os.path.join(DIST_DIR, 'sitemap.xml')}")

def generate_robots():
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
    with open(os.path.join(DIST_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots_txt)
    print(f"Generated {os.path.join(DIST_DIR, 'robots.txt')}")

def main():
    print("=== Building Raupulus Music Website ===")
    ensure_dirs()
    copy_assets()
    songs = load_songs()
    generate_index(songs)
    generate_song_pages(songs)
    generate_sitemap(songs)
    generate_robots()
    print("=== Build Completed Successfully! ===")

if __name__ == "__main__":
    main()
