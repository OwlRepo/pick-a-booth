# Implementation prompt — Pick-a-Booth v2 UI (1:1)

Paste everything below into your coding agent (e.g. Claude Code), run from the **photobooth-frontend** (Vue 3 + Quasar) source repo — not the compiled `src/web/frontend` bundle.

---

You are implementing a finished visual redesign of the photobooth frontend. The reference is `design/Booth Redesign v2.dc.html` (open it in a browser — it renders all 22 screens on one canvas). **Match it 1:1**: spacing, radii, font sizes, colors, copy and layout. Do not invent UI, do not "improve" it, do not drop states. When the reference and this prompt disagree, the reference wins. Do NOT change backend logic, API calls, stores, routes or SSE handling — this is a presentation-layer change only.

## 0. Ground rules
- Keep every existing component, prop, emit, API call and config flag. Only replace templates/styles.
- Every artboard is labeled with the component it maps to (e.g. `07 GalleryDetailPage · itemPresenterMode`). Implement each in that component.
- Use the exact pixel values from the reference at 1280×800 (landscape) and 800×1280 (portrait). Choose layout by `orientation: portrait` media query, not by device sniffing.
- Remove all Quasar default looks on these screens (glass-effect, rounded Quasar buttons, q-btn stack styles). Plain elements + scoped CSS are fine; Quasar components may stay as behavior wrappers if fully restyled.

## 1. Design tokens (add as global CSS variables)
```css
:root{
  --pb-bg:#0a0b10; --pb-canvas:#05060a;
  --pb-surface-1:#12141c; --pb-surface-2:#1a1d28; --pb-surface-2-hover:#232736;
  --pb-text:#f4f5f8; --pb-muted:#9aa0b4; --pb-muted-2:#c9cdd9;
  --pb-line:1px solid rgba(255,255,255,.10);
  --pb-glass-bg:rgba(18,20,28,.62); --pb-glass-blur:18px; --pb-glass-border:1px solid rgba(255,255,255,.14);
  --pb-danger-text:#ff7a8a; --pb-live:#22d39a;
  /* Event palette (theme) — t1..t5, plus readable ink per color */
  --t1:#ff4d2e; --t2:#ff3d9a; --t3:#ffc933; --t4:#3d6bff; --t5:#22d39a;
  --t1i:#0a0b10; --t2i:#0a0b10; --t3i:#0a0b10; --t4i:#ffffff; --t5i:#0a0b10;
  --r-tile:28px; --r-tile-lg:32px; --r-card:32px; --r-card-sm:28px; --r-input:22px; --r-small:14px; --r-pill:999px;
}
*,*::before,*::after{box-sizing:border-box}
```
- Fonts: **Sora** 500/600/700 (headings, `letter-spacing:-.02em`, weight 600) and **Manrope** 500–800 (body/UI). Self-host the woff2 files (kiosks may be offline) — do not rely on Google Fonts at runtime.
- Icons: **Lucide**, stroke 2 (2.2 on tiles/big buttons), round caps/joins. Map existing `sym_o_*` config icon names to Lucide (camera, layout-grid, images, video, repeat, box, printer, mail, download, trash-2, sparkles, rotate-ccw, check, x, square, chevron-left/right, hand, lock, arrow-left, arrow-up, log-out, power, layout-dashboard, settings, folder, list, camera(+plus), ellipsis). Keep a fallback to Material Symbols for unmapped names.
- Ink color per palette color: choose `#0a0b10` or `#ffffff` by higher WCAG contrast (same function as `ink()` in the reference logic).

### Palette as a new theme setting
Add `uisettings.theme_palette: string[5]` (default the Party palette above). Presets in the reference Tweaks: Party `#ff4d2e #ff3d9a #ffc933 #3d6bff #22d39a`, Tropical `#ff7a1a #ff4f8b #ffe14d #19c3e6 #3ddc84`, Neon `#b44dff #ff3dc8 #eaff4d #2ee6ff #4dff9e`, Wedding `#e0457b #f59fb4 #f2cf6b #5b8fd9 #86cba6`. Write them to `--t1..--t5` (+ computed `--tNi`) on app load.
Mode tiles: use the trigger's `custom_color` when `use_custom_color` is true; otherwise default by index → Photo t1, Collage t2, GIF t3, Video t4, Boomerang t5, Wigglegram `#ffffff` with ink text.

## 2. Shared components (build once)
- **Pill button**: height 64 (52 in panels, 60 in top bars), `border-radius:999px`, padding `0 0.4×height`, icon 1.2× font size, gap 12, label Manrope 700. Variants: glass (on camera: glass bg + blur + glass border), solid surface-2.
- **Big button**: height per screen (68–124), radius `min(32, height/3)`, centered icon+label, Sora 600. Hover `brightness(1.08)`, active `scale(.98)`.
- **Ghost button**: height 72 (88 portrait), radius 20, surface-2 + line border, hover surface-2-hover.
- **Round icon button**: 56–72 circle, glass.
- **Mode tile**: radius 28 (32 portrait), padding 22 (26), icon in 64 (76) circle `rgba(255,255,255,.28)`, label Sora 27px (34px), `box-shadow:0 12px 32px -12px <tile color>`, hover `translateY(-3px)`, active `scale(.97)`. Show only title + icon (no subtitle).
- **QR card**: surface-2, radius 24, padding 18; white 118–140px QR plate radius 16 padding 8; "Scan to get your photo" Sora 23 + muted 15px line. Text above/below come from `qrcode_text_above` / `qrcode_text_below`.
- **Auto-return bar**: "Photo X of Y" left, "Back to start in Ns" right (muted 14/600), 6px track `rgba(255,255,255,.1)`, fill t3, driven by the existing `HeaderCountdownTimer` value.
- **Step dots**: active 44×14 pill in color, inactive 14×14 `rgba(255,255,255,.18)`, gap 8.
- **Countdown ring**: 420px (440 portrait) SVG r=46 stroke 3 track `rgba(255,255,255,.18)`, progress stroke t1 (t2 on the "Smile!" moment), inner glass circle (size −48) with numeral Sora 230px.
- **Processing spinner**: 3×3 grid of 56px squares radius 18, gap 14, colors cycle t1–t5 with centre `#f4f5f8`, glow `0 0 24px -4px <color>`, animation `pbPulse 1.2s ease-in-out infinite` (scale 1→.55, opacity 1→.35) with delays `[0,.1,.3,.6,.8,.4,.7,.5,.2]s`.

