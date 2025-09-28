# HTTPS & Security Settings

- SECURE_SSL_REDIRECT=True: Forces HTTPS for all requests
- HSTS settings: Instructs browsers to always use HTTPS for 1 year, including subdomains
- SESSION_COOKIE_SECURE & CSRF_COOKIE_SECURE: Ensure cookies only sent over HTTPS
- X_FRAME_OPTIONS='DENY': Prevent clickjacking
- SECURE_CONTENT_TYPE_NOSNIFF=True: Prevent MIME-type sniffing
- SECURE_BROWSER_XSS_FILTER=True: Enable browser XSS filtering

Deployment: Configure SSL certificates in Nginx or Apache to serve site via HTTPS.
