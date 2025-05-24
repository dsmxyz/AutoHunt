// Dark mode toggle functionality
document.addEventListener('DOMContentLoaded', function() {
    const darkModeToggle = document.getElementById('darkModeSwitch');
    const darkModeCSS = document.getElementById('dark-mode-css');
    
    // Check for saved user preference
    const savedMode = localStorage.getItem('darkMode');
    if (savedMode === 'enabled') {
        document.documentElement.setAttribute('data-bs-theme', 'dark');
        darkModeToggle.checked = true;
        darkModeCSS.disabled = false;
    }
    
    // Toggle dark mode
    darkModeToggle.addEventListener('change', function() {
        if (this.checked) {
            document.documentElement.setAttribute('data-bs-theme', 'dark');
            darkModeCSS.disabled = false;
            localStorage.setItem('darkMode', 'enabled');
        } else {
            document.documentElement.setAttribute('data-bs-theme', 'light');
            darkModeCSS.disabled = true;
            localStorage.setItem('darkMode', 'disabled');
        }
    });
});