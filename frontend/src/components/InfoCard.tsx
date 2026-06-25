interface Props {
  label: string
  value: string | number
  unit?: string
  colour?: string
}

export default function InfoCard({ label, value, unit, colour = '#F97316' }: Props) {
  return (
    <div className="bg-cream-50 rounded-xl p-4 text-center border border-amber-100">
      <p className="text-xs uppercase tracking-widest text-gray-400 mb-1">{label}</p>
      <p className="text-2xl font-bold" style={{ color: colour }}>
        {value}
        {unit && <span className="text-sm font-normal text-gray-400 ml-1">{unit}</span>}
      </p>
    </div>
  )
}
