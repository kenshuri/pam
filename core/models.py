# Create your models here.
from django.db import models
from django.db.models import CheckConstraint, Q
from django.db.models.fields import CharField

from accounts.models import CustomUser
import datetime
import pytz

from moderation.models import ModerationResult


class Offer(models.Model):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'

    # Types d'annonces
    OFFER = 'offer'
    DEMAND = 'demand'
    TYPE_CHOICES = [
        (OFFER, 'Offre'),
        (DEMAND, 'Demande'),
    ]

    # Rubriques principales du site
    ARTISTS_GROUPS = 'artists_groups'
    COURSES_TRAINING = 'courses_training'
    CALLS_EVENTS = 'calls_events'
    SERVICES_EQUIPMENT = 'services_equipment'

    SECTION_CHOICES = [
        (ARTISTS_GROUPS, 'Artistes & Groupes'),
        (COURSES_TRAINING, 'Cours & Formations'),
        (CALLS_EVENTS, 'Appels & Événements'),
        (SERVICES_EQUIPMENT, 'Services & Matériel'),
    ]

    # Rémunération
    UNPAID = 'unpaid'
    PAID = 'paid'
    CATEGORY_CHOICES = [
        (UNPAID, 'Bénévole'),
        (PAID, 'Rémunéré'),
    ]

    # Champs principaux
    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
        default=OFFER,
    )

    section = models.CharField(
        max_length=255,
        choices=SECTION_CHOICES,
        default=ARTISTS_GROUPS)

    category = models.CharField(
        max_length=255,
        choices=CATEGORY_CHOICES,
        default=UNPAID,
    )

    title = models.CharField(max_length=50, null=False)
    summary = models.CharField(max_length=255, null=False)
    description = models.TextField(max_length=5000, blank=True)

    # Tags liés
    INSTRUMENT_CHOICES = [
        ('voice', 'Voix / Chant'),
        ('choir_conductor', 'Chef de chœur'),

        # Claviers
        ('piano', 'Piano'),
        ('organ', 'Orgue'),
        ('harpsichord', 'Clavecin'),
        ('synthesizer', 'Synthétiseur'),
        ('accordeon', 'Accordéon'),

        # Cordes frottées
        ('violin', 'Violon'),
        ('viola', 'Alto'),
        ('cello', 'Violoncelle'),
        ('double_bass', 'Contrebasse'),
        ('viola_da_gamba', 'Viole de gambe'),

        # Cordes pincées
        ('guitar', 'Guitare'),
        ('electric_guitar', 'Guitare électrique'),
        ('bass_guitar', 'Basse'),
        ('mandolin', 'Mandoline'),
        ('lute', 'Luth'),
        ('oud', 'Oud'),
        ('sitar', 'Sitar'),
        ('ukulele', 'Ukulélé'),

        # Bois
        ('flute', 'Flûte'),
        ('recorder', 'Flûte à bec'),
        ('clarinet', 'Clarinette'),
        ('oboe', 'Hautbois'),
        ('bassoon', 'Basson'),
        ('saxophone', 'Saxophone'),

        # Cuivres
        ('trumpet', 'Trompette'),
        ('trombone', 'Trombone'),
        ('french_horn', 'Cor'),
        ('tuba', 'Tuba'),

        # Percussions
        ('drums', 'Batterie'),
        ('classical_percussion', 'Percussions classiques'),
        ('djembe', 'Djembé'),
        ('congas', 'Congas'),
        ('cajon', 'Cajón'),

        # Instruments électroniques et MAO
        ('electronic_music', 'MAO / Musique assistée par ordinateur'),
        ('dj', 'DJ / Mix'),
        ('sound_design', 'Sound design'),

        # Autres
        ('ondes_martenot', 'Ondes Martenot'),
        ('theremin', 'Thérémine'),
        ('other', 'Autre'),
    ]
    instrument = models.CharField(max_length=50, choices=INSTRUMENT_CHOICES, blank=True)

    STYLE_CHOICES = [
        # Musique classique et contemporaine
        ('classical', 'Musique classique'),
        ('baroque', 'Musique baroque'),
        ('romantic', 'Musique romantique'),
        ('contemporary_classical', 'Musique contemporaine'),
        ('early_music', 'Musique ancienne'),
        ('electroacoustic', 'Musique électroacoustique'),

        # Musiques actuelles
        ('pop', 'Pop'),
        ('rock', 'Rock'),
        ('indie', 'Indé'),
        ('metal', 'Metal'),
        ('punk', 'Punk'),
        ('jazz', 'Jazz'),
        ('blues', 'Blues'),
        ('funk', 'Funk'),
        ('soul', 'Soul'),
        ('reggae', 'Reggae'),
        ('rap', 'Rap'),
        ('hiphop', 'Hip-hop'),
        ('rnb', 'R&B'),
        ('electronic', 'Musique électronique'),
        ('techno', 'Techno'),
        ('house', 'House'),
        ('ambient', 'Ambient'),
        ('lofi', 'Lo-fi'),

        # Musiques traditionnelles et du monde
        ('world', 'Musiques du monde'),
        ('african', 'Musique africaine'),
        ('arabic', 'Musique arabe'),
        ('indian', 'Musique indienne'),
        ('asian', 'Musiques asiatiques'),
        ('latin', 'Musique latino-américaine'),
        ('flamenco', 'Flamenco'),
        ('celtic', 'Musique celtique'),
        ('balkan', 'Musiques balkaniques'),
        ('klezmer', 'Klezmer'),

        # Musique vocale et chorale
        ('choral', 'Musique chorale'),
        ('opera', 'Opéra'),
        ('vocal', 'Musique vocale'),
        ('a_cappella', 'A cappella'),
        ('chanson', 'Chanson française'),

        # Autres
        ('film_music', 'Musique de film'),
        ('musical_theatre', 'Comédie musicale'),
        ('experimental', 'Expérimental'),
        ('improvised', 'Musique improvisée'),
        ('sacred', 'Musique sacrée'),
        ('children', 'Musique pour enfants'),
        ('other', 'Autre'),
    ]
    style = models.CharField(max_length=50, choices=STYLE_CHOICES, blank=True)

    city = models.CharField(max_length=255, blank=True)

    # Infos complémentaires
    created_on = models.DateTimeField(auto_now_add=True)
    filled = models.BooleanField(default=False)

    # Auteur
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    show_author_mail = models.BooleanField(default=False)

    # Contacts
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_phone = models.CharField(max_length=255, null=True, blank=True)
    contact_website = models.URLField(null=True, blank=True)
    contact_details = models.TextField(null=True, blank=True)

    # Modération
    moderation = models.ForeignKey(
        ModerationResult, null=True, blank=True,
        on_delete=models.SET_NULL, related_name="offers"
    )


    def __str__(self):
        return f'{self.title} - {self.author} - {self.created_on.strftime("%Y-%m-%d, %H:%M")}'

    @property
    def recent(self):
        utc = pytz.UTC
        offer_date = self.created_on
        threshold = utc.localize(datetime.datetime.now() - datetime.timedelta(weeks=1))
        return offer_date > threshold


    def get_moderation_text(self) -> str:
        """
        Retourne une chaîne de texte contenant toutes les informations importantes de l'annonce,
        formatée pour être soumise à la modération de contenu.
        """
        details = [
            f"Type: {self.get_type_display()}",
            f"Rubrique: {self.get_section_display()}",
            f"Rémunération: {self.get_category_display()}",
            f"Titre: {self.title}",
            f"Résumé: {self.summary}",
            f"Description: {self.description}",
            f"Instrument: {self.instrument}" if self.instrument else None,
            f"Style musical: {self.style}" if self.style else None,
            f"Ville: {self.city}" if self.city else None,
        ]

        # Filtrer les valeurs None et joindre les éléments par une nouvelle ligne
        return "\n".join(filter(None, details))

