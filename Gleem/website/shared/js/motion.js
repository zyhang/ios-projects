/**
 * Stillwall site motion — subtle reveals + reduced-motion safe.
 * Usage: add data-reveal (and optional data-reveal-delay="80") on elements.
 */
(function () {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const nodes = document.querySelectorAll("[data-reveal]");

  if (!nodes.length) return;

  if (reduce || !("IntersectionObserver" in window)) {
    nodes.forEach((el) => el.classList.add("is-visible"));
    return;
  }

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        const el = entry.target;
        const delay = Number(el.getAttribute("data-reveal-delay") || 0);
        if (delay) el.style.transitionDelay = `${delay}ms`;
        el.classList.add("is-visible");
        io.unobserve(el);
      });
    },
    { rootMargin: "0px 0px -8% 0px", threshold: 0.12 }
  );

  nodes.forEach((el) => io.observe(el));
})();
