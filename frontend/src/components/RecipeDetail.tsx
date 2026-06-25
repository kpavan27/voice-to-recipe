import { useState, useEffect, useMemo, useRef } from 'react'
import { RecipeOption, RecipeStep } from '../App'
import Confetti from './Confetti'

// ─────────────────────────────────────────── step category system
interface StepCategory {
  icon: string
  label: string
  color: string
  bg: string
  circleGradient: string
  connectorColor: string
}

const CATEGORIES: Record<string, StepCategory> = {
  prep:   { icon: '🔪', label: 'Prep',   color: '#7C3AED', bg: 'rgba(139,92,246,0.09)',  circleGradient: 'linear-gradient(145deg,#7C3AED,#8B5CF6)', connectorColor: '#C4B5FD' },
  heat:   { icon: '🔥', label: 'Cook',   color: '#EA580C', bg: 'rgba(249,115,22,0.09)',  circleGradient: 'linear-gradient(145deg,#EA580C,#F97316)', connectorColor: '#FDBA74' },
  mix:    { icon: '🥣', label: 'Mix',    color: '#0891B2', bg: 'rgba(6,182,212,0.09)',   circleGradient: 'linear-gradient(145deg,#0891B2,#06B6D4)', connectorColor: '#A5F3FC' },
  season: { icon: '🧂', label: 'Season', color: '#DC2626', bg: 'rgba(220,38,38,0.08)',   circleGradient: 'linear-gradient(145deg,#DC2626,#EF4444)', connectorColor: '#FCA5A5' },
  rest:   { icon: '⏸',  label: 'Rest',   color: '#059669', bg: 'rgba(5,150,105,0.09)',   circleGradient: 'linear-gradient(145deg,#059669,#10B981)', connectorColor: '#6EE7B7' },
  plate:  { icon: '🎨', label: 'Plate',  color: '#BE185D', bg: 'rgba(190,24,93,0.08)',   circleGradient: 'linear-gradient(145deg,#BE185D,#EC4899)', connectorColor: '#F9A8D4' },
  serve:  { icon: '🍽️', label: 'Serve',  color: '#D97706', bg: 'rgba(217,119,6,0.09)',   circleGradient: 'linear-gradient(145deg,#D97706,#F59E0B)', connectorColor: '#FDE68A' },
}

const DONE_CATEGORY: StepCategory = {
  icon: '✓', label: 'Done', color: '#16A34A', bg: 'rgba(22,163,74,0.1)',
  circleGradient: 'linear-gradient(145deg,#16A34A,#22C55E)', connectorColor: '#86EFAC',
}

function detectCategory(title: string, detail: string): string {
  const t = (title + ' ' + detail).toLowerCase()
  if (/serve|enjoy|eat|dish up|pile into|slurp|bowl time/.test(t))             return 'serve'
  if (/plate|arrange|garnish|top with|drizzle|scatter|finish with|sprinkle/.test(t)) return 'plate'
  if (/rest|stand|leave it|wait|resting|cover and/.test(t))                    return 'rest'
  if (/season|taste and adjust|salt and pepper|a pinch of|adjust with|flavour/.test(t)) return 'season'
  if (/whisk|mix|combine|stir|toss|blend|beat|fold|ladle/.test(t))             return 'mix'
  if (/heat|cook|fry|bake|boil|sear|roast|simmer|sauté|flame|oven|wok|pan/.test(t)) return 'heat'
  return 'prep'
}

// ─────────────────────────────────────────── text utilities

// Cooking technique terms to highlight
const TECHNIQUE_TERMS = [
  "Maillard reaction", "mise en place", "mantecatura", "wok hei",
  "all'onda", "al dente", "roux", "béchamel", "fond", "paillard",
  "beta-glucan", "deglaze", "bloom", "caramelise", "caramelisation",
  "emulsify", "blanching", "baste", "sauté", "julienne",
]

