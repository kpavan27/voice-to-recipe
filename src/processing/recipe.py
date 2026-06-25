"""Recipe generation — 15 world cuisines, three options per query (healthy, comfort, quick)."""
from typing import Any, Dict, List, Tuple


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

_BADGE_LABELS: Dict[str, str] = {
    "healthy": "🌿 Healthy Choice",
    "comfort": "💕 Comfort Food",
    "quick": "⚡ Quick & Fast",
}


def _r(data: tuple) -> Dict[str, Any]:
    """Convert raw tuple (title,emoji,badge_type,desc,time,servings,diff,hr,hl,steps,tips,pros,cons) to recipe dict."""
    title, emoji, badge_type, desc, time, servings, diff, hr, hl, steps, tips, pros, cons = data
    return {
        "title": title,
        "emoji": emoji,
        "badge": _BADGE_LABELS[badge_type],
        "badge_type": badge_type,
        "description": desc,
        "cooking_time": time,
        "servings": servings,
        "difficulty": diff,
        "health_rating": hr,
        "health_label": hl,
        "instructions": [{"step": s[0], "title": s[1], "detail": s[2]} for s in steps],
        "pro_tips": list(tips),
        "health_notes": {"pros": list(pros), "cons": list(cons)},
    }


# ---------------------------------------------------------------------------
# Raw cuisine data  (title, emoji, badge_type, desc, time, servings, diff,
#                   health_rating, health_label, steps, tips, pros, cons)
# ---------------------------------------------------------------------------

_RAW: Dict[str, List[tuple]] = {}

_RAW['italian'] = [('Light Pasta Primavera',
  '🍝',
  'healthy',
  'A vibrant celebration of seasonal vegetables tossed with linguine, golden olive oil, bright lemon zest and a '
  'snowfall of parmesan. This dish proves that eating well never has to mean sacrificing flavour or satisfaction!',
  '30 minutes',
  4,
  'Easy',
  4,
  'Nutritious & Light',
  [(1,
    'Salt the water generously',
    'Bring a large pot of water to a rolling boil and season it as salty as the sea. Well-salted pasta water is your '
    'first and most important seasoning layer, flavouring the pasta from the inside out as it cooks.'),
   (2,
    'Cook the linguine al dente',
    'Add the linguine and cook 1–2 minutes less than the packet suggests. Al dente pasta (with a tiny bite at the '
    'centre) will finish cooking in the pan, absorbing the sauce beautifully rather than turning mushy.'),
   (3,
    'Sauté garlic and vegetables',
    'Warm olive oil in a wide pan over medium heat and gently cook sliced garlic until fragrant but not coloured. Add '
    'your seasonal vegetables and sauté until just tender-crisp, preserving both colour and nutrients.'),
   (4,
    'Reserve pasta water',
    'Before draining, ladle out a full cup of the starchy cooking water — this liquid gold is full of dissolved starch '
    'that will act as a natural emulsifier, binding oil and water into a silky, clingy sauce.'),
   (5,
    'Toss and emulsify',
    'Add the drained pasta to the pan and splash in pasta water a little at a time, tossing vigorously. The agitation '
    'combined with the starch creates an emulsion that coats every strand of pasta luxuriously.'),
   (6,
    'Add lemon zest and parmesan',
    'Remove from the heat and stir in lemon zest and freshly grated parmesan. Finishing off the heat prevents the '
    'cheese from clumping and keeps the zest aromas bright and floral rather than cooked-out.'),
   (7,
    'Garnish and serve',
    'Scatter fresh basil leaves, an extra grating of parmesan and a drizzle of your best olive oil. Serve immediately '
    'in warmed bowls so the sauce stays fluid and the pasta maintains that perfect al dente texture.')],
  ['🧂 Salt your pasta water until it tastes pleasantly salty — under-seasoned water produces bland pasta no sauce can '
   'fix.',
   '🍦 Always save pasta water before draining — its starch is the secret to a glossy, restaurant-quality sauce.',
   '🌿 Use the freshest seasonal vegetables you can find — primavera means spring, so let the season inspire you.'],
  ['Linguine provides complex carbohydrates for sustained energy.',
   'A generous portion of vegetables delivers fibre, vitamins and antioxidants.',
   'Extra-virgin olive oil contributes heart-healthy monounsaturated fats.'],
  ['Parmesan adds sodium, so taste before adding extra salt at the table.',
   'Portion size matters — pasta can be calorie-dense if served in large quantities.']),
 ('Creamy Mushroom Risotto',
  '🍚',
  'comfort',
  'A soul-warming pot of Arborio rice slow-coaxed with porcini mushrooms, white wine and aged parmesan, finished with '
  'a generous mantecatura of cold butter. Every spoonful is deeply savoury, impossibly creamy and completely '
  'irresistible!',
  '45 minutes',
  4,
  'Medium',
  2,
  'Indulgent Treat',
  [(1,
    'Warm the stock',
    'Keep your chicken or vegetable stock at a gentle simmer in a separate saucepan. Adding cold stock to the rice '
    'would shock it, slowing starch release and producing an uneven, gluey texture instead of a flowing, wave-like '
    'consistency.'),
   (2,
    'Sauté shallots until translucent',
    'Melt butter in a heavy-bottomed pan and sweat finely diced shallots over medium-low heat until soft and '
    'translucent but not coloured. Shallots are milder and sweeter than onions, providing an elegant base that will '
    'not overpower the delicate rice.'),
   (3,
    'Toast the Arborio rice',
    'Add the dry Arborio rice and stir for 2 minutes until each grain turns chalky-white and slightly translucent at '
    'the edges. This toasting step coats the starch granules in fat, helping them release their starch gradually for '
    'that signature creamy texture.'),
   (4,
    'Add the white wine',
    'Pour in a generous splash of dry white wine and stir until completely absorbed. The alcohol carries aromatic '
    'compounds deep into the rice, adding acidity that will balance the richness of the finished dish.'),
   (5,
    'Add stock ladle by ladle',
    'Add warm stock one ladle at a time, stirring constantly and waiting for each addition to be absorbed before '
    'adding the next. This patient, rhythmic stirring coaxes the surface starch off the grains, creating the '
    'characteristic oozy creaminess of a great risotto.'),
   (6,
    'Mantecatura — beat in butter and parmesan',
    'Remove from heat and vigorously beat in cold cubed butter and finely grated parmesan. This technique, called '
    'mantecatura, creates an emulsion between the butter fat and the starchy cooking liquid, producing a glossy, '
    'velvety finish.'),
   (7,
    'Rest and serve',
    'Cover and rest for 2 minutes before serving. This brief rest allows the emulsion to stabilise and the temperature '
    'to even out, so the risotto flows like lava when ladled into warmed bowls — the hallmark of perfect consistency.'),
   (8,
    'Finish and garnish',
    'Spoon into warmed deep bowls, tap the base to spread, and top with sautéed mushrooms, a ribbon of parmesan and a '
    'drizzle of truffle oil if you have it. Serve at once before the risotto tightens as it cools.')],
  ['🍾 Keep your stock warm — adding cold stock shocks the rice and disrupts starch release.',
   '🧈 Cold butter for mantecatura is essential — the temperature difference creates the emulsion.',
   '🍄 Rehydrate dried porcini in warm water and add the strained soaking liquid as part of your stock for deeper '
   'umami.'],
  ['Arborio rice provides a satisfying source of carbohydrates that keep you full.',
   'Mushrooms contribute B vitamins, selenium and immune-supporting beta-glucans.',
   'A moderate serving is deeply satisfying, helping to prevent overeating later.'],
  ['Butter and parmesan make this a high-fat, calorie-dense dish best enjoyed occasionally.',
   'The refined carbohydrates in white Arborio rice can spike blood sugar quickly.']),
 ('Aglio e Olio Spaghetti',
  '🍝',
  'quick',
  'The Roman classic — just spaghetti, golden garlic, good olive oil, chilli and parsley — proves that genius '
  'simplicity is the highest form of Italian cooking. Ready in a flash and tasting absolutely spectacular!',
  '15 minutes',
  2,
  'Easy',
  3,
  'Balanced & Quick',
  [(1,
    'Boil spaghetti in well-salted water',
    'Cook spaghetti in aggressively salted boiling water until 1 minute shy of al dente. You want it slightly '
    'underdone here because it will finish cooking in the garlic oil, absorbing all that flavour directly.'),
   (2,
    'Slowly golden the garlic in olive oil',
    'While the pasta cooks, gently warm plenty of extra-virgin olive oil in a wide pan and add thinly sliced garlic '
    'over low heat. Patience is everything — slowly golden garlic is nutty and sweet, while burnt garlic is '
    'unforgivably bitter.'),
   (3,
    'Add chilli flakes',
    'Once the garlic is lightly golden, add a pinch of dried chilli flakes and let them bloom in the oil for 30 '
    'seconds. Heat activates the capsaicin compounds, making the warmth permeate the entire sauce rather than sitting '
    'in isolated hot pockets.'),
   (4,
    'Toss pasta with pasta water',
    'Add the drained pasta and a splash of starchy pasta water to the pan, tossing energetically over medium heat. The '
    'starch emulsifies the oil and water into a glossy, light coating that clings to every strand.'),
   (5,
    'Finish with parsley',
    'Off the heat, toss in a generous handful of freshly chopped flat-leaf parsley. Adding it off the heat preserves '
    'the bright green colour and fresh, grassy flavour that would be lost if cooked.'),
   (6,
    'Serve immediately',
    'Twirl into warmed bowls and eat at once — aglio e olio waits for no one and is at its silky best the moment it '
    'leaves the pan. A final drizzle of raw olive oil adds a peppery freshness.')],
  ['🧄 Slice garlic thinly and evenly so it all colours at the same rate — uneven pieces mean some burn while others '
   'are still raw.',
   '🟡 Use your best olive oil here — with so few ingredients, quality is everything you taste.',
   '🌿 Add a squeeze of lemon at the end to lift all the flavours and add a welcome brightness.'],
  ['Olive oil provides heart-healthy monounsaturated fats and powerful antioxidants.',
   'Garlic contains allicin, a compound with anti-inflammatory and immune-boosting properties.',
   'A simple, minimally processed dish with no hidden sugars or additives.'],
  ['High in refined carbohydrates from white spaghetti — swap for wholemeal for more fibre.',
   'Generous olive oil makes this calorie-dense despite its light appearance.'])]


_RAW['japanese'] = [('Teriyaki Salmon Bowl',
  '🐟',
  'healthy',
  'A showstopping bowl of soy-mirin glazed salmon over nutty brown rice with edamame, cool cucumber and toasted '
  'sesame. Every bite delivers that perfect balance of sweet-savoury glaze, omega-rich salmon and nourishing '
  'wholegrains!',
  '25 minutes',
  2,
  'Easy',
  5,
  'Super Nutritious',
  [(1,
    'Cook the brown rice',
    'Rinse brown rice until the water runs clear, then cook in a 1:2 ratio with water for about 40 minutes. Brown rice '
    'takes longer than white but rewards you with a nutty flavour, more fibre and a lower glycaemic index that '
    'sustains energy far longer throughout the day.'),
   (2,
    'Make the teriyaki glaze',
    'Combine soy sauce, mirin and a little honey in a small pan and simmer until lightly syrupy. The sugar in the '
    'mirin undergoes caramelisation when it hits the hot pan, creating that characteristic lacquered glaze with deep, '
    'complex sweetness that makes teriyaki so irresistible.'),
   (3,
    'Sear the salmon skin-side down',
    'Place salmon fillets skin-side down in a hot, lightly oiled pan over medium-high heat for 4 minutes. Starting '
    'skin-side down renders the fat from the skin, making it crisp and delicious while protecting the delicate flesh '
    'from direct heat.'),
   (4,
    'Glaze and flip',
    'Spoon the teriyaki glaze over the salmon and flip for a final 2 minutes. The Maillard reaction between the '
    'protein and sugars in the glaze creates hundreds of flavour compounds, producing that irresistible caramelised '
    'crust you see in Japanese restaurants.'),
   (5,
    'Blanch the edamame',
    'Boil edamame in salted water for 3–4 minutes then refresh in ice water. The ice bath immediately halts cooking, '
    'locking in a vibrant green colour and a pleasantly firm, popping texture rather than a soft, overcooked one.'),
   (6,
    'Slice the cucumber',
    'Thinly slice cucumber on the diagonal and toss with a tiny pinch of salt and rice vinegar. The salt draws out '
    'excess water and the vinegar adds a gentle tang that contrasts beautifully with the rich, savoury salmon.'),
   (7,
    'Assemble the bowl',
    'Arrange brown rice in the base of a bowl and top with glazed salmon, edamame and cucumber, then scatter sesame '
    'seeds. A bowl format means every forkful is a different combination of textures and flavours, making eating a '
    'genuinely joyful experience.')],
  ['🐟 Pat salmon completely dry before searing — surface moisture creates steam that prevents a gorgeous caramelised '
   'crust from forming.',
   '🍚 Use day-old brown rice if possible — slightly drier grains absorb the glaze more readily and have a better bowl '
   'texture.',
   '🌿 Add a drizzle of sesame oil at the end — its toasty, nutty flavour ties all the bowl components together '
   'beautifully.'],
  ['Salmon is one of the richest dietary sources of omega-3 fatty acids, supporting brain and heart health.',
   'Brown rice provides fibre, B vitamins and a sustained energy release unlike refined white rice.',
   'Edamame delivers plant-based protein and isoflavones with anti-inflammatory properties.'],
  ['Soy sauce is high in sodium — use reduced-sodium varieties and taste before adding extra seasoning.',
   'The glaze contains added sugar — use in moderation if managing blood glucose levels.']),
 ('Tonkotsu-Style Ramen',
  '🍜',
  'comfort',
  'A deeply satisfying bowl of rich pork bone broth, springy ramen noodles, melt-in-the-mouth chashu pork and a '
  'custard-centred marinated egg. This is Japanese comfort food at its most soul-warming and spectacular!',
  '50 minutes',
  2,
  'Medium',
  2,
  'Indulgent Treat',
  [(1,
    'Simmer the pork broth',
    'Place pork bones in cold water, bring to a boil, discard the water, rinse bones, then simmer in fresh water for '
    'at least 4 hours. This blanching step removes blood and impurities, leaving a cleaner, milky-white broth rich in '
    'collagen that will set to a jelly when cooled.'),
   (2,
    'Prepare the chashu pork',
    'Roll pork belly tightly, tie with twine, and braise in soy, mirin, sake and sugar for 90 minutes. The gentle heat '
    'slowly breaks down the collagen in the pork belly into gelatin, creating that melt-in-the-mouth texture and a '
    'glossy, deeply savoury coating.'),
   (3,
    'Marinate the soft-boiled eggs',
    'Soft-boil eggs for exactly 6 minutes, cool in ice water, peel, then marinate in equal parts soy and mirin '
    'overnight. The slightly runny yolk absorbs the marinade from the edges inward, creating those beautiful '
    'gradient-coloured, custard-centred ramen eggs.'),
   (4,
    'Season the broth',
    'Stir in miso paste or tare to taste and adjust with soy and salt. Seasoning only at the end preserves the '
    'delicate fermented complexity of miso, which degrades with prolonged high-heat cooking.'),
   (5,
    'Cook the ramen noodles',
    'Cook fresh ramen noodles in a separate pot of boiling water for 2–3 minutes, drain and divide into bowls. Cooking '
    'noodles separately prevents their starch from clouding your precious broth and keeps their springy, alkaline '
    'texture intact.'),
   (6,
    'Assemble the bowl',
    'Ladle the rich, piping-hot broth over the noodles and arrange chashu slices, a halved marinated egg and a sheet '
    'of nori. The presentation is part of the ritual — ramen is Japan’s most beloved comfort food and deserves to look '
    'as beautiful as it tastes.'),
   (7,
    'Add toppings',
    'Finish with sliced spring onion, sesame seeds and a drizzle of chilli oil. Each topping adds a layer of flavour '
    'and texture, from the fresh bite of spring onion to the heat of chilli oil, making every bowl a personalised '
    'experience.'),
   (8,
    'Savour immediately',
    'Ramen waits for nobody — eat it while the broth is blazing hot and the noodles are still springy. Slurping is '
    'encouraged in Japan, as it aerates the broth and sends aromatic steam to your nose, enhancing the eating '
    'experience.')],
  ['🥩 Pork belly needs to be fully submerged in braising liquid — weigh it down with a cartouche or small plate.',
   '🥚 Marinate the eggs for at least 4 hours but no more than 24 — over-marinating makes the whites rubbery and the '
   'yolk too salty.',
   '🍜 Make the broth a day ahead — chilling it overnight lets you lift off the solidified fat easily for a cleaner '
   'bowl.'],
  ['Pork bone broth is rich in collagen and gelatin, supporting joint health and gut lining.',
   'Nori provides iodine, which is essential for healthy thyroid function.',
   'A deeply satisfying, protein-rich meal that genuinely keeps hunger at bay for hours.'],
  ['Ramen broth is very high in sodium — drink the broth in moderation if watching salt intake.',
   'Pork belly and chashu are high in saturated fat, making this a treat rather than an everyday meal.']),
 ('Miso Soup & Onigiri',
  '🍙',
  'quick',
  'A deeply comforting Japanese classic — silky dashi miso soup with tofu and wakame alongside perfectly shaped '
  'nori-wrapped rice balls. This nourishing duo has sustained Japan for centuries and is ready in under 15 minutes!',
  '15 minutes',
  2,
  'Easy',
  4,
  'Light & Nourishing',
  [(1,
    'Dissolve the dashi and miso',
    'Bring dashi stock to a gentle simmer and whisk in miso paste off the heat. Never boil miso soup once the miso is '
    'added — heat destroys the probiotic bacteria and volatile aromatic compounds that give miso its distinctive, '
    'fermented depth.'),
   (2,
    'Add tofu and wakame',
    'Gently slide cubed silken tofu and rehydrated wakame seaweed into the warm broth. Silken tofu is incredibly '
    'delicate and needs only a minute or two to warm through — stirring vigorously will break it into unattractive '
    'chunks.'),
   (3,
    'Cook the sushi rice',
    'Rinse sushi rice several times until the water runs clear, then cook and season with rice vinegar, sugar and salt '
    'while still warm. The starch washed away during rinsing is what would otherwise make your rice gluey — clean rice '
    'grains stick together from their own surface starch alone.'),
   (4,
    'Shape the onigiri',
    'Wet your hands with salted water and shape warm rice into triangles or balls around a filling of your choice. The '
    'salt on your hands seasons the outside of the onigiri, and warm rice is much easier to shape — cold rice will '
    'crumble and refuse to hold together.'),
   (5,
    'Wrap with nori',
    'Press a strip of nori around the base of each onigiri just before serving. Nori should be added just before '
    'eating if crispness is desired, or wrapped in advance if you prefer a softer, more integrated texture where the '
    'seaweed becomes part of the rice.'),
   (6,
    'Serve together',
    'Ladle the miso soup into small bowls and arrange the onigiri on a plate. This simple, nourishing combination has '
    'been a Japanese staple for centuries — the umami-rich broth and the satisfying rice parcel make a perfectly '
    'balanced, restorative meal at any hour.')],
  ['🧆 Never boil miso once added to the soup — a brief, gentle warm is all it needs to preserve its complex fermented '
   'character.',
   '🍙 Keep hands damp and lightly salted when shaping onigiri — this prevents sticking and adds a subtle seasoning to '
   'the outside.',
   '🥦 Add a pinch of sesame seeds and a few drops of sesame oil to the miso soup for extra flavour depth.'],
  ['Miso provides beneficial probiotics and B vitamins from its fermentation process.',
   'Rice is easily digestible and provides quick, clean energy without burdening the digestive system.',
   'Wakame seaweed is a rich plant source of iodine, calcium and omega-3 fatty acids.'],
  ['White sushi rice has a high glycaemic index — mix in some brown rice for extra fibre if desired.',
   'Miso broth is high in sodium, so those watching salt intake should enjoy in moderation.'])]


