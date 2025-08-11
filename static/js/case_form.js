document.addEventListener('DOMContentLoaded', () => {
  // Select the incident date input by its name attribute
  const incidentDateInput = document.querySelector('input[type="datetime-local"][name="incident_date"]');

  if (incidentDateInput) {
    // Get current date/time and format it to YYYY-MM-DDTHH:mm
    const now = new Date();

    const year = now.getFullYear();
    const month = String(now.getMonth() + 1).padStart(2, '0');  // month is zero-indexed
    const day = String(now.getDate()).padStart(2, '0');

    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');

    const maxDateTime = `${year}-${month}-${day}T${hours}:${minutes}`;

    // Set the max attribute
    incidentDateInput.setAttribute('max', maxDateTime);
  }
});
