import { useMemo } from 'react'

const COLORS = [
  '#F97316', '#22C55E', '#EC4899', '#F59E0B',
  '#3B82F6', '#8B5CF6', '#EF4444', '#14B8A6',
]

interface Piece {
  color: string
  cx: string
  cy: string
  cr: string
  delay: string
  size: number
  borderRadius: string
}

function usePieces(count: number): Piece[] {
  return useMemo(() => {
    return Array.from({ length: count }, (_, i) => {
      const angle   = (i / count) * Math.PI * 2 + (Math.random() - 0.5) * 0.8
      const dist    = 120 + Math.random() * 220
      return {
        color:        COLORS[i % COLORS.length],
        cx:           `${Math.cos(angle) * dist}px`,
        cy:           `${Math.sin(angle) * dist - 80}px`,
        cr:           `${Math.random() * 640 - 320}deg`,
        delay:        `${Math.random() * 0.35}s`,
        size:         6 + Math.random() * 8,
        borderRadius: Math.random() > 0.5 ? '50%' : '2px',
      }
    })
  // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [count])
}

interface Props {
  active: boolean
}

export default function Confetti({ active }: Props) {
  const pieces = usePieces(48)

  if (!active) return null

  return (
    <div className="confetti-wrap" aria-hidden>
      {pieces.map((p, i) => (
        <div
          key={i}
          className="confetti-piece"
          style={{
            '--cx': p.cx,
            '--cy': p.cy,
            '--cr': p.cr,
            background: p.color,
            width: p.size,
            height: p.size,
            borderRadius: p.borderRadius,
            animationDelay: p.delay,
          } as React.CSSProperties}
        />
      ))}
    </div>
  )
}