_RAW['indian'] = [('Yellow Dal Tadka',
  '🫘',
  'healthy',
  'A deeply nourishing pot of yellow lentils simmered with turmeric, then crowned with a sizzling tempering of cumin, '
  'garlic and dried chilli. This ancient, protein-rich dish is as comforting as it is wildly good for you!',
  '35 minutes',
  4,
  'Easy',
  5,
  'Incredibly Nutritious',
  [(1,
    'Rinse and soak the lentils',
    'Rinse yellow lentils (moong dal) until the water runs clear, then soak for 20 minutes. Soaking begins to break '
    'down phytic acid, an anti-nutrient that can interfere with mineral absorption, making the lentils both faster to '
    'cook and easier to digest.'),
   (2,
    'Simmer with turmeric',
    'Cover the lentils generously with water, add turmeric and a pinch of salt, and simmer for 20–25 minutes until '
    'completely soft. Turmeric’s curcumin is fat-soluble, so cooking it with a little ghee dramatically improves its '
    'absorption by your body.'),
   (3,
    'Blend to your preferred consistency',
    'Mash or partially blend the cooked lentils to your preferred texture — anywhere from chunky to silky smooth. Dal '
    'thickens significantly as it cools, so keep it slightly thinner than you want the final result to be.'),
   (4,
    'Prepare the tadka (tempering)',
    'Heat ghee in a small pan until it shimmers, then add cumin seeds and let them sizzle for 30 seconds until they '
    'pop and turn aromatic. This technique, called tadka, blooms the spices in fat, releasing oil-soluble flavour '
    'compounds that water-based cooking simply cannot extract.'),
   (5,
    'Add aromatics to the tadka',
    'Add garlic, dried chilli and a pinch of asafoetida to the hot ghee and cook for another minute. Asafoetida (hing) '
    'is a powerful digestive aid that also reduces the gas-causing compounds in lentils — a brilliant piece of '
    'culinary wisdom built into the recipe.'),
   (6,
    'Pour tadka over the dal',
    'Pour the sizzling, aromatic ghee mixture directly over the cooked dal with a satisfying hiss. That dramatic pour '
    'infuses the entire dal with concentrated spice flavour in a way that cooking spices directly into the lentils '
    'never achieves.'),
   (7,
    'Add tomatoes and finish',
    'Stir in chopped tomatoes, squeeze in a little lemon juice and simmer for 5 more minutes. The acidity from the '
    'tomatoes and lemon brightens all the earthy, warm flavours and adds a freshness that makes each spoonful sing.'),
   (8,
    'Garnish and serve',
    'Top with fresh cilantro and serve with warm rice or roti. The fresh herb added at the very end retains its '
    'volatile essential oils, adding a cool, herbal lift that perfectly contrasts the warm, earthy depth of the dal.')],
  ['🧂 Season generously — lentils absorb a surprising amount of salt, so taste and adjust boldly.',
   '🧈 Use ghee for the tadka if possible — its nutty, caramelised dairy flavour adds a richness no other fat can '
   'replicate.',
   '🍋 A squeeze of fresh lemon right before serving brightens every element and makes the turmeric flavour pop.'],
  ['Yellow lentils are an exceptional plant source of protein, fibre and folate.',
   'Turmeric’s curcumin is one of the most studied anti-inflammatory compounds in food.',
   'A complete, deeply nutritious meal that is naturally vegan, gluten-free and budget-friendly.'],
  ['Lentils contain phytates that can reduce mineral absorption — soaking beforehand significantly reduces this.',
   'The high fibre content can cause gas if your gut is not accustomed to legumes — build up gradually.']),
 ('Butter Chicken (Murgh Makhani)',
  '🍗',
  'comfort',
  'Perfectly marinated chicken in a velvety, rose-gold tomato and cream sauce scented with fenugreek and garam masala. '
  'This is the most beloved Indian dish in the world for very good reason — it is an absolute triumph of flavour!',
  '50 minutes',
  4,
  'Medium',
  2,
  'Indulgent Treat',
  [(1,
    'Marinate the chicken in yogurt and spices',
    'Combine chicken pieces with yogurt, garam masala, turmeric, chilli and salt, and marinate for at least 2 hours. '
    'The lactic acid in yogurt gently tenderises the protein fibres, while the spices penetrate deeply, ensuring '
    'flavour in every bite rather than just on the surface.'),
   (2,
    'Sear the chicken',
    'Shake off excess marinade and sear the chicken in a hot pan until golden. The caramelisation from high-heat '
    'searing creates a crust with intense, roasted flavours through the Maillard reaction — a foundation of complexity '
    'the sauce will build upon.'),
   (3,
    'Build the makhani sauce',
    'Sauté onions until deep golden, then add ginger-garlic paste and cook for 2 more minutes. The long, patient '
    'caramelisation of the onions produces sweetness and depth that form the very backbone of the sauce.'),
   (4,
    'Add tomatoes and simmer',
    'Add blended fresh or tinned tomatoes and cook for 15 minutes until the oil separates. When the oil pools around '
    'the edges and the tomato colour deepens to a rich brick-red, you know the sauce is properly cooked — raw tomato '
    'flavour has been driven off and deep umami remains.'),
   (5,
    'Add cream and butter',
    'Stir in cream, a knob of butter and a pinch of sugar. Butter and cream round out the acidic tomato and add a '
    'luxurious silkiness, while a touch of sugar balances any residual sharpness — this is the secret to that '
    'restaurant-smooth makhani base.'),
   (6,
    'Add kasuri methi',
    'Crush dried fenugreek leaves (kasuri methi) between your palms and stir them in. This final addition is the '
    'authentic finishing touch of murgh makhani — the slightly bitter, maple-like aroma of fenugreek is what gives the '
    'dish its unmistakable signature fragrance.'),
   (7,
    'Simmer chicken in the sauce',
    'Add the seared chicken to the sauce and simmer gently for 15 minutes. Simmering rather than boiling keeps the '
    'chicken tender, while the sauce flavours permeate the meat and the chicken juices further enrich the sauce in a '
    'beautiful exchange.'),
   (8,
    'Serve with naan',
    'Serve with pillowy naan or fragrant basmati rice. Naan’s slightly charred, chewy surface is perfect for scooping '
    'up the velvety sauce — a pairing so iconic it borders on the sacred in North Indian cuisine.')],
  ['🧈 Do not skip the kasuri methi — it is the single ingredient that makes butter chicken taste authentically '
   'restaurant-quality.',
   '🍅 Blending the tomatoes smooth before adding gives the sauce its characteristic silky, restaurant-style texture.',
   '🍗 Marinate overnight for maximum tenderness and flavour penetration — the difference is dramatic.'],
  ['Chicken provides lean, high-quality protein essential for muscle maintenance and repair.',
   'Tomatoes are rich in lycopene, an antioxidant associated with reduced cancer risk.',
   'Garam masala spices including cardamom and cinnamon have anti-inflammatory properties.'],
  ['Cream and butter make this a calorie-dense dish — enjoy the full version occasionally and use lighter alternatives '
   'for everyday cooking.',
   'Restaurant versions can be very high in sodium — making it at home gives you full control.']),
 ('Egg Curry',
  '🥚',
  'quick',
  'Perfectly hard-boiled eggs nestled in a boldly spiced tomato-onion masala — a quick, protein-packed Indian staple '
  'that goes from pantry to plate in 20 minutes. Wonderfully warming, deeply satisfying and endlessly versatile!',
  '20 minutes',
  3,
  'Easy',
  3,
  'Balanced & Quick',
  [(1,
    'Hard-boil the eggs',
    'Place eggs in cold water, bring to a boil, cook for 8 minutes, then transfer to ice water. The ice bath stops the '
    'cooking process instantly, preventing the greying ring around the yolk that forms when eggs are overcooked — you '
    'want a fully set but still bright-yellow centre.'),
   (2,
    'Score and lightly fry the eggs',
    'Peel the eggs, make a few shallow cuts in the whites, then fry briefly in oil until golden. Scoring allows the '
    'spiced sauce to penetrate the egg whites, and the light frying creates a slightly textured surface that grips the '
    'curry sauce beautifully.'),
   (3,
    'Build the masala base',
    'Fry onion until golden, add ginger, garlic, chilli and tomato, and cook down into a thick, fragrant paste. This '
    'concentrated base — the masala — is the flavour engine of the entire dish, so give it enough time for the raw '
    'edge to cook out completely.'),
   (4,
    'Add spices',
    'Add cumin, coriander, turmeric and a pinch of garam masala, stir and cook for 1 minute. Adding dry spices to the '
    'hot oil-slicked masala blooms them in fat, releasing fat-soluble flavour compounds and producing a far more '
    'aromatic curry than simply adding them to water would.'),
   (5,
    'Add water and simmer',
    'Pour in a little water to create a sauce and simmer for 5 minutes. The brief simmer lets all the spices meld '
    'together, the tomatoes fully break down and the sauce reach the right consistency to coat the eggs evenly.'),
   (6,
    'Add eggs and serve',
    'Nestle the fried eggs into the sauce and heat through for 2 minutes, then serve with rice or roti. Heating gently '
    'rather than vigorously ensures the eggs stay intact and absorb the sauce’s flavour without breaking into the '
    'curry.')],
  ['🧂 Score the eggs before frying — the cuts help the masala penetrate and the fried texture grips the sauce '
   'beautifully.',
   '🍅 Cook the masala until the oil separates and floats to the surface — this is how you know the raw spice flavour '
   'has been fully cooked out.',
   '🥚 Use a tight-fitting lid when simmering — it keeps the moisture in and prevents the sauce from becoming too thick '
   'too quickly.'],
  ['Eggs are a complete protein source containing all nine essential amino acids.',
   'Tomatoes and onions provide vitamin C and quercetin, both powerful antioxidants.',
   'A low-cost, high-nutrition meal that is naturally gluten-free.'],
  ['Eggs are high in dietary cholesterol, though research shows this has minimal impact on most people’s blood '
   'cholesterol.',
   'Frying the eggs before adding to the curry adds extra calories — omit this step to keep the dish lighter.'])]


_RAW['mexican'] = [('Grilled Fish Tacos with Mango Salsa',
  '🌮',
  'healthy',
  'Zesty chipotle-marinated white fish grilled to perfection, piled into warm corn tortillas with a vibrant mango pico '
  'de gallo and sliced avocado. This is sunshine on a plate — bright, fresh and utterly irresistible!',
  '25 minutes',
  4,
  'Easy',
  4,
  'Fresh & Nutritious',
  [(1,
    'Prepare the chipotle marinade',
    'Blend chipotle peppers in adobo with lime juice, garlic and cumin into a smooth paste. Chipotle’s smoky heat '
    'comes from jalapeños that are dried and smoked — the combination of capsaicin heat and wood smoke complexity '
    'gives the fish a char-grilled flavour even before it touches the grill.'),
   (2,
    'Marinate the fish',
    'Coat white fish fillets in the marinade and rest for 15 minutes but no longer, or the lime acid will begin to '
    'cook the protein. Fish is so delicate that even a brief marinade penetrates deeply, unlike tougher meats that '
    'need hours.'),
   (3,
    'Make the mango pico de gallo',
    'Dice mango, red onion, jalapeño, cilantro and tomato, then dress with lime juice. The acid from the lime '
    'brightens all the flavours and acts as a natural preservative, while the combination of sweet mango and spicy '
    'jalapeño creates a classic Mexican flavour contrast.'),
   (4,
    'Warm the corn tortillas',
    'Toast tortillas in a dry pan for 30 seconds per side until pliable and lightly charred. Heating tortillas not '
    'only makes them more pliable and less prone to cracking, but the slight char adds a delicious roasted corn '
    'flavour that balances the fresh, bright toppings.'),
   (5,
    'Grill the fish over high heat',
    'Grill the marinated fish on a preheated ridged grill pan over high heat for 3–4 minutes per side. The high heat '
    'creates char marks and caramelises the sugars in the marinade, adding that essential smoky-sweet depth that '
    'defines great fish tacos.'),
   (6,
    'Assemble the tacos',
    'Flake fish onto warm tortillas and top generously with mango pico, sliced avocado and a squeeze of lime. The '
    'order of assembly matters — the warm fish should be the first thing on the tortilla so it slightly warms the '
    'toppings and the flavours meld together.'),
   (7,
    'Serve with lime wedges',
    'Serve immediately with extra lime wedges and hot sauce. Lime juice added at the very end adds a brightness that '
    'cuts through the richness of the avocado and rounds out the entire flavour profile of the taco.')],
  ['🌟 Do not over-marinate the fish — the lime acid will denature the proteins and produce a cooked, mealy texture in '
   'under 30 minutes.',
   '🥭 Use just-ripe mango for the pico — fully ripe mango is too soft and will turn the salsa mushy.',
   '🌿 Fresh cilantro is non-negotiable in this dish — it is the herb that ties every component together.'],
  ['White fish is an excellent lean protein source, low in calories and rich in B vitamins.',
   'Avocado provides heart-healthy monounsaturated fats and potassium.',
   'Mango is rich in vitamin C, folate and beta-carotene, all powerful antioxidants.'],
  ['Corn tortillas are naturally gluten-free but can be high in refined carbohydrates.',
   'The avocado adds significant calories — portion mindfully if managing calorie intake.']),
 ('Beef Birria Tacos',
  '🌮',
  'comfort',
  'Deeply braised beef cheek in a rich guajillo-ancho consommé, stuffed into crispy cheese-fried tortillas and served '
  'with a dipping cup of the extraordinary braising broth. The most glorious taco you will ever encounter!',
  '90 minutes',
  6,
  'Hard',
  2,
  'Indulgent Treat',
  [(1,
    'Toast the dried chillies',
    'Tear open guajillo and ancho chillies, remove seeds, and toast in a dry hot pan for 30 seconds per side until '
    'fragrant and pliable. Toasting dried chillies is transformative — it activates and deepens their earthy, fruity, '
    'smoky flavour compounds and removes any mustiness from the drying process.'),
   (2,
    'Rehydrate and blend the chillies',
    'Soak toasted chillies in hot water for 20 minutes, then blend with garlic, tomatoes, onion, cumin and oregano '
    'into a smooth, deep-red consommé base. This vibrant, complex sauce is the soul of birria — every aromatic '
    'compound you can coax out of these chillies goes into that pot.'),
   (3,
    'Sear the beef cheek',
    'Season beef cheek generously and sear in a smoking-hot pot until deeply browned on all sides. The Maillard '
    'reaction at this stage builds a crust packed with hundreds of flavour compounds that will dissolve into the '
    'braising liquid, enriching the consommé with meaty depth.'),
   (4,
    'Braise the beef low and slow',
    'Pour the chilli consommé over the beef, cover tightly and braise at 160°C for 3 hours. The collagen-rich beef '
    'cheek slowly converts its collagen to gelatin over the long, gentle braise, producing impossibly tender, silky '
    'meat that practically pulls itself apart.'),
   (5,
    'Shred and season the beef',
    'Remove the beef, shred it with two forks, and stir it back into the consommé. Returning the shredded meat to the '
    'braising liquid allows the collagen-rich, intensely flavoured consommé to coat every strand of beef, ensuring '
    'maximum flavour in every bite.'),
   (6,
    'Char the tortillas in beef fat',
    'Dip corn tortillas in the fat that has risen to the surface of the consommé and cook in a hot pan until crispy. '
    'That fat is saturated with chilli and beef flavour — charring the tortillas in it is the step that elevates '
    'birria from a stew to an extraordinary taco experience.'),
   (7,
    'Build the tacos',
    'Fill charred tortillas with shredded beef and Oaxacan cheese, fold and press in the pan until the cheese melts '
    'and the tortilla is crispy. Oaxacan string cheese has a high melting point and stretches beautifully, binding the '
    'taco together and adding a mild, milky richness.'),
   (8,
    'Serve with dipping consommé',
    'Ladle warm consommé into cups for dipping and serve immediately. Dipping the taco into the consommé is the '
    'defining ritual of birria — the contrast between the crispy, cheesy taco and the rich, warming broth is one of '
    'the most satisfying sensory experiences in food.')],
  ['🌶 Toast the dried chillies until just fragrant — over-toasting makes them bitter and ruins the entire consommé.',
   '🥩 Beef cheek is the ideal cut for birria — its extraordinary collagen content produces an incomparably silky '
   'braise.',
   '🧀 Oaxacan cheese can be substituted with low-moisture mozzarella — it melts and stretches in a very similar way.'],
  ['Beef provides iron, zinc and B12, nutrients that are often deficient in modern diets.',
   'The braising liquid is rich in collagen peptides, which support skin and joint health.',
   'Chillies are rich in vitamin C and capsaicin, which may boost metabolism.'],
  ['Birria is high in saturated fat from the beef and cheese — enjoy as an occasional treat.',
   'The braising process is long and requires active attention — this is a weekend project, not a weeknight meal.']),
 ('Speedy Chicken Quesadillas',
  '🧀',
  'quick',
  'Crispy, golden flour tortillas packed with spiced chicken and melted cheese — the ultimate quick-fix Mexican '
  'comfort food that goes from fridge to table in 15 brilliant minutes. Serve with salsa and sour cream for maximum '
  'joy!',
  '15 minutes',
  2,
  'Easy',
  3,
  'Balanced & Quick',
  [(1,
    'Season and cook the chicken',
    'Slice chicken breast thin, season with cumin, garlic powder and smoked paprika, and cook in a hot pan for 3–4 '
    'minutes per side. Thin slices increase surface area, dramatically speeding up cooking time while maximising the '
    'caramelised, savoury crust from the spice rub.'),
   (2,
    'Warm the tortillas',
    'Heat flour tortillas in a dry pan for 30 seconds each side. A briefly toasted tortilla is pliable enough to fold '
    'without cracking but has a slight toasty flavour that adds another layer of depth to the finished quesadilla.'),
   (3,
    'Assemble the quesadillas',
    'Layer chicken and grated cheese over half of each tortilla. Using half the tortilla as the base and folding over '
    'creates a more compact, evenly heated quesadilla where the cheese melts before the tortilla burns.'),
   (4,
    'Cook until golden and melted',
    'Cook quesadillas in a lightly oiled pan over medium heat for 2 minutes per side, pressing gently with a spatula. '
    'The gentle pressure ensures even contact between the tortilla and the pan, creating uniform golden colour and '
    'complete cheese melt throughout.'),
   (5,
    'Rest briefly before cutting',
    'Transfer to a board and rest for 1 minute before cutting into wedges. This brief rest allows the molten cheese to '
    'firm up just enough to hold the quesadilla together when sliced, rather than spilling out immediately.'),
   (6,
    'Serve with salsa and sour cream',
    'Serve with fresh salsa, sour cream and a wedge of lime. The cool, tangy sour cream contrasts the hot, crispy '
    'quesadilla, and the lime’s acidity cuts through the richness of the melted cheese, making every bite feel '
    'balanced and fresh.')],
  ['🧀 Grate your own cheese rather than using pre-shredded — the anti-caking agents in pre-shredded cheese prevent it '
   'from melting as smoothly.',
   '🍗 Use chicken thigh instead of breast for extra juiciness — its higher fat content means it stays moist even at '
   'high heat.',
   '🌮 Press down firmly with a spatula while cooking — maximum contact means even golden colour across the entire '
   'surface.'],
  ['Chicken provides lean protein and B vitamins essential for energy metabolism.',
   'Choosing a corn tortilla over flour significantly reduces calorie and carbohydrate content.',
   'A quick, satisfying meal that can be balanced with a simple green salad on the side.'],
  ['Flour tortillas are high in refined carbohydrates and calories compared to corn alternatives.',
   'Generous cheese makes this calorie-dense — measure portions if managing calorie intake.'])]


