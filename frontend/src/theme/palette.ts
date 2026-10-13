export const DEFAULT_PALETTE = ['#ff4d2e', '#ff3d9a', '#ffc933', '#3d6bff', '#22d39a'] as const
const WIGGLEGRAM_TILE = { bg: '#ffffff', fg: '#0a0b10' }

// port of ink() in docs/design/booth-redesign-v2/Booth Redesign v2.dc.html L352-358
export function ink(hex: string): '#0a0b10' | '#ffffff' {
  const h = hex.replace('#', '').slice(0, 6)
  const n = parseInt(
    h.length === 3
      ? h
          .split('')
          .map(c => c + c)
          .join('')
      : h,
    16
  )
  const ch = [(n >> 16) & 255, (n >> 8) & 255, n & 255].map(v => {
    v /= 255
    return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4)
  })
  const L = 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]
  const cw = 1.05 / (L + 0.05)
  const ci = (L + 0.05) / (0.0035 + 0.05)
  return ci > cw ? '#0a0b10' : '#ffffff'
}

export function resolvePalette(input: unknown): string[] {
  const valid =
    Array.isArray(input) && input.length === 5 && input.every(c => typeof c === 'string' && /^#([0-9a-f]{3}|[0-9a-f]{6}|[0-9a-f]{8})$/i.test(c))
  return valid ? (input as string[]) : [...DEFAULT_PALETTE]
}

export function applyPalette(input: unknown, root: HTMLElement = document.documentElement): void {
  resolvePalette(input).forEach((color, i) => {
    root.style.setProperty(`--t${i + 1}`, color)
    root.style.setProperty(`--t${i + 1}i`, ink(color))
  })
}

// canvas normalizes any CSS color (names, rgb()) to #rrggbb
export function normalizeHex(color: string): string {
  if (/^#([0-9a-f]{3}|[0-9a-f]{6}|[0-9a-f]{8})$/i.test(color)) return color
  const ctx = document.createElement('canvas').getContext('2d')
  if (!ctx) return '#000000'
  ctx.fillStyle = '#000000'
  ctx.fillStyle = color
  return ctx.fillStyle
}

// handoff §1: custom_color wins when use_custom_color; otherwise default by tile index t1..t5,
// multicamera (Wigglegram) is white with dark ink
export function tileColor(trigger: { action: string; use_custom_color: boolean; custom_color: string }, index: number): { bg: string; fg: string } {
  if (trigger.use_custom_color) {
    const bg = normalizeHex(trigger.custom_color)
    return { bg, fg: ink(bg) }
  }
  if (trigger.action === 'multicamera') return WIGGLEGRAM_TILE
  const slot = (index % 5) + 1
  return { bg: `var(--t${slot})`, fg: `var(--t${slot}i)` }
}
