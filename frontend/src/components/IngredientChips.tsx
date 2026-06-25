interface Props {
  ingredients: string[]
  emojis: Record<string, string>
}

export default function IngredientChips({ ingredients, emojis }: Props) {
  if (!ingredients.length) return null

  return (
    <div className="mb-8">
      <p className="text-xs font-semibold uppercase tracking-[0.14em] text-gray-300 mb-3">
        You've got these ingredients
      </p>
      <div className="flex flex-wrap gap-2">
        {ingredients.map((ing, i) => (
          <span
            key={ing}
            className="ing-chip anim-chip"
            style={{ animationDelay: `${i * 55}ms` }}
          >
            <span className="text-base leading-none">{emojis[ing] ?? '🍽️'}</span>
            <span className="capitalize">{ing}</span>
          </span>
        ))}
      </div>
    </div>
  )
}
