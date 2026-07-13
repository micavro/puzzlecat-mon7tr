(() => {
  const root = document.documentElement;
  const themeButton = document.getElementById("themeButton");
  const savedTheme = localStorage.getItem("puzzlecat-theme");
  if (savedTheme) root.dataset.theme = savedTheme;

  themeButton?.addEventListener("click", () => {
    const next = root.dataset.theme === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    localStorage.setItem("puzzlecat-theme", next);
  });

  const input = document.getElementById("searchInput");
  if (!input) return;
  const cards = [...document.querySelectorAll(".puzzle-card")];
  const count = document.getElementById("resultCount");
  const noResults = document.getElementById("noResults");

  input.addEventListener("input", () => {
    const tokens = input.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    cards.forEach((card) => {
      const haystack = card.dataset.search.toLocaleLowerCase();
      const match = tokens.every((token) => haystack.includes(token));
      card.hidden = !match;
      if (match) visible += 1;
    });
    count.textContent = String(visible);
    noResults.hidden = visible !== 0;
  });
})();
