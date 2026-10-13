import { describe, expect, it } from 'vitest'
import { DEFAULT_PALETTE, ink, normalizeHex, resolvePalette, tileColor } from './palette'

describe('resolvePalette', () => {
  it('error: falls back to the default palette when fewer than 5 colors are given', () => {
    expect(resolvePalette(['#000'])).toEqual([...DEFAULT_PALETTE])
  })

  it('error: falls back to the default palette when input is undefined', () => {
    expect(resolvePalette(undefined)).toEqual([...DEFAULT_PALETTE])
  })

  it('error: falls back to the default palette when a color is not hex', () => {
    expect(resolvePalette(['red', '#fff', '#fff', '#fff', '#fff'])).toEqual([...DEFAULT_PALETTE])
  })

  it('happy: returns a valid 5-color hex palette unchanged', () => {
    const palette = ['#ff7a1a', '#ff4f8b', '#ffe14d', '#19c3e6', '#3ddc84']
    expect(resolvePalette(palette)).toEqual(palette)
  })
})

describe('ink', () => {
  it('edge: expands 3-digit hex', () => {
    expect(ink('#fff')).toBe('#0a0b10')
  })

  it('happy: dark ink on white', () => {
    expect(ink('#ffffff')).toBe('#0a0b10')
  })

  // The reference ink() (dc.html L352-358) scores #3d6bff as a near-tie (dark 4.43:1 vs white 4.43:1) and picks
  // dark ink; the rendered reference sets --t4i from ink(), so the reference wins over the handoff's static #ffffff.
  it('edge: t4 blue is a near-tie and resolves to dark ink, like the rendered reference', () => {
    expect(ink('#3d6bff')).toBe('#0a0b10')
  })

  it('happy: white ink on a dark blue', () => {
    expect(ink('#196cb0')).toBe('#ffffff')
  })

  it('happy: dark ink on t3 yellow', () => {
    expect(ink('#ffc933')).toBe('#0a0b10')
  })
})

describe('tileColor', () => {
  it('edge: multicamera (Wigglegram) tile is white with dark ink regardless of index', () => {
    expect(tileColor({ action: 'multicamera', use_custom_color: false, custom_color: '#196cb0' }, 5)).toEqual({ bg: '#ffffff', fg: '#0a0b10' })
  })

  it('happy: default color by tile index', () => {
    expect(tileColor({ action: 'video', use_custom_color: false, custom_color: '#196cb0' }, 3)).toEqual({ bg: 'var(--t4)', fg: 'var(--t4i)' })
  })

  it('happy: custom color wins when use_custom_color is set', () => {
    expect(tileColor({ action: 'image', use_custom_color: true, custom_color: '#196cb0' }, 0)).toEqual({ bg: '#196cb0', fg: '#ffffff' })
  })
})

describe('normalizeHex', () => {
  it('happy: hex input is returned as-is without touching the DOM', () => {
    expect(normalizeHex('#22d39a')).toBe('#22d39a')
  })
})
