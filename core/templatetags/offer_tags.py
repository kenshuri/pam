# offers/templatetags/instrument_tags.py
from django import template

register = template.Library()

INSTRUMENT_LABELS = {
    'voice': 'Voix / Chant',
    'choir_conductor': 'Chef de chœur',
    'piano': 'Piano',
    'organ': 'Orgue',
    'harpsichord': 'Clavecin',
    'synthesizer': 'Synthétiseur',
    'accordeon': 'Accordéon',
    'violin': 'Violon',
    'viola': 'Alto',
    'cello': 'Violoncelle',
    'double_bass': 'Contrebasse',
    'viola_da_gamba': 'Viole de gambe',
    'guitar': 'Guitare',
    'electric_guitar': 'Guitare électrique',
    'bass_guitar': 'Basse',
    'mandolin': 'Mandoline',
    'lute': 'Luth',
    'oud': 'Oud',
    'sitar': 'Sitar',
    'ukulele': 'Ukulélé',
    'flute': 'Flûte',
    'recorder': 'Flûte à bec',
    'clarinet': 'Clarinette',
    'oboe': 'Hautbois',
    'bassoon': 'Basson',
    'saxophone': 'Saxophone',
    'trumpet': 'Trompette',
    'trombone': 'Trombone',
    'french_horn': 'Cor',
    'tuba': 'Tuba',
    'drums': 'Batterie',
    'classical_percussion': 'Percussions classiques',
    'djembe': 'Djembé',
    'congas': 'Congas',
    'cajon': 'Cajón',
    'electronic_music': 'MAO',
    'dj': 'DJ / Mix',
    'sound_design': 'Sound design',
    'ondes_martenot': 'Ondes Martenot',
    'theremin': 'Thérémine',
    'other': 'Autre',
}

@register.filter
def instrument_label(value):
    return INSTRUMENT_LABELS.get(value, value)


STYLE_LABELS = {
    # Musique classique et contemporaine
    'classical': 'Musique classique',
    'baroque': 'Musique baroque',
    'romantic': 'Musique romantique',
    'contemporary_classical': 'Musique contemporaine',
    'early_music': 'Musique ancienne',
    'electroacoustic': 'Musique électroacoustique',

    # Musiques actuelles
    'pop': 'Pop',
    'rock': 'Rock',
    'indie': 'Indé',
    'metal': 'Metal',
    'punk': 'Punk',
    'jazz': 'Jazz',
    'blues': 'Blues',
    'funk': 'Funk',
    'soul': 'Soul',
    'reggae': 'Reggae',
    'rap': 'Rap',
    'hiphop': 'Hip-hop',
    'rnb': 'R&B',
    'electronic': 'Musique électronique',
    'techno': 'Techno',
    'house': 'House',
    'ambient': 'Ambient',
    'lofi': 'Lo-fi',

    # Musiques traditionnelles et du monde
    'world': 'Musiques du monde',
    'african': 'Musique africaine',
    'arabic': 'Musique arabe',
    'indian': 'Musique indienne',
    'asian': 'Musiques asiatiques',
    'latin': 'Musique latino-américaine',
    'flamenco': 'Flamenco',
    'celtic': 'Musique celtique',
    'balkan': 'Musiques balkaniques',
    'klezmer': 'Klezmer',

    # Musique vocale et chorale
    'choral': 'Musique chorale',
    'opera': 'Opéra',
    'vocal': 'Musique vocale',
    'a_cappella': 'A cappella',
    'chanson': 'Chanson française',

    # Autres
    'film_music': 'Musique de film',
    'musical_theatre': 'Comédie musicale',
    'experimental': 'Expérimental',
    'improvised': 'Musique improvisée',
    'sacred': 'Musique sacrée',
    'children': 'Musique pour enfants',
    'other': 'Autre',
}

@register.filter
def style_label(value):
    return STYLE_LABELS.get(value, value)
