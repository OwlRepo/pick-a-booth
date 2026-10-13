import type { Component } from 'vue'
import {
  ArrowLeft,
  ArrowUp,
  Box,
  Camera,
  Check,
  ChevronLeft,
  ChevronRight,
  Download,
  Ellipsis,
  Folder,
  Hand,
  Images,
  LayoutDashboard,
  LayoutGrid,
  List,
  Lock,
  LogOut,
  Mail,
  Plus,
  Power,
  Printer,
  Repeat,
  RotateCcw,
  Settings,
  Sparkles,
  Square,
  Trash,
  Trash2,
  Video,
  X,
} from 'lucide-vue-next'

// Config / Material Symbols names (handoff §1, plan Phase 3 step 8) -> Lucide.
// Config icons arrive bare ("photo_camera") or prefixed ("sym_o_photo_camera").
const CONFIG_ICONS = new Map<string, Component>(
  Object.entries({
    photo_camera: Camera,
    auto_awesome_mosaic: LayoutGrid,
    animated_images: Images,
    movie: Video,
    '3d': Box,
    print: Printer,
    mail: Mail,
    download: Download,
    delete: Trash,
    filter: Sparkles,
    close: X,
    arrow_back_ios_new: ArrowLeft,
    logout: LogOut,
    dashboard: LayoutDashboard,
    settings: Settings,
    folder_shared: Folder,
    list: List,
    power_settings_new: Power,
    restart_alt: RotateCcw,
    thumb_up: Check,
    thumb_down: RotateCcw,
    cancel: X,
    admin_panel_settings: Lock,
    photo_library: Images,
  })
)

// Lucide kebab-case keys used directly by the screens (handoff §1 icon list).
const LUCIDE_ICONS = new Map<string, Component>(
  Object.entries({
    camera: Camera,
    'layout-grid': LayoutGrid,
    images: Images,
    video: Video,
    repeat: Repeat,
    box: Box,
    printer: Printer,
    mail: Mail,
    download: Download,
    trash: Trash,
    'trash-2': Trash2,
    sparkles: Sparkles,
    'rotate-ccw': RotateCcw,
    check: Check,
    x: X,
    square: Square,
    'chevron-left': ChevronLeft,
    'chevron-right': ChevronRight,
    hand: Hand,
    lock: Lock,
    'arrow-left': ArrowLeft,
    'arrow-up': ArrowUp,
    'log-out': LogOut,
    power: Power,
    'layout-dashboard': LayoutDashboard,
    settings: Settings,
    folder: Folder,
    list: List,
    plus: Plus,
    ellipsis: Ellipsis,
  })
)

/** Resolve a config/sym_o_ name or a Lucide kebab key to a Lucide component; null means "use Material Symbols". */
export function lucideFor(name: string): Component | null {
  const key = name.startsWith('sym_o_') ? name.slice('sym_o_'.length) : name
  return CONFIG_ICONS.get(key) ?? LUCIDE_ICONS.get(key) ?? null
}