_RAW['chinese'] = [('Steamed Sea Bass with Ginger & Scallion',
  '🐟',
  'healthy',
  'A showpiece of Cantonese cooking — silken sea bass steamed over aromatic ginger and spring onion, then crowned with '
  'a dramatic pour of searing hot oil. Breathtakingly delicious, effortlessly healthy and ready in 20 minutes!',
  '20 minutes',
  2,
  'Easy',
  5,
  'Super Nutritious',
  [(1,
    'Prepare the fish',
    'Score the fish on both sides with diagonal cuts down to the bone, every 2cm. Scoring allows heat to penetrate '
    'evenly and lets the ginger and scallion aromatics permeate the flesh deeply, ensuring the delicate flavour '
    'reaches the innermost parts of the fish.'),
   (2,
    'Prepare the aromatics',
    'Shred fresh ginger and spring onion into fine julienne and place half inside the cavity of the fish. The '
    'aromatics inside the cavity steam from the inside out, perfuming the flesh with their clean, bright flavour while '
    'also neutralising any fishiness.'),
   (3,
    'Steam over boiling water',
    'Place the fish on a heatproof plate, set over a wok of vigorously boiling water, cover tightly and steam for '
    '10–12 minutes per kilogram. Steaming is the gentlest cooking method for fish, preserving the delicate proteins '
    'that would toughen and dry out under direct high heat.'),
   (4,
    'Test for doneness',
    'The fish is done when the flesh near the bone pulls away cleanly with a chopstick. Perfectly steamed fish should '
    'be just opaque and incredibly moist — a minute’s overcooking at this stage would render it disappointingly dry.'),
   (5,
    'Drain excess liquid',
    'Pour away the liquid that has collected on the plate during steaming. This liquid contains blood and released '
    'moisture that would dilute your dressing — removing it ensures a clean, pure flavour in the final dish.'),
   (6,
    'Pour on the hot oil',
    'Heat groundnut oil in a small pan until smoking, then pour it sizzling over the ginger and spring onion on the '
    'fish. This dramatic pour is the defining moment of the dish — the searing oil instantly cooks the raw aromatics, '
    'releasing their essential oils and creating a fragrant, slightly caramelised topping.'),
   (7,
    'Add soy and serve',
    'Pour light soy sauce around (not over) the fish and serve immediately at the table. Adding soy around rather than '
    'over prevents it from washing away the aromatics, and letting diners take the fish off the bone at the table is '
    'part of the communal, convivial spirit of Chinese family cooking.')],
  ['🐟 Score the fish deeply to the bone — shallow scoring is decorative but does not allow the aromatics to flavour '
   'the centre of the flesh.',
   '🧄 The thinner and more uniform your ginger and spring onion julienne, the more elegantly they cook under the hot '
   'oil pour.',
   '🟡 Use groundnut or vegetable oil for the pour — olive oil has too strong a flavour and a lower smoke point.'],
  ['Sea bass is an excellent lean protein source, low in saturated fat and rich in omega-3 fatty acids.',
   'Steaming preserves virtually all of the fish’s vitamins and minerals, unlike frying or roasting.',
   'Ginger has potent anti-inflammatory and anti-nausea properties and aids digestion.'],
  ['Light soy sauce is high in sodium — use low-sodium varieties and use sparingly if watching salt intake.',
   'Sea bass can be expensive — the same technique works beautifully with grey mullet or sea bream.']),
 ('Kung Pao Chicken',
  '🍗',
  'comfort',
  'Tender velveted chicken tossed with Sichuan peppercorns, dried chillies, peanuts and a glossy sweet-sour-spicy '
  'sauce in a blazing hot wok. This legendary Sichuan dish delivers the thrilling mala (numbing-hot) sensation that '
  'makes you reach for one more piece!',
  '30 minutes',
  3,
  'Medium',
  2,
  'Indulgent Treat',
  [(1,
    'Velvet the chicken',
    'Cut chicken into bite-sized pieces and toss with egg white, cornstarch, baking soda and a pinch of salt, then '
    'marinate for 20 minutes. This technique, called velveting, coats each piece in a protective layer that keeps the '
    'chicken impossibly tender and silky during high-heat stir-frying.'),
   (2,
    'Prepare the Sichuan aromatics',
    'Toast Sichuan peppercorns in a dry pan until fragrant, then crush lightly. Sichuan peppercorns are unique — they '
    'contain hydroxy-alpha-sanshool, a compound that causes a tingling, numbing sensation (ma) that complements the '
    'fiery heat (la) of the chillies, creating the legendary mala flavour profile.'),
   (3,
    'Flash-fry the chicken',
    'Stir-fry the velveted chicken in very hot oil for 2–3 minutes until just cooked, then remove. The ultra-hot wok '
    'creates wok hei — a smoky, slightly charred flavour from the Maillard reaction happening at intense temperatures '
    'that a regular pan simply cannot replicate.'),
   (4,
    'Fry the dried chillies and peppercorns',
    'In the same wok, fry whole dried chillies and crushed Sichuan peppercorns in oil for 30 seconds. The chillies’ '
    'capsaicin and the peppercorns’ sanshool are fat-soluble, so frying them in oil creates an aromatically charged '
    'cooking medium that infuses everything cooked in it.'),
   (5,
    'Add the chicken back with sauce',
    'Return the chicken to the wok and toss with a sauce of soy, rice vinegar, sugar and hoisin. The sweet-sour-salty '
    'sauce is the counterpoint to the intense heat and numbing spice, creating a beautifully balanced dish where no '
    'single element overwhelms.'),
   (6,
    'Toss in peanuts and spring onion',
    'Add roasted peanuts and sliced spring onion and toss for 30 seconds. The peanuts add a textural crunch and a '
    'nutty sweetness that plays against the fiery sauce, while the spring onion brings a fresh sharpness that cuts '
    'through the richness.'),
   (7,
    'Serve over steamed rice',
    'Serve immediately over steamed jasmine rice. The neutral, fluffy rice absorbs the intensely flavoured, slightly '
    'oily sauce and provides the perfect cooling backdrop for the Sichuan heat and numbing spice.'),
   (8,
    'Garnish and enjoy',
    'Garnish with extra Sichuan peppercorns and chilli if desired, and dive in while it is blazing hot. The heat of '
    'the dish keeps the aromatic compounds volatile and active — this is food designed to make you feel truly alive.')],
  ['🧪 The velveting step is non-negotiable — it is the reason restaurant Kung Pao chicken is silky while homemade '
   'versions are often chewy.',
   '🌶 Do not skip the Sichuan peppercorns — the numbing mala sensation is what makes this dish Sichuan rather than '
   'simply spicy.',
   '🥜 Roast your own peanuts in a dry pan before adding — the extra toastiness makes a significant difference to the '
   'final flavour.'],
  ['Chicken provides lean protein; peanuts add healthy fats and plant-based protein.',
   'Sichuan peppercorns contain antioxidants and have been used medicinally for centuries.',
   'A satisfying, protein-rich meal that is genuinely filling without excessive calorie density.'],
  ['This dish is high in sodium from soy sauce and hoisin — use low-sodium alternatives where possible.',
   'The generous oil needed for wok cooking makes this a higher-fat meal best enjoyed occasionally.']),
 ('Egg Fried Rice',
  '🍚',
  'quick',
  'The ultimate 12-minute pantry hero — day-old rice blasted in a scorching wok with eggs, spring onion and soy sauce '
  'to produce that legendary smoky wok hei flavour. Simple, satisfying and impossibly delicious!',
  '12 minutes',
  2,
  'Easy',
  3,
  'Balanced & Quick',
  [(1,
    'Use day-old rice',
    'Spread freshly cooked rice on a tray and refrigerate overnight, or spread and fan to dry. Day-old rice has dried '
    'out slightly, meaning the grains separate in the wok rather than clumping, and the lower moisture content is key '
    'to achieving wok hei — the elusive smoky quality of great fried rice.'),
   (2,
    'Heat the wok until smoking',
    'Get your wok ripping hot — a bead of water should evaporate in under a second. A properly hot wok is the '
    'non-negotiable secret of wok hei: the intense heat flashcooks the rice and creates thousands of tiny Maillard '
    'reactions on the grain surfaces almost simultaneously.'),
   (3,
    'Scramble the eggs first',
    'Add oil, crack in eggs and scramble quickly until just set, then push to the side. Cooking the eggs separately in '
    'the wok and then incorporating them means they stay light and fluffy rather than dry and rubbery from being '
    'overcooked with the rice.'),
   (4,
    'Fry the rice over maximum heat',
    'Add the cold rice, breaking up any clumps, and toss constantly over maximum heat for 2 minutes. The constant '
    'movement prevents burning while ensuring every grain gets direct contact with the hot wok surface, building that '
    'characteristic smoky, slightly caramelised flavour.'),
   (5,
    'Season with soy sauce',
    'Drizzle soy sauce around the edges of the wok rather than directly on the rice. Adding soy to the hot wok edges '
    '(rather than the rice) means it sizzles and slightly caramelises before hitting the rice, adding an extra layer '
    'of roasted soy flavour.'),
   (6,
    'Finish with spring onion and serve',
    'Toss in sliced spring onion, give one final toss, and serve immediately. Spring onion added at the very end '
    'retains its fresh, sharp bite and vibrant green colour, providing a clean contrast to the rich, smoky fried '
    'rice.')],
  ['🍚 Always use cold, day-old rice — freshly cooked rice contains too much moisture and will produce clumpy, steamed '
   'fried rice rather than the properly separated, wok-charred variety.',
   '🍳 Season at the very end and taste before adding — soy sauce is intensely salty and it is very easy to over-season '
   'fried rice.',
   '🧂 Add a drop of sesame oil off the heat at the very end — it adds a toasty, nutty fragrance that elevates the dish '
   'instantly.'],
  ['Eggs provide complete protein and choline, an important nutrient for brain health.',
   'Rice is gluten-free, easily digestible and provides sustained carbohydrate energy.',
   'A versatile base dish that can absorb virtually any leftover vegetables for extra nutrition.'],
  ['White rice is a refined carbohydrate with a high glycaemic index — substitute brown rice for more fibre and '
   'nutrients.',
   'Soy sauce is very high in sodium — use sparingly or choose a reduced-sodium version.'])]


_RAW['thai'] = [('Green Papaya Salad (Som Tum)',
  '🥗',
  'healthy',
  'A spectacular tangle of shredded green papaya dressed in a bold lime-fish sauce-palm sugar dressing with cherry '
  'tomatoes, long beans and roasted peanuts. This iconic Thai salad is a masterclass in the perfect balance of sour, '
  'salty, sweet and spicy!',
  '15 minutes',
  2,
  'Easy',
  5,
  'Super Nutritious',
  [(1,
    'Prepare the green papaya',
    'Peel and shred green papaya using a julienne peeler or the traditional technique of scoring and shaving with a '
    'knife. Green papaya contains papain, a natural enzyme that tenderises protein and aids digestion — eating it raw '
    'preserves this valuable enzyme that cooking would destroy.'),
   (2,
    'Pound the dressing base',
    'In a mortar, pound garlic and chillies to a rough paste. The mortar and pestle bruises the fibres of the chilli '
    'and garlic rather than cutting them, releasing more essential oils and creating a rawer, more complex flavour '
    'than a blender ever could.'),
   (3,
    'Create the rot chart balance',
    'Add fish sauce, lime juice and palm sugar to the mortar and taste. This is the critical step of achieving rot '
    'chart — the Thai principle of balancing sour (lime), salty (fish sauce), sweet (palm sugar) and spicy (chilli) in '
    'perfect harmony. Adjust each until the dressing sings.'),
   (4,
    'Add the tomatoes',
    'Add halved cherry tomatoes to the mortar and pound gently until they just crack. Bruising the tomatoes rather '
    'than crushing them releases just enough juice to thin the dressing while keeping textural interest in the salad.'),
   (5,
    'Toss with papaya and long beans',
    'Combine the shredded papaya and halved long beans with the dressing in the mortar, using a spoon to toss and '
    'bruise them lightly. Light bruising softens the papaya slightly and helps it absorb the dressing, while the long '
    'beans add a satisfying snap.'),
   (6,
    'Top with roasted peanuts',
    'Scatter roasted, unsalted peanuts over the salad just before serving. Peanuts add a textural contrast and a '
    'nutty, fatty richness that smooths out the sharp edges of the lime and fish sauce dressing, creating a more '
    'rounded, satisfying bite.'),
   (7,
    'Serve immediately',
    'Som tum is at its very best the moment it is dressed — serve straight from the mortar onto a plate. The papaya '
    'will begin to wilt as it sits, so speed is your ally here: this is a salad that rewards those who eat without '
    'delay.')],
  ['🍋 Start with less chilli and fish sauce than you think you need — you can always add more, but you cannot take it '
   'away once it’s in the mortar.',
   '🥜 Roast your peanuts in a dry pan until golden — the extra toastiness makes a significant difference to the '
   'finished salad.',
   '🍌 If green papaya is unavailable, green mango or kohlrabi makes an excellent substitute.'],
  ['Green papaya is very low in calories and high in vitamin C, folate and dietary fibre.',
   'Fish sauce provides iodine and umami without significant calories.',
   'Peanuts contribute protein, healthy fats and vitamin E.'],
  ['Fish sauce is very high in sodium — use sparingly and do not add extra salt.',
   'Raw papaya contains latex which can cause reactions in people with latex allergy — peel carefully and consider '
   'wearing gloves.']),
 ('Thai Green Curry',
  '🟢',
  'comfort',
  'Fragrant green curry paste bloomed in cracked coconut cream, slow-simmered with tender chicken thighs, kaffir lime '
  'leaves and Thai basil until the entire kitchen smells of paradise. Rich, aromatic and deeply satisfying!',
  '35 minutes',
  4,
  'Medium',
  3,
  'Balanced Comfort',
  [(1,
    'Bloom the green curry paste',
    'Scoop the thick top layer of coconut cream from an unshaken can and cook it in a wok over medium heat until it '
    'cracks — the oil separates from the solids. Frying the curry paste in this separated coconut oil allows the '
    'paste’s volatile aromatics to bloom at a higher temperature, creating a much more fragrant, deeper-flavoured '
    'base.'),
   (2,
    'Fry the curry paste',
    'Add the green curry paste to the cracked coconut cream and fry for 2–3 minutes, stirring constantly. The paste '
    'frying in the coconut oil undergoes a beautiful transformation — raw lemongrass, galangal and kaffir lime leaf '
    'aromas cook out and are replaced by rounder, more complex cooked flavours.'),
   (3,
    'Add chicken and coat in paste',
    'Add sliced chicken thigh and toss to coat thoroughly in the fragrant paste. Thigh meat is used rather than breast '
    'because its higher fat content means it stays juicy through the entire cooking time, while breast would become '
    'dry and chewy in the same timeframe.'),
   (4,
    'Add coconut milk and simmer',
    'Pour in the remaining coconut milk and bring to a gentle simmer. The coconut milk’s rich fat carries and '
    'amplifies the fat-soluble flavour compounds from the curry paste, distributing them evenly throughout the sauce '
    'and creating the silky, aromatic broth that defines Thai curry.'),
   (5,
    'Season with fish sauce and sugar',
    'Add fish sauce, a pinch of palm sugar and a squeeze of lime. Fish sauce provides the salty, umami depth; palm '
    'sugar rounds out the heat; and lime lifts the whole dish. These three elements together create the characteristic '
    'Thai sweet-sour-salty-spicy balance.'),
   (6,
    'Add kaffir lime leaves and Thai basil',
    'Tear in kaffir lime leaves and add a large handful of Thai basil right at the end. These aromatics are added late '
    'because their essential oils are incredibly volatile and would evaporate away in a long simmer, leaving you with '
    'a flavour that is flat and indefinable rather than vibrantly, unmistakably Thai.'),
   (7,
    'Serve over jasmine rice',
    'Ladle the curry over fluffy steamed jasmine rice and garnish with a fresh Thai basil sprig. Jasmine rice’s floral '
    'aroma complements the herbal, citrusy Thai curry in a way that plainer rice cannot — this pairing has been '
    'perfected over centuries of Thai culinary tradition.')],
  ['🛖 Always use the thick coconut cream layer for blooming the paste — it contains a higher proportion of fat which '
   'is essential for the cracking step.',
   '🌿 Add the Thai basil in the very last 30 seconds — any longer and its volatile essential oils disappear '
   'completely.',
   '🍋 Kaffir lime leaves must be fresh or frozen, not dried — dried leaves have a completely different, muted flavour '
   'that does not work in this dish.'],
  ['Coconut milk provides medium-chain triglycerides (MCTs) which are metabolised differently from other saturated '
   'fats.',
   'Galangal, lemongrass and kaffir lime are all rich in anti-inflammatory and anti-bacterial compounds.',
   'Chicken thigh provides excellent protein, iron and zinc.'],
  ['Full-fat coconut milk is high in saturated fat and calories — use reduced-fat versions for a lighter result.',
   'Fish sauce is very high in sodium — use in moderation if watching salt intake.']),
 ('Pad Thai Noodles',
  '🍜',
  'quick',
  'Rice noodles tossed in a tangy tamarind sauce with eggs, beansprouts, peanuts and lime in a blazing hot wok. One of '
  'the world’s most loved noodle dishes, ready in 20 minutes and tasting like it took all day!',
  '20 minutes',
  2,
  'Easy',
  3,
  'Balanced & Quick',
  [(1,
    'Soak the rice noodles',
    'Soak flat rice noodles in cold water for 30 minutes until pliable, then drain. Cold-soaking (rather than boiling) '
    'pre-softens the noodles without cooking them, so they finish perfectly in the wok without going mushy or clumping '
    'together.'),
   (2,
    'Make the tamarind sauce',
    'Combine tamarind paste, fish sauce, palm sugar and a splash of water in a bowl. Tamarind is the defining souring '
    'agent of Pad Thai — its complex tartness, fruity depth and slight sweetness create a more interesting base than '
    'lime juice alone could achieve.'),
   (3,
    'Stir-fry protein over high heat',
    'Cook prawns or tofu in a very hot, lightly oiled wok until just done, then push to the side. Starting with the '
    'protein means it gets direct contact with the hottest part of the wok, developing colour and flavour before the '
    'noodles are added.'),
   (4,
    'Add noodles and sauce',
    'Add the soaked noodles and tamarind sauce to the wok and toss constantly over high heat until the noodles absorb '
    'the sauce and begin to caramelise slightly. The caramelisation of the palm sugar on the hot wok surface gives Pad '
    'Thai its characteristic, slightly sticky, complex sweetness.'),
   (5,
    'Scramble in the egg',
    'Push everything to one side, crack in an egg and scramble briefly before folding into the noodles. Cooking the '
    'egg separately in the wok and then incorporating it creates distinct, light, fluffy pieces of egg rather than a '
    'coating that makes the noodles heavy.'),
   (6,
    'Add beansprouts and serve',
    'Toss in fresh beansprouts at the very last second, then serve with peanuts, lime, chilli flakes and extra fish '
    'sauce on the side. Beansprouts added at the very end retain their satisfying crunch — a crucial textural contrast '
    'to the soft, saucy noodles.')],
  ['🍜 Soak the noodles in cold water, not hot — hot water over-softens them and they will become mushy when tossed in '
   'the hot wok.',
   '🦴 Real tamarind paste is far superior to tamarind concentrate — worth seeking out for its much more complex, '
   'layered sourness.',
   '🍥 Serve all the condiments — lime, chilli, sugar and fish sauce — in individual small dishes so each diner can '
   'personalise their bowl.'],
  ['Rice noodles are naturally gluten-free and easily digestible.',
   'Eggs and prawns provide high-quality complete protein with all essential amino acids.',
   'Beansprouts add crunch, vitamin C and a boost of fibre with virtually no calories.'],
  ['Pad Thai can be surprisingly high in sodium from fish sauce and high in sugar from palm sugar — adjust seasoning '
   'to your needs.',
   'White rice noodles are a refined carbohydrate — pair with extra protein and vegetables for a more balanced meal.'])]


