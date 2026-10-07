# REGLAS Y ESTÁNDARES OFICIALES DEL PROYECTO WEB: RAUPULUS MUSIC (music.raupulus.dev)

> [!IMPORTANT]
> Estas reglas son de cumplimiento estricto y permanente en todas las sesiones para el desarrollo, diseño, generación de páginas, SEO, despliegue y mantenimiento de la web oficial de Raupulus Music.

---

## 1. PRIVACIDAD Y SEGURIDAD ESTRICTA (PERMANENTE)

* **Correo personal estrictamente prohibido:** NUNCA utilizar bajo ningún concepto ningún correo personal o privado del creador en código, plantillas, metadatos, commits o documentación.
* **Único correo público permitido:** El ÚNICO correo que puede utilizarse en proyectos públicos, metadatos, avisos legales, contacto o menciones es: `public@raupulus.dev`.
* **Protección de datos:** NUNCA publicar ni compartir datos personales privados (nombres reales completos sin autorización, números de teléfono, IPs privadas, credenciales o tokens).

---

## 2. IDENTIDAD DE MARCA Y CANALES OFICIALES

* **Dominio Oficial:** `https://music.raupulus.dev`
* **Canal Oficial de YouTube del Proyecto:** `https://www.youtube.com/@RaupulusMusic`
* **Canal Principal Tech / Programación:** `https://www.youtube.com/@raupulus`
* **Contacto Oficial:** `public@raupulus.dev`
* **Álbum Principal:** *CD 1 - Nunca venderé mi alma de Metal* (23 canciones, Metal Industrial / Cyber Hardcore).
* **Protagonista del Universo Visual:** `R-Avatar` (Entidad biomecánica y bio-orgánica de ébano, venas bioluminiscentes violetas, 8 ojos morados y cerebro expuesto).

---

## 3. ESTÁNDAR DE DISEÑO VISUAL Y ESTÉTICA

* **Paleta Cromática Obligatoria:**
  * **Fondo Principal (Ébano oscuro / Madera calcinada):** `#07060a` y gradientes hacia `#0e0b16` y `#151022`.
  * **Superficies y Tarjetas:** `#13101c` con bordes sutiles `#2e2244` y efectos glow `#9b4dff33`.
  * **Acento Primario (Bioluminiscencia R-Avatar):** Violeta brillante `#9b4dff` y Neón Púrpura `#b829ea`.
  * **Acento Secundario (Energía / Contraste):** Magenta eléctrico `#e024c3` y Cyan cibernético `#00f0ff`.
  * **Tipografía:** Texto blanco marfil `#f3f1f7` y gris lavanda `#a9a4b8` para lectura cómoda y alto contraste.
* **Integración del Personaje en el Diseño:**
  * Siluetas y poses de `R-Avatar` semitransparentes en fondos de sección (`opacity: 0.04 - 0.08`, `mix-blend-mode: screen`).
  * Iconografía y badges inspirados en runas mecánicas y cyber-metal.
  * Portadas cinematográficas oficiales 16:9 destacadas en cada canción.
  * Efectos de hover sutiles con sombras bioluminiscentes violetas.

---

## 4. ARQUITECTURA TÉCNICA Y ESTRUCTURA DE ARCHIVOS

* **Tecnologías:** HTML5 semántico + CSS3 moderno (Custom Properties / Flexbox / Grid) + JavaScript ligero (vanilla / Alpine.js).
* **Sin dependencias pesadas:** Cero frameworks pesados que ralenticen la carga. Velocidad máxima y Core Web Vitals excelentes.
* **Directorio de Distribución (`dist/`):**
  * `dist/` contiene el sitio estático 100% listo para producción y despliegue (Cloudflare Pages, Vercel, Netlify, Apache, Nginx o GitHub Pages).
  * `dist/index.html`: Portada principal, catálogo completo de canciones, listas de reproducción, buscador y universo R-Avatar.
  * `dist/canciones/<slug>.html`: Página individual dedicada para cada una de las 23 canciones, con reproductor, letra completa, historia del clip, créditos, copyright y botones visibles hacia YouTube.
  * `dist/assets/`: CSS (`style.css`), JS (`main.js`, `alpine.min.js`), e imágenes (`images/`).
  * `dist/sitemap.xml` y `dist/robots.txt`: Generados automáticamente para indexación en Google.