function highlightTechniques(text: string): React.ReactNode {
  const escaped = TECHNIQUE_TERMS.map((t) =>
    t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  )
  const pattern = new RegExp(`(${escaped.join('|')})`, 'gi')
  const parts = text.split(pattern)
  if (parts.length === 1) return text
  return (
    <>
      {parts.map((part, i) =>
        TECHNIQUE_TERMS.some((t) => t.toLowerCase() === part.toLowerCase()) ? (
          <span key={i} className="technique-term">{part}</span>
        ) : (
          part
        )
      )}
    </>
  )
}

/** Split detail into [action sentence, insight/science text] */
function splitDetail(detail: string): { action: string; insight: string } {
  // Find the end of the first sentence (. or ! or ?)
  const match = detail.match(/^(.+?[.!?])\s+(.+)$/s)
  if (!match) return { action: detail, insight: '' }
  return { action: match[1], insight: match[2] }
}

/** Extract the first time expression from text */
function extractTime(detail: string): string | null {
  const m = detail.match(/(\d+(?:[-–]\d+)?)\s*(minutes?|seconds?|mins?|secs?|hours?)/i)
  if (!m) return null
  const [, amount, unit] = m
  if (/sec/i.test(unit)) {
    const s = parseInt(amount)
    return s <= 90 ? `${s}s` : `${Math.round(s / 60)} min`
  }
  if (/hour/i.test(unit)) return `${amount}h`
  return `${amount} min`
}

// ─────────────────────────────────────────── sub-components

function CategoryBadge({ cat }: { cat: StepCategory }) {
  return (
    <span
      className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold"
      style={{ background: cat.bg, color: cat.color }}
    >
      <span className="text-sm leading-none">{cat.icon}</span>
      {cat.label}
    </span>
  )
}

function TimeChip({ time }: { time: string }) {
  return (
    <span className="step-time-chip">
      ⏱ {time}
    </span>
  )
}

// ─────────────────────────────────────────── step action GIF

/** Noto Animated Emoji codepoints — all served from fonts.gstatic.com */
const CATEGORY_GIF_CODE: Record<string, string> = {
  prep:   '1f52a',  // 🔪 kitchen knife
  heat:   '1f525',  // 🔥 fire
  mix:    '1f300',  // 🌀 cyclone / swirl
  season: '2728',   // ✨ sparkles
  rest:   '23f3',   // ⏳ hourglass not done
  plate:  '1f3a8',  // 🎨 artist palette
  serve:  '1f373',  // 🍳 cooking / pan
}
const DONE_GIF_CODE = '1f389'  // 🎉 party popper

function StepGif({ catKey, done }: { catKey: string; done: boolean }) {
  const [status, setStatus] = useState<'loading' | 'loaded' | 'error'>('loading')
  const code = done ? DONE_GIF_CODE : (CATEGORY_GIF_CODE[catKey] ?? '1f373')
  const url  = `https://fonts.gstatic.com/s/e/notoemoji/latest/${code}/512.gif`

  // re-trigger loading state when the GIF source changes (step checked/unchecked)
  const prevCode = useRef(code)
  useEffect(() => {
    if (prevCode.current !== code) {
      setStatus('loading')
      prevCode.current = code
    }
  }, [code])

  return (
    <div className="step-gif-wrap" aria-hidden="true">
      {status === 'loading' && <div className="step-gif-shimmer" />}
      {status === 'error' ? (
        <span className="step-gif-fallback">
          {done ? '✓' : (CATEGORIES[catKey]?.icon ?? '🍳')}
        </span>
      ) : (
        <img
          src={url}
          alt=""
          width={52}
          height={52}
          className={`step-gif ${status === 'loaded' ? 'step-gif--loaded' : ''}`}
          onLoad={() => setStatus('loaded')}
          onError={() => setStatus('error')}
        />
      )}
    </div>
  )
}

function InsightBox({ text }: { text: string }) {
  if (!text.trim()) return null
  return (
    <div className="step-insight-box">
      <div className="step-insight-icon">💡</div>
      <p className="step-insight-text">{highlightTechniques(text)}</p>
    </div>
  )
}

interface StepRowProps {
  step: RecipeStep
  index: number
  total: number
  done: boolean
  onToggle: () => void
}

