import { describe, expect, it } from 'vitest'
import { Camera, ChevronLeft } from 'lucide-vue-next'
import { lucideFor } from './icons'

describe('lucideFor', () => {
  it('error: unknown name returns null', () => {
    expect(lucideFor('definitely_not_an_icon')).toBeNull()
  })

  it('edge: Object prototype keys are not icons', () => {
    expect(lucideFor('constructor')).toBeNull()
    expect(lucideFor('toString')).toBeNull()
  })

  it('edge: Lucide kebab key resolves', () => {
    expect(lucideFor('chevron-left')).toBe(ChevronLeft)
  })

  it('edge: sym_o_ prefixed name resolves like the bare config name', () => {
    expect(lucideFor('sym_o_photo_camera')).toBe(Camera)
  })

  it('happy: known config name returns a component', () => {
    expect(lucideFor('photo_camera')).toBe(Camera)
  })
})
