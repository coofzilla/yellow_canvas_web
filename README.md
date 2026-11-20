# YellowCanvas web

Static product, support, and privacy pages for YellowCanvas. GitHub Pages deploys the root of `main` through the existing branch-based Pages setup.

- Home: https://coofzilla.github.io/yellow_canvas_web/
- Support: https://coofzilla.github.io/yellow_canvas_web/support/
- Privacy policy: https://coofzilla.github.io/yellow_canvas_web/privacy/
- Public support/privacy contact: `yellowdevjay@gmail.com`

The pages work without JavaScript, external fonts, analytics, a contact-form backend, or third-party runtime dependencies. FAQ disclosures use native HTML. Internal links use relative URLs so direct navigation works under the repository base path.

## Update and verify

1. Edit the static HTML and `assets/site.css`. Keep the existing `/privacy/` and `/support/` URLs stable.
2. Keep the policy aligned with the app's local-only storage and actual release scope. MP4 Download and trimming are supported; app accounts, cloud project sync, automatic synchronization, and Files import are not. Describe offer-code redemption generically without publishing ambassador codes.
3. Run `python3 Scripts/check_site.py` and inspect the responsive pages in a browser.
4. Commit a scoped change and push the approved `main` revision. Existing GitHub Pages deployment publishes it automatically.
5. Verify the deployment and each live HTTPS route, including the support email links.

Serve locally with `python3 -m http.server 8139 --bind 127.0.0.1`. There is no build step.

Brand SVGs are derived from the same vector master as the app icon and launch artwork. Palette: yellow `#FFDC00`, near-black `#111318`, and white `#FFFFFF`.

YellowCanvas 1.0.3 is publicly available as a Free download. Video review, comparison, drawing, and export require a one-time Full Access in-app purchase. Apple handles payment, eligible offer-code redemption, and restoration. There is no free trial or subscription.