function StepRow({ step, index, total, done, onToggle }: StepRowProps) {
  const catKey  = detectCategory(step.title, step.detail)
  const cat     = done ? DONE_CATEGORY : CATEGORIES[catKey]
  const time    = useMemo(() => extractTime(step.detail), [step.detail])
  const { action, insight } = useMemo(() => splitDetail(step.detail), [step.detail])
  const isLast  = index === total - 1

  return (
    <div className="step-row">
      {/* ── left: circle + connector ── */}
      <div className="step-left">
        <button
          className="step-circle-btn"
          style={{ background: cat.circleGradient }}
          onClick={onToggle}
          aria-label={done ? `Uncheck step ${step.step}` : `Check step ${step.step}`}
          title={done ? 'Click to uncheck' : 'Click to mark done'}
        >
          {done ? (
            <svg className="w-3.5 h-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={3}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
            </svg>
          ) : (
            <span className="text-sm font-bold">{step.step}</span>
          )}
        </button>

        {/* connecting line */}
        {!isLast && (
          <div
            className="step-connector"
            style={{
              background: done
                ? `linear-gradient(to bottom, ${cat.connectorColor}, ${CATEGORIES[catKey].connectorColor}88)`
                : 'linear-gradient(to bottom, rgba(0,0,0,0.1), rgba(0,0,0,0.03))',
            }}
          />
        )}
      </div>

      {/* ── right: card ── */}
      <div
        className={`step-card-new ${done ? 'step-card-new--done' : ''}`}
        onClick={onToggle}
        role="checkbox"
        aria-checked={done}
        tabIndex={0}
        onKeyDown={(e) => e.key === ' ' && (e.preventDefault(), onToggle())}
      >
        {/* card header row */}
        <div className="step-card-header-row">
          <div className="flex items-center gap-1.5 flex-wrap flex-1 min-w-0 pr-2">
            <CategoryBadge cat={done ? DONE_CATEGORY : CATEGORIES[catKey]} />
            {time && <TimeChip time={time} />}
            <h4 className={`step-card-title w-full ${done ? 'step-card-title--done' : ''}`}>
              {step.title}
            </h4>
          </div>
          <StepGif catKey={catKey} done={done} />
        </div>

        {/* action sentence */}
        <p className={`step-action-text ${done ? 'step-action-text--done' : ''}`}>
          {highlightTechniques(action)}
        </p>

        {/* insight / why it works */}
        {!done && insight && <InsightBox text={insight} />}

        {/* done state overlay hint */}
        {done && (
          <p className="text-xs text-herb-500 font-semibold mt-2 flex items-center gap-1">
            <svg className="w-3 h-3" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
              <path strokeLinecap="round" strokeLinejoin="round" d="M5 13l4 4L19 7" />
            </svg>
            Done! Tap to undo.
          </p>
        )}
      </div>
    </div>
  )
}

// ─────────────────────────────────────────── progress ring
function ProgressRing({ pct, size = 56 }: { pct: number; size?: number }) {
  const r = (size - 8) / 2
  const circ = 2 * Math.PI * r
  const offset = circ - (pct / 100) * circ
  return (
    <svg width={size} height={size} className="flex-shrink-0" style={{ transform: 'rotate(-90deg)' }}>
      <circle cx={size / 2} cy={size / 2} r={r} fill="none" stroke="#F3F4F6" strokeWidth={5} />
      <circle
        cx={size / 2} cy={size / 2} r={r}
        fill="none"
        stroke="url(#progressGrad)"
        strokeWidth={5}
        strokeLinecap="round"
        strokeDasharray={circ}
        strokeDashoffset={offset}
        style={{ transition: 'stroke-dashoffset 0.6s cubic-bezier(0.34,1.56,0.64,1)' }}
      />
      <defs>
        <linearGradient id="progressGrad" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%"   stopColor="#22C55E" />
          <stop offset="100%" stopColor="#86EFAC" />
        </linearGradient>
      </defs>
    </svg>
  )
}

// ─────────────────────────────────────────── accordion
const BADGE_ACCENT: Record<string, string> = {
  healthy: '#16A34A', comfort: '#BE185D', quick: '#D97706',
}