---

## 5. ESTRATEGIA DE SEO Y METADATOS OBLIGATORIOS PARA REDES SOCIALES

> [!IMPORTANT]
> **REGLA ESTRICTA Y PERMANENTE DE SEO Y SOCIAL SHARING:**
> Todas las páginas actuales y cualquier página nueva que se cree o edite deben mantener obligatoriamente la suite completa de metadatos SEO y tarjetas de previsualización para redes sociales (WhatsApp, Facebook, Twitter/X, Telegram, Discord, LinkedIn).
>
> 1. **Página Principal (`dist/index.html`):**
>    - **Imagen Oficial Obligatoria:** Debe utilizar OBLIGATORIAMENTE el **logotipo oficial** (`https://music.raupulus.dev/assets/images/logo.png`).
>    - Metadatos Open Graph obligatorios:
>      - `og:image`: `https://music.raupulus.dev/assets/images/logo.png`
>      - `og:image:secure_url`: `https://music.raupulus.dev/assets/images/logo.png`
>      - `og:image:type`: `image/png`
>      - `og:image:width`: `1024`
>      - `og:image:height`: `1024`
>      - `og:image:alt`: `Logotipo Oficial de Raupulus Music`
>      - `og:site_name`: `Raupulus Music`
>      - `og:locale`: `es_ES`
>      - `og:type`: `website`
>    - Metadatos Twitter Card:
>      - `twitter:card`: `summary_large_image`
>      - `twitter:site`: `@RaupulusMusic`
>      - `twitter:creator`: `@raupulus`
>      - `twitter:image`: `https://music.raupulus.dev/assets/images/logo.png`
>      - `twitter:image:alt`: `Logotipo Oficial de Raupulus Music`
>
> 2. **Páginas de Canciones (`dist/canciones/*.html`):**
>    - **Imagen Oficial Obligatoria:** Debe utilizar OBLIGATORIAMENTE la **portada cinematográfica oficial 16:9** de la canción en el disco (`https://music.raupulus.dev/assets/images/covers/cover-XX.jpg`).
>    - Metadatos Open Graph obligatorios:
>      - `og:image`: `https://music.raupulus.dev/assets/images/covers/{cover_file}`
>      - `og:image:secure_url`: `https://music.raupulus.dev/assets/images/covers/{cover_file}`
>      - `og:image:type`: `image/jpeg`
>      - `og:image:width`: `1376`
>      - `og:image:height`: `768`
>      - `og:image:alt`: `Portada oficial de {Título} — Álbum Nunca venderé mi alma de Metal`
>      - `og:site_name`: `Raupulus Music`
>      - `og:locale`: `es_ES`
>      - `og:type`: `music.song`
>      - Metadatos de música: `music:duration`, `music:album`, `music:musician`, `music:song:disc`, `music:song:track`.
>    - Metadatos Twitter Card:
>      - `twitter:card`: `summary_large_image`
>      - `twitter:site`: `@RaupulusMusic`
>      - `twitter:creator`: `@raupulus`
>      - `twitter:image`: `https://music.raupulus.dev/assets/images/covers/{cover_file}`
>      - `twitter:image:alt`: `Portada oficial de {Título} — Álbum Nunca venderé mi alma de Metal`
>
> 3. **Metadatos Globales Obligatorios en TODAS las Páginas:**
>    - `robots`: `index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1`
>    - `keywords`: Palabras clave relevantes optimizadas para SEO.
>    - `author`: `Raúl Caro Pastorino (@raupulus)`
>    - `publisher`: `Raupulus Music`
>    - `theme-color`: `#9b4dff`
>    - `msapplication-TileColor`: `#07060a`
>    - `link rel="canonical"`: URL canónica absoluta.
>    - Datos estructurados Schema.org (`MusicAlbum` / `MusicRecording`) con la propiedad `"image"` siempre sincronizada.
>
> 4. **Mantenimiento y Automatización Obligatoria:** Tras editar cualquier metadato, letra, sinopsis o añadir nuevas canciones/páginas, es imperativo ejecutar `python3 build.py` para regenerar todos los archivos estáticos en `dist/`.