_RAW['french'] = [('Salade Niçoise',
  '🥗',
  'healthy',
  'The Riviera’s finest — premium tuna, tender French beans, ripe tomatoes, soft-boiled eggs, olives and a deeply '
  'savoury anchovy vinaigrette arranged on a beautiful platter. A composed salad that is simultaneously elegant, '
  'nutritious and utterly satisfying!',
  '20 minutes',
  4,
  'Easy',
  5,
  'Super Nutritious',
  [(1,
    'Cook the French beans',
    'Blanch fine French beans in heavily salted boiling water for 3 minutes, then plunge into ice water. The ice bath '
    'halts cooking precisely, preserving the vivid emerald green colour and firm, squeaky texture that makes a proper '
    'Niçoise so visually striking.'),
   (2,
    'Hard-boil the eggs',
    'Place eggs in cold water, bring to the boil, simmer for exactly 9 minutes, then cool in ice water. A 9-minute egg '
    'has a fully set white and a yolk that is just barely set in the centre — sliced, it creates those beautiful '
    'half-moon cross-sections that are the hallmark of a classic Niçoise.'),
   (3,
    'Make the anchovy vinaigrette',
    'Pound anchovy fillets to a paste, then whisk with Dijon mustard, red wine vinegar, garlic and olive oil. The '
    'mustard acts as an emulsifier, its lecithin-rich compounds binding oil and vinegar into a stable, glossy '
    'dressing. The anchovy dissolves entirely but adds a deep, savoury umami backbone.'),
   (4,
    'Slice and season the tomatoes',
    'Halve ripe tomatoes and season with flaky salt 10 minutes before assembling. Salt draws out a little moisture and '
    'concentrates the tomato flavour — a simple step that transforms average tomatoes into something far more intense '
    'and delicious.'),
   (5,
    'Assemble on a large platter',
    'Arrange all the components separately on a large platter rather than tossing them together. The classic Niçoise '
    'is composed, not tossed — keeping the elements distinct means every element can be appreciated individually and '
    'guests can build their own perfect forkful.'),
   (6,
    'Add the tuna',
    'Break tuna into large chunks and place on the salad. The best Niçoise uses highest-quality tinned tuna in olive '
    'oil — the oil the tuna is packed in can be incorporated into the dressing, adding extra depth and linking the '
    'components of the dish.'),
   (7,
    'Dress and serve',
    'Drizzle the anchovy vinaigrette generously over everything just before serving. Dressing at the last moment '
    'prevents the acidic vinegar from wilting the vegetables or breaking down the egg whites before your guests have a '
    'chance to appreciate the full, vivid beauty of the salad.')],
  ['🧳 Compose the salad rather than tossing it — this keeps the individual components beautiful and allows each '
   'flavour to be appreciated distinctly.',
   '🐟 Use the highest-quality tinned tuna you can afford — it is the centrepiece of the dish and cheap tuna will '
   'undermine everything else.',
   '🧄 Pound the anchovy properly into a paste before whisking — tiny anchovy pieces in the dressing are distracting '
   'and unpleasant in the mouth.'],
  ['Tuna is an excellent source of lean protein and selenium, a mineral important for thyroid function.',
   'Eggs provide complete protein, vitamin D and choline, a nutrient essential for brain function.',
   'The olive oil-based vinaigrette provides heart-healthy monounsaturated fats and powerful polyphenol antioxidants.'],
  ['Tinned tuna (especially albacore) may contain significant mercury — limit to 2–3 servings per week.',
   'Anchovies are very high in sodium — the dressing provides significant salt so do not add extra seasoning without '
   'tasting first.']),
 ('Coq au Vin',
  '🍗',
  'comfort',
  'Chicken thighs braised low and slow in an entire bottle of red wine with smoky lardons, mushrooms and pearl onions '
  'until the sauce turns glossy, the chicken falls from the bone and the whole house smells extraordinary. The '
  'quintessential French comfort dish!',
  '75 minutes',
  4,
  'Medium',
  2,
  'Indulgent Treat',
  [(1,
    'Brown the chicken thighs',
    'Season chicken thighs generously and brown skin-side down in a wide casserole until deeply golden. The skin-down '
    'start renders the fat from beneath the skin, making it crisp and delicious, while the dripping fat creates the '
    'perfect medium for caramelising all the aromatic vegetables that follow.'),
   (2,
    'Sauté lardons and pearl onions',
    'In the same pot, cook lardons until their fat renders and they turn golden, then add pearl onions. The fond — the '
    'caramelised brown bits left by the chicken — is dissolved by the fat from the lardons, building a layer of '
    'savoury complexity that would otherwise require hours of stock-making.'),
   (3,
    'Add the mushrooms',
    'Add sliced mushrooms and cook until they give up their liquid and begin to brown. Patience here matters — '
    'mushrooms release a huge amount of water and will steam rather than sauté if the pan is too crowded or the heat '
    'too low. Golden mushrooms have an entirely different, deeper flavour to steamed ones.'),
   (4,
    'Deglaze with cognac and flambé',
    'Add a splash of cognac and carefully flambé — the alcohol burns off spectacularly, leaving behind complex '
    'caramelised compounds. The flambé is not merely theatrical: the brief, intense heat caramelises the cognac’s '
    'sugars and softens its raw alcohol flavour into something warming and complex.'),
   (5,
    'Braise in red wine',
    'Pour in a full bottle of good red wine, add a bouquet garni, and return the chicken. Use a wine you would drink — '
    'its quality will be concentrated during the long braise, and a poor wine will produce a sauce with equally poor '
    'flavour. The wine’s tannins and acids slowly break down the collagen in the chicken.'),
   (6,
    'Slow braise for an hour',
    'Cover and braise at 160°C for 1 hour. The low temperature is critical — it allows the collagen in the chicken '
    'thighs to convert slowly to gelatin, enriching the braising liquid with body and silkiness while keeping the meat '
    'moist and tender rather than stringy.'),
   (7,
    'Thicken with beurre manié',
    'Mix equal parts softened butter and flour into a paste and whisk pieces into the simmering sauce until it reaches '
    'the perfect nappé consistency. This classical French thickener distributes evenly without lumps and adds a rich, '
    'buttery gloss that a plain flour slurry could never achieve.'),
   (8,
    'Rest and serve',
    'Allow to rest off the heat for 10 minutes before serving over creamy mashed potatoes. Resting allows the sauce to '
    'cool slightly and thicken further, and the chicken fibres to relax, absorbing back some of the sauce and becoming '
    'even more tender and flavourful.')],
  ['🍷 Use a proper drinking-quality red wine — Burgundy is traditional, but any medium-bodied red you enjoy works '
   'beautifully.',
   '🍄 Cook the mushrooms in a separate pan if you are making a large batch — overcrowding the pan causes them to steam '
   'rather than caramelise.',
   '🧈 The beurre manié can be made in advance and stored in the fridge — use it cold, not at room temperature, for the '
   'best emulsification.'],
  ['Chicken thighs provide iron, zinc and B12 in addition to excellent protein.',
   'Red wine polyphenols may have cardiovascular protective effects when consumed in moderation.',
   'Mushrooms contribute immune-supporting beta-glucans and vitamin D when sun-dried.'],
  ['The butter-based sauce and lardons make this a high-saturated-fat dish — best enjoyed as an occasional treat.',
   'The long cooking time and relatively high complexity make this a dedicated weekend cooking project.']),
 ('Croque Monsieur',
  '🧀',
  'quick',
  'The ultimate Parisian bistro snack — thick bread loaded with quality ham and gruyère, smothered in velvety béchamel '
  'and grilled until golden and bubbling. Ready in 15 minutes and tasting like you are sitting at a zinc-topped bar on '
  'the Rue de Rivoli!',
  '15 minutes',
  2,
  'Easy',
  3,
  'Balanced & Quick',
  [(1,
    'Make the béchamel',
    'Melt butter over medium heat, add flour and stir for 2 minutes to cook out the raw flour taste. This mixture is '
    'called a roux, and cooking it for at least 2 minutes is essential — under-cooked roux produces a sauce that '
    'tastes unmistakably of uncooked flour, no matter how much butter or cheese you add.'),
   (2,
    'Add warm milk gradually',
    'Add warm milk gradually, whisking constantly after each addition. Adding milk in stages prevents lumps by '
    'allowing each portion to be fully absorbed before the next is added — the constant whisking prevents the starch '
    'granules from clumping together before they gelatinise smoothly.'),
   (3,
    'Season the béchamel',
    'Season with salt, white pepper, a pinch of nutmeg and a tablespoon of Dijon mustard. Nutmeg is the classic French '
    'pairing with béchamel — it adds a warm, slightly floral note that enhances the dairy without being identifiable '
    'in the finished dish.'),
   (4,
    'Assemble the croque',
    'Spread béchamel on both halves of thick white bread, layer with quality ham and generously grated gruyère. '
    'Gruyère is the classic choice because its low moisture content and high fat content mean it melts smoothly and '
    'completely without becoming oily or stringy.'),
   (5,
    'Grill until golden and bubbling',
    'Place under a hot grill until the béchamel is golden and the cheese is bubbling. The grill’s direct overhead heat '
    'caramelises the sugars in the béchamel and the cheese simultaneously, creating a golden, slightly crisp crust '
    'over the oozy interior.'),
   (6,
    'Serve immediately',
    'Eat straight from the grill, perhaps with a simple green salad. A croque monsieur is at its absolute best in the '
    'first 2 minutes — the cheese is at peak melt, the béchamel is creamy and the bread is still crisp before the '
    'steam from the filling softens it.')],
  ['🧀 Grate the gruyère yourself from a block — freshly grated cheese melts more evenly and has a far superior flavour '
   'to pre-grated.',
   '🧈 Cook the roux for the full 2 minutes — under-cooked roux produces a paste-like, floury taste that no amount of '
   'cheese can disguise.',
   '🍞 Use thick-cut white bread — thin bread will collapse under the weight of the béchamel and cheese before the '
   'croque is ready to eat.'],
  ['Ham provides lean protein and B vitamins, particularly thiamine (B1).',
   'Gruyère is an excellent source of calcium, phosphorus and protein.',
   'A satisfying, quick meal that provides a good balance of protein, fat and carbohydrates.'],
  ['The béchamel and cheese make this a high-calorie, high-fat dish — pair with a green salad to add nutrients and '
   'volume.',
   'High in saturated fat from the butter, cheese and ham — enjoy occasionally rather than as an everyday lunch.'])]


_RAW['spanish'] = [('Gazpacho Andaluz',
  '🍅',
  'healthy',
  'Andalusia’s gift to the world — sun-ripe tomatoes blended raw with cucumber, pepper, sherry vinegar and olive oil '
  'into a silky, ice-cold soup of extraordinary depth and freshness. The most refreshing dish ever conceived!',
  '15 minutes + chilling',
  6,
  'Easy',
  5,
  'Super Nutritious',
  [(1,
    'Blend the base vegetables',
    'Combine ripe tomatoes, cucumber, red and green peppers and a slice of stale white bread in a blender. The stale '
    'bread acts as a natural thickener and an emulsifier, giving the gazpacho a beautifully smooth, slightly velvety '
    'texture rather than a thin, watery one.'),
   (2,
    'Add the sherry vinegar',
    'Add sherry vinegar, garlic and salt, then blend to a completely smooth puree. Sherry vinegar’s nutty, slightly '
    'oxidised character adds a depth of flavour that ordinary wine vinegar or balsamic cannot replicate — it is what '
    'gives Andalusian gazpacho its distinctive, complex taste.'),
   (3,
    'Emulsify with olive oil',
    'With the blender running, slowly stream in excellent extra-virgin olive oil. This technique emulsifies the oil '
    'into the vegetable puree, creating a soup with body and richness that turns it from a thin vegetable juice into '
    'something truly luxurious.'),
   (4,
    'Season and taste',
    'Season generously with salt and taste for balance — it should be bright, cold and intensely flavoured, as '
    'chilling will mute the flavours slightly. Whatever tastes perfect at room temperature will taste slightly flat '
    'from the fridge, so season boldly.'),
   (5,
    'Chill for at least 2 hours',
    'Pass through a fine sieve for extra smoothness, then chill for a minimum of 2 hours. Resting in the refrigerator '
    'does more than just cool the soup — it allows the flavours to meld and develop, the olive oil to fully integrate, '
    'and the bread to disappear entirely into the texture.'),
   (6,
    'Prepare the garnishes',
    'Dice cucumber, tomato and pepper into tiny cubes (brunoise) and set aside. The small, precise garnish cubes — '
    'placed on top of the smooth gazpacho at serving — provide textural contrast and a fresh visual presentation that '
    'turns a simple soup into an elegant dish.'),
   (7,
    'Serve ice cold',
    'Pour the icy gazpacho into chilled bowls, scatter the brunoise and drizzle with more olive oil. Gazpacho is one '
    'of the few soups that is not only acceptable but actually perfect at fridge temperature — the cold amplifies its '
    'refreshing quality and makes it the ideal dish for a hot summer day.')],
  ['🍅 Use the ripest, most flavourful tomatoes you can find — the tomato is the star of gazpacho and its quality '
   'determines everything.',
   '🧄 Do not skip the stale bread — it is the secret to gazpacho’s signature smooth, velvety body rather than a thin '
   'vegetable juice.',
   '🟡 Use your finest extra-virgin olive oil — it gets blended raw into the soup and its flavour is front and centre.'],
  ['Gazpacho is extraordinarily rich in lycopene from the raw tomatoes — one of the most powerful antioxidants '
   'associated with cancer prevention.',
   'Being entirely raw, it retains 100% of the vitamins C and folate that cooking would destroy.',
   'Olive oil provides oleocanthal, a natural compound with anti-inflammatory effects similar to ibuprofen.'],
  ['Very high in vitamin K from the olive oil — those on blood thinners should be mindful of portion sizes.',
   'Gazpacho is relatively high in sodium if seasoned generously — taste before adding salt at the table.']),
 ('Chicken Paella',
  '🥘',
  'comfort',
  'Fragrant saffron-stained bomba rice cooked with chicken, smoked paprika and rich sofrito in a wide paella pan until '
  'the legendary socarrat — the treasured crispy rice crust — forms at the bottom. A spectacular dish that commands '
  'attention!',
  '55 minutes',
  6,
  'Medium',
  3,
  'Balanced Comfort',
  [(1,
    'Make the sofrito',
    'Cook finely diced onion, tomato and red pepper in olive oil over very low heat for 30 minutes until collapsed and '
    'sweet. Sofrito is the flavour foundation of Spanish cooking and must not be rushed — the long, gentle cooking '
    'breaks down the vegetables and caramelises their sugars into a concentrated, sweet-savoury paste.'),
   (2,
    'Bloom the saffron',
    'Steep saffron threads in a cup of warm stock for 10 minutes. This step extracts the brilliant orange colour and '
    'distinctive honey-like aroma of the saffron into the liquid, which then distributes evenly throughout the rice — '
    'simply adding saffron threads directly gives uneven colour and flavour.'),
   (3,
    'Brown the chicken',
    'Season chicken pieces and sear in the paella pan until deeply golden on all sides. A proper paella is made in a '
    'wide, shallow pan to maximise the surface area for evaporation and socarrat formation — the prized crispy rice '
    'crust at the bottom that is the mark of a masterful paella.'),
   (4,
    'Add the bomba rice and spread evenly',
    'Add the bomba rice to the pan, stir once to coat in the sofrito and chicken fat, then spread in a single even '
    'layer. Bomba rice is a short-grain variety from Valencia that absorbs three times its volume in liquid without '
    'bursting — after this initial stir, you must not stir again or you will break the starch structure essential for '
    'socarrat.'),
   (5,
    'Add the saffron stock and do not stir',
    'Pour the saffron-infused stock over the rice and shake the pan to distribute evenly. From this moment until the '
    'paella is done, do not stir — the undisturbed layer of rice at the bottom is slowly toasting against the hot pan, '
    'creating the socarrat that every serious paella enthusiast considers the crowning jewel.'),
   (6,
    'Cook on high then low heat',
    'Cook over high heat for 10 minutes, then reduce to medium-low for 8 minutes until the stock is absorbed. The '
    'initial high heat brings everything to the boil and starts the cooking, while the reduced heat allows the rice to '
    'finish gently and the socarrat to form slowly without burning.'),
   (7,
    'Rest under newspaper',
    'Remove from the heat, cover loosely with newspaper or foil and rest for 5 minutes. Newspaper is the traditional '
    'cover because it absorbs steam, preventing the socarrat from going soggy while the rice finishes steaming in '
    'residual heat to perfection.'),
   (8,
    'Serve directly from the pan',
    'Bring the paella pan directly to the table and serve. Paella is not plated individually in Spain — it is shared '
    'directly from the pan, with each person eating from their segment. This communal ritual is as important to the '
    'experience as the food itself.')],
  ['🧁 Never stir the paella once the stock is added — the socarrat forms only when the rice stays in undisturbed '
   'contact with the hot pan base.',
   '🇪🇸 Use proper bomba or calasparra rice — regular risotto or long-grain rice will not produce the characteristic '
   'texture or socarrat.',
   '💛 Bloom the saffron in warm (not boiling) water — boiling water destroys the delicate volatile aromatics that make '
   'saffron so special.'],
  ['Chicken provides lean protein and is a good source of niacin (B3) and phosphorus.',
   'Saffron contains safranal and crocin, compounds with antioxidant and potential mood-lifting properties.',
   'Bomba rice has a lower glycaemic index than most other white rice varieties due to its unique starch structure.'],
  ['Paella is traditionally quite high in sodium from the chicken stock and seasoning — use low-sodium stock if '
   'watching salt intake.',
   'A generous paella serving is high in carbohydrates — balance with a simple green salad to complete the meal.']),
 ('Tortilla Española',
  '🥚',
  'quick',
  'Spain’s iconic potato omelette — thinly sliced potato slow-confited in olive oil, combined with beaten eggs and '
  'cooked to a golden, just-set masterpiece with a legendary wobble in the centre. Simple perfection in 20 minutes!',
  '20 minutes',
  4,
  'Easy',
  3,
  'Balanced & Quick',
  [(1,
    'Slice and confit the potato',
    'Peel and slice potato thinly and cook gently in abundant olive oil over low heat until completely tender but not '
    'coloured, about 15 minutes. This slow confit in oil is what makes Spanish tortilla different from a regular '
    'potato omelette — the potato absorbs the oil and becomes meltingly soft and flavoured throughout.'),
   (2,
    'Drain and season',
    'Lift the potato from the oil with a slotted spoon, season generously with salt and leave to cool slightly. '
    'Seasoning while still warm allows the salt to penetrate into the starchy potato rather than sitting on the '
    'surface, and cooling slightly prevents the egg mixture from cooking prematurely when combined.'),
   (3,
    'Beat the eggs',
    'Beat 6 eggs until just combined and add the potato, pressing down so every slice is coated. The egg to potato '
    'ratio is crucial — enough egg to bind but not so much that it becomes a frittata. The potato should poke through '
    'the surface when the mixture is added to the pan.'),
   (4,
    'Cook the first side',
    'Pour the mixture into a warm, oiled pan and cook over medium-low heat until the edges are set and the centre '
    'wobbles like jelly. Patience at this stage is rewarded — cooking too fast will brown the outside while leaving '
    'the inside raw. The wobble tells you the centre is still custardy and ready for the flip.'),
   (5,
    'The legendary flip',
    'Place a large plate over the pan, flip confidently in one swift motion, then slide back into the pan. The flip is '
    'the moment that separates a competent cook from a tortilla master — commit fully, move fast and the tortilla will '
    'slide perfectly. Hesitation causes disaster.'),
   (6,
    'Cook the second side and rest',
    'Cook for 3–4 more minutes until set but still with a slight jiggle, then slide onto a plate and rest for 10 '
    'minutes. The resting time is not optional — it allows the residual heat to finish cooking the centre to that '
    'prized custardy consistency that is the hallmark of a perfect tortilla española.')],
  ['🧄 Confit the potato slowly in plenty of oil — the potato must be completely submerged to cook evenly and absorb '
   'the oil’s flavour throughout.',
   '🥚 Beat the eggs minimally — over-beaten eggs produce a tougher, less custardy tortilla than gently combined ones.',
   '🍳 Serve at room temperature rather than hot — the flavours are more pronounced and the texture is more custardy '
   'when slightly cooled.'],
  ['Eggs provide complete protein, vitamin D and choline, an important nutrient for brain health.',
   'Potatoes are an excellent source of potassium, vitamin C and resistant starch (when cooled).',
   'A satisfying, protein-rich dish that is naturally gluten-free.'],
  ['The generous olive oil used for confiting the potato makes this a calorie-dense dish despite its simple '
   'appearance.',
   'Eggs are high in dietary cholesterol, though evidence suggests this has minimal impact on blood cholesterol for '
   'most people.'])]


