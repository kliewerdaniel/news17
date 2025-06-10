import yaml

def load_persona(persona_file="persona.yaml"):
    """
    Loads persona traits from a YAML file and returns them as a dictionary.
    """
    try:
        with open(persona_file, 'r') as f:
            persona = yaml.safe_load(f)

        required_fields = [
    'name',
    'description',
    'tone',
    'style',
    'bias',
    'formality',
    'audience',
    'humor',
    'vocabulary_level',
    'perspective',
    'emotional_expression',
    'intellectual_focus',
    'moral_positioning',
    'rhetorical_style',
    'argumentation_method',
    'clarity_priority',
    'use_of_metaphor',
    'cultural_context',
    'reference_style',
    'domain_expertise',
    'critical_thinking',
    'opinion_strength',
    'dialogue_preference',
    'visual_imagery',
    'personal_disclosure',
    'value_system',
    'motivational_drive',
    'ideal_reader',
    'temporal_focus',
    'philosophical_alignment',
    'epistemology',
    'certainty_expression',
    'narrative_structure'
]        
        for field in required_fields:
            if field not in persona:
                raise ValueError(f"Missing required persona field: '{field}' in {persona_file}")

        return persona
    except FileNotFoundError:
        raise FileNotFoundError(f"Persona file '{persona_file}' not found.")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file '{persona_file}': {e}")
    except ValueError as e:
        raise e