function Accordion({ title, children, accent }: { title: string; children: React.ReactNode; accent: string }) {
  const [open, setOpen] = useState(false)
  return (
    <div>
      <button className="accordion-trigger" onClick={() => setOpen((o) => !o)}>
        <span>{title}</span>
        <svg
          className={`accordion-chevron w-4 h-4 ${open ? 'accordion-chevron--open' : ''}`}
          fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}
          style={{ color: accent }}
        >
          <path strokeLinecap="round" strokeLinejoin="round" d="M19 9l-7 7-7-7" />
        </svg>
      </button>
      {open && <div className="accordion-content pt-3 pb-1 px-1">{children}</div>}
    </div>
  )
}

// ─────────────────────────────────────────── main component
interface Props {
  recipe: RecipeOption
  onBack: () => void
}

export default function RecipeDetail({ recipe, onBack }: Props) {
  const n       = recipe.instructions.length
  const accent  = BADGE_ACCENT[recipe.badge_type]
  const [checked, setChecked]   = useState<boolean[]>(Array(n).fill(false))
  const [confetti, setConfetti] = useState(false)

  const toggle = (i: number) =>
    setChecked((prev) => prev.map((v, idx) => (idx === i ? !v : v)))

  const doneCount = checked.filter(Boolean).length
  const allDone   = doneCount === n
  const pct       = n > 0 ? Math.round((doneCount / n) * 100) : 0

  useEffect(() => {
    if (allDone && n > 0) {
      setConfetti(true)
      const t = setTimeout(() => setConfetti(false), 2400)
      return () => clearTimeout(t)
    }
  }, [allDone, n])

  return (
    <>
      <Confetti active={confetti} />

      <div className="anim-slide-up">
        {/* back */}
        <button
          onClick={onBack}
          className="flex items-center gap-1.5 text-sm font-semibold mb-7 transition-all duration-200 group"
          style={{ color: accent }}
        >
          <svg className="w-4 h-4 transition-transform group-hover:-translate-x-0.5"
               fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2.5}>
            <path strokeLinecap="round" strokeLinejoin="round" d="M15 19l-7-7 7-7" />
          </svg>
          Back to recipe choices
        </button>

        {/* ── hero card ── */}
        <div className="glass rounded-2xl overflow-hidden mb-6">
          <div className="px-6 pt-5 pb-6"
               style={{ background: recipe.badge_type === 'healthy' ? 'rgba(220,252,231,0.55)' : recipe.badge_type === 'comfort' ? 'rgba(252,231,243,0.55)' : 'rgba(254,243,199,0.55)' }}>
            <span className={`badge-pill badge-pill--${recipe.badge_type} mb-4`}>{recipe.badge}</span>
            <div className="flex items-start gap-4">
              <span className="text-6xl flex-shrink-0" style={{ filter: 'drop-shadow(0 4px 8px rgba(0,0,0,0.1))' }}>{recipe.emoji}</span>
              <div>
                <h2 className="font-display font-bold text-espresso-900 leading-tight mb-1.5"
                    style={{ fontSize: 'clamp(1.3rem,3vw,1.8rem)' }}>
                  {recipe.title}
                </h2>
                <p className="text-sm text-gray-500 leading-relaxed">{recipe.description}</p>
              </div>
            </div>
          </div>
          <div className="px-6 py-3 flex flex-wrap gap-2"
               style={{ background: 'rgba(255,255,255,0.7)', borderTop: '1px solid rgba(255,255,255,0.7)' }}>
            {[`⏱ ${recipe.cooking_time}`, `👥 ${recipe.servings} servings`, `📊 ${recipe.difficulty}`].map((m) => (
              <span key={m} className="meta-chip">{m}</span>
            ))}
          </div>
        </div>

        {/* ── progress card ── */}
        <div className="glass rounded-2xl p-5 mb-6">
          <div className="flex items-center gap-4">
            {/* SVG ring */}
            <div className="relative flex-shrink-0">
              <ProgressRing pct={pct} size={60} />
              <div className="absolute inset-0 flex items-center justify-center">
                <span className="text-xs font-bold tabular-nums" style={{ color: accent }}>
                  {pct}%
                </span>
              </div>
            </div>

            {/* text */}
            <div className="flex-1">
              {allDone ? (
                <p className="font-display font-bold text-lg text-herb-500">
                  🎉 You did it — nicely cooked!
                </p>
              ) : (
                <>
                  <p className="font-semibold text-espresso-900 text-sm">Cooking progress</p>
                  <p className="text-xs text-gray-400 mt-0.5">
                    {doneCount > 0
                      ? `${doneCount} step${doneCount !== 1 ? 's' : ''} done · ${n - doneCount} to go`
                      : `${n} steps · tap each to check off`}
                  </p>
                </>
              )}
            </div>

            {/* step count chips */}
            <div className="hidden sm:flex gap-1 flex-wrap justify-end max-w-[120px]">
              {checked.map((d, i) => (
                <div
                  key={i}
                  className="w-3 h-3 rounded-sm transition-all duration-300"
                  style={{ background: d ? '#22C55E' : '#E5E7EB' }}
                  title={`Step ${i + 1}`}
                />
              ))}
            </div>
          </div>

          {/* bar */}
          <div className="progress-bar mt-4">
            <div className="progress-fill" style={{ width: `${pct}%` }} />
          </div>
        </div>

        {/* ── timeline steps ── */}
        <div className="glass rounded-2xl p-5 sm:p-6 mb-5">
          <div className="flex items-center justify-between mb-5">
            <h3 className="font-display font-bold text-espresso-900 text-xl">
              Cooking Steps
            </h3>
            <span className="text-xs text-gray-400">
              Tap any step to check it off
            </span>
          </div>

          {/* legend */}
          <div className="flex flex-wrap gap-1.5 mb-5 pb-4" style={{ borderBottom: '1px solid rgba(0,0,0,0.06)' }}>
            {Object.entries(CATEGORIES).map(([key, c]) => (
              <span
                key={key}
                className="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-medium"
                style={{ background: c.bg, color: c.color }}
              >
                <span className="text-xs">{c.icon}</span>
                {c.label}
              </span>
            ))}
          </div>

          {/* steps */}
          <div className="step-timeline">
            {recipe.instructions.map((step, i) => (
              <StepRow
                key={step.step}
                step={step}
                index={i}
                total={n}
                done={checked[i]}
                onToggle={() => toggle(i)}
              />
            ))}
          </div>
        </div>

        {/* ── accordions ── */}
        <div className="glass rounded-2xl p-5 flex flex-col gap-3">
          <Accordion title="💡 Chef's Pro Tips" accent={accent}>
            <ul className="flex flex-col gap-3 px-1">
              {recipe.pro_tips.map((tip, i) => (
                <li key={i} className="flex gap-3 items-start">
                  <span
                    className="w-5 h-5 rounded-full flex items-center justify-center text-xs font-bold flex-shrink-0 mt-0.5"
                    style={{ background: `${accent}22`, color: accent }}
                  >{i + 1}</span>
                  <span className="text-sm text-gray-600 leading-relaxed">{tip}</span>
                </li>
              ))}
            </ul>
          </Accordion>

          <Accordion title="🌱 Health Info" accent={accent}>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-5 px-1">
              <div>
                <p className="text-xs font-bold uppercase tracking-wider text-herb-500 mb-3">Benefits</p>
                <ul className="flex flex-col gap-2">
                  {recipe.health_notes.pros.map((p, i) => (
                    <li key={i} className="flex gap-2 items-start">
                      <span className="text-herb-500 mt-0.5 flex-shrink-0 text-sm">✓</span>
                      <span className="text-sm text-gray-600 leading-relaxed">{p}</span>
                    </li>
                  ))}
                </ul>
              </div>
              <div>
                <p className="text-xs font-bold uppercase tracking-wider text-amber-500 mb-3">Watch out for</p>
                <ul className="flex flex-col gap-2">
                  {recipe.health_notes.cons.map((c, i) => (
                    <li key={i} className="flex gap-2 items-start">
                      <span className="text-amber-400 mt-0.5 flex-shrink-0 text-sm">!</span>
                      <span className="text-sm text-gray-600 leading-relaxed">{c}</span>
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </Accordion>
        </div>
      </div>
    </>
  )
}