_RAW['greek'] = [('Greek Salad with Grilled Halloumi',
  '🧀',
  'healthy',
  'A generous platter of chunky tomatoes, cool cucumber, kalamata olives and crumbled feta topped with golden, squeaky '
  'grilled halloumi and a shower of dried oregano. This is the Mediterranean diet in its purest, most delicious form!',
  '15 minutes',
  4,
  'Easy',
  5,
  'Super Nutritious',
  [(1,
    'Prepare the salad vegetables',
    'Chop tomatoes into chunky wedges, slice cucumber thickly, halve the olives and cut red onion into thin rings. A '
    'Greek salad is never finely chopped — the large, rustic cuts preserve the juice and texture of each vegetable and '
    'create a salad that feels abundant and generous rather than dainty.'),
   (2,
    'Make the oregano dressing',
    'Whisk together extra-virgin olive oil, red wine vinegar, dried Greek oregano and a pinch of salt. Greek dried '
    'oregano (rigani) has a more intense, earthy flavour than Italian oregano — it is the unmistakable aroma of the '
    'Greek countryside and the defining herb of this salad.'),
   (3,
    'Grill the halloumi',
    'Slice halloumi and grill or griddle over high heat for 2 minutes per side until golden with attractive char '
    'marks. Halloumi has a uniquely high melting point due to its low acid content — it holds its shape under heat and '
    'develops a golden, slightly crisp exterior while the interior becomes warm and squeaky.'),
   (4,
    'Assemble the salad',
    'Arrange the vegetables in a wide bowl or platter, place the halloumi slices on top and crumble the feta '
    'generously over everything. Feta should be crumbled, not diced — crumbling creates irregular pieces of varying '
    'sizes that distribute unevenly and melt into the dressing in a way that neat cubes never do.'),
   (5,
    'Dress and finish',
    'Pour the oregano dressing over the salad and give everything a very gentle toss. A heavy hand here is the enemy — '
    'you want to coat rather than drown, preserve the large pieces rather than turn them into mush.'),
   (6,
    'Eat with warm pita',
    'Serve immediately with warm, charred pita bread for scooping. Warm pita is essential — cold pita is tough and '
    'chewy, while warm pita is pillowy, slightly smoky and the perfect vehicle for the salty feta, juicy tomato and '
    'herby dressing.'),
   (7,
    'Drizzle with more olive oil',
    'A final, generous drizzle of your best Greek olive oil over the halloumi just before serving. Greek extra-virgin '
    'olive oil from the Peloponnese has a distinctively peppery, herbaceous character that finishes this dish and '
    'brings every element together.')],
  ['🧀 Do not refrigerate feta before serving — cold feta is dense and flavourless, while room-temperature feta is '
   'creamy, pungent and delicious.',
   '🧀 Halloumi should be eaten immediately while hot — cooled halloumi turns rubbery and loses its appealing squeaky '
   'texture.',
   '🌿 Use dried Greek oregano (rigani) rather than Italian — the flavour difference is significant and makes the salad '
   'taste authentically Greek.'],
  ['Olive oil is at the heart of the Mediterranean diet and provides powerful antioxidant polyphenols.',
   'Feta is lower in calories than most other cheeses and provides calcium and protein.',
   'Tomatoes are an excellent source of lycopene, vitamin C and potassium.'],
  ['Feta and halloumi are both high in sodium — do not add extra salt to the dressing without tasting first.',
   'Halloumi is high in saturated fat compared to most other salad proteins — a smaller portion alongside more '
   'vegetables creates a better nutritional balance.']),
 ('Lamb Moussaka',
  '🥘',
  'comfort',
  'Silky fried aubergine layered with cinnamon-spiced lamb mince and a luscious, golden-crusted béchamel, baked until '
  'deeply comforting and fragrant. This iconic Greek baked dish is the definition of love on a plate — best made for a '
  'crowd!',
  '80 minutes',
  8,
  'Medium',
  2,
  'Indulgent Treat',
  [(1,
    'Slice and salt the aubergines',
    'Cut aubergines into 1cm slices, salt generously and leave for 30 minutes in a colander. Salting draws out bitter '
    'juices and excess moisture — less moisture means the aubergine will absorb less oil during frying and develop a '
    'firmer, silkier texture in the final dish.'),
   (2,
    'Fry the aubergine slices',
    'Pat the aubergine dry and fry in batches in hot olive oil until golden on both sides. Do not rush this step — '
    'properly fried aubergine should be golden, slightly collapsed and almost jammy in texture, which is what creates '
    'the silky layers that define a great moussaka.'),
   (3,
    'Brown the lamb mince with aromatics',
    'Fry onion until golden, add lamb mince and brown well, then add cinnamon, allspice, tomatoes and a little red '
    'wine. The use of cinnamon in a savoury lamb mince is quintessentially Greek — it adds a warmth and fragrant '
    'complexity that transforms ordinary mince into something evocative of sun-drenched Greek cooking.'),
   (4,
    'Simmer the lamb sauce',
    'Simmer the lamb sauce until thick and aromatic, about 20 minutes. A well-reduced lamb sauce is essential — a '
    'watery sauce will create a soupy moussaka that collapses when cut. The sauce should be thick enough to hold its '
    'shape when spooned.'),
   (5,
    'Make the béchamel',
    'Make a thick béchamel with butter, flour and warm milk, season with nutmeg, and beat in egg yolks. Adding egg '
    'yolks to the béchamel creates a richer, more stable sauce that sets firmly in the oven to create the distinctive, '
    'golden crust that makes a moussaka look so magnificent when sliced.'),
   (6,
    'Layer the moussaka',
    'In a deep baking dish, layer aubergine, then lamb sauce, another layer of aubergine, then the béchamel. The '
    'layering is more than aesthetic — the aubergine acts as a barrier between the meat sauce and the béchamel, '
    'preventing the latter from curdling from the acidity of the tomatoes.'),
   (7,
    'Bake until golden',
    'Bake at 180°C for 40–45 minutes until the béchamel is deeply golden and the dish is bubbling at the edges. The '
    'long bake allows the layers to set completely and for the top béchamel crust to form a firm, gratinated surface '
    'that holds the beautiful slice together when served.'),
   (8,
    'Rest before serving',
    'Rest for at least 20 minutes before cutting. This resting time is absolutely crucial — hot moussaka is a '
    'beautiful mess of molten béchamel and soft aubergine. Allowing it to set means you get a glorious, neat slice '
    'that shows off all those gorgeous layers.')],
  ['🥦 Salt the aubergine for the full 30 minutes — this step cannot be skipped without a significant impact on the '
   'final texture and oil absorption.',
   '🍳 Beat the egg yolks into the béchamel only after it has cooled slightly — adding them to a boiling sauce will '
   'scramble them and ruin the texture.',
   '🧀 Moussaka is far better the next day, reheated — the layers set completely overnight and slice beautifully.'],
  ['Lamb provides complete protein, iron and zinc, nutrients particularly important for women and athletes.',
   'Aubergine is very low in calories and provides nasunin, a powerful antioxidant found in the skin.',
   'Cinnamon has been shown to have blood sugar-regulating properties in multiple studies.'],
  ['The béchamel and lamb mince make this a calorie-dense, high-saturated-fat dish — a celebratory meal rather than an '
   'everyday one.',
   'The recipe requires multiple stages of preparation — plan for at least 90 minutes from start to table.']),
 ('Chicken Souvlaki Wraps',
  '🌯',
  'quick',
  'Marinated chicken skewers grilled to charred perfection, wrapped in warm pita with cooling tzatziki, fresh tomato '
  'and red onion. Greek street food at its absolute finest — simple, protein-packed and ready in 20 minutes!',
  '20 minutes',
  4,
  'Easy',
  4,
  'Fresh & Nutritious',
  [(1,
    'Marinate the chicken',
    'Combine chicken breast or thighs with olive oil, lemon juice, garlic, oregano and salt for a minimum of 15 '
    'minutes. Even a brief marinade transforms chicken — the acid in the lemon begins to denature the surface '
    'proteins, allowing flavour to penetrate while also slightly tenderising the outer layer.'),
   (2,
    'Thread onto skewers',
    'Thread the marinated chicken onto metal or pre-soaked wooden skewers, packing tightly. Packing the chicken '
    'tightly on the skewer means the pieces insulate each other, keeping the inside moist while the outside chars and '
    'caramelises on the grill.'),
   (3,
    'Grill over high heat',
    'Grill or griddle the souvlaki over high heat, turning every 2 minutes for 8–10 minutes total. Frequent turning '
    'ensures even cooking on all sides and prevents the outside from burning before the centre is cooked — the char '
    'you develop on each surface adds the characteristic smoky flavour of great Greek street food.'),
   (4,
    'Warm the pita',
    'Warm pita directly over a gas flame or in a dry hot pan until lightly charred. The slight char on pita is not '
    'just visual — it adds a smoky depth that complements the lemony, herby chicken and provides a textural contrast '
    'to the soft tzatziki.'),
   (5,
    'Make quick tzatziki',
    'Grate cucumber, squeeze out excess liquid, and combine with strained yogurt, garlic, dill and a drizzle of olive '
    'oil. Squeezing out the cucumber’s water is the critical step — omitting it produces a watery tzatziki that '
    'immediately soaks through the pita, while properly drained tzatziki stays thick and creamy.'),
   (6,
    'Assemble and serve',
    'Slide chicken off skewers, wrap in warm pita with tzatziki, sliced tomato and red onion. Souvlaki is street food '
    'in its purest form — eat it standing up, let the tzatziki drip and enjoy the combination of charred meat, cool '
    'yogurt and fresh vegetables that has sustained Greeks for millennia.')],
  ['🍋 Marinate for as long as possible — even 1 hour in the fridge transforms the depth of flavour dramatically '
   'compared to 15 minutes.',
   '🧀 Use Greek strained yogurt for the tzatziki — regular yogurt is too liquid and produces a runny sauce no matter '
   'how much cucumber you squeeze out.',
   '🌿 Dried Greek oregano is the key herb in the marinade — do not substitute with fresh oregano as the flavour '
   'profile is entirely different.'],
  ['Chicken provides lean, complete protein and is an excellent source of selenium and B vitamins.',
   'Greek yogurt in the tzatziki provides probiotics, protein and calcium.',
   'A balanced meal combining protein, carbohydrates and healthy fats in excellent proportions.'],
  ['Pita bread is a refined carbohydrate — use wholemeal pita for extra fibre and a lower glycaemic response.',
   'Marinating in olive oil adds calories — use a light hand and drain well before grilling.'])]


_RAW['middle_eastern'] = [
    ('Falafel & Golden Tabbouleh Bowl', '🥙', 'healthy',
     'Herb-packed falafel balls served over a bright, lemony tabbouleh of bulgur, fresh parsley, mint and tomato, finished with a generous drizzle of nutty tahini. This is the Middle Eastern mezze tradition at its most nourishing and gloriously delicious!',
     '35 minutes', 4, 'Medium', 5, 'Incredibly Nutritious',
     [(1, 'Soak the chickpeas', 'Cover dried chickpeas in cold water and soak for 24 hours. Using dried, soaked chickpeas rather than tinned is the most important step in falafel — canned chickpeas have been cooked until their starch has gelatinised, making falafel that is dense and doughy instead of light, crunchy and airy.'),
      (2, 'Make the falafel mixture', 'Drain the chickpeas without cooking and blend with herbs, onion, garlic, cumin and baking powder to a coarse paste. The raw chickpea starch will set and expand during frying, creating the characteristic light, airy interior, while the herbs keep the colour a beautiful, vibrant green throughout.'),
      (3, 'Rest and shape', 'Rest the mixture in the refrigerator for 30 minutes, then shape into small balls or patties. The refrigerator rest allows the mixture to firm up, making it much easier to shape without crumbling, and lets the baking powder begin its work before it hits the hot oil.'),
      (4, 'Fry until crispy', 'Fry in oil at 175°C for 3–4 minutes until deeply golden and crunchy. The exact temperature matters — too low and they absorb oil and turn greasy; too high and they brown outside before cooking through. The perfect falafel shatters on impact and reveals a vibrant herb-green interior.'),
      (5, 'Make the tabbouleh', 'Soak fine bulgur in boiling water for 15 minutes, then drain and mix with mountains of fresh parsley, mint, tomato, lemon and olive oil. True Lebanese tabbouleh is primarily a herb salad with a little grain — the ratio is opposite to most Western versions, with far more parsley than bulgur.'),
      (6, 'Make the tahini sauce', 'Whisk tahini with lemon juice, garlic and water until smooth and pourable. The lemon makes the tahini temporarily seize and thicken — keep adding water a tablespoon at a time and it will relax into a smooth, velvety sauce. The ratio of lemon to tahini is what makes the sauce bright rather than heavy.'),
      (7, 'Assemble the bowl', 'Arrange tabbouleh in bowls, top with hot falafel and drizzle generously with tahini sauce and a sprinkle of sumac. The warm falafel against the cool, herby tabbouleh and the rich, creamy tahini creates a perfect contrast of temperatures, textures and flavours that makes every forkful genuinely exciting.'),
      (8, 'Finish with pickles', 'Add pickled turnips, cucumber or chilli alongside and a final squeeze of lemon. The pickles cut through the richness of the tahini and the oiliness of the falafel, providing the brightness that keeps the entire bowl from feeling heavy — a crucial element of the Middle Eastern mezze tradition.')],
     ['🧆 Never use tinned chickpeas for falafel — the starch structure of raw soaked chickpeas is what creates the proper light, airy texture.',
      '🌿 Be generous with the parsley and mint in both the falafel and the tabbouleh — the herbs are the soul of both dishes.',
      '🍋 Add lemon juice generously to both the tabbouleh and the tahini — acidity is what makes both dishes sing rather than taste flat.'],
     ['Chickpeas are an excellent plant-based source of protein, fibre and iron.',
      'Fresh parsley in tabbouleh provides exceptionally high levels of vitamin C and K.',
      'Tahini delivers healthy fats, calcium and all essential amino acids.'],
     ['Deep-frying adds significant calories — for a lighter version, brush with oil and bake at 200°C for 20 minutes.',
      'The 24-hour chickpea soak requires advance planning — not a spontaneous weekday meal.']),
    ('Slow-Braised Lamb & Chickpea Stew', '🍲', 'comfort',
     'Tender chunks of lamb shoulder slow-braised with chickpeas, tomatoes and a warm baharat spice blend until the sauce is deeply fragrant and the meat falls apart at a glance. Served with warm flatbread for scooping — deeply comforting and utterly spectacular!',
     '75 minutes', 6, 'Medium', 2, 'Indulgent Treat',
     [(1, 'Toast and make baharat', 'Toast cumin, coriander, paprika, cinnamon, black pepper, cardamom and nutmeg in a dry pan for 60 seconds until fragrant. Making your own baharat from freshly toasted whole spices produces an incomparably more complex and aromatic blend than any pre-ground jar — the essential oils you smell during toasting are exactly the flavour compounds you are activating.'),
      (2, 'Brown the lamb', 'Cut lamb shoulder into large chunks, season with salt and the baharat, then brown deeply in oil over high heat. The Maillard reaction at this stage creates a crust packed with hundreds of complex flavour compounds that will slowly dissolve into the braising liquid, enriching the entire stew with extraordinary meaty depth.'),
      (3, 'Build the aromatic base', 'In the same pot, fry onion until golden, add garlic, tomato paste and the remaining baharat and cook for 2 minutes. Cooking the tomato paste in the hot oil causes it to caramelise and darken, transforming its raw, sharp flavour into a sweet, complex, umami-rich base that forms the backbone of the stew.'),
      (4, 'Add tomatoes and stock', 'Add crushed tomatoes and lamb or chicken stock, return the browned lamb and bring to a simmer. The acidity from the tomatoes will begin to break down the collagen in the lamb shoulder during the long braise, contributing to the silky, full-bodied texture of the final sauce.'),
      (5, 'Add chickpeas and braise', 'Stir in cooked chickpeas, cover and braise gently for 1 hour until the lamb is falling tender. The chickpeas absorb the spiced, meaty braising liquid and take on an extraordinary depth of flavour that plainly cooked chickpeas can never achieve — they become the most flavourful chickpeas you have ever eaten.'),
      (6, 'Finish with preserved lemon', "Stir in sliced preserved lemon and fresh coriander. Preserved lemon's intense, fermented citrus punch is the defining flavour accent of North African and Middle Eastern braises — it cuts through the richness of the lamb fat and lifts every element of the dish with its extraordinary, complex citrus character."),
      (7, 'Serve with flatbread', 'Ladle the stew into wide bowls and serve with warm flatbread or rice. The flatbread is not merely an accompaniment — it is the vehicle by which the extraordinary braising sauce is conveyed to your mouth. Tearing bread and scooping is a deeply communal, joyful way to eat.'),
      (8, 'Garnish and rest', 'Top with a dollop of yogurt, a drizzle of chilli oil and extra coriander. The cool yogurt melts into the hot stew, adding a gentle dairy tang that balances the warm spices, while the chilli oil adds a final layer of heat that keeps the flavour building right through the last mouthful.')],
     ['🌶 Toast your own spices for the baharat — the difference between freshly toasted and pre-ground is remarkable and worth every extra minute.',
      '🧀 Preserved lemon is the single most important finishing ingredient — it is what makes this taste unmistakably Middle Eastern.',
      '🍲 Brown the lamb in batches without crowding the pot — a crowded pan steams instead of sears, and you want maximum crust, not maximum steam.'],
     ['Lamb is an excellent source of complete protein, iron, zinc and B12.',
      'Chickpeas double the fibre and plant protein content, making this an exceptionally nutritious dish.',
      'Baharat spices including cinnamon and cardamom have well-documented anti-inflammatory properties.'],
     ['Lamb shoulder is high in saturated fat — a wonderful occasional dish rather than an everyday meal.',
      'Requires 1+ hour of active simmering — this is a weekend dish that rewards patience.']),
    ("Za'atar Hummus & Warm Flatbread Mezze", '🫓', 'quick',
     "A generous spread of silky za'atar-topped hummus with warm flatbreads, cucumber, cherry tomatoes, olives and creamy labneh — the Middle Eastern mezze tradition assembled in 10 minutes. Sociable, nourishing and genuinely wonderful!",
     '10 minutes', 4, 'Easy', 4, 'Light & Nutritious',
     [(1, 'Make the hummus', 'Blend tinned chickpeas with tahini, lemon juice, garlic and ice water until smooth and airy. Adding ice water — cold, not room temperature — makes a dramatic difference to hummus texture, producing a lighter, more airy, smoother result. The goal is a hummus that is far more voluptuous and silky than anything that comes from a supermarket tub.'),
      (2, 'Season the hummus', 'Season generously with salt, taste, and adjust with more lemon if needed. Hummus should taste bright and nutty, not flat and heavy — if it tastes dull, it needs more lemon juice and salt. Blend for a full 3 minutes for the silkiest possible texture; most home cooks under-blend by a significant margin.'),
      (3, "Make za'atar oil", "Combine za'atar, dried sumac and excellent olive oil in a small bowl and stir. Za'atar is an ancient spice blend of dried thyme, sesame and sumac — its herby, sesame, citrus character complements hummus beautifully and adds a layer of complexity to a simple plate that makes it feel special and considered."),
      (4, 'Plate the hummus', 'Spread hummus on a large flat plate using the back of a spoon to create a wide well in the centre. The classic Middle Eastern way to present hummus is spread flat with a well in the centre — this creates the right surface area for the olive oil topping to pool in and be scooped up with bread.'),
      (5, "Add the za'atar oil", "Pour the za'atar oil generously into the hummus well and scatter with a pinch of paprika. The olive oil soaks into the surface of the hummus and carries the za'atar's aromatics throughout — every scoop of bread brings up hummus, oil and herb together in a perfect combination."),
      (6, 'Warm the flatbreads', 'Heat flatbreads directly over a gas flame or in a dry pan until warm and lightly charred. A warm flatbread is entirely different from a cold one — it becomes soft, slightly smoky and pliable, perfect for tearing and scooping. The slight char edges are as desirable as they are inevitable.'),
      (7, 'Arrange the mezze', 'Arrange the warm flatbreads, sliced cucumber, cherry tomatoes, olives and labneh around the hummus. A mezze plate is about abundance and variety — the different flavours mean every bite is a different experience, and the shared format makes eating together a pleasure.')],
     ["🧈 Blend the hummus for a full 3 minutes — under-blending is the most common reason home hummus is never as smooth as restaurant hummus.",
      "🫒 Use extra-virgin olive oil generously — it is the principal flavour of the za'atar topping.",
      '❄️ Use ice water, not room temperature water, when blending the hummus — the cold temperature produces a noticeably lighter, more airy texture.'],
     ['Chickpeas are an excellent source of plant protein, fibre and folate.',
      'Tahini provides calcium and all essential amino acids, making hummus a nutritionally complete plant protein.',
      'Extra-virgin olive oil delivers heart-protective polyphenol antioxidants.'],
     ['Shop-bought hummus is far higher in sodium and thickeners than homemade — making it from scratch is always healthier.',
      'High in calories from olive oil and tahini — a moderate portion alongside vegetables creates the best nutritional balance.']),
]

