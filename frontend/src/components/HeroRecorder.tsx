import { useRef, useState } from 'react'
import { RecipeData } from '../App'

type AppState = 'idle' | 'recording' | 'processing' | 'done' | 'error'

interface Props {
  appState: AppState
  setAppState: (s: AppState) => void
  onResult: (data: RecipeData) => void
  onError: (msg: string) => void
  onReset: () => void
}

const FLOAT_FOODS = [
  { em: '🍅', x: '8%',  y: '18%', dur: 6, delay: 0,   size: 'text-5xl', opacity: 0.22 },
  { em: '🧄', x: '18%', y: '65%', dur: 8, delay: 1.2, size: 'text-4xl', opacity: 0.18 },
  { em: '🥦', x: '82%', y: '20%', dur: 7, delay: 0.6, size: 'text-5xl', opacity: 0.2  },
  { em: '🍋', x: '88%', y: '60%', dur: 9, delay: 2,   size: 'text-4xl', opacity: 0.18 },
  { em: '🥕', x: '72%', y: '80%', dur: 6, delay: 1.8, size: 'text-4xl', opacity: 0.16 },
  { em: '🍗', x: '25%', y: '82%', dur: 7, delay: 0.9, size: 'text-4xl', opacity: 0.16 },
  { em: '🧅', x: '93%', y: '40%', dur: 8, delay: 2.4, size: 'text-3xl', opacity: 0.14 },
  { em: '🫑', x: '4%',  y: '45%', dur: 9, delay: 3,   size: 'text-3xl', opacity: 0.14 },
]

