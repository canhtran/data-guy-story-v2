// Site override of Hextra v0.12.1 assets/js/core/sidebar.js.
// Identical to the theme file except for scrollToActiveItem(): the stock
// version scrolls the sidebar on every page load, even when the active item
// is already visible, which makes the sidebar jump on each navigation.
// This version only scrolls when the active item is out of view, and only
// by the amount needed to reveal it.
document.addEventListener("DOMContentLoaded", function () {
  scrollToActiveItem();
  enableCollapsibles();
});

function enableCollapsibles() {
  const buttons = document.querySelectorAll(".hextra-sidebar-collapsible-button");
  buttons.forEach(function (button) {
    button.addEventListener("click", function (e) {
      e.preventDefault();
      const list = button.closest('li');
      if (list) {
        list.classList.toggle("open");
        button.setAttribute('aria-expanded', list.classList.contains('open') ? 'true' : 'false');
      }
    });
  });
}

function scrollToActiveItem() {
  const sidebarScrollbar = document.querySelector("aside.hextra-sidebar-container > .hextra-scrollbar");
  const activeItems = document.querySelectorAll(".hextra-sidebar-active-item");
  const visibleActiveItem = Array.from(activeItems).find(function (activeItem) {
    return activeItem.getBoundingClientRect().height > 0;
  });

  if (!sidebarScrollbar || !visibleActiveItem) {
    return;
  }

  const containerRect = sidebarScrollbar.getBoundingClientRect();
  const itemRect = visibleActiveItem.getBoundingClientRect();
  const yOffset = visibleActiveItem.clientHeight;

  let delta = 0;
  if (itemRect.top < containerRect.top) {
    // Active item is above the visible area: reveal it with a one-row margin.
    delta = itemRect.top - containerRect.top - yOffset;
  } else if (itemRect.bottom > containerRect.bottom) {
    // Active item is below the visible area: scroll just enough to reveal it.
    delta = itemRect.bottom - containerRect.bottom + yOffset;
  }

  if (delta === 0) {
    return;
  }

  sidebarScrollbar.scrollTo({
    behavior: "instant",
    top: sidebarScrollbar.scrollTop + delta
  });
}
