// // Actions:

// const closeButton = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
// <title>remove</title>
// <path d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"></path>
// </svg>
// `;
// const menuButton = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
// <title>ellipsis-horizontal</title>
// <path d="M16 7.843c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 1.98c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// <path d="M16 19.908c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 14.046c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// <path d="M16 31.974c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 26.111c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// </svg>
// `;

// const actionButtons = document.querySelectorAll('.action-button');

// if (actionButtons) {
//   actionButtons.forEach(button => {
//     button.addEventListener('click', () => {
//       const buttonId = button.dataset.id;
//       let popup = document.querySelector(`.popup-${buttonId}`);
//       console.log(popup);
//       if (popup) {
//         button.innerHTML = menuButton;
//         return popup.remove();
//       }

//       const deleteUrl = button.dataset.deleteUrl;
//       const editUrl = button.dataset.editUrl;
//       button.innerHTML = closeButton;

//       popup = document.createElement('div');
//       popup.classList.add('popup');
//       popup.classList.add(`popup-${buttonId}`);
//       popup.innerHTML = `<a href="${editUrl}">Edit</a>
//       <form action="${deleteUrl}" method="delete">
//         <button type="submit">Delete</button>
//       </form>`;
//       button.insertAdjacentElement('afterend', popup);
//     });
//   });
// }

// Menu

