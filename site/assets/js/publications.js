document.addEventListener('DOMContentLoaded', () => {
  const search = document.getElementById('pub-search');
  const buttons = Array.from(document.querySelectorAll('.pub-filter-button'));
  const items = Array.from(document.querySelectorAll('.pub-item'));
  if (!items.length) return;

  let activeFilter = 'all';

  const apply = () => {
    const query = (search?.value || '').trim().toLowerCase();
    items.forEach((item) => {
      const haystack = item.textContent.toLowerCase();
      const keywords = (item.dataset.keywords || '').toLowerCase().split(/\s+/).filter(Boolean);
      const filterOk = activeFilter === 'all' || keywords.includes(activeFilter);
      const searchOk = !query || haystack.includes(query);
      item.style.display = filterOk && searchOk ? '' : 'none';
    });
  };

  buttons.forEach((button) => {
    button.addEventListener('click', () => {
      activeFilter = button.dataset.filter || 'all';
      buttons.forEach((b) => b.classList.toggle('is-active', b === button));
      apply();
    });
  });

  search?.addEventListener('input', apply);
  apply();
});
