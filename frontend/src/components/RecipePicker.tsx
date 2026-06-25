import { RecipeOption } from '../App'

interface Props {
  recipes: RecipeOption[]
  onSelect: (idx: number) => void
}

const ZONE_CLASS: Record<string, string> = {
  healthy: 'card-zone-healthy',
  comfort: 'card-zone-comfort',
  quick:   'card-zone-quick',
}

const ACCENT: Record<string, string> = {
  healthy: '#16A34A',
  comfort: '#BE185D',
  quick:   '#D97706',
}

function HealthLeaves({ rating }: { rating: number }) {
  return (
    <div className="flex gap-0.5" aria-label={`Health: ${rating}/5`}>
      {Array.from({ length: 5 }).map((_, i) => (
        <span
          key={i}
          className="text-sm"
          style={{ opacity: i < rating ? 1 : 0.2, filter: i < rating ? 'none' : 'grayscale(1)' }}
        >
          🌿
        </span>
      ))}
    </div>
  )
}

export default function RecipePicker({ recipes, onSelect }: Props) {
  return (
    <div className="mb-2">
      {/* section header */}
      <div className="mb-7">
        <h2
          className="font-display font-bold text-espresso-900 leading-tight"
          style={{ fontSize: 'clamp(1.6rem, 4vw, 2.25rem)' }}
        >
          Pick your recipe
        </h2>
        <p className="text-sm text-gray-400 mt-1">
          Three options — choose what feels right today.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-5">
        {recipes.map((recipe, idx) => (
          <button
            key={recipe.badge_type}
            onClick={() => onSelect(idx)}
            className="recipe-card anim-chip text-left"
            style={{ animationDelay: `${idx * 90}ms` }}
          >
            {/* ── gradient zone ── */}
            <div className={`${ZONE_CLASS[recipe.badge_type]} relative px-5 pt-5 pb-6`}>
              {/* badge */}
              <span className={`badge-pill badge-pill--${recipe.badge_type} mb-3`}>
                {recipe.badge}
              </span>
              {/* big emoji */}
              <div
                className="text-6xl mb-1 block"
                style={{
                  filter: 'drop-shadow(0 4px 8px rgba(0,0,0,0.12))',
                  animation: `float-food ${6 + idx}s ease-in-out infinite`,
                  animationDelay: `${idx * 0.8}s`,
                }}
                aria-hidden
              >
                {recipe.emoji}
              </div>
            </div>

            {/* ── content zone ── */}
            <div className="flex flex-col flex-1 px-5 pt-4 pb-5">
              {/* title */}
              <h3 className="font-display font-bold text-espresso-900 text-lg leading-snug mb-2">
                {recipe.title}
              </h3>

              {/* description */}
              <p
                className="text-sm leading-relaxed mb-4 flex-1"
                style={{ color: '#6B5E52', display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}
              >
                {recipe.description}
              </p>

              {/* meta */}
              <div className="flex flex-wrap gap-1.5 mb-4">
                <span className="meta-chip">⏱ {recipe.cooking_time}</span>
                <span className="meta-chip">👥 {recipe.servings}</span>
                <span className="meta-chip">📊 {recipe.difficulty}</span>
              </div>

              {/* health */}
              <div className="flex items-center justify-between mb-5">
                <HealthLeaves rating={recipe.health_rating} />
                <span className="text-xs font-semibold" style={{ color: ACCENT[recipe.badge_type] }}>
                  {recipe.health_label}
                </span>
              </div>

              {/* CTA */}
              <div
                className="w-full py-2.5 rounded-xl text-sm font-semibold text-center text-white transition-all duration-200"
                style={{
                  background: `linear-gradient(135deg, ${ACCENT[recipe.badge_type]}, ${ACCENT[recipe.badge_type]}CC)`,
                  boxShadow: `0 4px 14px ${ACCENT[recipe.badge_type]}44`,
                }}
              >
                Let's Cook This →
              </div>
            </div>
          </button>
        ))}
      </div>
    </div>
  )
}