_RAW['korean'] = [
    ('Bibimbap Rainbow Rice Bowl', '🍲', 'healthy',
     "A magnificent rainbow rice bowl of individually seasoned vegetables, marinated beef, a golden sunny-side egg and fiery gochujang sauce, arranged like a painting over fluffy short-grain rice. Korea's most iconic dish is a nourishing, visually stunning celebration of contrasts!",
     '35 minutes', 2, 'Medium', 5, 'Super Nutritious',
     [(1, 'Cook the short-grain rice', 'Rinse short-grain rice until the water runs clear and cook with a 1:1.2 ratio of water until perfectly fluffy. The excess starch rinsed away prevents the grains from sticking together in a gluey mass, while the precise water ratio ensures each grain is separate but tender — the essential base that carries all the other flavours.'),
      (2, 'Prepare the namul vegetables', 'Blanch and season each vegetable separately: spinach with sesame oil and garlic, beansprouts with soy, carrots with sesame. Seasoning each vegetable individually rather than together is the fundamental philosophy of bibimbap — each component has its own distinct flavour and purpose, and combining them too early blurs their individual characters.'),
      (3, 'Marinate and cook the beef', 'Slice beef thin against the grain and marinate in soy, sesame oil, garlic and a pinch of sugar for 15 minutes. The sugar acts as a tenderiser and promotes caramelisation on contact with the hot pan, while the sesame oil adds a characteristic nutty fragrance that is the backbone of Korean bulgogi flavour.'),
      (4, 'Make the gochujang sauce', 'Combine gochujang paste with sesame oil, rice vinegar, a little sugar and garlic into a smooth, glossy sauce. Gochujang is a fermented chilli paste that provides not just heat but extraordinary depth — the fermentation adds umami and complexity that fresh chilli alone can never achieve, making the sauce far more interesting than its simple ingredients suggest.'),
      (5, 'Fry the egg', 'Fry an egg until the white is set but the yolk is still runny. The runny yolk is not merely traditional — when you mix the bibimbap with the gochujang sauce, the yolk breaks and enriches the rice with a silky, fatty, golden coating that binds all the separate components together into a unified, extraordinary dish.'),
      (6, 'Arrange the bowl', 'Place rice in the centre of a wide, warm bowl and arrange each seasoned vegetable in a separate sector around the rice. The radial arrangement is the visual language of bibimbap and a genuine expression of care — each ingredient has its place, each colour is separate, and the bowl looks like art before the first bite.'),
      (7, 'Top and serve', "Place the beef and fried egg on top and serve with gochujang sauce on the side. The serving at table — with the sauce on the side to be added according to each diner's heat tolerance — is an important aspect of Korean hospitality. The diner completes the dish themselves, mixing everything together at the table."),
      (8, 'Mix vigorously', 'Add gochujang sauce to taste and mix the entire bowl vigorously with a spoon until every grain of rice is coated in the red sauce and the yolk has emulsified through everything. The mixing is as important as the preparation — bibimbap means \"mixed rice\" and the vigorous combination is when the dish truly becomes itself, all those separate flavours merging into one extraordinary whole.')],
     ['🍳 A runny egg is non-negotiable — the yolk is what binds all the components together when you mix the bibimbap at the table.',
      '🌶 Add gochujang to your own taste — start with less, mix well, then add more. The heat builds as you eat.',
      '🥢 Season each vegetable topping separately — this individual seasoning is what gives bibimbap its extraordinary complexity despite using simple ingredients.'],
     ['A diverse range of vegetables means an exceptional array of vitamins, minerals and antioxidants in a single bowl.',
      'Fermented gochujang provides beneficial probiotics and B vitamins from the fermentation process.',
      'Short-grain rice, beef and egg contribute carbohydrates, complete protein and healthy fats — a balanced macronutrient profile.'],
     ['Gochujang is moderately high in sodium — use in moderation if watching salt intake.',
      'The multiple vegetable preparations make this a multi-step cook — efficient mise en place is essential for a calm experience.']),
    ('Kimchi Jjigae (Kimchi & Tofu Stew)', '🍲', 'comfort',
     "A ferociously flavourful Korean stew of well-fermented kimchi, silken tofu and pork belly simmered in a rich, brick-red broth that warms the soul from the inside out. Korea's most beloved comfort dish is unashamedly bold, deeply savoury and completely irresistible!",
     '30 minutes', 2, 'Easy', 3, 'Balanced Comfort',
     [(1, 'Choose well-fermented kimchi', 'Use kimchi that has been fermenting for at least 2–3 weeks — the sourer, the better for this stew. Well-fermented kimchi has significantly more depth and complexity than fresh kimchi, with lactic acid that creates the characteristic savoury-sour backbone of jjigae that fresh kimchi simply cannot provide.'),
      (2, 'Fry the pork and kimchi', "Fry sliced pork belly over medium-high heat until lightly golden, then add kimchi and fry together for 5 minutes. Frying the kimchi in the pork fat before adding liquid is the most important step — it concentrates the kimchi's flavour and allows the kimchi paste to caramelise slightly, creating a depth that simmering from raw can never achieve."),
      (3, 'Add the kimchi juice', 'Pour in the juice from the kimchi jar along with gochugaru and gochujang. Kimchi juice is liquid gold — it is essentially a concentrated, flavoured, probiotic-rich brine that provides the distinctive sour, spicy, funky character that is the essence of jjigae. Never discard it.'),
      (4, 'Add stock and simmer', 'Add enough water or stock to just cover everything and bring to a vigorous simmer. The Korean preference for jjigae is a broth that is intense and concentrated rather than thin — the brief cook time and reduced amount of liquid produces a stew that is bold and punchy rather than watery and mild.'),
      (5, 'Add tofu and spring onion', 'Slide cubed silken or firm tofu gently into the simmering broth and add sliced spring onion. Tofu is added late and handled gently because it is delicate — vigorous boiling will break it into unattractive crumbles. The tofu absorbs the spiced, sour broth beautifully, becoming deeply flavoured and providing a cool, creamy contrast to the fiery kimchi.'),
      (6, 'Season and serve in the pot', 'Taste and adjust the broth with soy sauce and sesame oil, then bring the pot directly to the table. Jjigae is traditionally served in the same earthenware pot (dolsot) it was cooked in — the pot retains heat and keeps the stew bubbling at the table, which is part of the theatre and pleasure of eating this remarkable dish.')],
     ['🥬 Older, more sour kimchi produces a far superior jjigae — if your kimchi is fresh and mild, add more gochujang and a splash of rice vinegar to compensate.',
      '🌶 Gochugaru (Korean chilli flakes) is what gives jjigae its distinctive, fruity heat — it is worth finding in an Asian grocery rather than substituting with regular chilli flakes.',
      '🥩 The pork belly fat is essential for the richness of the broth — do not substitute with lean pork or the stew will lose significant body and flavour.'],
     ['Kimchi is a probiotic food rich in beneficial lactobacillus bacteria that support gut health.',
      'Tofu provides plant-based protein and calcium with very few calories.',
      'Gochugaru contains capsaicin, which may boost metabolism and has anti-inflammatory properties.'],
     ['Kimchi and soy sauce are both very high in sodium — this dish is not suitable for those on a strict low-salt diet.',
      'The fermented, spicy character of jjigae may not suit those with sensitive digestive systems — start with a smaller portion.']),
    ('Spicy Gochujang Egg & Rice Bowl', '🍳', 'quick',
     'A blazing, utterly satisfying Korean-style egg rice bowl with caramelised gochujang sauce, crispy fried egg, sesame and spring onion — the perfect 12-minute meal that punches well above its humble ingredient list!',
     '12 minutes', 1, 'Easy', 3, 'Balanced & Quick',
     [(1, 'Cook short-grain rice', 'Heat day-old or freshly steamed short-grain rice in a pan or microwave until hot and fluffy. Short-grain rice has a slightly stickier, more satisfying texture than long-grain — this gentle chewiness is what makes it so perfect for absorbing the bold gochujang sauce and provides a satisfying base that holds together when eaten with a spoon.'),
      (2, 'Make the gochujang sauce', 'Stir together gochujang, soy sauce, sesame oil and a pinch of sugar in a small bowl. This four-ingredient sauce is the engine of the entire bowl — the fermented heat of gochujang, the umami of soy, the nuttiness of sesame and the touch of sugar create a sauce far more complex and satisfying than its simplicity suggests.'),
      (3, 'Warm the sauce', 'Heat the gochujang sauce gently in a small pan for 1 minute until it sizzles and darkens slightly. Briefly heating the sauce caramelises the natural sugars and deepens the fermented flavour compounds in the gochujang, transforming the sauce from raw and sharp to rounded, glossy and deeply savoury.'),
      (4, 'Fry the egg', 'Fry an egg in a splash of oil over medium-high heat until the white is set and lightly crisped at the edges but the yolk is still completely runny. The crispy white edges provide textural contrast to the sticky rice, while the runny yolk is the entire point — it breaks over the rice and creates a rich, golden sauce that unifies the entire bowl.'),
      (5, 'Dress the rice', 'Pour the hot gochujang sauce over the rice and mix until every grain is coated in red. Use a spoon to fold and cut through the rice rather than stirring in circles, which ensures even coating without mashing the grains. The rice should be uniformly red and glistening.'),
      (6, 'Top and serve', 'Slide the fried egg onto the rice, scatter with sesame seeds and sliced spring onion, and eat immediately. The spring onion provides a fresh, sharp contrast to the deep, fermented heat of the gochujang, while the sesame seeds add a gentle nuttiness and textural interest that elevates this simple bowl into something genuinely craveable.')],
     ['🌶 Quality gochujang makes a significant difference — Korean brands like Bibigo or Haechandle are far more complex and flavourful than generic alternatives.',
      '🥚 The runny yolk is the key — overcooking the egg turns this from a luscious, silky bowl into a dry one. Watch the egg carefully.',
      '🧄 Add a grated clove of garlic to the gochujang sauce if you have it — the raw garlic adds a sharp, pungent kick that makes the sauce even more compelling.'],
     ['Eggs provide complete protein with all essential amino acids and are one of the best dietary sources of choline for brain health.',
      'Gochujang is a fermented food that provides beneficial probiotics and B vitamins.',
      'A genuinely fast, single-pan meal with minimal washing up.'],
     ['White rice is a refined carbohydrate with a high glycaemic index — using brown rice adds significantly more fibre and nutrients.',
      'Gochujang and soy sauce contribute significant sodium — watch portions if managing blood pressure.']),
]

_RAW['vietnamese'] = [
    ('Fragrant Chicken Pho', '🍜', 'healthy',
     'A clear, deeply aromatic broth perfumed with star anise, cinnamon and charred ginger, served over silky rice noodles with poached chicken and a generous plate of fresh herbs. The most nourishing, restorative bowl of soup you will ever encounter!',
     '40 minutes', 4, 'Medium', 5, 'Deeply Nourishing',
     [(1, 'Char the ginger and onion', 'Halve ginger and onion and char directly over a gas flame or under a very hot grill until blackened in spots. This charring step is the defining technique of pho broth — the char adds a complex, slightly smoky, sweet bitterness that transforms a good broth into an extraordinary one. Do not skip it.'),
      (2, 'Toast the aromatics', 'Toast star anise, cinnamon stick, cloves and cardamom in a dry pan until fragrant. Toasting the whole spices activates and concentrates their volatile aromatic oils, releasing a far more complex and intense fragrance than adding them raw — these spices are what give pho its instantly recognisable, ethereal aroma.'),
      (3, 'Simmer the broth', 'Combine the charred aromatics, toasted spices, chicken carcasses or stock, and simmer gently for 30 minutes with fish sauce and rock sugar. The slow simmer extracts every bit of flavour while keeping the broth crystal clear — a boiling broth will be cloudy, while a gently simmering one will be magnificently clear.'),
      (4, 'Poach the chicken', 'Add chicken thighs to the broth and poach gently at 80°C for 15 minutes. Poaching at this low temperature keeps the chicken extraordinarily tender and juicy. The collagen in the thighs also enriches the broth further as they cook, adding body and a silky mouthfeel.'),
      (5, 'Soak the rice noodles', 'Soak flat rice noodles in cold water for 30 minutes, then blanch briefly in boiling water for 30 seconds. Cold soaking pre-softens the noodles without making them mushy — they then need only a brief blanch to reach the perfect, silky, just-al-dente consistency that makes pho noodles so pleasing to eat.'),
      (6, 'Shred the chicken', 'Remove the poached chicken and shred into generous pieces. The slow, gentle poach produces chicken that shreds effortlessly into tender, flavour-saturated pieces — entirely different from dry, chewy chicken that has been boiled too vigorously.'),
      (7, 'Strain and season the broth', 'Pass the broth through a fine sieve and adjust seasoning with fish sauce and a little more rock sugar. The ideal pho broth is aromatic but balanced — the fish sauce provides the savoury depth, the sugar rounds out the spices, and the two together should never taste like either fish sauce or sugar, but like something far more ethereal and complex.'),
      (8, 'Assemble and serve', 'Divide noodles into bowls, top with shredded chicken and pour the sizzling broth over everything. Serve with bean sprouts, Thai basil, sliced chilli, hoisin and sriracha on the side. Pho is personalised at the table — each diner adjusts the herbs, heat and sauce to their own preference, making the bowl uniquely theirs.')],
     ['🔥 Char the ginger and onion until genuinely blackened — timidity here produces a pale, bland broth. The char is the soul of pho.',
      '⭐ Use whole star anise, not ground — whole spices infuse slowly and can be removed cleanly; ground spices would make the broth murky.',
      '🌿 Serve the herb plate generously — the fresh herbs added at the table are not garnish but an essential flavour component of the finished bowl.'],
     ['Bone broth is rich in collagen, gelatin and glycine, which support gut health and joint integrity.',
      'Rice noodles are gluten-free and easily digestible, making this an excellent meal for sensitive digestive systems.',
      'An extraordinarily restorative meal that is very low in calories relative to its satiety.'],
     ["Fish sauce is high in sodium — the broth's apparent lightness can be misleading from a salt perspective.",
      'The charring and long simmering time make this a more involved cook than it might appear at first glance.']),
    ('Caramelised Pork Belly Bánh Mì Bowl', '🍱', 'comfort',
     'Sticky, caramelised Vietnamese pork belly lacquered in fish sauce and palm sugar, served over jasmine rice with quick pickled carrots, fresh cucumber and a spoonful of sriracha mayo. The soul of bánh mì in a spectacular bowl!',
     '45 minutes', 4, 'Medium', 2, 'Indulgent Treat',
     [(1, 'Prepare the pork belly', 'Slice pork belly into 1cm pieces and score the fat cap. Scoring the fat cap allows the caramelised fish sauce and sugar to penetrate deeper into the fat and prevents the slices from curling dramatically as the fat contracts under high heat — producing a more even, elegant caramelised result.'),
      (2, 'Caramelise the sugar', 'Heat palm sugar or brown sugar in a heavy pan until it liquifies and turns deep amber. Cooking sugar to this stage adds extraordinary depth and complexity to the final glaze. The slightly bitter, smoky caramel notes counterbalance the rich, sweet, fatty pork belly in a way that plain soy sauce simply cannot.'),
      (3, 'Add the pork and fish sauce', "Add the pork belly slices and fish sauce to the caramel and toss to coat. Adding fish sauce to the hot caramel creates an instant, intense, savory-sweet glaze that coats the pork — the fish sauce's glutamates amplify and deepen the caramel's sweetness while adding the umami backbone that makes every bite incredibly complex."),
      (4, 'Braise until lacquered', 'Add a splash of water and cook over medium heat, turning regularly, for 20 minutes until the sauce reduces to a thick, glossy lacquer coating each piece. The repeated turning ensures every surface of the pork gets contact with the simmering glaze, building multiple layers of caramelisation that produce the extraordinary stickiness and depth of colour the dish is famous for.'),
      (5, 'Quick-pickle the vegetables', 'Julienne carrots and daikon, toss with rice vinegar, sugar and a pinch of salt, and rest for 15 minutes. The quick pickle creates a sharp, crunchy foil to the rich, fatty pork — the acidity cuts through the sweetness of the glaze and refreshes the palate. This balance of fat and acid is a fundamental principle of Vietnamese cuisine.'),
      (6, 'Cook jasmine rice', "Cook jasmine rice by the absorption method until fluffy and fragrant. Jasmine rice's distinctive floral aroma comes from a compound called 2-acetyl-1-pyrroline activated by the heat of cooking — it is the perfect backdrop for the sweet-savoury pork, carrying its sauce without competing with its bold flavours."),
      (7, 'Make the sriracha mayo', 'Mix sriracha with Japanese mayonnaise (Kewpie if available) to a pink, spicy, deeply savoury condiment. Kewpie mayo uses egg yolks and rice vinegar, making it richer and tangier than standard mayonnaise — combined with sriracha, it creates a condiment of extraordinary flavour that elevates every component it touches.'),
      (8, 'Assemble the bowl', 'Arrange rice in bowls and top with caramelised pork, pickled vegetables, sliced cucumber and coriander, then dollop with sriracha mayo. The combination of hot pork, cool cucumber, sharp pickle and spicy mayo in a single spoonful is a genuinely world-class eating experience.')],
     ['🍬 Cook the caramel to a deep amber — a pale caramel means underdeveloped flavour; a deep amber provides the complexity that makes this dish extraordinary.',
      '🥕 Make the pickled vegetables first and rest them for the full 15 minutes — properly pickled vegetables are a completely different experience from vegetables simply splashed with vinegar.',
      '🥩 Slice the pork thinly and evenly — uneven slices cook at different rates, resulting in some overcooked and dried out while others are perfectly lacquered.'],
     ['Pork provides complete protein and excellent levels of B vitamins, particularly thiamine.',
      'The pickled vegetables add significant vitamins without adding calories.',
      'Vietnamese cuisine is characterised by balance — the fresh herbs, vegetables and acid balance the richness of the pork.'],
     ['Pork belly is high in saturated fat — a more occasional dish than an everyday meal.',
      'The palm sugar and fish sauce glaze makes this a high-sodium, high-sugar preparation — portion awareness is worthwhile.']),
    ('Fresh Vietnamese Prawn Rice Paper Rolls', '🥗', 'quick',
     'Glistening rice paper rolls filled with plump prawns, rice vermicelli, fresh mint, crunchy lettuce and cucumber, served with a tangy, nutty peanut dipping sauce. Light, fresh and utterly spectacular — Vietnamese street food at its finest, ready in 25 minutes!',
     '25 minutes', 4, 'Easy', 5, 'Super Healthy',
     [(1, 'Prepare the fillings', 'Cook rice vermicelli according to the packet, rinse under cold water and drain. Rinsing the cooked vermicelli under cold water serves two purposes: it immediately stops the cooking, preventing mushiness, and removes excess surface starch that would otherwise make the strands clump together into an unappealing mass in your rolls.'),
      (2, 'Cook the prawns', 'Poach prawns in barely simmering water with a little fish sauce for 2 minutes until just pink and curled. Poaching rather than boiling keeps prawns tender — vigorous boiling toughens the delicate proteins within seconds, while gentle poaching preserves the sweet, succulent texture. The fish sauce adds a subtle savoury note that raw water cannot provide.'),
      (3, 'Make the peanut dipping sauce', 'Whisk together hoisin sauce, peanut butter, rice vinegar, sesame oil, sriracha and warm water until smooth and glossy. This sauce is the backbone of the entire dish — the umami depth of hoisin, the richness of peanut butter and the heat of sriracha create a dipping experience that makes every fresh, clean roll suddenly extraordinary.'),
      (4, 'Prepare the wrapping station', 'Set out the prawns, vermicelli, lettuce, mint, coriander, cucumber and a large bowl of warm water for the rice paper. A well-organised rolling station is the key to confident, beautiful rolls — having everything prepped and within reach allows you to work quickly while the rice paper is at the perfect pliable consistency.'),
      (5, 'Soak and fill the rice paper', 'Dip a rice paper sheet in warm water for 10 seconds until pliable but not fully softened, then lay flat and fill. Ten seconds is the critical timing — fully softened rice paper tears; under-softened paper cracks when rolled. It will continue to soften as you fill and roll, so removing it slightly early is the professional technique.'),
      (6, 'Roll tightly', 'Place fillings in the lower third, fold in the sides and roll upward tightly and firmly. The tight roll is essential — loose rolls fall apart the moment they are picked up and dipped. The key is pulling the rice paper back toward you as you roll, applying tension that compresses the filling and creates a firm, beautiful cylinder.'),
      (7, 'Serve with peanut sauce', 'Arrange the rolls on a plate and serve immediately with the peanut dipping sauce and additional sliced chilli. Rice paper rolls are at their absolute best within 20 minutes — the rice paper gradually absorbs moisture from the fillings and becomes soft and sticky over time, so serving immediately is genuinely important.')],
     ['💧 Ten seconds in the water is the key — remove rice paper while still slightly stiff; it will soften further as you add fillings.',
      '🥢 Roll tightly and with confidence — a loose roll falls apart on first bite. Practice on the first one and the technique will click immediately.',
      '🥜 Make extra peanut sauce — everyone always wants more. It also keeps in the fridge for a week and works on everything.'],
     ['Prawns are an excellent lean protein source, very low in calories and rich in iodine and selenium.',
      'This dish is largely uncooked — all the vegetables and herbs retain virtually all of their vitamins and enzymes.',
      'Rice paper and vermicelli are naturally gluten-free, making this suitable for those with gluten sensitivity.'],
     ['Rice paper rolls must be eaten immediately — they become sticky and unpleasant if left to sit for more than 30 minutes.',
      'The peanut dipping sauce adds significant calories from fat — use in moderation if managing calorie intake.']),
]