---

## 6. SCRIPT DE GENERACIÓN AUTOMÁTICA (`build.py`)

* La web cuenta con un script en Python (`build.py`) que lee los metadatos de las canciones desde `data/songs.json` (extraídos de los storyboards, letras y portadas de `videoclips/CD 1 - Nunca venderé mi alma de Metal`).
* Al actualizar un ID de YouTube o añadir un tema, basta con ejecutar `python3 build.py` para regenerar todo el sitio en `dist/` en cuestión de segundos.

---

## 7. PROTOCOLO TRAS TRANSCODIFICACIÓN DE VÍDEOS (ACTUALIZACIÓN WEB)

* **Solicitud Obligatoria de ID de YouTube:** Cada vez que se transcodifique, monte o finalice un vídeo de una canción (`*_wm.mp4`), el agente debe **pedir obligatoriamente al usuario el ID del vídeo de YouTube** (o enlace del vídeo subido al canal `@RaupulusMusic`).
* **Actualización Automática de la Web:** Con el ID proporcionado:
  1. Insertar el ID en el campo `"youtube_id"` correspondiente en `data/songs.json`.
  2. Ejecutar `python3 build.py` para regenerar `dist/index.html`, la página de la canción con el reproductor embebido y `dist/sitemap.xml`.
  3. Confirmar la actualización y comitear en Git.

---

## 8. NOMENCLATURA OFICIAL: CÓDIGO INTERNO VS. CARA AL PÚBLICO

> [!IMPORTANT]
> Los nombres técnicos con sufijo `-Avatar` son códigos internos para la consistencia en prompts de IA y organización técnica. De cara al público, la web oficial, descripciones de YouTube, redes sociales y metadatos se debe utilizar rigurosamente la nomenclatura artística:
>
> 1. **`R-Avatar` (código interno) ➔ `Raupulus` (nombre público):**  
>    El protagonista indiscutible del proyecto. Nunca llamarlo "R-Avatar" ante los usuarios o en la web pública; para el público es simplemente **Raupulus**.
>
> 2. **`Wolf-Avatar` (código interno) ➔ `Su Perro` / `Su Mascota` / `Su Mejor Amigo` (nombre público):**  
>    El lobo titánico de ojos esmeralda. Presentarlo en la narrativa como su perro, su mascota o su mejor amigo.
>
> 3. **`M-Love-Avatar` (código interno) ➔ `Amada` / `Su Amada` (nombre público):**  
>    La elfa-ogra híbrida musa trágica del universo. Presentarla ante el público como su amada.

---

## 9. ESTÁNDAR NARRATIVO Y VISUAL EN FICHAS DE CANCIÓN (UNIVERSO CINEMATOGRÁFICO)

> [!IMPORTANT]
> En la web oficial (`canciones/*.html`) y en la documentación de cada tema, el bloque **🎬 Universo Cinematográfico** debe seguir rigurosamente este estándar narrativo extenso, concreto y oxigenado:
>
> 1. **Prohibición de textos abstractos o genéricos:** NUNCA usar sinopsis abstractas ni frases vacías. Debe describirse el entorno tangible (ciudadelas de hierro, bosques de coníferas, acantilados volcánicos, etc.), las acciones físicas y el conflicto visual del clip.
> 2. **Estructura vertical obligatoria en el lateral (`<aside>` de la ficha):**
>    - **1) Resumen Cinematográfico:** Sinopsis tangible y directa del argumento y atmósfera del tema.
>    - **2) Ficha de Producción:** Metadatos técnicos (Pista, Duración, Número de clips de 10s, Protagonista, Género, Dirección).
>    - **3) Arte de Portada:** Imagen oficial en formato 16:9 de la portada.
>    - **4) Botones de Conversión a YouTube:** "Ver en YouTube" y "🔔 Suscribirse al Canal" (con `?sub_confirmation=1`).
>    - **5) Historia Cinematográfica Completa (Crónica del Storyboard):** Situada obligatoriamente **al final, debajo de los botones de suscripción**, narrando de forma extensa y detallada el recorrido visual completo basado en el `01_guion_storyboard.md` de cada videoclip, estructurado en párrafos amplios y bien oxigenados (con interlineado generoso y espaciado claro).

