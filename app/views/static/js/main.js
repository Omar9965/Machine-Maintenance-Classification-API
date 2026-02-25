/**
 * Machine Predictive Maintenance — Client-side JS
 */

document.addEventListener('DOMContentLoaded', () => {
    initFormHandling();
    initActiveNavLink();
});


/**
 * Highlight the current page's nav link.
 */
function initActiveNavLink() {
    const currentPath = window.location.pathname;
    document.querySelectorAll('.nav-link').forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPath || (href !== '/' && currentPath.startsWith(href))) {
            link.style.color = 'var(--text-primary)';
            link.style.background = 'var(--bg-glass)';
        }
    });
}


/**
 * Handle form submission with loading state.
 */
function initFormHandling() {
    const form = document.getElementById('predictForm');
    if (!form) return;

    form.addEventListener('submit', (e) => {
        const submitBtn = document.getElementById('submitBtn');
        if (!submitBtn) return;

        const btnText = submitBtn.querySelector('.btn-text');
        const btnLoader = submitBtn.querySelector('.btn-loader');

        if (btnText) btnText.style.display = 'none';
        if (btnLoader) btnLoader.style.display = 'inline-flex';
        submitBtn.disabled = true;
        submitBtn.style.opacity = '0.7';
    });

    // Reset button state on reset
    form.addEventListener('reset', () => {
        const submitBtn = document.getElementById('submitBtn');
        if (!submitBtn) return;

        const btnText = submitBtn.querySelector('.btn-text');
        const btnLoader = submitBtn.querySelector('.btn-loader');

        if (btnText) btnText.style.display = 'inline';
        if (btnLoader) btnLoader.style.display = 'none';
        submitBtn.disabled = false;
        submitBtn.style.opacity = '1';
    });
}