_RAW['moroccan'] = [
    ('Spiced Chickpea & Vegetable Tagine', '🫕', 'healthy',
     "Morocco's ancient one-pot tradition — a warmly spiced tagine of tender chickpeas, sweet potato and courgette simmered in a fragrant tomato broth with preserved lemon, olives and harissa, served over fluffy couscous. Vibrant, nourishing and deeply satisfying!",
     '40 minutes', 6, 'Easy', 5, 'Super Nutritious',
     [(1, 'Build the sofrito', 'Sauté onion, garlic and tomatoes gently in olive oil for 10 minutes until collapsed and fragrant. This initial slow cooking of the aromatics creates a deeply flavourful base — patience at this stage pays dividends throughout the dish, as the caramelised onions and tomatoes become the backbone that supports all the spices added next.'),
      (2, 'Bloom the ras el hanout', 'Add ras el hanout, cumin, coriander and a pinch of cinnamon and stir for 2 minutes in the oil. Ras el hanout — "head of the shop" in Arabic — is the most complex spice blend in Moroccan cooking, typically containing 12–30 spices. Toasting it in the olive oil extracts its fat-soluble aromatic compounds, releasing a fragrance that is floral, warm and utterly mesmerising.'),
      (3, 'Add the vegetables', "Add cubed sweet potato, courgette and chickpeas and stir to coat in the spiced base. Cutting the sweet potato and courgette into similar sizes ensures they cook at the same rate — the sweet potato's starch will thicken the sauce slightly as it cooks, adding body without the need for any separate thickening agent."),
      (4, 'Add tomatoes and stock', 'Add crushed tomatoes and vegetable stock, bring to a simmer and cook for 20 minutes until the sweet potato is tender. The tomatoes provide acidity that balances the warm spices and sweetness of the sweet potato, while the slow simmer allows all the vegetables to absorb the spiced broth until they are fully flavoured throughout.'),
      (5, 'Add preserved lemon and olives', 'Stir in sliced preserved lemon and green olives. Preserved lemon is the defining ingredient of Moroccan cuisine — the long fermentation produces a rounded, complex citrus flavour with none of the sharp rawness of fresh lemon. Combined with the briny olives, they add a layer of savoury-citrus complexity that completely transforms the stew.'),
      (6, 'Cook the couscous', 'Pour boiling stock or water over couscous at a 1:1.5 ratio, cover tightly and rest for 5 minutes, then fluff with a fork. Couscous is not actually cooked — it is rehydrated by the steam trapped under the lid. Fluffing with a fork separates the grains and allows them to dry and separate properly rather than clumping into a stodgy mass.'),
      (7, 'Serve and garnish', 'Spoon the tagine over the couscous and garnish with fresh coriander, a drizzle of argan oil and a pinch of harissa. Argan oil — unique to Morocco — has a wonderfully distinctive toasty, nutty flavour that adds the finishing touch of authenticity to the dish.'),
      (8, 'Add harissa to taste', "Serve extra harissa on the side for heat. Harissa's complex, smoky chilli flavour builds through the meal — starting with a small amount and adding more allows each diner to calibrate the heat to their own preference while still experiencing the full fragrance and flavour of the stew beneath.")],
     ['🌶 Quality ras el hanout makes a significant difference — look for a blend that smells genuinely floral and complex, not simply of cumin and paprika.',
      '🍋 Use preserved lemon rind only, not the flesh — the fermented rind has the concentrated, complex flavour; the flesh is simply salty.',
      '🫒 Green olives (rather than black) are the traditional choice for tagine — their slight bitterness and firmer texture work better in the warm sauce.'],
     ['Chickpeas are a nutritional powerhouse — exceptional plant-based protein, fibre, iron and folate in a single ingredient.',
      'Sweet potato is one of the richest dietary sources of beta-carotene, which converts to vitamin A.',
      'The broad spectrum of Moroccan spices — cinnamon, cumin, coriander — all have individually documented anti-inflammatory properties.'],
     ['Couscous is made from refined wheat — use wholegrain couscous for significantly more fibre and a lower glycaemic index.',
      'Preserved lemon and olives are both high in sodium — taste the tagine before adding extra salt.']),
    ('Slow-Cooked Lamb & Preserved Lemon Tagine', '🍲', 'comfort',
     "Fall-apart tender lamb shoulder slow-cooked with preserved lemon, olives, honey and a warming blend of Moroccan spices until the sauce is glossy, fragrant and absolutely extraordinary. The most romantic, aromatic stew in the world!",
     '90 minutes', 6, 'Medium', 2, 'Indulgent Treat',
     [(1, 'Season the lamb generously', 'Cut lamb shoulder into large chunks and rub thoroughly with ras el hanout, salt, turmeric and cumin. Seasoning 24 hours in advance is ideal — the spices penetrate deeper into the meat, and the salt begins to break down the proteins and season the meat from the inside out rather than just on the surface.'),
      (2, 'Brown the lamb deeply', 'Brown lamb chunks in batches in hot oil until deeply caramelised on all sides. This browning step is what separates a good tagine from a magnificent one — the Maillard reaction creates a crust packed with complex flavour compounds that will gradually dissolve into the braising liquid, enriching the final sauce with extraordinary depth.'),
      (3, 'Cook the aromatics', "In the same pan, slowly fry onion and garlic until deeply golden and sweet, then add saffron soaked in warm water. The long caramelisation of the onions creates a natural sweetness that forms the perfect counterpoint to the sour preserved lemon and salty olives. The saffron's honey-like aroma is the crowning aromatic note of the entire dish."),
      (4, 'Add tomatoes and spices', 'Add tomatoes, ginger, cinnamon and the browned lamb, and stir to combine. The tomatoes provide body and acidity that will be slowly transformed during the braise — after 90 minutes, their fresh sharpness will have mellowed into a rich, rounded, jammy sweetness that is the heart of the sauce.'),
      (5, 'Braise gently for an hour', 'Add enough stock to just cover, bring to a gentle simmer, cover and braise for 1 hour. The low, steady heat is critical — it slowly converts the collagen in the lamb shoulder into gelatin, enriching the braising liquid with body and silkiness while keeping the meat moist and tender. High heat would produce dry, stringy meat.'),
      (6, 'Add preserved lemon and olives', 'Add sliced preserved lemon (rind only) and green olives for the final 15 minutes. Adding these ingredients too early would make the lemon bitter and the olives lose their texture — added toward the end, they retain their character while absorbing the flavour of the sauce.'),
      (7, 'Stir in honey', 'Drizzle in a tablespoon of honey and stir gently. This final touch of honey is a classically Moroccan concept — the sweet note balances the sour preserved lemon and salty olives, bringing the sauce into the perfect, harmonious equilibrium that defines the best Moroccan cooking.'),
      (8, 'Rest and serve', 'Allow the tagine to rest off the heat for 10 minutes before serving over couscous. The resting period allows the sauce to cool slightly, thickening and intensifying, and gives the lamb time to reabsorb some of the sauce it released during braising — producing a more flavourful, juicy result.')],
     ['🌙 Make this the day before and refrigerate overnight — like all braises, the tagine tastes significantly better the next day as the flavours continue to develop.',
      '🧂 Taste the sauce before adding extra seasoning — preserved lemon, olives and the spice rub contribute significant salt already.',
      '🔥 Maintain a gentle simmer throughout the braise — the lid should fit tightly and the broth should barely move. A vigorous boil will dry out the lamb and cloud the sauce.'],
     ['Lamb shoulder is rich in complete protein, iron, zinc and B12 — particularly beneficial for those with anaemia or iron deficiency.',
      'Preserved lemon provides vitamin C and probiotics from the fermentation process.',
      'Saffron contains safranal and crocin, compounds studied for their potential mood-elevating properties.'],
     ['Lamb shoulder is high in saturated fat — a celebratory dish rather than an everyday meal.',
      'The 90-minute cooking time makes this impractical for a weeknight meal — it is best planned as a weekend project.']),
    ('Harissa Chicken & Fluffy Couscous', '🍗', 'quick',
     'Boldly spiced chicken thighs marinated in fiery harissa and lemon, pan-seared until gloriously charred and served over fluffy, herbed couscous with a cool yogurt sauce. Moroccan flavours at full throttle — ready in 30 minutes!',
     '30 minutes', 4, 'Easy', 4, 'Fresh & Nutritious',
     [(1, 'Marinate in harissa', 'Slash chicken thighs deeply and marinate in harissa, olive oil, garlic, cumin and lemon juice for at least 15 minutes. Slashing the chicken allows the spiced harissa to penetrate deeply into the meat — without slashes, the marinade sits on the surface and the flavour barely reaches the centre.'),
      (2, 'Make the herb couscous', 'Pour boiling stock over couscous with olive oil and salt at a 1:1.5 ratio, cover tightly and rest for 5 minutes. The olive oil prevents the couscous grains from sticking together during the absorption process, ensuring they fluff up into separate, individual grains rather than a compressed, stodgy block.'),
      (3, 'Fluff and herb the couscous', 'Fluff the couscous with a fork, adding fresh parsley, mint, lemon zest and more olive oil. The herbs must go in while the couscous is still warm — the residual heat wilts the parsley and mint just enough to release their essential oils, infusing the grain with a green, herby fragrance that cold couscous would never absorb as effectively.'),
      (4, 'Sear the chicken', "Cook the marinated chicken in a very hot, oiled pan for 6–7 minutes per side until deeply charred and cooked through. The harissa's natural sugars caramelise dramatically in the high heat, creating a char that looks almost burnt but tastes extraordinary — that blackened crust carries the most concentrated, complex flavour of the entire dish."),
      (5, 'Make the yogurt sauce', 'Combine Greek yogurt with grated garlic, lemon juice and mint. Harissa chicken needs the cooling dairy contrast of yogurt — without it, the cumulative heat of the harissa becomes uncomfortable over a full portion. The yogurt softens the chilli and provides a creamy, tangy backdrop that makes each bite perfectly balanced.'),
      (6, 'Rest the chicken', 'Rest the chicken off the heat for 5 minutes before slicing. Resting allows the muscle fibres to relax and reabsorb the juices that have been driven toward the surface during high-heat cooking. Slicing immediately loses those juices to the chopping board — resting for even 5 minutes keeps them where they belong, inside the meat.'),
      (7, 'Assemble and serve', 'Spoon herbed couscous onto plates, top with sliced chicken and dollop with yogurt sauce. Scatter extra harissa, fresh mint and a drizzle of olive oil over the top. The visual contrast of the charred, red chicken against the green herbed couscous and white yogurt makes this dish as beautiful as it is delicious.')],
     ['🌶 Use good quality harissa — the difference between a complex, smoky rose harissa and a generic supermarket paste is remarkable.',
      '🍋 The lemon zest in the couscous is essential — it adds a freshness that prevents the dish from feeling heavy despite the bold, spiced chicken.',
      '⏰ Let the harissa chicken char properly — do not be tempted to move it around the pan too early. Leave it for the full time on each side for maximum caramelisation.'],
     ['Chicken thighs provide excellent protein, iron and zinc, and remain juicy even at high heat.',
      'Harissa contains capsaicin and roasted red pepper, providing both heat and vitamin C.',
      'Fresh herbs in the couscous contribute significant vitamin K and antioxidants.'],
     ['Harissa varies significantly in heat level between brands — taste your brand before adding the full quantity in the marinade.',
      'Greek yogurt adds calories — for a lighter option, use a thin tahini dressing instead.']),
]

_RAW['american'] = [
    ('Grilled Chicken Caesar Salad', '🥗', 'healthy',
     'Properly grilled chicken breast with golden char marks served over crisp romaine lettuce, homemade anchovy Caesar dressing and house-baked croutons. The most celebrated American salad reimagined for maximum flavour and impressive nutrition!',
     '25 minutes', 4, 'Easy', 4, 'Fresh & Nutritious',
     [(1, 'Pound the chicken breast flat', 'Place chicken breast between plastic wrap and pound to an even 2cm thickness. Even thickness is the single most important step for perfectly cooked chicken — uneven breasts cook at different rates, with the thin end drying out while the thick end finishes. A uniformly thin breast cooks quickly, evenly and stays beautifully juicy throughout.'),
      (2, 'Season simply and boldly', 'Drizzle with olive oil, season very generously with salt, pepper and garlic powder. Proper seasoning of chicken before grilling means you never need to add salt at the table — the surface develops a flavourful crust from the high-heat grill, and well-seasoned chicken underneath the crust tastes good all the way through.'),
      (3, 'Make the anchovy Caesar dressing', 'Pound anchovy fillets to a paste, then whisk with garlic, lemon juice, Dijon mustard, Worcestershire sauce and olive oil. The anchovy provides glutamate-rich umami without any detectable fishiness — it simply makes the dressing taste more savoury and complex than it would with salt alone. This is the reason a proper Caesar tastes utterly unlike a dressed salad.'),
      (4, 'Make the croutons', 'Tear sourdough into chunks, toss with olive oil, garlic and salt, and bake at 190°C for 12 minutes until golden and crunchy. Tearing the bread (rather than cutting) creates irregular surfaces with more nooks and crannies that absorb the olive oil and develop more surface area for crisping — producing croutons with far more textural complexity than cubed bread.'),
      (5, 'Grill the chicken', 'Grill the chicken on a preheated ridged pan over high heat for 4–5 minutes per side without moving it until char marks develop. High heat with no movement allows the Maillard reaction to create those characteristic golden char lines. The moment you see char beginning around the edge, it is time to flip.'),
      (6, 'Rest and slice', 'Rest the chicken for 5 minutes before slicing diagonally. Diagonal slicing is not merely aesthetic — it cuts across the muscle fibres rather than along them, producing shorter fibre lengths that feel more tender when you chew. Serving sliced rather than whole also allows the dressing to reach the interior of the chicken.'),
      (7, 'Dress the romaine', 'Tear romaine into large pieces and toss generously with Caesar dressing until every leaf is coated. Large pieces of romaine create the ideal surface area — enough to carry dressing but not so small that every leaf becomes saturated. The crunch of fresh romaine against the creamy dressing is the essential textural experience of Caesar salad.'),
      (8, 'Assemble and serve', 'Arrange dressed romaine on plates, top with sliced chicken and croutons, then finish with shaved parmesan and fresh black pepper. The cold, crunchy salad against the warm, charred chicken is a temperature and texture contrast that makes this salad far more interesting to eat than a simple salad of uniform ingredients.')],
     ['🥄 Pound the chicken to even thickness — this single step is the difference between perfectly cooked, juicy chicken and dry, unevenly cooked disappointment.',
      '🐟 Do not fear the anchovy — it adds savoury depth without fishiness. A Caesar without anchovy is a fundamentally lesser thing.',
      '🥙 Make double the croutons — they are irresistible and will disappear. Store extras in an airtight container for up to a week.'],
     ['Chicken breast is one of the leanest, highest-protein foods available.',
      'Romaine lettuce provides folate, vitamin K and potassium with virtually no calories.',
      'Anchovies in the dressing provide omega-3 fatty acids and a significant amount of calcium.'],
     ['A traditional Caesar dressing is rich in olive oil — use a lighter hand with the dressing if managing calories.',
      'Store-bought croutons are often high in sodium and preservatives — homemade is always a better choice.']),
    ('Smoky BBQ Pulled Pork Sliders', '🍔', 'comfort',
     'Pork shoulder slow-braised for hours in a smoky, tangy homemade BBQ sauce until it falls apart at a touch, piled high onto warm brioche sliders with crunchy coleslaw. This is American BBQ culture at its most magnificent and deeply satisfying!',
     '90 minutes', 8, 'Medium', 2, 'Indulgent Treat',
     [(1, 'Make the dry rub', 'Combine smoked paprika, brown sugar, garlic powder, cumin, mustard powder, salt and black pepper and rub generously over the pork shoulder. The brown sugar in the rub caramelises in the oven, creating a dark, sticky bark on the surface of the pork — that bark is the most intensely flavoured part of the whole shoulder and the hallmark of great BBQ.'),
      (2, 'Sear the pork', 'Sear the rubbed pork shoulder in a hot pan until deeply browned on all sides. The Maillard reaction creates the crust from which all the fat-soluble flavour compounds will slowly dissolve into the cooking liquid during the long braise, enriching the entire dish with extraordinary meaty complexity.'),
      (3, 'Make the BBQ sauce', 'Combine ketchup, apple cider vinegar, Worcestershire sauce, hot sauce, brown sugar, smoked paprika, onion powder and mustard in a pan and simmer for 5 minutes. A homemade BBQ sauce is a very different proposition from bottled — the balance of sweet, sour, savoury and smoky is calibrated to your exact taste, not a lowest-common-denominator commercial formula.'),
      (4, 'Braise low and slow', 'Place pork in a deep roasting tin, pour over half the BBQ sauce, cover tightly with foil and braise at 150°C for 3 hours. The long, low braise is the fundamental technique of American pulled pork — the extended time at low temperature allows the extensive collagen in the pork shoulder to slowly convert to gelatin, producing the extraordinary melt-in-the-mouth tenderness the dish is famous for.'),
      (5, 'Pull the pork', 'Remove from the oven and pull the pork apart using two forks. Well-braised pork shoulder should offer virtually no resistance — the forks should glide through it. The act of pulling shreds the meat along natural muscle grain lines, creating strands with enormous surface area that absorb the BBQ sauce far more effectively than chunks would.'),
      (6, 'Sauce and rest', 'Toss the pulled pork with the remaining BBQ sauce and rest for 10 minutes to absorb. Resting the sauced pork allows the meat fibres to reabsorb the liquid and the sauce to penetrate fully — the result is moist, deeply flavoured meat throughout rather than surface-sauced meat that dries out quickly at the table.'),
      (7, 'Make the coleslaw', 'Combine finely shredded cabbage, carrot and spring onion with mayonnaise, cider vinegar, sugar and salt, and rest for 10 minutes. Coleslaw is essential rather than optional — its cool crunch and tangy dairy richness are the perfect counterpoint to the hot, smoky, sticky pork, providing a textural and temperature contrast that makes sliders genuinely thrilling to eat.'),
      (8, 'Build and serve the sliders', 'Toast brioche slider buns, pile on pulled pork and crown with coleslaw. Toasting the buns is non-negotiable — the structural integrity of a toasted bun withstands the weight and moisture of the pulled pork, while an untoasted bun becomes soggy within seconds.')],
     ['🍖 Pork shoulder is the only cut for pulled pork — its collagen content is what produces the extraordinary tenderness. Loin will always be dry and disappointing.',
      '🔥 Do not rush the braise — 3 hours at 150°C cannot be shortened to 1.5 hours at 180°C with the same result. The low temperature is essential.',
      '🥬 Make the coleslaw at least 15 minutes before serving — the salt and vinegar draw out moisture and the flavours meld into something far better than immediate assembly.'],
     ['Pork provides complete protein, thiamine and selenium.',
      'Apple cider vinegar in the BBQ sauce and coleslaw may support blood sugar regulation.',
      'A batch-cooking recipe that feeds a crowd and reheats beautifully.'],
     ['Pulled pork with BBQ sauce is high in both sugar and saturated fat — a celebratory dish rather than everyday food.',
      'The 3-hour braising time requires advance planning — this is a weekend project.']),
    ('Smash Burgers with Special Sauce', '🍔', 'quick',
     'Thinly smashed beef patties seared at high heat until the edges are crispy, lacy and deeply caramelised, topped with melted American cheese and a legendary special sauce in a toasted brioche bun. The most flavour-packed burger you will ever make in 15 minutes!',
     '15 minutes', 2, 'Easy', 2, 'Indulgent Treat',
     [(1, 'Make the special sauce', 'Combine mayonnaise, American mustard, ketchup, finely chopped gherkin, a splash of pickle juice and a pinch of smoked paprika. The gherkin juice is the key — its acid brightens and cuts through the rich mayo base in a way that fresh lemon cannot, while the gherkin adds a sweet-sour crunch that provides the textural surprise that makes special sauce so addictive.'),
      (2, 'Form the beef balls', 'Divide beef mince (80/20 fat ratio) into 80g balls — do not compress them. The key to a proper smash burger is NOT to pre-form patties — loose beef balls smash more evenly and their irregular surface area creates more jagged, caramelised edges. The 80/20 fat ratio is essential; leaner beef produces dry, flavourless smash burgers.'),
      (3, 'Heat the pan until smoking', 'Heat a cast iron pan or thick-bottomed skillet over maximum heat until a drop of water evaporates instantly. The extremely high heat is the entire point of a smash burger — it is what creates the dramatic Maillard crust that makes the burger taste incomparably better than a gently cooked thick patty.'),
      (4, 'Smash the burgers', 'Place a beef ball in the screaming-hot pan and immediately smash flat with a spatula, pressing hard for 10 seconds. The smashing action increases the surface area in contact with the hot pan by 300%, dramatically accelerating the Maillard reaction and creating those gloriously crispy, lacy edges that are the defining characteristic of a perfect smash burger.'),
      (5, 'Season and wait', 'Season the smashed patty immediately with salt and pepper, then do not touch it for 2 minutes. The two minutes of contact time without disturbance is what allows the crust to develop fully — releasing too early tears the crust off the pan and destroys the very thing you are working toward. The patty is ready to flip when it releases cleanly.'),
      (6, 'Add cheese and cover', 'Flip the patty, immediately place American cheese on top and cover the pan with a lid for 30 seconds. The brief steaming under the lid melts the cheese completely and evenly in seconds — American cheese melts more smoothly than most others due to its added emulsifiers, producing that characteristic glossy, completely molten finish.'),
      (7, 'Toast the buns', 'Toast the brioche buns in the beef fat left in the pan until golden. Toasting the buns in the beef fat from the patties adds a subtly meaty, savoury flavour to the bun that links it to the burger and elevates the entire sandwich without any additional effort.'),
      (8, 'Build and serve immediately', 'Spread special sauce on both bun halves, add lettuce and gherkin, then stack the cheesy patty and eat at once. Smash burgers must be eaten immediately — the contrast between the still-hot, crispy-edged patty and the cool sauce and lettuce is at its peak in the first two minutes, and diminishes noticeably as the patty cools.')],
     ['🥩 Use 80/20 beef mince — the fat content is what produces the crispy, caramelised edges. Lean mince produces a dry, tasteless smash burger.',
      '🔥 Heat the pan until it is genuinely smoking — a barely warm pan is the enemy of a smash burger. The heat must be extreme for the Maillard magic to happen.',
      '🧀 Use American cheese slices — their emulsifiers produce the characteristic smooth, complete melt that is the hallmark of a proper smash burger.'],
     ['Beef provides complete protein, iron, zinc and B12 in significant amounts.',
      'The high-heat, fast cooking method retains moisture in the patty more effectively than longer cooking at lower temperatures.',
      'A double patty smash burger provides over 40g of protein.'],
     ['The 80/20 fat ratio means this is a high-saturated-fat meal — best enjoyed occasionally.',
      'American cheese and special sauce add significant sodium and calories — balance with a green salad if nutrition is a priority.']),
]