## 3. Screen-by-screen (component → design)
01/12 **IndexPage idle** — padding 24; rows: top bar (event name Sora 34 + "Pick a mode and tap — that's it." muted 16; right: Gallery pill if `show_gallery_on_frontpage`, 60px lock circle if `show_admin_on_frontpage`, honour `admin_button_invisible` + 5-tap), camera card radius 32 with glass "Live" pill (green glow dot), mode tiles row (6 cols, gap 14, height 196; portrait 3×2, height 380). Event name = `FRONTPAGE_TEXT`.
02/13 **CountdownTimer** — camera card inset 24, 25% dark overlay, top-centre glass "Look up at the camera" pill, centred ring, bottom step dots.
03 **Capture message** — same, ring full in t2, text = `TAKEPIC_MSG_TEXT`.
04/14 **Processing** (replace QSpinnerGrid) — centred spinner, "Almost there…" Sora 84 (76), muted 22px sub.
05/15 **MediaItemApprovalViewer** — photo card + glass "Stop collage" pill (abort); panel: "Shot N of M" + step dots (t2), "Keep this one?", "Try again" (surface-2) and "Awesome, next!" (t5). Wire to existing reject/confirm/abort.
06 **Recording** — glass REC pill with blinking t1 dot + timer, bottom-centre "Stop recording" pill big button (t1).
07/16 **GalleryDetailPage itemPresenterMode** — photo card (contain, radius 20) + right panel 460px (portrait: below): "Looking good!", Done pill (ReturnButton), auto-return bar, QR card (`gallery_show_qrcode`), Print (t3) + Email (t4), Filter + Delete ghost (`gallery_show_filter`, `gallery_show_delete`), "Take one more!" (t1, `itempresenter_show_trigger_last_action_again`). Print/Email are the configured share actions — render ShareTriggerButtons in this style, colours by index t3, t4, then t5, t2.
08/17 **PageShareParameters dialog** — backdrop `rgba(5,6,10,.72)` + blur 6, dialog surface-1 radius 36 padding 32, t4 icon circle, title, labeled input 80px radius 22 with 2px t4 border, helper text, Send big button t4. Labels come from the share action's `parameters_dialog_*` config.
09/18 **GalleryPage** — Back pill + "Gallery" + count; grid 5 cols (3 portrait) gap 12, square thumbs radius 22, media-type pill badge top-right in the type's colour (collage t2, gif t3, video t4, boomerang t5, wigglegram white).
10 **GalleryDetailPage** — same as 07 without auto-bar/"Take one more!", with Back pill, counter, Save/Filter/Delete row, 72px glass round chevrons on the carousel.
11/19 **SlideshowPage** — full-bleed photo; bottom glass bar (inset 24, radius 32): event name + "The booth is open — come say cheese." and t1 "Tap to take your own" button.
20 **LoginPage** — t1 poster card "Host only." + form card (password 64px radius 18, Sign in t1). Replace the documentation link with: "Forgot it? The password is set by whoever installed this booth."
21 **AdminLayout + AdminDashboardPage** — header: Booth back pill, pill tab group (active = white bg dark text), ⋯ menu, Sign out pill. Three cards (Server control / Health meters / Media counts). Keep all existing dialogs & actions; restyle.
22 **AdminConfigPage** — left section nav card, right form card with title + Save pill, rows = label + config key in monospace muted + control (pill toggles 60×34, inputs 48px radius 14).

## 4. Remove fork footprints (required)
- `AdminLayout`: header logo `<a href="https://photobooth-app.org/">` and the "photobooth-app.org" menu item.
- `AdminDashboardPage`: GitHub "help translating" + "supported languages" buttons, "Translate in context using Crowdin" button, PyPI upgrade button on app version.
- `LoginPage`: "Check the documentation." link.
- `AdminHelpPage`: replace content with local help text (no external links).
- `index.html`: title → event/brand name, description, remove Crowdin `_jipt` script and the in-context translation import (`i18n` crowdin call `D()`).
- Backend demo asset `demoassets/userdata/frames/frame_image_photobooth-app.png` ("made with the PHOTOBOOTH APP" watermark) — remove from defaults / frame overlay config.
- Replace `icons/logo-*.png` and favicon with your own brand assets.
- `grep -ri "photobooth-app\|crowdin\|github.com\|pypi" src/` must return nothing in UI code afterwards.

## 5. Acceptance checklist
- Screenshot each screen at 1280×800 and 800×1280 and diff against the matching artboard; no element missing, no clipping, radii and sizes equal.
- All hit targets ≥ 52px (guest buttons ≥ 88px).
- Works offline (fonts/icons bundled).
- All existing config flags still toggle the same elements.
- No console errors; SSE/state transitions unchanged.
