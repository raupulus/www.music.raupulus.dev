# REGLAS Y ESTÁNDARES OFICIALES DEL PROYECTO WEB: RAUPULUS MUSIC (music.raupulus.dev)

> [!IMPORTANT]
> Estas reglas son de cumplimiento estricto y permanente en todas las sesiones para el desarrollo, diseño, generación de páginas, SEO, despliegue y mantenimiento de la web oficial de Raupulus Music.

---

## 1. PRIVACIDAD Y SEGURIDAD ESTRICTA (PERMANENTE)

* **Correo personal estrictamente prohibido:** NUNCA utilizar bajo ningún concepto ningún otro correo privado en código, plantillas, metadatos, commits o documentación.
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

## 5. ESTRATEGIA DE SEO Y CONVERSIÓN A YOUTUBE

* **Objetivo de Tráfico:** Atraer tráfico orgánico desde motores de búsqueda (búsquedas por títulos de canciones, letras, metal industrial, cyber metal, música IA) y canalizarlo directamente a YouTube para reproducciones y suscripciones.
* **Metadatos por Página:**
  * OpenGraph (`og:title`, `og:description`, `og:image`, `og:url`, `og:type`).
  * Twitter Card (`summary_large_image`).
  * Etiquetas canónicas apuntando a `https://music.raupulus.dev/...`.
  * Datos estructurados Schema.org (`MusicGroup`, `MusicAlbum`, `MusicRecording`, `VideoObject`).
* **Llamadas a la Acción (CTA) de YouTube:**
  * Botones grandes y contrastados: "Ver en YouTube", "Suscribirse al Canal", "Comentar en YouTube".
  * Reproductor embebido accesible y responsive con lazy loading.

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



