import { useState } from 'react'
import Header from './components/Header'
import HeroRecorder from './components/HeroRecorder'
import IngredientChips from './components/IngredientChips'
import RecipePicker from './components/RecipePicker'
import RecipeDetail from './components/RecipeDetail'
import SustainabilityCard from './components/SustainabilityCard'
import NutritionCard from './components/NutritionCard'

// ─────────────────────────────────────────────────────── types
export interface RecipeStep {
  step: number
  title: string
  detail: string
}

export interface RecipeOption {
  title: string
  emoji: string
  badge: string
  badge_type: 'healthy' | 'comfort' | 'quick'
  description: string
  cooking_time: string
  servings: number
  difficulty: string
  health_rating: number
  health_label: string
  instructions: RecipeStep[]
  pro_tips: string[]
  health_notes: { pros: string[]; cons: string[] }
}

export interface Nutrition {
  total_calories: number
  protein_g: number
  carbs_g: number
  fat_g: number
}

export interface Sustainability {
  total_carbon_kg_co2: number
  average_recipe_carbon_kg_co2: number
  carbon_saved_kg_co2: number
  sustainability_rating: string
  carbon_per_ingredient: Record<string, number>
  nutrition: Nutrition
}

export interface RecipeData {
  original_text: string
  extracted_ingredients: string[]
  ingredient_emojis: Record<string, string>
  recipes: RecipeOption[]
  sustainability: Sustainability
}

type AppState = 'idle' | 'recording' | 'processing' | 'done' | 'error'

// ─────────────────────────────────────────────────────── app
export default function App() {
  const [appState, setAppState]                     = useState<AppState>('idle')
  const [data, setData]                             = useState<RecipeData | null>(null)
  const [errorMsg, setErrorMsg]                     = useState<string>('')
  const [selectedRecipeIdx, setSelectedRecipeIdx]   = useState<number | null>(null)

  const reset = () => {
    setData(null)
    setErrorMsg('')
    setAppState('idle')
    setSelectedRecipeIdx(null)
  }

  const handleResult = (result: RecipeData) => {
    setData(result)
    setSelectedRecipeIdx(null)
    setAppState('done')
  }

  const handleError = (msg: string) => {
    setErrorMsg(msg)
    setAppState('error')
  }

  return (
    <div className="relative min-h-screen" style={{ backgroundColor: '#FFFBF5' }}>
      {/* ── ambient background orbs ── */}
      <div aria-hidden className="pointer-events-none">
        <div className="bg-orb bg-orb-1" />
        <div className="bg-orb bg-orb-2" />
        <div className="bg-orb bg-orb-3" />
      </div>

      {/* ── content ── */}
      <div className="relative z-10">
        <Header />

        <main className="max-w-5xl mx-auto px-4 pb-20">
          <HeroRecorder
            appState={appState}
            setAppState={setAppState}
            onResult={handleResult}
            onError={handleError}
            onReset={reset}
          />

          {/* Error */}
          {appState === 'error' && (
            <div className="mt-6 glass rounded-2xl p-5 border-red-200 anim-slide-up">
              <p className="font-semibold text-red-700">Something went wrong</p>
              <p className="text-sm mt-1 text-red-500">{errorMsg}</p>
              <button
                onClick={reset}
                className="mt-3 text-sm text-red-500 underline hover:no-underline"
              >
                Try again
              </button>
            </div>
          )}

          {/* Results */}
          {data && appState === 'done' && (
            <div className="mt-10">
              <div className="anim-slide-up" style={{ animationDelay: '0ms' }}>
                <IngredientChips
                  ingredients={data.extracted_ingredients}
                  emojis={data.ingredient_emojis}
                />
              </div>

              <div className="anim-slide-up" style={{ animationDelay: '80ms' }}>
                {selectedRecipeIdx === null ? (
                  <RecipePicker
                    recipes={data.recipes}
                    onSelect={setSelectedRecipeIdx}
                  />
                ) : (
                  <RecipeDetail
                    recipe={data.recipes[selectedRecipeIdx]}
                    onBack={() => setSelectedRecipeIdx(null)}
                  />
                )}
              </div>

              <div
                className="grid grid-cols-1 lg:grid-cols-2 gap-6 mt-8 anim-slide-up"
                style={{ animationDelay: '160ms' }}
              >
                <SustainabilityCard sustainability={data.sustainability} />
                <NutritionCard nutrition={data.sustainability.nutrition} />
              </div>
            </div>
          )}
        </main>

        <footer className="relative z-10 text-center py-8 text-sm text-gray-300 border-t border-amber-50">
          <span className="font-display text-base text-amber-200">🍳 VoiceChef</span>
          <span className="mx-3 text-gray-200">·</span>
          Speak ingredients. Pick a recipe. Know your footprint.
        </footer>
      </div>
    </div>
  )
}
