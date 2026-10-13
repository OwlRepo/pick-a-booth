/**
 * Plain-text rendering for admin-configured HTML strings (e.g. uisettings.FRONTPAGE_TEXT).
 *
 * The v2 UI renders these as text via `{{ }}` interpolation, never v-html: markup is
 * dropped, `<br>` becomes a space and whitespace collapses to a single line.
 */

/** Extracts the text content of an HTML fragment. */
export type HtmlTextParser = (html: string) => string

const BR_PATTERN = /<br\s*\/?>/gi

export const domTextParser: HtmlTextParser = html => new DOMParser().parseFromString(html, 'text/html').body.textContent ?? ''

export function plainText(html: string | null | undefined, parse: HtmlTextParser = domTextParser): string {
  if (!html) return ''
  return parse(html.replace(BR_PATTERN, ' ')).replace(/\s+/g, ' ').trim()
}
