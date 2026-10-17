document.addEventListener('click', async (event) => {
  const button = event.target.closest('[data-notebook-copy]');
  if (!button) return;
  const target = document.getElementById(button.dataset.notebookCopy);
  if (!target) return;
  const text = target.textContent.trim();
  const status = button.parentElement.querySelector('[role="status"]');
  try {
    await navigator.clipboard.writeText(text);
    if (status) status.textContent = 'Đã sao chép. Bạn có thể dán vào NotebookLM.';
  } catch (_) {
    const range = document.createRange();
    range.selectNodeContents(target);
    const selection = window.getSelection();
    selection.removeAllRanges();
    selection.addRange(range);
    if (status) status.textContent = 'Đã chọn nội dung. Nhấn Ctrl+C hoặc ⌘C để sao chép.';
  }
});
