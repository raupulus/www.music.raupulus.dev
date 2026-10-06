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
