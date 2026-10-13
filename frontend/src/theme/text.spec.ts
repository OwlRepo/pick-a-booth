import { describe, expect, it } from 'vitest'
import { plainText, type HtmlTextParser } from './text'

// vitest runs in node (no DOMParser): strip tags with a regex instead
const stripTags: HtmlTextParser = html => html.replace(/<[^>]*>/g, '')

describe('plainText', () => {
  it('error: returns an empty string for empty, null or undefined input', () => {
    expect(plainText('', stripTags)).toBe('')
    expect(plainText(null, stripTags)).toBe('')
    expect(plainText(undefined, stripTags)).toBe('')
  })

  it('edge: returns an empty string when the html has only markup and whitespace', () => {
    expect(plainText('<br>  <br/>\n<b> </b>', stripTags)).toBe('')
  })

  it('edge: replaces every <br> variant with a single space', () => {
    expect(plainText('Anna<br>&amp;<BR/>Ben<br />2026<br   >party', stripTags)).toBe('Anna &amp; Ben 2026 party')
  })

  it('edge: collapses newlines, tabs and repeated spaces and trims', () => {
    expect(plainText('  \n\tAnna   &\n Ben\t ', stripTags)).toBe('Anna & Ben')
  })

  it('regression: drops markup around the text instead of rendering it', () => {
    expect(plainText('<div class="x"><h1>Welcome</h1><p>to the <i>party</i></p></div>', stripTags)).toBe('Welcometo the party')
  })

  it('happy: keeps plain text unchanged', () => {
    expect(plainText('Anna & Ben 2026', stripTags)).toBe('Anna & Ben 2026')
  })
})