_RAW['mediterranean'] = [
    ('Pan-Seared Sea Bass with Herb Oil & Capers', '🐟', 'healthy',
     'Skin-on sea bass fillets seared to golden-crisp perfection over a bed of wilted cherry tomatoes, olives and spinach, finished with a vibrant green herb oil and briny capers. The Mediterranean diet in its purest, most beautiful expression!',
     '20 minutes', 2, 'Easy', 5, 'Super Nutritious',
     [(1, 'Prepare the herb oil', 'Blend fresh basil, parsley, garlic and extra-virgin olive oil until smooth and bright green. Making the herb oil first allows the flavours to meld while the fish cooks — the heat from the seared fish will warm the oil slightly when poured, releasing the volatile aromatics at exactly the right temperature for maximum impact.'),
      (2, 'Score and dry the fish', 'Pat the sea bass skin completely dry and score diagonally through the skin every 2cm without cutting through to the flesh. Completely dry skin is the non-negotiable first step for a perfectly crisped result — any residual moisture steams rather than fries on contact with the hot pan, producing soft, pale skin rather than the golden, shatteringly crisp skin you want.'),
      (3, 'Heat the pan properly', 'Heat a stainless steel or non-stick pan over high heat for 2 minutes until a drop of water sizzles instantly. A properly hot pan is what prevents the fish from sticking — the protein immediately sears on contact and releases cleanly, while a cool pan causes it to bond to the surface.'),
      (4, 'Sear the fish', "Add olive oil and place the fish skin-side down. Press firmly with a spatula for 30 seconds to prevent curling, then cook undisturbed for 4 minutes. The pressing counteracts the skin's natural tendency to contract and curl as it heats, ensuring flat, even contact with the pan across the entire surface — this is what produces uniformly golden skin."),
      (5, 'Flip and finish', 'Flip the fish and cook for just 60 seconds on the flesh side. Sea bass fillets are delicate — cooking the flesh side for more than 60–90 seconds at high heat will dry out the thin, delicate fillet. The fish is properly cooked when the flesh turns from translucent to just barely opaque throughout.'),
      (6, 'Wilt the tomatoes and spinach', 'In the same pan, add cherry tomatoes and spinach with a splash of white wine and wilt for 2 minutes. Cooking in the same pan means the tomatoes and spinach absorb the caramelised fish oils left on the surface — a small step that dramatically concentrates the flavour of the vegetables without requiring any additional seasoning.'),
      (7, 'Assemble and dress', 'Arrange the wilted vegetables on plates and place the fish on top skin-side up. Spoon herb oil around and scatter capers and olives over the plate. Plating the fish skin-side up preserves its crispness until the final moment — a crispy skin laid against warm vegetables would immediately soften, and the sound and sensation of that first bite through crisp skin is one of food\'s great pleasures.')],
     ['🐟 Dry skin is everything for crispy sea bass — press it thoroughly with kitchen paper, then let it rest on a wire rack for 5 minutes to air-dry further.',
      '🫒 Capers are a powerful flavour accent — their pickled, briny character cuts through the richness of the fish and olive oil beautifully. Do not skip them.',
      '🌿 Make the herb oil just before serving — freshly blended herb oil is vivid green and aromatic; pre-made oil oxidises and loses both its colour and its fragrance.'],
     ['Sea bass is an excellent source of lean protein, omega-3 fatty acids and selenium.',
      'Extra-virgin olive oil provides oleocanthal, a natural anti-inflammatory compound comparable in effect to ibuprofen.',
      'A complete meal with protein, healthy fats and vegetables in under 20 minutes.'],
     ['Sea bass can be expensive — grey mullet, sea bream or any firm white fish works identically with this technique.',
      'As with all oily fish, 2–3 portions per week is the recommended guideline.']),
    ('Baked Aubergine Parmigiana', '🍆', 'comfort',
     'Golden-fried aubergine layered with a rich, herb-flecked tomato sauce and molten mozzarella, baked until bubbling and deeply caramelised. This magnificent Italian-Mediterranean baked dish is pure comfort food at its most elegant and satisfying!',
     '60 minutes', 6, 'Medium', 3, 'Balanced Comfort',
     [(1, 'Slice and salt the aubergines', 'Slice aubergines 0.5cm thick, salt both sides generously and leave in a colander for 30 minutes. Salting the aubergine draws out the bitter juices that make raw aubergine taste harsh, and removes enough moisture that the slices absorb significantly less oil during frying — producing a dish that is rich but not greasy.'),
      (2, 'Fry the aubergine slices', 'Pat the aubergine completely dry and fry in batches in hot olive oil until deeply golden on both sides. The gold colour that develops is not just visual — the Maillard browning creates complex, slightly nutty flavour compounds that are essential to the finished dish. Undercooked, pale aubergine produces a dish that is watery and lacks depth.'),
      (3, 'Make the herb tomato sauce', 'Sauté garlic in olive oil, add crushed tomatoes, fresh basil and oregano, and simmer for 20 minutes until thick and reduced. Simmering uncovered for 20 minutes transforms fresh tomatoes from an acidic, thin sauce to a sweet, concentrated, deeply flavourful base — the water evaporation concentrates the sugars and flavour until the sauce tastes genuinely like concentrated tomato essence.'),
      (4, 'Season and taste the sauce', 'Taste the sauce and season carefully — it should be sweet, slightly acidic and deeply herby. A properly seasoned tomato sauce should taste complete on its own; if it tastes flat, add a pinch more salt; if too acidic, add a small pinch of sugar; if lacking depth, add a tiny splash of red wine vinegar.'),
      (5, 'Layer the parmigiana', 'In a deep baking dish, alternate layers of tomato sauce, fried aubergine and torn mozzarella, finishing with sauce and mozzarella. The layering technique creates a dish where each forkful contains every element — the distribution of cheese throughout (not just on top) ensures melted mozzarella pulls as you serve, creating the irresistible stretchiness that is the signature of great parmigiana.'),
      (6, 'Bake until bubbling and golden', 'Bake at 200°C for 25–30 minutes until the top is deeply golden and the sauce is bubbling at the edges. The high oven temperature creates the Maillard browning on the cheese that turns it from a simple melted dairy product to a complex, savoury, golden crust — this gratinated top layer is arguably the best part of the dish.'),
      (7, 'Add parmesan and rest', 'Grate parmesan over the top in the final 5 minutes of baking, then rest for 15 minutes before serving. The resting period is not optional — hot parmigiana is a beautiful, collapsing mess. Resting allows the cheese and sauce to firm slightly, meaning each serving comes out as a neat, attractive portion that showcases the layers.'),
      (8, 'Serve with bread', 'Cut into generous portions and serve with crusty bread for scooping up the sauce. Parmigiana produces an extraordinary, reduced tomato-mozzarella sauce at the base of the dish during baking — arguably as delicious as the layers themselves, and requiring good bread to do it justice.')],
     ['🧂 Salt the aubergine for the full 30 minutes — cutting this short means excess moisture in the dish and significantly more oil absorption during frying.',
      '🧀 Tear the mozzarella rather than slicing — torn pieces melt more unevenly, creating beautiful pools and strings of cheese rather than uniform layers.',
      '⏰ Rest the parmigiana for the full 15 minutes — serving immediately is the most common mistake, producing a dish that collapses and loses its beautiful layered structure.'],
     ['Aubergine is very low in calories but rich in nasunin, a powerful antioxidant found in its purple skin.',
      'A substantial, filling dish that is naturally vegetarian and provides good amounts of calcium and protein from the cheeses.',
      'Tomatoes provide exceptional levels of lycopene — their antioxidant content actually increases when cooked.'],
     ['The frying of the aubergine adds significant oil — for a lighter version, brush with oil and grill instead.',
      'Mozzarella and parmesan together make this a calorie-dense, high-sodium dish — best enjoyed as an occasional treat.']),
    ('Shakshuka — Eggs in Spiced Tomato Sauce', '🍳', 'quick',
     'Eggs poached directly in a boldly spiced, slow-cooked tomato and pepper sauce until the whites are just set and the yolks are gloriously runny. The Middle Eastern and Mediterranean breakfast icon that works for any meal of the day — ready in 20 minutes, one pan!',
     '20 minutes', 2, 'Easy', 4, 'Light & Nutritious',
     [(1, 'Cook the peppers and onion', 'Fry diced red pepper and onion in olive oil over medium heat for 8–10 minutes until completely soft and beginning to caramelise. This is the most important step in the entire recipe — properly cooked-down vegetables provide a sweet, jammy base that makes the sauce taste like it has been cooking for hours rather than minutes.'),
      (2, 'Bloom the spices', 'Add cumin, smoked paprika, chilli flakes and a pinch of cinnamon and cook for 2 minutes. These spices are fat-soluble and bloom beautifully in the olive oil, releasing their aromatic compounds far more effectively than they would in a water-based sauce. The cinnamon is the unexpected secret ingredient — a tiny amount adds an exotic warmth that transforms the sauce.'),
      (3, 'Add garlic and tomatoes', 'Add garlic for 1 minute, then add crushed tomatoes and simmer for 10 minutes until thick and deeply flavoured. The garlic is added after the spices because garlic burns quickly at the temperatures needed to bloom spices — adding it to the slightly cooled spice paste ensures it cooks gently and sweetly rather than turning bitter.'),
      (4, 'Season the sauce', 'Taste the sauce and season generously with salt, pepper and a pinch of sugar if needed. The sauce should be rich, tangy, slightly sweet and complexly spiced. This moment of tasting and adjusting is what separates a good shakshuka from a great one.'),
      (5, 'Create wells for the eggs', 'Use a spoon to create wells in the sauce and crack one egg into each well. Creating defined wells ensures the egg whites and yolks stay contained and cook evenly — eggs dropped randomly into the sauce spread unpredictably and create ragged, unattractive whites.'),
      (6, 'Cover and cook the eggs', 'Cover the pan with a lid and cook for 4–5 minutes until the whites are just set but the yolks are still completely runny. The steam trapped under the lid cooks the eggs from above as well as below, producing a fully set white without having to flip. Four minutes is typically right for a runny yolk — check at 3 minutes and proceed accordingly.'),
      (7, 'Finish and serve from the pan', 'Scatter crumbled feta, fresh coriander and a drizzle of olive oil over the pan and bring directly to the table. Shakshuka is one of those wonderful dishes that presents beautifully in the pan it was cooked in — the vivid red sauce and white egg whites is inherently beautiful, and removing it to plates would only diminish that visual drama.')],
     ['🍅 Use the best quality crushed tomatoes you can find — the tomato is the backbone of the sauce and its quality determines the final flavour more than any spice.',
      '⏱️ Start checking the eggs at 3 minutes — overcooked yolks are a significant disappointment in shakshuka. The yolks should wobble freely when the pan is moved.',
      '🌿 The feta at the end is essential — its cool, salty, creamy character against the hot, spiced sauce and runny yolk is one of the most pleasing flavour combinations in Mediterranean cooking.'],
     ['Eggs provide complete protein, vitamin D and choline, important for brain function.',
      'A very low-calorie yet genuinely filling meal due to the high protein and fibre content.',
      'Tomatoes and peppers together provide exceptional levels of vitamin C, lycopene and beta-carotene.'],
     ['This dish is best eaten immediately — shakshuka does not reheat well, as the eggs overcook.',
      'Feta adds sodium — taste the sauce before seasoning to avoid over-salting.']),
]


# ---------------------------------------------------------------------------
# Build CUISINE_RECIPES at module load time
# ---------------------------------------------------------------------------

CUISINE_RECIPES: Dict[str, List[Dict[str, Any]]] = {
    cuisine: [_r(t) for t in recipes]
    for cuisine, recipes in _RAW.items()
}


# ---------------------------------------------------------------------------
# Cuisine detection
# ---------------------------------------------------------------------------

CUISINE_SIGNATURES: Dict[str, List[str]] = {
    "italian": ["pasta", "spaghetti", "parmesan", "basil", "mozzarella", "prosciutto",
                "risotto", "polenta", "olive oil", "oregano", "arugula", "pesto"],
    "japanese": ["soy sauce", "miso", "dashi", "mirin", "sake", "wasabi", "seaweed",
                 "nori", "edamame", "tofu", "sesame", "rice vinegar", "ginger", "sushi"],
    "indian": ["turmeric", "cumin", "coriander", "garam masala", "curry", "ghee",
               "lentil", "chickpea", "naan", "basmati", "cardamom", "fenugreek",
               "mustard seed", "paneer", "masala"],
    "mexican": ["tortilla", "jalapeño", "chipotle", "avocado", "lime", "cilantro",
                "salsa", "taco", "black bean", "queso", "corn", "epazote"],
    "chinese": ["sesame oil", "five spice", "oyster sauce", "hoisin", "bok choy",
                "Sichuan", "rice wine", "spring onion", "wok", "soy", "tofu", "ginger"],
    "thai": ["lemongrass", "kaffir lime", "fish sauce", "coconut milk", "galangal",
             "thai basil", "pad thai", "tamarind", "jasmine rice", "peanut", "chilli"],
    "french": ["butter", "baguette", "brie", "camembert", "tarragon", "shallot",
               "Dijon", "cognac", "thyme", "bay leaf", "gruyère", "cream", "wine"],
    "spanish": ["saffron", "paprika", "chorizo", "pimento", "sherry", "manchego",
                "paella", "jamón", "piquillo", "sofrito", "tomato", "garlic"],
    "greek": ["feta", "olives", "oregano", "lamb", "cucumber", "tzatziki", "pita",
              "halloumi", "dolma", "lemon", "yogurt", "olive"],
    "middle_eastern": ["tahini", "za'atar", "sumac", "harissa", "pomegranate",
                       "hummus", "flatbread", "baharat", "rose water", "preserved lemon",
                       "chickpea", "lamb", "cumin"],
    "korean": ["gochujang", "gochugaru", "kimchi", "sesame", "doenjang", "mirin",
               "bulgogi", "bibimbap", "spring onion", "rice", "noodle", "tofu", "soy"],
    "vietnamese": ["fish sauce", "rice noodle", "pho", "bean sprout", "lemongrass",
                   "mint", "cilantro", "spring roll", "banh mi", "hoisin", "sriracha",
                   "vermicelli"],
    "moroccan": ["ras el hanout", "harissa", "preserved lemon", "couscous", "lamb",
                 "chickpea", "cinnamon", "saffron", "argan oil", "dates", "cumin",
                 "tagine"],
    "american": ["bbq", "burger", "cornbread", "maple syrup", "bacon", "cheddar",
                 "pulled pork", "biscuit", "coleslaw", "hot sauce", "ranch", "mac"],
    "mediterranean": ["olive oil", "lemon", "garlic", "tomato", "cucumber", "feta",
                      "fish", "oregano", "thyme", "capers", "eggplant", "zucchini",
                      "chickpea"],
}


def _detect_cuisine(ingredients: List[str]) -> str:
    """Score ingredients against cuisine signatures and return the best match."""
    ing_text = " ".join(ingredients).lower()
    scores: Dict[str, int] = {}
    for cuisine, keywords in CUISINE_SIGNATURES.items():
        score = sum(1 for kw in keywords if kw.lower() in ing_text)
        if score:
            scores[cuisine] = score
    if not scores:
        return "mediterranean"
    return max(scores, key=lambda k: scores[k])


# ---------------------------------------------------------------------------
# public API
# ---------------------------------------------------------------------------

def generate_three_recipes(ingredients: List[str]) -> List[Dict[str, Any]]:
    """Return [healthy_recipe, comfort_recipe, quick_recipe] for the detected cuisine."""
    cuisine = _detect_cuisine(ingredients)
    return CUISINE_RECIPES[cuisine]
