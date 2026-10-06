# ⚡ RAUPULUS MUSIC — WEB OFICIAL (music.raupulus.dev)

> Sitio web oficial y catálogo cinematográfico para el proyecto musical y audiovisual **Raupulus Music** (`@RaupulusMusic`), centrado en el álbum conceptual **CD 1: Nunca venderé mi alma de Metal** y el universo visual de **R-Avatar**.

---

## 🌐 Dominios y Canales Oficiales
* **Web Oficial:** [https://music.raupulus.dev](https://music.raupulus.dev)
* **Canal Oficial de YouTube:** [https://www.youtube.com/@RaupulusMusic](https://www.youtube.com/@RaupulusMusic)
* **Canal Personal / Tech:** [https://www.youtube.com/@raupulus](https://www.youtube.com/@raupulus)
* **Contacto:** `public@raupulus.dev`

---

## 🎯 Propósito del Sitio y Estrategia SEO
1. **Captación de Tráfico Orgánico:** Posicionamiento en Google mediante búsquedas de títulos, letras, metal industrial, cyber hardcore y música/videoclips con inteligencia artificial.
2. **Embudo Directo a YouTube:** Botones prominentes y contrastados para ver los videoclips completos, escuchar la música, suscribirse al canal y dejar comentarios.
3. **Página Dedicada por Canción:** Cada una de las 23 pistas dispone de su propia página estática optimizada (`/canciones/<slug>.html`) con:
   * Reproductor de YouTube embebido y responsive.
   * Letra oficial limpia con botón interactivo de copiado.
   * Sinopsis y trasfondo narrativo de la escena cinematográfica.
   * Ficha técnica de producción (duración exacta, número de clips de 10s, protagonista).
   * Arte de portada 16:9 en alta resolución.
   * Navegación secuencial entre pistas (anterior / siguiente).
   * Aviso legal de copyright y créditos completos.
4. **Diseño Visual Temático:** Estética oscura inspirada en el R-Avatar (ébano calcinado `#06050a`, bioluminiscencia púrpura `#9b4dff`, siluetas semitransparentes del personaje, acentos cian y neón).

---

## 📁 Arquitectura del Proyecto

```text
web/
├── AGENTS.md                 # Reglas obligatorias, privacidad y estándares de diseño
├── README.md                 # Este manual técnico
├── build.py                  # Generador estático en Python (compila dist/ en 1 segundo)
├── data/
│   └── songs.json            # Base de datos JSON con las 23 canciones, letras y YouTube IDs
├── src/
│   ├── css/
│   │   └── style.css         # Hoja de estilos moderna, responsive y con diseño bioluminiscente
│   └── js/
│       ├── main.js           # Buscador en tiempo real, menú móvil, spotlight y copiar letras
│       └── alpine.min.js     # Alpine.js vendored localmente (sin CDNs externos)
└── dist/                     # 🚀 DIRECTORIO PUBLICABLE FINAL (Deploy-ready)
    ├── index.html            # Portada principal, catálogo de 23 canciones y buscador
    ├── canciones/            # 23 páginas individuales para cada canción
    │   ├── 01-corona-de-hierro.html
    │   ├── 02-desde-el-cielo-mando.html
    │   └── ...
    ├── assets/
    │   ├── css/style.css
    │   ├── js/main.js
    │   └── images/
    │       ├── logo.png
    │       ├── r-avatar-face.png
    │       ├── avatar-circular.png
    │       ├── banner.jpg
    │       ├── r-avatar-portrait.jpg
    │       ├── r-avatar-character-sheet.jpg
    │       └── covers/       # 23 portadas cinematográficas oficiales 16:9
    ├── sitemap.xml           # Mapa del sitio para indexación completa en Google
    └── robots.txt            # Reglas para rastreadores de motores de búsqueda
```

---

## 🚀 Cómo Actualizar Vídeos de YouTube y Regenerar la Web

Cuando subas un nuevo videoclip a YouTube y tengas su ID (por ejemplo `dQw4w9WgXcQ` en `youtube.com/watch?v=dQw4w9WgXcQ`):

1. Abre `data/songs.json`.
2. Busca la canción correspondiente y rellena el campo `"youtube_id"`:
   ```json
   {
     "number": 1,
     "title": "Corona de Hierro",
     "youtube_id": "dQw4w9WgXcQ"
   }
   ```
3. Ejecuta el generador desde la terminal:
   ```bash
   python3 build.py
   ```
4. ¡Listo! El script regenerará automáticamente la portada, las páginas de canciones con el reproductor oficial de YouTube embebido y el `sitemap.xml` en milisegundos.

---

## 🛠️ Opciones de Despliegue (Deploy)

El directorio `dist/` es 100% estático e independiente. Se puede desplegar directamente en:
* **Cloudflare Pages:** Conectar el repositorio o subir la carpeta `dist`.
* **Netlify / Vercel:** Configurar `dist` como el *Publish Directory*.
* **GitHub Pages:** Publicar la rama o carpeta `dist`.
* **Nginx / Apache:** Apuntar el `DocumentRoot` de `music.raupulus.dev` a `/ruta/a/web/dist`.

---

## 🔒 Privacidad y Autoría
* Contacto oficial público: `public@raupulus.dev`.
* Creado por: **Raúl Caro Pastorino (@raupulus)**.
* Todos los derechos reservados © 2026 Raupulus Music.
