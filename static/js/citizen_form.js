        let uploadedFiles = [];

        function handleFileUpload(event) {
            const files = event.target.files;
            const preview = document.getElementById('filePreview');
            const fileName = document.getElementById('fileName');
            const fileSize = document.getElementById('fileSize');
            
            if (files.length > 0) {
                uploadedFiles = Array.from(files);
                let totalSize = 0;
                let fileNames = [];
                
                for (let file of files) {
                    totalSize += file.size;
                    fileNames.push(file.name);
                }
                
                fileName.textContent = files.length === 1 ? files[0].name : `${files.length} files selected`;
                fileSize.textContent = `Total size: ${(totalSize / 1024 / 1024).toFixed(2)} MB`;
                preview.classList.add('show');
            } else {
                preview.classList.remove('show');
                uploadedFiles = [];
            }
            
            updateProgress();
        }

        function updateProgress() {
            const form = document.getElementById('caseReportForm');
            const requiredFields = form.querySelectorAll('[required]');
            let filledFields = 0;
            
            requiredFields.forEach(field => {
                if (field.value.trim() !== '') {
                    filledFields++;
                }
            });
            
            const progress = (filledFields / requiredFields.length) * 100;
            document.getElementById('progressFill').style.width = progress + '%';
        }

        function handleSubmit(event) {
            event.preventDefault();
            
            // Validate required fields
            const form = document.getElementById('caseReportForm');
            const requiredFields = form.querySelectorAll('[required]');
            let isValid = true;
            
            requiredFields.forEach(field => {
                if (field.value.trim() === '') {
                    field.style.borderColor = 'var(--color-error)';
                    isValid = false;
                } else {
                    field.style.borderColor = 'var(--color-dark-light)';
                }
            });
            
            if (!isValid) {
                alert('Please fill in all required fields.');
                return;
            }
            
            // Validate description length
            const description = document.getElementById('description').value;
            if (description.length < 20) {
                alert('Please provide a more detailed description (at least 20 characters).');
                document.getElementById('description').focus();
                return;
            }
            
            // Confirmation dialog
            const title = document.getElementById('title').value;
            const caseType = document.getElementById('case_type').options[document.getElementById('case_type').selectedIndex].text;
            const priority = document.getElementById('priority').options[document.getElementById('priority').selectedIndex].text;
            
            const confirmMessage = `Please confirm your case report:

Title: ${title}
Type: ${caseType}
Priority: ${priority}
Evidence files: ${uploadedFiles.length} file(s)

Submit this report?`;
            
            if (confirm(confirmMessage)) {
                // Simulate form submission
                alert(`Case report submitted successfully!

Your report has been received and will be reviewed by our officers. You will receive a case number via email shortly.

Thank you for helping keep our community safe.`);
                
                // In a real application, you would submit the form data here
                // window.location.href = 'citizen-dashboard.html';
            }
        }

        function goBack() {
            if (confirm('Are you sure you want to go back? All entered information will be lost.')) {
                alert('Navigating back to dashboard...');
                // In a real application: window.history.back() or redirect
            }
        }

        // Auto-update progress on field changes
        document.addEventListener('DOMContentLoaded', () => {
            const form = document.getElementById('caseReportForm');
            form.addEventListener('input', updateProgress);
        });