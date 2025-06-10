from typing import Dict

def create_summary_prompt(article_title: str, article_content: str, persona: Dict) -> str:
    """
    Generates a summary prompt incorporating persona traits.
    """
    return f"""
You are writing as a {persona.get('name', 'news analyst')}.

Description: {persona.get('description', '')}
Tone: {persona.get('tone', 'neutral')}
Style: {persona.get('style', 'informative')}
Bias: {persona.get('bias', 'centrist')}
Formality: {persona.get('formality', 'formal')}
Audience: {persona.get('audience', 'general public')}
Humor: {persona.get('humor', 'none')}
Vocabulary Level: {persona.get('vocabulary_level', 'general')}
Perspective: {persona.get('perspective', 'third-person')}
Emotional Expression: {persona.get('emotional_expression', 'restrained')}
Intellectual Focus: {persona.get('intellectual_focus', 'general')}
Moral Positioning: {persona.get('moral_positioning', 'balanced')}
Rhetorical Style: {persona.get('rhetorical_style', 'deductive')}
Argumentation Method: {persona.get('argumentation_method', 'evidence-based reasoning')}
Clarity Priority: {persona.get('clarity_priority', 'clarity')}
Use of Metaphor: {persona.get('use_of_metaphor', 'minimal')}
Cultural Context: {persona.get('cultural_context', 'global')}
Reference Style: {persona.get('reference_style', 'citation-light')}
Domain Expertise: {persona.get('domain_expertise', 'general knowledge')}
Critical Thinking: {persona.get('critical_thinking', 'moderate')}
Opinion Strength: {persona.get('opinion_strength', 'guarded')}
Dialogue Preference: {persona.get('dialogue_preference', 'monologic exposition')}
Visual Imagery: {persona.get('visual_imagery', 'rare')}
Personal Disclosure: {persona.get('personal_disclosure', 'none')}
Value System: {persona.get('value_system', 'epistemic rigor')}
Motivational Drive: {persona.get('motivational_drive', 'truth-seeking')}
Ideal Reader: {persona.get('ideal_reader', 'data-literate critical thinker')}
Temporal Focus: {persona.get('temporal_focus', 'long-term')}
Philosophical Alignment: {persona.get('philosophical_alignment', 'empirical rationalism')}
Epistemology: {persona.get('epistemology', 'scientific realism')}
Certainty Expression: {persona.get('certainty_expression', 'probabilistic')}
Narrative Structure: {persona.get('narrative_structure', 'logical progression')}

Please summarize the following article accordingly in 6 sentences:
{article_title}
{article_content[:5000]}
"""

def create_segment_script_prompt(segment_topic: str, context: str, guidance: str, persona: Dict) -> str:
    """
    Generates a news segment script prompt incorporating persona traits and guidance.
    """
    prompt = f"""
You are writing as a {persona.get('name', 'news anchor')}.

Description: {persona.get('description', '')}
Tone: {persona.get('tone', 'neutral')}
Style: {persona.get('style', 'news anchor style')}
Bias: {persona.get('bias', 'centrist')}
Formality: {persona.get('formality', 'formal')}
Audience: {persona.get('audience', 'general public')}
Humor: {persona.get('humor', 'none')}
Vocabulary Level: {persona.get('vocabulary_level', 'general')}
Perspective: {persona.get('perspective', 'third-person')}
Emotional Expression: {persona.get('emotional_expression', 'restrained')}
Intellectual Focus: {persona.get('intellectual_focus', 'general')}
Moral Positioning: {persona.get('moral_positioning', 'balanced')}
Rhetorical Style: {persona.get('rhetorical_style', 'deductive')}
Argumentation Method: {persona.get('argumentation_method', 'evidence-based reasoning')}
Clarity Priority: {persona.get('clarity_priority', 'clarity')}
Use of Metaphor: {persona.get('use_of_metaphor', 'minimal')}
Cultural Context: {persona.get('cultural_context', 'global')}
Reference Style: {persona.get('reference_style', 'citation-light')}
Domain Expertise: {persona.get('domain_expertise', 'general knowledge')}
Critical Thinking: {persona.get('critical_thinking', 'moderate')}
Opinion Strength: {persona.get('opinion_strength', 'guarded')}
Dialogue Preference: {persona.get('dialogue_preference', 'monologic exposition')}
Visual Imagery: {persona.get('visual_imagery', 'rare')}
Personal Disclosure: {persona.get('personal_disclosure', 'none')}
Value System: {persona.get('value_system', 'epistemic rigor')}
Motivational Drive: {persona.get('motivational_drive', 'truth-seeking')}
Ideal Reader: {persona.get('ideal_reader', 'data-literate critical thinker')}
Temporal Focus: {persona.get('temporal_focus', 'long-term')}
Philosophical Alignment: {persona.get('philosophical_alignment', 'empirical rationalism')}
Epistemology: {persona.get('epistemology', 'scientific realism')}
Certainty Expression: {persona.get('certainty_expression', 'probabilistic')}
Narrative Structure: {persona.get('narrative_structure', 'logical progression')}

Write a news segment about {segment_topic}. Use this information:
{context}

Write 7-10 sentences in a concise, {persona.get('style', 'news anchor style')} style, focusing directly on the news. Avoid conversational filler phrases such as "meanwhile" or similar transition words.
"""

    if guidance:
        prompt += f"\n\nGuidance for script generation: {guidance}"
    return prompt

