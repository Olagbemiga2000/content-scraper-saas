import streamlit as st

st.title("📈 SEO Prompt Optimizer")

st.markdown("**Generate professional-level SEO prompts for content creation – in French or English.**")

lang = st.selectbox("Language / Langue :", ["English", "Français"])
platform = st.selectbox("Target Platform / Plateforme :", ["Instagram", "TikTok", "LinkedIn", "Blog", "YouTube Shorts"])
user_prompt = st.text_area("Your basic prompt / Ton prompt de base :", placeholder="Ex: Parler d’un savon pour le visage...")

use_expert_mode = st.checkbox("🔒 Activer le Mode Expert (Prompt structuré niveau agence)", value=True)

# -------- MODE EXPERT ----------
def generate_expert_prompt(prompt, lang, platform):
    if lang == "Français":
        if platform == "Instagram":
            return f"""Agis comme un copywriter expert en cosmétiques ou produits lifestyle.

Crée une publication Instagram pour promouvoir : {prompt}  
Structure :
1. Hook émotionnel
2. Présentation sensorielle du produit
3. 3 avantages concrets
4. Avis client
5. Appel à l’action
6. Hashtags SEO francophones

Ton : élégant, rassurant, authentique."""
        elif platform == "Blog":
            return f"""Rédige un brief de contenu SEO pour un article de blog autour de : {prompt}

Structure attendue :
- Titre H1 optimisé pour le référencement
- Introduction engageante liée à une douleur ou problème client
- H2 x 3 à 5 pour structurer les idées principales
- Suggestions de mots-clés secondaires
- Appel à l’action clair à la fin

Ton : informatif, fluide, orienté solution."""
        else:
            return f"""Tu es un expert en rédaction persuasive.

Crée un script de contenu pour {platform} destiné à promouvoir : {prompt}

Structure :
1. Accroche forte en 1 phrase
2. 3 bénéfices ou résultats clés
3. Une preuve sociale ou avis client
4. Appel à l’action clair
5. Hashtags SEO

Ton : professionnel, engageant, centré sur le problème client."""
    else:
        if platform == "TikTok":
            return f"""Act as a TikTok content expert.

Create a viral TikTok script to promote: {prompt}

Structure:
1. Hook in first 3 seconds (stat or pain)
2. Quick story or value
3. 3 key benefits
4. Social proof or trust element
5. Call-to-action (comment / follow / bio link)

Tone: punchy, confident, scroll-stopping."""
        elif platform == "Blog":
            return f"""You are a top-tier SEO content strategist.

Write an SEO content brief for a blog post about: {prompt}

Structure:
- SEO-optimized H1 title
- Engaging intro (pain point or story)
- 4–5 main H2 sections
- Secondary keywords to include
- Final CTA (subscribe / comment / download)

Tone: professional, educational, benefit-driven."""
        else:
            return f"""Act like a persuasive content copywriter.

Write a {platform} post to promote: {prompt}

Structure:
1. Strong hook
2. Problem + solution
3. 3 core benefits
4. CTA at the end
5. Add SEO-relevant hashtags

Tone: clear, relatable, result-focused."""

# -------- MODE SIMPLE ----------
def generate_basic_prompt(prompt, lang, platform):
    if lang == "Français":
        return f"""🎯 Objectif : Créer un contenu optimisé SEO pour {platform}

“Crée un contenu {platform} pour promouvoir : {prompt}.  
Structure : Accroche, 3 avantages, appel à l’action.  
Ajoute des hashtags SEO.”"""
    else:
        return f"""🎯 Goal: Create SEO content for {platform}

“Write a {platform} content to promote: {prompt}.  
Structure: Hook, 3 benefits, CTA.  
Add SEO hashtags.”"""

# -------- BOUTON GÉNÉRER ----------
if st.button("🚀 Generate Prompt"):
    if user_prompt:
        if use_expert_mode:
            result = generate_expert_prompt(user_prompt, lang, platform)
        else:
            result = generate_basic_prompt(user_prompt, lang, platform)
        st.success("✅ Prompt generated successfully!")
        st.code(result, language="markdown")

        if "history" not in st.session_state:
            st.session_state.history = []
        st.session_state.history.append(result)
    else:
        st.warning("Please enter a prompt first.")
