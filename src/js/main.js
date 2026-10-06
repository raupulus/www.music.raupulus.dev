/**
 * RAUPULUS MUSIC — main.js
 * Funcionalidad interactiva: Buscador en tiempo real, reproductor spotlight,
 * menú móvil, copia de letras y notificaciones toast.
 */

document.addEventListener('DOMContentLoaded', () => {
  initSearch();
  initMobileMenu();
  initCopyLyrics();
  initSpotlight();
  initFileProtocolNotice();
});

/**
 * Buscador en tiempo real de canciones
 */
function initSearch() {
  const searchInput = document.getElementById('song-search');
  const countDisplay = document.getElementById('search-count');
  const cards = document.querySelectorAll('.song-card');
  const noResults = document.getElementById('no-results');

  if (!searchInput || !cards.length) return;

  const total = cards.length;

  searchInput.addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase().trim();
    let visibleCount = 0;

    cards.forEach((card) => {
      const title = card.getAttribute('data-title') || '';
      const text = card.textContent.toLowerCase();

      if (!term || title.includes(term) || text.includes(term)) {
        card.style.display = 'flex';
        visibleCount++;
      } else {
        card.style.display = 'none';
      }
    });

    if (countDisplay) {
      countDisplay.textContent = `Mostrando ${visibleCount} de ${total} canciones`;
    }

    if (noResults) {
      noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }
  });
}

/**
 * Menú Móvil
 */
function initMobileMenu() {
  const btn = document.querySelector('.mobile-menu-btn');
  const links = document.querySelector('.nav-links');

  if (!btn || !links) return;

  btn.addEventListener('click', () => {
    const isOpen = links.classList.toggle('mobile-open');
    btn.setAttribute('aria-expanded', isOpen);
    btn.innerHTML = isOpen ? '✕' : '☰';
  });

  // Cerrar al pulsar un enlace
  links.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      links.classList.remove('mobile-open');
      btn.innerHTML = '☰';
    });
  });
}

/**
 * Copiar Letra con Feedback
 */
function initCopyLyrics() {
  const copyBtn = document.getElementById('btn-copy-lyrics');
  const lyricsElem = document.querySelector('.lyrics-content');

  if (!copyBtn || !lyricsElem) return;

  copyBtn.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(lyricsElem.innerText);
      showToast('¡Letra copiada al portapapeles!');
    } catch (err) {
      showToast('Error al copiar la letra');
    }
  });
}

/**
 * Notificación Toast
 */
function showToast(message) {
  let toast = document.getElementById('site-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'site-toast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }

  toast.textContent = message;
  toast.style.display = 'block';

  setTimeout(() => {
    toast.style.display = 'none';
  }, 2800);
}

/**
 * Reproductor Spotlight interactivo
 */
function initSpotlight() {
  const triggerBtns = document.querySelectorAll('[data-spotlight-switch]');
  const spotlightTitle = document.getElementById('spotlight-title');
  const spotlightNum = document.getElementById('spotlight-num');
  const spotlightDur = document.getElementById('spotlight-dur');
  const spotlightSyn = document.getElementById('spotlight-synopsis');
  const spotlightImg = document.getElementById('spotlight-img');
  const spotlightLink = document.getElementById('spotlight-link');
  const spotlightYt = document.getElementById('spotlight-yt');

  if (!triggerBtns.length || !spotlightTitle) return;

  triggerBtns.forEach((btn) => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const num = btn.getAttribute('data-num');
      const title = btn.getAttribute('data-title');
      const dur = btn.getAttribute('data-duration');
      const syn = btn.getAttribute('data-synopsis');
      const cover = btn.getAttribute('data-cover');
      const slug = btn.getAttribute('data-slug');
      const ytId = btn.getAttribute('data-ytid');

      if (spotlightTitle) spotlightTitle.textContent = title;
      if (spotlightNum) spotlightNum.textContent = `#${num.padStart(2, '0')}`;
      if (spotlightDur) spotlightDur.textContent = dur;
      if (spotlightSyn) spotlightSyn.textContent = syn;
      if (spotlightImg) spotlightImg.src = cover;
      if (spotlightLink) spotlightLink.href = `canciones/${slug}.html`;

      if (spotlightYt) {
        if (ytId) {
          spotlightYt.href = `https://www.youtube.com/watch?v=${ytId}`;
        } else {
          spotlightYt.href = `https://www.youtube.com/@RaupulusMusic`;
        }
      }

      // Smooth scroll to player
      const card = document.querySelector('.spotlight-card');
      if (card) {
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      showToast(`Pista #${num} seleccionada: ${title}`);
    });
  });
}

/**
 * Detectar protocolo file:// y mostrar aviso amigable si los embeds de YouTube se bloquean
 */
function initFileProtocolNotice() {
  if (window.location.protocol !== 'file:') return;

  const playerContainers = document.querySelectorAll('.video-player-container');
  playerContainers.forEach((container) => {
    if (container.querySelector('.file-protocol-warning') || container.parentElement.querySelector('.file-protocol-warning')) return;

    const notice = document.createElement('div');
    notice.className = 'file-protocol-warning';
    notice.innerHTML = `
      <div class="warning-header">
        <span>⚠️</span>
        <strong>Aviso de Previsualización Local (protocolo file://)</strong>
      </div>
      <p>
        Google y YouTube bloquean la inicialización de reproductores incrustados desde archivos en disco (<strong>Error 153</strong>) por seguridad, al no enviar cabeceras de origen web.
      </p>
      <div class="warning-footer">
        <div>🚀 <strong>Para ver el vídeo embebido en local:</strong> ejecuta en tu terminal <code>python3 serve.py</code> y abre <a href="http://localhost:8080" target="_blank" style="color: var(--accent-cyan); text-decoration: underline;">http://localhost:8080</a>.</div>
        <div>🌐 En el servidor de producción (<strong>music.raupulus.dev</strong>) se reproduce directamente sin restricciones.</div>
      </div>
    `;

    container.parentElement.insertBefore(notice, container);
  });
}
