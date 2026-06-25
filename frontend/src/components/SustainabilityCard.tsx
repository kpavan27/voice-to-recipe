import { Sustainability } from '../App'

interface Props {
  sustainability: Sustainability
}

const RATING_COLOUR: Record<string, string> = {
  Excellent:          '#16A34A',
  Good:               '#65A30D',
  Fair:               '#D97706',
  'Needs Improvement':'#DC2626',
}

const LEAF_COUNT: Record<string, number> = {
  Excellent: 5, Good: 4, Fair: 3, 'Needs Improvement': 1,
}

export default function SustainabilityCard({ sustainability: s }: Props) {
  const colour = RATING_COLOUR[s.sustainability_rating] ?? '#D97706'
  const leaves = LEAF_COUNT[s.sustainability_rating] ?? 2

  const sorted = Object.entries(s.carbon_per_ingredient)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 5)

  const maxC = sorted[0]?.[1] ?? 1

  return (
    <div className="glass-warm rounded-2xl overflow-hidden">
      {/* header accent */}
      <div
        className="px-6 py-4"
        style={{ background: `${colour}14`, borderBottom: `1px solid ${colour}22` }}
      >
        <div className="flex items-center justify-between">
          <h3 className="font-display font-bold text-espresso-900 text-lg">🌱 Sustainability</h3>
          <span
            className="text-xs font-bold px-2.5 py-1 rounded-full"
            style={{ background: `${colour}20`, color: colour }}
          >
            {s.sustainability_rating}
          </span>
        </div>
      </div>

      <div className="px-6 py-5">
        {/* main metric */}
        <div className="flex items-end gap-3 mb-4">
          <span className="font-display font-bold text-5xl" style={{ color: colour }}>
            {s.total_carbon_kg_co2}
          </span>
          <div className="pb-1 text-sm text-gray-400 leading-tight">
            <div>kg CO₂</div>
            <div className="text-xs">avg {s.average_recipe_carbon_kg_co2} kg</div>
          </div>
        </div>

        {/* leaves */}
        <div className="flex items-center gap-2 mb-1">
          {Array.from({ length: 5 }).map((_, i) => (
            <span
              key={i}
              className="text-xl"
              style={{
                opacity: i < leaves ? 1 : 0.18,
                filter: i < leaves ? 'none' : 'grayscale(1)',
                transition: 'opacity 0.3s ease',
              }}
            >
              🍃
            </span>
          ))}
        </div>
        <p className="text-xs text-gray-400 mb-6">
          Saved&nbsp;
          <span className="font-semibold" style={{ color: colour }}>
            {s.carbon_saved_kg_co2} kg
          </span>
          &nbsp;vs average recipe
        </p>

        {/* per-ingredient bars */}
        {sorted.length > 0 && (
          <div className="flex flex-col gap-2.5">
            <p className="text-xs font-semibold uppercase tracking-wider text-gray-300 mb-0.5">
              By ingredient
            </p>
            {sorted.map(([ing, val]) => (
              <div key={ing} className="flex items-center gap-3 text-xs">
                <span className="w-20 text-gray-500 truncate capitalize font-medium">{ing}</span>
                <div className="flex-1 h-1.5 bg-gray-100 rounded-full overflow-hidden">
                  <div
                    className="h-full rounded-full transition-all duration-700"
                    style={{
                      width: `${(val / maxC) * 100}%`,
                      background: `linear-gradient(90deg, ${colour}, ${colour}88)`,
                    }}
                  />
                </div>
                <span className="w-10 text-right text-gray-400 font-mono">{val}</span>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
