import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from 'recharts'
import { Nutrition } from '../App'

interface Props {
  nutrition: Nutrition
}

const MACROS = [
  { key: 'protein_g' as const, label: 'Protein', colour: '#F97316', icon: '💪' },
  { key: 'carbs_g'   as const, label: 'Carbs',   colour: '#F59E0B', icon: '⚡' },
  { key: 'fat_g'     as const, label: 'Fat',      colour: '#EC4899', icon: '🫀' },
]

export default function NutritionCard({ nutrition: n }: Props) {
  const data = MACROS
    .map((m) => ({ name: m.label, value: n[m.key], colour: m.colour }))
    .filter((d) => d.value > 0)

  return (
    <div className="glass-warm rounded-2xl overflow-hidden">
      {/* header accent */}
      <div
        className="px-6 py-4"
        style={{
          background: 'rgba(249,115,22,0.06)',
          borderBottom: '1px solid rgba(249,115,22,0.1)',
        }}
      >
        <div className="flex items-center justify-between">
          <h3 className="font-display font-bold text-espresso-900 text-lg">🥗 Nutrition</h3>
          <span
            className="text-xs font-bold px-2.5 py-1 rounded-full"
            style={{ background: 'rgba(249,115,22,0.12)', color: '#EA6C00' }}
          >
            Per serve
          </span>
        </div>
      </div>

      <div className="px-6 py-5">
        {/* kcal */}
        <div className="flex items-end gap-2 mb-5">
          <span
            className="font-display font-bold text-5xl"
            style={{
              background: 'linear-gradient(135deg, #F97316, #EA580C)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
            }}
          >
            {n.total_calories}
          </span>
          <span className="text-sm text-gray-400 pb-1">kcal total</span>
        </div>

        {/* donut */}
        {data.length > 0 && (
          <div className="h-40 mb-5">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={data}
                  cx="50%"
                  cy="50%"
                  innerRadius={42}
                  outerRadius={64}
                  paddingAngle={4}
                  dataKey="value"
                  animationBegin={0}
                  animationDuration={700}
                  strokeWidth={0}
                >
                  {data.map((entry) => (
                    <Cell key={entry.name} fill={entry.colour} />
                  ))}
                </Pie>
                <Tooltip
                  formatter={(v: number) => [`${v}g`, '']}
                  contentStyle={{
                    background: 'rgba(255,255,255,0.9)',
                    backdropFilter: 'blur(12px)',
                    border: '1px solid rgba(0,0,0,0.06)',
                    borderRadius: '0.75rem',
                    boxShadow: '0 8px 24px rgba(0,0,0,0.08)',
                    fontSize: '0.8rem',
                  }}
                />
              </PieChart>
            </ResponsiveContainer>
          </div>
        )}

        {/* macro chips */}
        <div className="grid grid-cols-3 gap-2.5">
          {MACROS.map(({ label, key, colour, icon }) => (
            <div
              key={label}
              className="rounded-xl p-3.5 text-center"
              style={{
                background: `${colour}0f`,
                border: `1.5px solid ${colour}22`,
              }}
            >
              <div className="text-lg mb-0.5">{icon}</div>
              <p className="text-xs text-gray-400 font-medium mb-0.5">{label}</p>
              <p className="text-lg font-bold" style={{ color: colour }}>
                {n[key]}<span className="text-xs font-normal text-gray-400">g</span>
              </p>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