---

## 10. ESTÁNDARES OBLIGATORIOS DE ACCESIBILIDAD (A11Y), W3C Y RESPONSIVE EN LA WEB

> [!IMPORTANT]
> Para garantizar una experiencia de usuario perfecta y una auditoría Lighthouse 100/100 en Accesibilidad y SEO, toda página en `dist/` debe respetar estrictamente:
>
> 1. **Contraste de Color WCAG AA (Mínimo 4.5:1 en texto normal, 7:1 en badges/pequeño):**
>    - Fondo oscuro `#06050a` / `#110e1c`: Texto principal `#f5f3f9`, atenuado (`--text-dim`) `#9c95b3` (ratio > 6:1).
>    - Badges e indicadores: Morado `#d8b4fe`, cian `#38f8ff`, rojo `#ffa0a0`. Prohibido usar morados oscuros `#9b4dff` directamente como color de texto sobre fondos oscuros.
>
> 2. **Navegación Accesible por Teclado y Foco Visible:**
>    - Enlace de salto al contenido inicial: `<a href="#main-content" class="skip-link">Saltar al contenido principal</a>`.
>    - Landmark semántico principal: `<main id="main-content">` que engloba el contenido esencial.
>    - Estilo global de `:focus-visible` con contorno nítido cian/violeta (`outline: 2px solid var(--accent-cyan); outline-offset: 3px;`).
>    - Los modales deben cerrarse con la tecla `Escape` y restablecer el scroll (`document.body.style.overflow = ''`).
>
> 3. **Jerarquía Estricta de Encabezados (W3C Sequentially Descending Order):**
>    - Prohibido saltar niveles de encabezado (ej: de `H1` a `H3` o de `H2` a `H4`).
>    - En Portada: `H1` (Título del álbum) ➔ `H2` (Secciones) ➔ `H3` (Tarjetas, personajes del lore, títulos de columnas del footer).
>    - En Fichas de Canción: `H1` (Título de canción) ➔ `H2` (CTA banner, Letra oficial, Universo cinematográfico) ➔ `H3` (Ficha de producción, Arte de portada, Crónica narrativa del storyboard, Columnas del footer).
>
> 4. **Textos Alternativos (`alt`) y Descripciones para Lectores de Pantalla:**
>    - Todas las imágenes `<img>` deben incluir un atributo `alt` exhaustivo y descriptivo. Prohibido dejar `alt` vacío o genérico.
>    - Bustos de lore y trípticos deben describir elementos anatómicos (cuernos, ojos violetas, cerebro expuesto, vestimenta/poses).
>    - Elementos puramente decorativos o de fondo deben llevar `aria-hidden="true"`.
>    - Los campos de entrada (como `#song-search`) deben contar con `<label for="..." class="visually-hidden">`.
>
> 5. **Dimensiones Explícitas y Prevención de CLS (Cumulative Layout Shift):**
>    - Toda etiqueta `<img>` debe contar con atributos `width` y `height` acordes a su proporción intrínseca para evitar saltos de maquetación durante la carga.
>
> 6. **Diseño Responsive y Touch Targets (Móviles):**
>    - Controles interactivos, botones y accesos con un área táctil mínima de 44x44px.
>    - Inputs de texto con `font-size: 16px` en vista móvil para evitar zoom involuntario en iOS Safari.
>    - En pantallas pequeñas (`<= 480px`), botones y selectores apilados en ancho 100% con espaciado cómodo.




