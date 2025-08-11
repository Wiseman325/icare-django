document.addEventListener('DOMContentLoaded', () => {
  const dateCollectedInput = document.querySelector('input[type="date"][name="date_collected"]');

  if (dateCollectedInput) {
    const now = new Date();
    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0'); // month is zero-indexed
    const day = String(now.getDate()).padStart(2, '0');

    const maxDate = `${year}-${month}-${day}`;
    dateCollectedInput.setAttribute('max', maxDate);
  }
});