const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput)
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;
        function showProfile(officerName) {
            alert(`Opening profile for: ${officerName}`);
        }

        function showCitizenProfile(citizenName) {
            alert(`Opening citizen profile for: ${citizenName}`);
        }

        function viewCase(caseTitle) {
            alert(`Opening case details for: ${caseTitle}`);
        }

        function assignOfficer(caseTitle) {
            alert(`Assigning officer to case: ${caseTitle}`);
        }

        // Add hover effects and interactions
        document.addEventListener('DOMContentLoaded', function() {
            // Add click handlers for better interactivity
            const buttons = document.querySelectorAll('.btn');
            buttons.forEach(button => {
                button.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-1px)';
                });
                
                button.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });
        });

        //case_detail.js
        function updateStatus() {
            alert('Opening status update form...');
        }

        function updateCase() {
            alert('Opening case update form...');
        }

        function goBack() {
            history.back();
        }

        function uploadEvidence() {
            alert('Opening evidence upload form...');
        }

        function viewFile(filename) {
            alert(`Opening file: ${filename}`);
        }

        function showProfile(name) {
            alert(`Opening profile for: ${name}`);
        }

        // Add interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            const buttons = document.querySelectorAll('.btn');
            buttons.forEach(button => {
                button.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-1px)';
                });
                
                button.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });

            // Add hover effects to evidence items
            const evidenceItems = document.querySelectorAll('.evidence-item');
            evidenceItems.forEach(item => {
                item.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateX(5px)';
                });
                
                item.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateX(0)';
                });
            });
        });

        //officer-profile.js
        function viewCase(caseTitle) {
            alert(`Opening case: ${caseTitle}`);
        }

        function goBack() {
            history.back();
        }

        // Add interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            // Button hover effects
            const buttons = document.querySelectorAll('.btn');
            buttons.forEach(button => {
                button.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-1px)';
                });
                
                button.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });

            // Profile card animation on load
            const profileCard = document.querySelector('.profile-card');
            setTimeout(() => {
                profileCard.style.transform = 'scale(1)';
                profileCard.style.opacity = '1';
            }, 200);
        });

        // Profile card initial state
        document.querySelector('.profile-card').style.transform = 'scale(0.95)';
        document.querySelector('.profile-card').style.opacity = '0.8';
        document.querySelector('.profile-card').style.transition = 'all 0.3s ease';

        //citizen-profile.js
                function viewCase(caseTitle) {
            alert(`Opening case: ${caseTitle}`);
        }

        function goBack() {
            history.back();
        }

        // Add interactive effects
        document.addEventListener('DOMContentLoaded', function() {
            // Button hover effects
            const buttons = document.querySelectorAll('.btn');
            buttons.forEach(button => {
                button.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-1px)';
                });
                
                button.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });

            // Profile card animation on load
            const profileCard = document.querySelector('.profile-card');
            setTimeout(() => {
                profileCard.style.transform = 'scale(1)';
                profileCard.style.opacity = '1';
            }, 200);

            // Table row hover effects
            const tableRows = document.querySelectorAll('.table tbody tr');
            tableRows.forEach(row => {
                row.addEventListener('mouseenter', function() {
                    this.style.boxShadow = '0 4px 8px rgba(243, 156, 18, 0.2)';
                });
                
                row.addEventListener('mouseleave', function() {
                    this.style.boxShadow = 'none';
                });
            });
        });

        // Profile card initial state
        document.querySelector('.profile-card').style.transform = 'scale(0.95)';
        document.querySelector('.profile-card').style.opacity = '0.8';
        document.querySelector('.profile-card').style.transition = 'all 0.3s ease';

        // assign-officer.js
                const officerData = {
            'detective_smith': {
                name: 'Detective Sarah Smith',
                badge: 'Badge #1234 • Detective',
                department: 'Criminal Investigation Division',
                status: 'Available • 3 Active Cases',
                avatar: 'SS'
            },
            'detective_jones': {
                name: 'Detective Mike Jones',
                badge: 'Badge #5678 • Detective',
                department: 'Robbery & Homicide Division',
                status: 'Available • 2 Active Cases',
                avatar: 'MJ'
            },
            'sergeant_brown': {
                name: 'Sergeant Lisa Brown',
                badge: 'Badge #9101 • Sergeant',
                department: 'Field Operations',
                status: 'Available • 1 Active Case',
                avatar: 'LB'
            },
            'detective_wilson': {
                name: 'Detective Tom Wilson',
                badge: 'Badge #1121 • Detective',
                department: 'Financial Crimes Unit',
                status: 'Available • 4 Active Cases',
                avatar: 'TW'
            },
            'lieutenant_davis': {
                name: 'Lieutenant Mark Davis',
                badge: 'Badge #3141 • Lieutenant',
                department: 'Special Operations',
                status: 'Available • 2 Active Cases',
                avatar: 'MD'
            }
        };

        function showOfficerInfo(officerId) {
            const infoDiv = document.getElementById('officerInfo');
            
            if (!officerId) {
                infoDiv.classList.remove('show');
                return;
            }

            const officer = officerData[officerId];
            if (officer) {
                document.getElementById('officerAvatar').textContent = officer.avatar;
                document.getElementById('officerName').textContent = officer.name;
                document.getElementById('officerBadge').textContent = officer.badge;
                document.getElementById('officerDepartment').textContent = officer.department;
                document.getElementById('officerStatus').textContent = officer.status;
                
                infoDiv.classList.add('show');
            }
        }

        function handleSubmit(event) {
            event.preventDefault();
            
            const selectedOfficer = document.getElementById('officer').value;
            if (!selectedOfficer) {
                alert('Please select an officer to assign to this case.');
                return;
            }

            const officer = officerData[selectedOfficer];
            
            // Simulate form submission
            alert(`Officer ${officer.name} has been successfully assigned to Case #CR-2024-0156!`);
            
            // In a real application, you would submit the form data here
            // window.location.href = 'case-details.html';
        }

        function goBack() {
            if (confirm('Are you sure you want to go back? Any unsaved changes will be lost.')) {
                // In a real application, this would navigate back
                alert('Navigating back to case management...');
            }
        }

        //officer-dashboaard.js
                function filterCases(status) {
            // Update active filter button
            document.querySelectorAll('.filter-btn').forEach(btn => {
                btn.classList.remove('active');
            });
            event.target.classList.add('active');

            // Filter table rows
            const rows = document.querySelectorAll('#casesTableBody tr');
            rows.forEach(row => {
                if (status === 'all') {
                    row.style.display = '';
                } else {
                    if (row.getAttribute('data-status') === status) {
                        row.style.display = '';
                    } else {
                        row.style.display = 'none';
                    }
                }
            });

            // Update workload counter based on active cases
            updateWorkloadCounter();
        }

        function updateWorkloadCounter() {
            const activeRows = document.querySelectorAll('#casesTableBody tr[style=""], #casesTableBody tr:not([style])');
            const count = Array.from(activeRows).filter(row => {
                const status = row.getAttribute('data-status');
                return status === 'open' || status === 'investigating';
            }).length;
            
            document.querySelector('.workload-counter').textContent = `${count} Active Case${count !== 1 ? 's' : ''}`;
        }

        // Initialize the dashboard
        document.addEventListener('DOMContentLoaded', function() {
            updateWorkloadCounter();
        });