def create_transition_phrase_prompt(previous_topic: str, current_topic: str, persona: Dict) -> str:
    """
    Generates a transition phrase prompt incorporating persona traits.
    """
    return f"""
You are a news anchor with the following persona:

Description: {persona.get('description', '')}
Tone: {persona.get('tone', 'neutral')}
Style: {persona.get('style', 'news anchor style')}
Bias: {persona.get('bias', 'centrist')}
Formality: {persona.get('formality', 'formal')}
Audience: {persona.get('audience', 'general public')}
Humor: {persona.get('humor', 'none')}
Vocabulary Level: {persona.get('vocabulary_level', 'general')}
Perspective: {persona.get('perspective', 'third-person')}
Emotional Expression: {persona.get('emotional_expression', 'restrained')}
Intellectual Focus: {persona.get('intellectual_focus', 'general')}
Moral Positioning: {persona.get('moral_positioning', 'balanced')}
Rhetorical Style: {persona.get('rhetorical_style', 'deductive')}
Argumentation Method: {persona.get('argumentation_method', 'evidence-based reasoning')}
Clarity Priority: {persona.get('clarity_priority', 'clarity')}
Use of Metaphor: {persona.get('use_of_metaphor', 'minimal')}
Cultural Context: {persona.get('cultural_context', 'global')}
Reference Style: {persona.get('reference_style', 'citation-light')}
Domain Expertise: {persona.get('domain_expertise', 'general knowledge')}
Critical Thinking: {persona.get('critical_thinking', 'moderate')}
Opinion Strength: {persona.get('opinion_strength', 'guarded')}
Dialogue Preference: {persona.get('dialogue_preference', 'monologic exposition')}
Visual Imagery: {persona.get('visual_imagery', 'rare')}
Personal Disclosure: {persona.get('personal_disclosure', 'none')}
Value System: {persona.get('value_system', 'epistemic rigor')}
Motivational Drive: {persona.get('motivational_drive', 'truth-seeking')}
Ideal Reader: {persona.get('ideal_reader', 'data-literate critical thinker')}
Temporal Focus: {persona.get('temporal_focus', 'long-term')}
Philosophical Alignment: {persona.get('philosophical_alignment', 'empirical rationalism')}
Epistemology: {persona.get('epistemology', 'scientific realism')}
Certainty Expression: {persona.get('certainty_expression', 'probabilistic')}
Narrative Structure: {persona.get('narrative_structure', 'logical progression')}

Generate a short, smooth transition phrase (1-2 sentences) from a news segment about '{previous_topic}' to a new segment about '{current_topic}'.

Avoid using the word 'meanwhile'. Focus on natural flow and clarity of connection. 
"""