export default function HeroRecorder({ appState, setAppState, onResult, onError, onReset }: Props) {
  const [transcript, setTranscript] = useState('')
  const [recTime, setRecTime]       = useState(0)
  const mediaRecRef = useRef<MediaRecorder | null>(null)
  const chunksRef   = useRef<Blob[]>([])
  const timerRef    = useRef<number | null>(null)

  const isIdle       = appState === 'idle'
  const isRecording  = appState === 'recording'
  const isProcessing = appState === 'processing'
  const isDone       = appState === 'done'

  const startRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true })
      const mr = new MediaRecorder(stream)
      chunksRef.current = []
      mr.ondataavailable = (e) => chunksRef.current.push(e.data)
      mr.onstop = submitAudio
      mr.start()
      mediaRecRef.current = mr
      setAppState('recording')
      setRecTime(0)
      timerRef.current = window.setInterval(() => setRecTime((t) => t + 1), 1000)
    } catch {
      onError('Could not access microphone. Please check permissions.')
    }
  }

  const stopRecording = () => {
    mediaRecRef.current?.stop()
    if (timerRef.current) clearInterval(timerRef.current)
    setAppState('processing')
  }

  const submitAudio = async () => {
    const blob = new Blob(chunksRef.current, { type: 'audio/webm' })
    const fd   = new FormData()
    fd.append('file', new File([blob], 'recording.webm', { type: 'audio/webm' }))
    try {
      const res = await fetch('/api/process-voice', { method: 'POST', body: fd })
      if (!res.ok) {
        const err = await res.json()
        throw new Error(err.detail || 'Unknown error')
      }
      const data: RecipeData = await res.json()
      setTranscript(data.original_text)
      onResult(data)
    } catch (e: unknown) {
      onError(e instanceof Error ? e.message : 'Request failed')
    }
  }

  const trySample = async () => {
    setAppState('processing')
    try {
      const res = await fetch('/api/sample')
      if (!res.ok) throw new Error('Sample request failed')
      const data: RecipeData = await res.json()
      setTranscript(data.original_text)
      onResult(data)
    } catch (e: unknown) {
      onError(e instanceof Error ? e.message : 'Request failed')
    }
  }

  const fmt = (s: number) => `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`

  return (
    <section className="relative min-h-[480px] flex flex-col items-center justify-center py-16 text-center overflow-hidden">
      {/* floating food emojis */}
      <div aria-hidden className="absolute inset-0 pointer-events-none select-none">
        {FLOAT_FOODS.map((f, i) => (
          <span
            key={i}
            className={`absolute ${f.size}`}
            style={{
              left: f.x,
              top: f.y,
              opacity: f.opacity,
              animation: `float-food ${f.dur}s ease-in-out infinite`,
              animationDelay: `${f.delay}s`,
            }}
          >
            {f.em}
          </span>
        ))}
      </div>

      {/* eyebrow */}
      <div className="relative z-10 mb-5">
        <span
          className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-sm font-medium"
          style={{
            background: 'rgba(254, 243, 199, 0.8)',
            border: '1px solid rgba(252, 211, 77, 0.4)',
            color: '#92400E',
            backdropFilter: 'blur(8px)',
          }}
        >
          <span className="w-1.5 h-1.5 rounded-full bg-saffron-500 animate-pulse" />
          AI-powered voice-to-recipe
        </span>
      </div>

      {/* headline */}
      <div className="relative z-10 mb-4 px-4">
        <h1
          className="font-display font-bold text-espresso-900 leading-[1.05] tracking-tight"
          style={{ fontSize: 'clamp(2.8rem, 7vw, 5rem)' }}
        >
          What's in your
          <span
            className="block"
            style={{
              background: 'linear-gradient(135deg, #F97316 0%, #EA580C 50%, #DC2626 100%)',
              WebkitBackgroundClip: 'text',
              WebkitTextFillColor: 'transparent',
              backgroundClip: 'text',
            }}
          >
            kitchen?
          </span>
        </h1>
        <p className="mt-4 text-gray-400 text-lg max-w-md mx-auto leading-relaxed">
          Speak your ingredients. Get three recipe choices.
          Discover your carbon footprint.
        </p>
      </div>

      {/* mic area */}
      <div className="relative z-10 flex flex-col items-center gap-5 mt-4">
        {/* steam wisps when processing */}
        {isProcessing && (
          <div aria-hidden className="absolute -top-10 left-1/2 -translate-x-1/2 flex gap-2.5">
            {[0, 1, 2, 3].map((i) => (
              <span
                key={i}
                className="text-2xl"
                style={{ animation: `steam-rise 2.2s ease-out infinite`, animationDelay: `${i * 0.45}s` }}
              >
                〰️
              </span>
            ))}
          </div>
        )}

        {/* mic / processing / done button */}
        {!isDone && !isProcessing && (
          <div className="relative">
            {isRecording && (
              <>
                <div className="pulse-ring" />
                <div className="pulse-ring-2" />
              </>
            )}
            <button
              onClick={isRecording ? stopRecording : startRecording}
              className={`mic-btn ${isRecording ? 'mic-btn--recording' : 'mic-btn--idle'}`}
              aria-label={isRecording ? 'Stop recording' : 'Start recording'}
            >
              {isRecording ? '⏹' : '🎤'}
            </button>
          </div>
        )}

        {isProcessing && (
          <div className="relative">
            <div
              className="w-28 h-28 rounded-full flex items-center justify-center text-4xl text-white"
              style={{
                background: 'linear-gradient(145deg, #FB923C, #F97316)',
                boxShadow: '0 12px 40px rgba(249,115,22,0.45)',
              }}
            >
              <span style={{ display: 'inline-block', animation: 'spin-slow 1.8s linear infinite' }}>
                🥄
              </span>
            </div>
          </div>
        )}

        {isDone && (
          <button
            onClick={onReset}
            className="flex items-center gap-2 px-7 py-3.5 rounded-2xl text-white font-semibold text-sm transition-all duration-300 hover:scale-105 active:scale-95"
            style={{
              background: 'linear-gradient(135deg, #F97316, #EA6C00)',
              boxShadow: '0 8px 24px rgba(249,115,22,0.35)',
            }}
          >
            🔄 New Recording
          </button>
        )}

        {/* label */}
        {isIdle && (
          <p className="text-sm text-gray-400 mt-1">Tap to start speaking</p>
        )}

        {isProcessing && (
          <p className="text-saffron-600 font-medium text-sm animate-pulse">
            Cooking up your recipes…
          </p>
        )}

        {/* waveform */}
        {isRecording && (
          <div className="flex items-center gap-1 h-10 mt-1" aria-hidden>
            {Array.from({ length: 11 }).map((_, i) => (
              <div
                key={i}
                className="wave-bar"
                style={{
                  height: '8px',
                  animationDelay: `${i * 0.09}s`,
                  animationDuration: `${0.75 + (i % 4) * 0.15}s`,
                }}
              />
            ))}
            <span className="ml-3 text-sm font-semibold text-red-500 tabular-nums">
              {fmt(recTime)}
            </span>
          </div>
        )}
      </div>

      {/* transcript */}
      {transcript && isDone && (
        <div
          className="relative z-10 mt-6 inline-flex items-center gap-2 px-4 py-2 rounded-full text-sm text-gray-400 italic"
          style={{
            background: 'rgba(255,255,255,0.5)',
            border: '1px solid rgba(0,0,0,0.06)',
            backdropFilter: 'blur(8px)',
          }}
        >
          🎤 I heard: &ldquo;{transcript}&rdquo;
        </div>
      )}

      {/* sample link */}
      {isIdle && (
        <button
          onClick={trySample}
          className="relative z-10 mt-5 text-sm font-medium transition-colors duration-200"
          style={{ color: '#F97316' }}
          onMouseOver={(e) => (e.currentTarget.style.color = '#EA6C00')}
          onMouseOut={(e) => (e.currentTarget.style.color = '#F97316')}
        >
          ✨ Try a sample — no mic needed
        </button>
      )}
    </section>
  )
}
