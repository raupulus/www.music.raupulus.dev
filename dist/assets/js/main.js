/**
 * RAUPULUS MUSIC — main.js
 * Funcionalidad interactiva: Buscador en tiempo real, reproductor spotlight,
 * menú móvil, copia de letras y notificaciones toast.
 */

document.addEventListener('DOMContentLoaded', () => {
  initSearch();
  initMobileMenu();
  initCopyLyrics();
  initPreviewModal();
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
 * Modal de Vista Previa Inmediata para las 23 canciones (sin scroll)
 */
function initPreviewModal() {
  const modal = document.getElementById('preview-modal');
  if (!modal) return;

  const closeBtn = modal.querySelector('.preview-modal-close');
  const footerCloseBtn = modal.querySelector('#preview-modal-close-btn');
  const titleEl = modal.querySelector('#preview-modal-title');
  const numEl = modal.querySelector('#preview-modal-num');
  const durEl = modal.querySelector('#preview-modal-dur');
  const synEl = modal.querySelector('#preview-modal-synopsis');
  const songLinkEl = modal.querySelector('#preview-modal-song-link');
  const ytLinkEl = modal.querySelector('#preview-modal-yt-link');
  const videoWrap = modal.querySelector('#preview-modal-video-wrap');

  function closeModal() {
    modal.classList.remove('open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
    // Limpiar reproductor para detener el audio/vídeo de inmediato
    if (videoWrap) {
      videoWrap.innerHTML = '';
    }
  }

  function openModal(data) {
    const { num, title, duration, synopsis, cover, slug, ytid } = data;

    if (numEl) numEl.textContent = `#${String(num).padStart(2, '0')} de 23`;
    if (durEl) durEl.textContent = duration;
    if (titleEl) titleEl.textContent = title;
    if (synEl) synEl.textContent = synopsis;
    if (songLinkEl) songLinkEl.href = `canciones/${slug}.html`;

    if (ytLinkEl) {
      if (ytid) {
        ytLinkEl.href = `https://www.youtube.com/watch?v=${ytid}`;
        ytLinkEl.style.display = 'inline-flex';
      } else {
        ytLinkEl.href = `https://www.youtube.com/@RaupulusMusic`;
        ytLinkEl.style.display = 'inline-flex';
      }
    }

    if (videoWrap) {
      if (ytid) {
        let isLocalFile = window.location.protocol === 'file:';
        let noticeHtml = '';
        if (isLocalFile) {
          noticeHtml = `
            <div class="file-protocol-warning" style="margin: 12px; font-size: 0.85rem;">
              <div class="warning-header" style="font-size: 0.95rem;">⚠️ Previsualización en archivo local (file://)</div>
              <p style="margin-bottom: 6px;">YouTube bloquea los reproductores embebidos locales sin servidor (Error 153). En <strong>music.raupulus.dev</strong> o corriendo <code>python3 serve.py</code> se reproduce automáticamente.</p>
              <a href="https://www.youtube.com/watch?v=${ytid}" target="_blank" class="btn btn-sm btn-yt">▶ Ver directamente en YouTube</a>
            </div>
          `;
        }
        videoWrap.innerHTML = `
          ${noticeHtml}
          <iframe src="https://www.youtube-nocookie.com/embed/${ytid}?autoplay=1&rel=0&modestbranding=1" 
                  title="${title} — Raupulus Music" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" 
                  referrerpolicy="strict-origin-when-cross-origin"
                  allowfullscreen></iframe>
        `;
      } else {
        videoWrap.innerHTML = `
          <div class="spotlight-poster">
            <img src="${cover}" alt="Portada ${title}" style="width: 100%; height: 100%; object-fit: cover;">
            <div class="spotlight-play-overlay">
              <a href="https://www.youtube.com/@RaupulusMusic" target="_blank" rel="noopener noreferrer" class="play-circle" aria-label="Ver canal">
                <svg width="34" height="34" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg>
              </a>
              <span class="badge badge-yt">🔴 Estreno Próximamente en @RaupulusMusic</span>
            </div>
          </div>
        `;
      }
    }

    modal.classList.add('open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
  }

  // Asignar a todos los botones y tarjetas con data-preview-trigger
  document.querySelectorAll('[data-preview-trigger]').forEach((el) => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      const data = {
        num: el.getAttribute('data-num') || '1',
        title: el.getAttribute('data-title') || '',
        duration: el.getAttribute('data-duration') || '',
        synopsis: el.getAttribute('data-synopsis') || '',
        cover: el.getAttribute('data-cover') || '',
        slug: el.getAttribute('data-slug') || '',
        ytid: el.getAttribute('data-ytid') || ''
      };
      openModal(data);
    });
  });

  // Eventos de cierre
  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (footerCloseBtn) footerCloseBtn.addEventListener('click', closeModal);

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal.classList.contains('open')) {
      closeModal();
    }
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
