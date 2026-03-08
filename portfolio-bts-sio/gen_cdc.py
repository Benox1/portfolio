# -*- coding: utf-8 -*-
from fpdf import FPDF
from fpdf.enums import XPos, YPos
import datetime, os

OUTPUT = "ARAM_Cup_Cahier_des_charges.pdf"
FONTS  = r"C:\Windows\Fonts"

# Couleurs
DARK       = (10, 10, 20)
DARK2      = (18, 22, 45)
ACCENT     = (88, 106, 246)
ACCENT2    = (34, 200, 238)
GOLD       = (220, 165, 30)
WHITE      = (235, 240, 255)
GREY       = (130, 140, 175)
GREY_LIGHT = (200, 210, 235)

class CDC(FPDF):
    def __init__(self):
        super().__init__('P', 'mm', 'A4')
        self.set_auto_page_break(auto=True, margin=22)
        # Polices Unicode (Arial Windows)
        self.add_font('Reg',  '',  os.path.join(FONTS, 'arial.ttf'))
        self.add_font('Reg',  'B', os.path.join(FONTS, 'arialbd.ttf'))
        self.add_font('Reg',  'I', os.path.join(FONTS, 'ariali.ttf'))
        self.add_font('Reg',  'BI',os.path.join(FONTS, 'arialbi.ttf'))

    def _bg(self):
        self.set_fill_color(*DARK)
        self.rect(0, 0, 210, 300, 'F')

    def header(self):
        if self.page_no() == 1:
            return
        self.set_fill_color(*DARK2)
        self.rect(0, 0, 210, 11, 'F')
        self.set_fill_color(*ACCENT)
        self.rect(0, 0, 4, 11, 'F')
        self.set_font('Reg', 'B', 7.5)
        self.set_text_color(*ACCENT2)
        self.set_xy(8, 2.5)
        self.cell(130, 6, 'ARAM CUP - Cahier des charges officiel', align='L',
                  new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_text_color(*GREY)
        self.cell(0, 6, f'Page {self.page_no()}', align='R',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_y(14)

    def footer(self):
        self.set_y(-12)
        self.set_fill_color(*DARK2)
        self.rect(0, self.get_y(), 210, 14, 'F')
        self.set_font('Reg', 'I', 7)
        self.set_text_color(*GREY)
        self.cell(0, 6,
            f'ARAM Cup - Document de reference - {datetime.date.today().strftime("%d/%m/%Y")}',
            align='C')

    # ─────────────────────────────────────────────
    def cover_page(self):
        self.add_page()
        self._bg()
        # Bandes decoratives
        self.set_fill_color(*ACCENT)
        self.rect(0, 0, 210, 7, 'F')
        self.set_fill_color(*ACCENT2)
        self.rect(0, 7, 210, 2.5, 'F')
        self.set_fill_color(*ACCENT)
        self.rect(0, 288, 210, 9, 'F')

        # Titre
        self.set_xy(0, 72)
        self.set_font('Reg', 'B', 44)
        self.set_text_color(*WHITE)
        self.cell(210, 18, 'ARAM CUP', align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.set_font('Reg', 'I', 15)
        self.set_text_color(*ACCENT2)
        self.cell(210, 10, 'Tournoi Communautaire - League of Legends', align='C',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        self.ln(12)
        self.set_fill_color(*ACCENT2)
        self.rect(60, self.get_y(), 90, 1, 'F')
        self.ln(13)

        self.set_font('Reg', 'B', 28)
        self.set_text_color(*WHITE)
        self.cell(210, 12, 'CAHIER DES CHARGES', align='C',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)
        self.set_font('Reg', '', 11)
        self.set_text_color(*GREY)
        self.cell(210, 7, 'Site web officiel - Systeme automatise de classements', align='C',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Bloc meta
        bx, by, bw, bh = 40, 198, 130, 66
        self.set_fill_color(*DARK2)
        self.set_draw_color(*ACCENT)
        self.set_line_width(0.4)
        self.rect(bx, by, bw, bh, 'FD')
        self.set_fill_color(*ACCENT)
        self.rect(bx, by, bw, 8, 'F')
        self.set_font('Reg', 'B', 8.5)
        self.set_text_color(*WHITE)
        self.set_xy(bx, by)
        self.cell(bw, 8, 'INFORMATIONS DU DOCUMENT', align='C',
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        meta = [
            ('Version',       '1.0'),
            ('Date',          datetime.date.today().strftime('%d %B %Y')),
            ('Statut',        'Document de reference'),
            ('Technologies',  'HTML - CSS - Python - Google Sheets API - Discord'),
            ('Auteur',        '-'),
        ]
        y = by + 10
        for k, v in meta:
            self.set_xy(bx + 5, y)
            self.set_font('Reg', 'B', 8.5)
            self.set_text_color(*ACCENT2)
            self.cell(35, 6, k + ' :', align='L', new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_font('Reg', '', 8.5)
            self.set_text_color(*WHITE)
            self.cell(84, 6, v, align='L')
            y += 9

    # ─────────────────────────────────────────────
    def toc_page(self, sections):
        self.add_page()
        self._bg()
        self.chapter_title('TABLE DES MATIERES', numbered=False)
        self.ln(3)
        for num, title, _ in sections:
            self.set_x(18)
            self.set_font('Reg', 'B', 9.5)
            self.set_text_color(*ACCENT2)
            self.cell(10, 7, str(num) + '.', new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_font('Reg', '', 9.5)
            self.set_text_color(*WHITE)
            self.cell(130, 7, '  ' + title, new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_text_color(*GREY)
            dots = '.' * max(0, 35 - len(title) // 3)
            self.cell(0, 7, dots, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # ─────────────────────────────────────────────
    def chapter_title(self, title, numbered=True, num=''):
        self.set_fill_color(*DARK2)
        self.rect(0, self.get_y() - 1, 210, 15, 'F')
        self.set_fill_color(*ACCENT)
        self.rect(0, self.get_y() - 1, 5, 15, 'F')
        self.set_x(10)
        if numbered and num:
            self.set_font('Reg', 'B', 14)
            self.set_text_color(*ACCENT2)
            self.cell(14, 13, str(num) + '.', new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.set_font('Reg', 'B', 13)
        self.set_text_color(*WHITE)
        self.cell(0, 13, '  ' + title if (numbered and num) else title,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(5)

    def section_title(self, title):
        self.ln(3)
        self.set_fill_color(*ACCENT2)
        self.rect(18, self.get_y(), 2.5, 7, 'F')
        self.set_x(24)
        self.set_font('Reg', 'B', 10.5)
        self.set_text_color(*ACCENT2)
        self.cell(0, 7, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def body(self, text):
        self.set_x(18)
        self.set_font('Reg', '', 9.5)
        self.set_text_color(*GREY_LIGHT)
        self.multi_cell(174, 5.5, text.strip(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(2)

    def bullet(self, items):
        for item in items:
            self.set_x(18)
            self.set_font('Reg', 'B', 9.5)
            self.set_text_color(*ACCENT2)
            self.cell(7, 5.5, '>', new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_font('Reg', '', 9.5)
            self.set_text_color(*GREY_LIGHT)
            self.multi_cell(165, 5.5, item, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(1)

    def table(self, headers, rows, col_widths=None):
        if col_widths is None:
            col_widths = [174 // len(headers)] * len(headers)
        self.set_x(18)
        self.set_fill_color(*ACCENT)
        self.set_text_color(*WHITE)
        self.set_font('Reg', 'B', 8.5)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, '  ' + h, fill=True, align='L',
                      new_x=XPos.RIGHT, new_y=YPos.TOP)
        self.ln()
        self.set_font('Reg', '', 8.5)
        for ri, row in enumerate(rows):
            self.set_x(18)
            fc = DARK2 if ri % 2 == 0 else (24, 28, 58)
            self.set_fill_color(*fc)
            self.set_text_color(*GREY_LIGHT)
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 6.5, '  ' + str(cell), fill=True, align='L',
                          new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.ln()
        self.ln(4)

    def info_box(self, title, text, color=None):
        if color is None:
            color = ACCENT
        self.set_x(18)
        self.set_fill_color(*color)
        self.set_font('Reg', 'B', 8.5)
        self.set_text_color(*WHITE)
        self.cell(174, 6.5, '  ' + title.upper(), fill=True,
                  new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.set_x(18)
        self.set_fill_color(*DARK2)
        self.set_font('Reg', '', 8.5)
        self.set_text_color(*GREY_LIGHT)
        self.multi_cell(174, 5.5, text.strip(), fill=True,
                        new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self.ln(4)


# ══════════════════════════════════════════════════════════════
def build():
    pdf = CDC()

    sections = [
        (1,  'Presentation du projet', ''),
        (2,  'Contexte et objectifs', ''),
        (3,  'Public cible', ''),
        (4,  'Arborescence du site', ''),
        (5,  'Description detaillee des pages', ''),
        (6,  'Charte graphique', ''),
        (7,  'Architecture technique', ''),
        (8,  'Script Python et Google Sheets API', ''),
        (9,  'Bot Discord et systeme de mise a jour', ''),
        (10, 'Organisation des fichiers', ''),
        (11, 'Contraintes techniques', ''),
        (12, 'Evolutions possibles', ''),
        (13, 'Planning indicatif', ''),
        (14, 'Conclusion', ''),
    ]

    pdf.cover_page()
    pdf.toc_page(sections)

    def new_chapter(num, title):
        pdf.add_page()
        pdf._bg()
        pdf.chapter_title(title, numbered=True, num=num)

    # ── 1. Presentation ─────────────────────────────────────────
    new_chapter(1, 'Presentation du projet')
    pdf.body(
        "ARAM Cup est un tournoi communautaire en ligne organise autour du mode ARAM "
        "(All Random All Mid) du jeu League of Legends. Ce document constitue le cahier des charges "
        "du site web officiel du tournoi, decrivant son architecture, ses fonctionnalites, ses choix "
        "technologiques et son organisation."
    )
    pdf.body(
        "Le site a ete concu pour etre simple a maintenir, visuellement immersif et automatise. "
        "Il repose exclusivement sur des technologies legeres (HTML, CSS, Python) sans necessiter "
        "de serveur ou de base de donnees dediee, ce qui garantit son accessibilite et sa facilite "
        "de deploiement."
    )
    pdf.info_box("Perimetre du projet",
        "Ce cahier des charges couvre :\n"
        "- Le site web statique (HTML/CSS) de l'ARAM Cup\n"
        "- Le script Python de collecte et de generation d'images\n"
        "- L'integration avec l'API Google Sheets\n"
        "- Le bot Discord d'automatisation des mises a jour\n"
        "- L'organisation des fichiers et les contraintes techniques")

    # ── 2. Contexte & objectifs ──────────────────────────────────
    new_chapter(2, 'Contexte et objectifs')
    pdf.section_title('Contexte')
    pdf.body(
        "La communaute gaming organisatrice de l'ARAM Cup souhaitait disposer d'un espace officiel "
        "en ligne pour presenter son tournoi, ses participants et ses resultats. Face a la complexite "
        "et au cout d'un site dynamique classique, le choix s'est porte sur une architecture statique "
        "augmentee par un pipeline automatise de generation d'images a partir de donnees issues de "
        "Google Sheets."
    )
    pdf.section_title('Objectifs principaux')
    pdf.bullet([
        "Presenter le tournoi ARAM Cup et ses regles de maniere claire et attrayante",
        "Mettre en avant les joueurs participants avec leurs profils et reseaux sociaux",
        "Afficher les classements individuels et par equipes en temps quasi-reel",
        "Presenter les statistiques de performances des joueurs (kills, assists, victoires, etc.)",
        "Centraliser toutes les informations du tournoi en un seul endroit",
        "Offrir une experience visuelle immersive dans un univers e-sport / gaming",
        "Permettre aux administrateurs de mettre a jour le site facilement via Discord",
    ])
    pdf.section_title('Objectifs secondaires')
    pdf.bullet([
        "Maintenir des couts d'hebergement faibles (site statique, pas de serveur dedie)",
        "Garantir la maintenabilite du projet par un developpeur unique",
        "Permettre des evolutions futures sans refonte complete (historique, nouvelles epreuves)",
        "Automatiser au maximum les taches repetitives (mise a jour des classements, images)",
    ])

    # ── 3. Public cible ──────────────────────────────────────────
    new_chapter(3, 'Public cible')
    pdf.body("Le site s'adresse a plusieurs types d'utilisateurs :")
    pdf.table(
        ['Profil', 'Besoins principaux', 'Frequence de visite'],
        [
            ['Joueurs participants', 'Consulter classements, stats, regles', 'Quotidienne'],
            ['Spectateurs / fans', 'Suivre le tournoi, resultats, classements', 'Hebdomadaire'],
            ['Communaute gaming', 'Decouvrir le tournoi, les joueurs', 'Ponctuelle'],
            ['Administrateurs', 'Verifier les mises a jour du site', 'Apres chaque update'],
            ['Streamers / createurs', 'Informations pour commentaires live', 'En direct'],
        ],
        col_widths=[50, 80, 44]
    )
    pdf.body(
        "Le design doit donc etre lisible rapidement, les informations cles (classements, resultats) "
        "accessibles en quelques secondes des la page d'accueil."
    )

    # ── 4. Arborescence ──────────────────────────────────────────
    new_chapter(4, 'Arborescence du site')
    pdf.body("Le site est structure autour de cinq pages principales reliees par un header et footer communs :")
    pdf.table(
        ['Fichier', 'Nom de la page', 'Role'],
        [
            ['index.html', 'Accueil', 'Page principale, presentation du tournoi'],
            ['participants.html', 'Participants', 'Cartes de joueurs avec reseaux sociaux'],
            ['classement.html', 'Classement', 'Classement solo et par equipes (images auto)'],
            ['regles.html', 'Regles', 'Reglement complet du tournoi'],
            ['header / footer', 'En-tete / Pied de page', 'Navigation commune a toutes les pages'],
        ],
        col_widths=[42, 42, 90]
    )
    pdf.section_title('Organisation des dossiers')
    pdf.bullet([
        "/ (racine) - fichiers HTML de chaque page",
        "/assets/img/ - images de l'interface (tiles, titres, cartes, fonds)",
        "/assets/img/rankings/ - images generees automatiquement par le script Python",
        "/assets/css/ - fichiers de styles (style.css)",
        "/assets/fonts/ - polices locales (style gaming/e-sport)",
        "/scripts/ - script Python de mise a jour (update.py)",
        "/scripts/credentials/ - cle API Google Sheets (dans .gitignore)",
    ])

    # ── 5. Description des pages ─────────────────────────────────
    new_chapter(5, 'Description detaillee des pages')

    pdf.section_title('5.1 - Page d\'accueil (index.html)')
    pdf.body("Point d'entree du site. Elle doit capter l'attention immediatement et communiquer l'identite du tournoi.")
    pdf.bullet([
        "Banniere principale avec le logo ARAM Cup et le nom du tournoi",
        "Presentation courte du tournoi (format, nombre de joueurs, saison en cours)",
        "Affichage des derniers resultats ou du prochain match a venir",
        "Navigation claire vers les autres sections du site",
        "Ambiance visuelle forte (fond immersif type Summoner's Rift ARAM)",
    ])

    pdf.section_title('5.2 - Page Participants (participants.html)')
    pdf.body("Galerie des joueurs inscrits au tournoi.")
    pdf.bullet([
        "Affichage en grille de cartes joueurs individuelles",
        "Chaque carte : pseudo LoL, avatar, nom d'equipe, rang / tier LoL",
        "Liens vers les profils externes du joueur (Twitch, Twitter/X, Discord, OP.GG)",
        "Effet hover sur les cartes pour mettre en valeur le joueur selectionne",
        "Filtrage optionnel par equipe ou par role",
    ])

    pdf.section_title('5.3 - Page Classement (classement.html)')
    pdf.body(
        "Page centrale du tournoi. Les classements sont presentes sous forme d'images generees "
        "automatiquement par le script Python."
    )
    pdf.bullet([
        "Section classement solo : rang de chaque joueur en fonction de ses performances",
        "Section classement par equipes : score global par equipe",
        "Images PNG generees automatiquement et embarquees via une balise <img>",
        "Horodatage de la derniere mise a jour affiche sur la page",
        "Style des images coherent avec la charte graphique (fond sombre, accents dores/bleus)",
    ])

    pdf.section_title('5.4 - Page Regles (regles.html)')
    pdf.body("Presentation structuree du reglement officiel du tournoi.")
    pdf.bullet([
        "Format du tournoi (nombre de rounds, systeme de points, criteres de classement)",
        "Regles de jeu specifiques au mode ARAM Cup",
        "Regles de conduite et fair-play",
        "Procedures en cas de deconnexion, lag, dispute",
        "Contact des organisateurs et modalites de reclamation",
    ])

    pdf.section_title('5.5 - Header et Footer communs')
    pdf.bullet([
        "Header : logo ARAM Cup, navigation principale, compte a rebours optionnel",
        "Footer : mentions legales, lien Discord officiel, credits, saison en cours",
        "Ces composants sont identiques sur toutes les pages du site",
    ])

    # ── 6. Charte graphique ──────────────────────────────────────
    new_chapter(6, 'Charte graphique')
    pdf.body(
        "L'identite visuelle d'ARAM Cup s'inscrit dans l'univers e-sport / gaming avec une esthetique "
        "sombre et des accents vibrants. Le design est principalement compositionnel : les images "
        "pre-concues definissent la majorite de l'interface."
    )
    pdf.table(
        ['Element', 'Valeur / Description'],
        [
            ['Ambiance', 'E-sport dark / gaming immersif'],
            ['Couleur de fond principale', 'Noir profond a bleu sombre (#080A18 - #0D1033)'],
            ['Accent principal', 'Or / Jaune LoL (#C89B3C - #F0C060)'],
            ['Accent secondaire', 'Bleu electrique / Cyan (#22D3EE - #3B82F6)'],
            ['Couleur texte', 'Blanc casse / gris clair (#E8EEFF)'],
            ['Police des titres', 'Beaufort for LOL / Cinzel / Orbitron (style epique)'],
            ['Police du corps', 'Raleway / Inter / Roboto (lisibilite)'],
            ['Style images classement', 'Fond sombre, texte dore, tableau structure, logo ARAM Cup'],
            ['Effets visuels', 'Lueurs (glow), ombres profondes, animations CSS legeres'],
            ['Responsive', 'Priorite desktop, adaptation mobile basique'],
        ],
        col_widths=[70, 104]
    )
    pdf.info_box("Note sur les images d'interface",
        "L'interface du site repose en grande partie sur des images graphiques pre-concues "
        "(panneaux, titres, divisions, backgrounds...). Ces assets constituent le coeur visuel "
        "du site et doivent etre crees en amont du developpement HTML/CSS. "
        "Les images de classements sont quant a elles generees dynamiquement par le script Python.",
        GOLD)

    # ── 7. Architecture technique ─────────────────────────────────
    new_chapter(7, 'Architecture technique')
    pdf.body("Le projet repose sur une architecture volontairement simple et sans backend :")
    pdf.table(
        ['Couche', 'Technologie', 'Role'],
        [
            ['Presentation', 'HTML5 + CSS3', 'Structure et style du site'],
            ['Donnees', 'Google Sheets', 'Base de donnees legere du tournoi'],
            ['Traitement', 'Python 3.x', 'Collecte, calcul et generation d\'images'],
            ['Images dynamiques', 'Pillow (PIL)', 'Generation des visuels de classement'],
            ['API donnees', 'Google Sheets API v4', 'Acces aux donnees du tournoi'],
            ['Automatisation', 'discord.py (Bot)', 'Declenchement des mises a jour'],
            ['Hebergement', 'GitHub Pages / Netlify', 'Hosting du site statique'],
            ['Versionning', 'Git / GitHub', 'Gestion du code source'],
        ],
        col_widths=[38, 50, 86]
    )
    pdf.section_title('Flux de donnees global')
    pdf.bullet([
        "1. Les donnees du tournoi (scores, resultats...) sont saisies dans Google Sheets",
        "2. Le script Python est declenche (manuellement ou via commande Discord)",
        "3. Le script se connecte a l'API Google Sheets et recupere les donnees",
        "4. Il calcule les classements, trie les joueurs, agregge les statistiques",
        "5. Il genere les images PNG de classement et statistiques",
        "6. Les images sont enregistrees dans /assets/img/rankings/",
        "7. Le site HTML charge automatiquement ces nouvelles images au prochain affichage",
    ])

    # ── 8. Script Python & Google Sheets ─────────────────────────
    new_chapter(8, 'Script Python et Google Sheets API')
    pdf.section_title('Connexion a l\'API Google Sheets')
    pdf.body(
        "Le script Python utilise la bibliotheque gspread et google-auth pour se connecter a "
        "l'API Google Sheets. L'authentification est realisee via un compte de service "
        "(service account) avec un fichier de cle JSON prive, partage avec le Google Sheet."
    )
    pdf.bullet([
        "Bibliotheques requises : gspread, google-auth, Pillow, pandas (optionnel)",
        "Authentification : Service Account (cle JSON dans /scripts/credentials/)",
        "Acces en lecture seule sur la feuille de calcul du tournoi",
        "Donnees lues : onglets joueurs, resultats des matchs, statistiques par game",
    ])
    pdf.section_title('Traitement des donnees')
    pdf.bullet([
        "Lecture des lignes de resultats (score, kills, deaths, assists par joueur par partie)",
        "Calcul des totaux et moyennes : kills/game, win rate, score total de classement",
        "Tri et ranking des joueurs selon les criteres definis (points, ratio K/D, victoires)",
        "Agregation des resultats par equipe pour le classement par equipes",
        "Formatage des donnees pour l'affichage (nombres entiers, pourcentages, rangs)",
    ])
    pdf.section_title('Generation des images')
    pdf.body(
        "Le script genere des images PNG a dimensions fixes, stylisees selon la charte graphique."
    )
    pdf.bullet([
        "Bibliotheque : Pillow (PIL) pour la creation et la mise en page",
        "Fond : image de base (template PNG) chargee en amont",
        "Contenu superpose : texte (pseudo, score, rang), icones, tableau",
        "Polices : fichiers .ttf locaux pour le style gaming",
        "Export : fichiers PNG dans /assets/img/rankings/ (nommage fixe)",
    ])
    pdf.info_box("Schema de fonctionnement simplifie",
        "update.py\n"
        "  -> gspread.open('ARAM_Cup_Data').worksheet('Resultats')\n"
        "  -> Lecture des lignes -> calcul des classements\n"
        "  -> Pillow.Image.open('template_classement.png')\n"
        "  -> Ecriture du texte (pseudo, score) sur l'image template\n"
        "  -> Sauvegarde -> assets/img/rankings/classement_solo.png", ACCENT2)

    # ── 9. Bot Discord ───────────────────────────────────────────
    new_chapter(9, 'Bot Discord et systeme de mise a jour')
    pdf.section_title('Role du bot Discord')
    pdf.body(
        "Un bot Discord (developpe avec discord.py) permet aux administrateurs du tournoi de "
        "declencher la mise a jour du site depuis le serveur Discord officiel, sans acces direct "
        "au serveur d'hebergement ou a la machine locale."
    )
    pdf.section_title('Fonctionnement de la commande de mise a jour')
    pdf.bullet([
        "Commande : !update (ou slash command /update selon la version du bot)",
        "Verification des permissions : seuls les roles Administrateur / Organisateur peuvent declencher",
        "Le bot execute le script Python update.py en sous-processus (subprocess.run)",
        "Le script recupere les nouvelles donnees Google Sheets et regenere les images",
        "Le bot envoie un message de confirmation dans le canal Discord avec un resume",
        "En cas d'erreur, le bot capture l'exception et envoie un message d'erreur",
    ])
    pdf.section_title('Deploiement du bot')
    pdf.bullet([
        "Hebergement : le bot doit tourner en continu (VPS, Raspberry Pi, ou Railway.app)",
        "Token Discord : stocke dans une variable d'environnement .env (jamais en dur)",
        "Bibliotheques : discord.py, python-dotenv",
        "Le bot peut envoyer automatiquement les images dans un canal #classements",
    ])
    pdf.info_box("Securite - Points critiques",
        "Le fichier de cle Google Sheets (JSON) et le token Discord doivent imperativement "
        "rester hors du depot Git. Utiliser un fichier .env et l'ajouter au .gitignore. "
        "Ne jamais exposer ces credentials dans le code source ou dans les commits.", GOLD)

    # ── 10. Organisation des fichiers ────────────────────────────
    new_chapter(10, 'Organisation des fichiers')
    pdf.body("Structure complete du depot Git du projet :")
    pdf.bullet([
        "aram-cup/",
        "  |- index.html",
        "  |- participants.html",
        "  |- classement.html",
        "  |- regles.html",
        "  |- assets/",
        "  |   |- css/  ->  style.css",
        "  |   |- fonts/  ->  polices .ttf / .woff",
        "  |   `- img/",
        "  |       |- ui/  ->  images d'interface statiques",
        "  |       `- rankings/  ->  images generees par Python",
        "  |- scripts/",
        "  |   |- update.py   ->  script principal de mise a jour",
        "  |   |- bot.py      ->  bot Discord",
        "  |   |- sheets.py   ->  module Google Sheets",
        "  |   |- generator.py ->  module generation images",
        "  |   `- credentials/ ->  cle JSON (gitignore)",
        "  |- .env         ->  tokens secrets (gitignore)",
        "  |- .gitignore",
        "  |- requirements.txt",
        "  `- README.md",
    ])

    # ── 11. Contraintes techniques ───────────────────────────────
    new_chapter(11, 'Contraintes techniques')
    pdf.table(
        ['Contrainte', 'Detail'],
        [
            ['Pas de backend', 'Le site est purement statique. Aucun langage serveur (PHP, Node.js...)'],
            ['Pas de BDD', 'Google Sheets sert de source de donnees unique'],
            ['Quota API Google', 'API limitee (100 req/100s). Prevoir une gestion des erreurs 429'],
            ['Nommage images', 'Les images generees doivent avoir un nom fixe pour le HTML'],
            ['Compatibilite', 'Cibler Chrome, Firefox, Edge. Mobile : affichage basique acceptable'],
            ['Accessibilite', 'Attributs alt sur toutes les images. Contrastes suffisants.'],
            ['Securite cles', 'Token Discord + cle JSON Google en .env/.gitignore'],
            ['Hebergement bot', 'Le bot doit tourner 24/7 sur une machine dediee (VPS recommande)'],
            ['Taille images', 'Optimiser les PNG (poids < 500 Ko) pour des temps de chargement rapides'],
        ],
        col_widths=[52, 122]
    )

    # ── 12. Evolutions possibles ─────────────────────────────────
    new_chapter(12, 'Evolutions possibles')
    pdf.section_title('Court terme')
    pdf.bullet([
        "Ajout d'un historique des tournois precedents (saisons passees archivees)",
        "Statistiques avancees par joueur : KDA moyen, champion le plus joue, win rate detaille",
        "Page de resultats match par match avec detail des parties",
        "Galerie de highlights / clips integree (Twitch clips / YouTube)",
    ])
    pdf.section_title('Moyen terme')
    pdf.bullet([
        "Systeme de bracket / arbre de tournoi genere automatiquement via Challonge API",
        "Integration de l'API Riot Games pour recuperer les stats directement depuis les comptes",
        "Interface d'administration legere (formulaire protege) pour saisir les scores sans Google Sheets",
        "Notifications automatiques sur Discord lors de chaque mise a jour (embed avec resume)",
    ])
    pdf.section_title('Long terme')
    pdf.bullet([
        "Migration vers un generateur de site statique (11ty, Hugo, Jekyll) pour plus de maintenabilite",
        "Mode spectateur live (overlay OBS avec les stats en temps reel)",
        "Ouverture a d'autres jeux (Valorant, TFT) avec des sections dediees",
        "Tableau de bord d'administration complet avec gestion des joueurs et des equipes",
    ])

    # ── 13. Planning indicatif ───────────────────────────────────
    new_chapter(13, 'Planning indicatif')
    pdf.body("Planning estimatif pour une equipe d'un developpeur solo :")
    pdf.table(
        ['Phase', 'Taches principales', 'Duree estimee'],
        [
            ['Phase 1 - Conception', 'Assets graphiques, maquettes, Google Sheet', '1 semaine'],
            ['Phase 2 - Integration HTML/CSS', 'Structure de toutes les pages, header, footer, styles', '1-2 semaines'],
            ['Phase 3 - Script Python', 'Connexion API Sheets, calcul classements, gen. images', '1-2 semaines'],
            ['Phase 4 - Bot Discord', 'Developpement bot, commandes, gestion des erreurs', '3-5 jours'],
            ['Phase 5 - Tests', 'Tests bout en bout, corrections, ajustements visuels', '3-5 jours'],
            ['Phase 6 - Deploiement', 'Mise en ligne (GitHub Pages), bot sur VPS', '1-2 jours'],
            ['Phase 7 - Documentation', 'README, guide d\'utilisation pour l\'organisateur', '1 jour'],
        ],
        col_widths=[48, 92, 34]
    )
    pdf.body("Duree totale estimee : 4 a 6 semaines pour un developpeur avec une bonne maitrise des technologies.")

    # ── 14. Conclusion ───────────────────────────────────────────
    new_chapter(14, 'Conclusion')
    pdf.body(
        "Le projet ARAM Cup represente une solution technique ingenieuse pour creer un site de tournoi "
        "professionnel sans les contraintes d'un backend lourd. En combinant un site statique HTML/CSS, "
        "Python pour le traitement et la generation d'images, et Google Sheets comme source de donnees, "
        "le projet atteint un equilibre optimal entre facilite de maintenance et richesse des fonctionnalites."
    )
    pdf.body(
        "L'automatisation via le bot Discord constitue un veritable atout : elle permet a l'organisateur "
        "de mettre a jour les classements en temps reel, depuis n'importe quel appareil, en une simple "
        "commande, sans manipulation technique complexe."
    )
    pdf.body(
        "Ce cahier des charges servira de reference tout au long du developpement et permettra a tout "
        "collaborateur de s'approprier rapidement l'architecture et le fonctionnement du projet."
    )
    pdf.ln(10)
    pdf.set_fill_color(*ACCENT)
    pdf.rect(18, pdf.get_y(), 174, 1.5, 'F')
    pdf.ln(10)
    pdf.set_font('Reg', 'B', 11)
    pdf.set_text_color(*GOLD)
    pdf.set_x(18)
    pdf.cell(0, 8, '>> Bonne chance a tous les participants de l\'ARAM Cup ! <<',
             align='C', new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    pdf.output(OUTPUT)
    print(f"PDF genere : {OUTPUT}")


if __name__ == '__main__':
    build()
