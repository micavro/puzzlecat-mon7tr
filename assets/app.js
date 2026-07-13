(() => {
  const body = document.body;
  const input = document.getElementById("searchInput");
  const count = document.getElementById("resultCount");
  const noResults = document.getElementById("noResults");
  const puzzles = [...document.querySelectorAll(".puzzle")];
  const navItems = [...document.querySelectorAll("#puzzleNav li")];
  const menuButton = document.getElementById("menuButton");
  const backdrop = document.getElementById("sidebarBackdrop");
  const themeButton = document.getElementById("themeButton");

  const savedTheme = localStorage.getItem("puzzlecat-theme");
  if (savedTheme) document.documentElement.dataset.theme = savedTheme;

  const closeSidebar = () => body.classList.remove("sidebar-open");
  menuButton.addEventListener("click", () => body.classList.toggle("sidebar-open"));
  backdrop.addEventListener("click", closeSidebar);
  navItems.forEach((item) => item.addEventListener("click", closeSidebar));

  themeButton.addEventListener("click", () => {
    const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
    document.documentElement.dataset.theme = next;
    localStorage.setItem("puzzlecat-theme", next);
  });

  input.addEventListener("input", () => {
    const tokens = input.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let visible = 0;
    puzzles.forEach((puzzle, index) => {
      const haystack = puzzle.dataset.search.toLocaleLowerCase();
      const match = tokens.every((token) => haystack.includes(token));
      puzzle.hidden = !match;
      navItems[index].hidden = !match;
      if (match) visible += 1;
    });
    count.textContent = String(visible);
    noResults.hidden = visible !== 0;
  });

  const linksById = new Map(
    navItems.map((item) => [item.querySelector("a").hash.slice(1), item])
  );
  const observer = new IntersectionObserver(
    (entries) => {
      const visible = entries
        .filter((entry) => entry.isIntersecting)
        .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top)[0];
      if (!visible) return;
      navItems.forEach((item) => item.classList.remove("active"));
      const active = linksById.get(visible.target.id);
      if (active) {
        active.classList.add("active");
        active.scrollIntoView({ block: "nearest" });
      }
    },
    { rootMargin: "-75px 0px -78% 0px", threshold: 0 }
  );
  puzzles.forEach((puzzle) => observer.observe(puzzle));
})();
