# -*- coding: utf-8 -*-
import os, json

LOCALES_DIR = r"d:\Nitin\removesynth\apps\removesynth\src\content\locales"
os.makedirs(LOCALES_DIR, exist_ok=True)

def save(code, var_name, data):
    with open(os.path.join(LOCALES_DIR, f"{code}.ts"), "w", encoding="utf-8") as f:
        f.write(f"import type {{ HomeContent }} from '../types';\n\nexport const {var_name}: HomeContent = {json.dumps(data, ensure_ascii=False, indent=2)};\n")
    print(f"Saved {code}.ts")

# 1. EN
save("en", "en", {
  "lang": "en",
  "title": "SynthID Remover Online: Free for Images and Video",
  "description": "Free online SynthID remover for AI images and video. Upload PNG, JPG, WebP, MP4 or MOV to strip SynthID and C2PA losslessly in-browser with zero uploads.",
  "hero": {
    "eyebrow": "No sign-up · Free · Images, video & audio",
    "h1Before": "Free ",
    "h1Accent": "SynthID remover",
    "h1After": " online",
    "lead": "Remove SynthID from AI-generated images and videos. Upload your file, process it in one click, and download it in its original format and quality.",
    "checks": ["Images, video & audio", "Every video frame", "Files deleted after processing"],
    "worksWith": "Works with files from"
  },
  "features": [
    { "title": "Images and video", "text": "One SynthID remover for PNG, JPG and WebP stills and MP4, WebM and MOV clips." },
    { "title": "Every frame", "text": "On video, the whole clip is processed, not just a few sample frames." },
    { "title": "Original quality", "text": "Your file keeps its resolution, format and frame rate." },
    { "title": "No sign-up", "text": "Drop a file and go. No account needed during early access." },
    { "title": "Files deleted", "text": "Uploads are deleted as soon as your result is sent back. Nothing is kept." },
    { "title": "Works anywhere", "text": "Runs in any modern browser on desktop, tablet or phone." }
  ],
  "inside": {
    "kicker": "What’s inside an AI file",
    "h2": "Two ways AI content gets labelled",
    "p": "Most AI tools mark what they generate. Neither mark is visible.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "An invisible signal in the pixels",
        "html": "SynthID (sometimes written “Synth ID”) is woven into the image data and across every video frame. You can’t see it, and it is built to survive cropping, filters, compression and screenshots. <a href=\"/what-is-synthid/\">What is SynthID?</a>"
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "A signed record in the metadata",
        "html": "Many generators also attach C2PA Content Credentials, a signed note in the file’s metadata saying how it was made. <a href=\"/blog/synthid-vs-c2pa/\">SynthID vs C2PA</a>"
      }
    ]
  },
  "how": {
    "kicker": "How it works",
    "h2": "Remove SynthID in four steps",
    "steps": [
      { "title": "Drop your file", "text": "Choose an image or video made with a tool that applies SynthID, such as Gemini, Imagen or Veo." },
      { "title": "Confirm your rights", "text": "Tick the box to confirm you own the file or are allowed to process it." },
      { "title": "We process it", "text": "Your file is checked and processed on our server, frame by frame for video." },
      { "title": "Download", "text": "Compare before and after, then download the result in its original format." }
    ]
  },
  "plans": {
    "kicker": "Plans",
    "h2": "Free while in early access",
    "p": "Every feature is free during early access. Paid plans will add higher limits.",
    "free": {
      "name": "Free",
      "note": "no card needed",
      "items": ["Images and video", "Up to 50 MB per file", "Original quality", "No account needed"],
      "cta": "Process a file"
    },
    "pro": {
      "badge": "Coming soon",
      "price": "Credits",
      "note": "monthly or yearly",
      "items": ["Larger files and longer videos", "Batch processing", "Priority processing", "API access"]
    }
  },
  "hood": {
    "kicker": "Under the hood",
    "h2": "Built for quality and privacy",
    "cards": [
      { "title": "Every frame processed", "text": "Video is handled across the whole clip, so nothing is skipped between frames.", "tag": "frame 1 → 240 · done" },
      { "title": "Nothing kept", "text": "Files live in a temporary folder only while they’re processed, then they’re deleted.", "tag": "0 files stored" },
      { "title": "Original quality", "text": "Resolution, format and frame rate stay the same as the file you uploaded.", "tag": "1080×1920 · 30fps → 1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Who it’s for",
    "h2": "Built for people who work with their own AI media",
    "cards": [
      { "title": "Creators", "text": "You made the image or video and want the clean file you intended to export." },
      { "title": "Researchers & journalists", "text": "You’re testing watermark robustness and need a fast way to test files." },
      { "title": "Developers", "text": "You’re building media pipelines and want an API for batch processing. Coming soon." }
    ],
    "note": "Only process files you own or have permission to use, and always be transparent about how your media was made."
  },
  "seo": [
    {
      "h2": "How to use the SynthID remover",
      "html": "Drop your file into the box above, tick the confirmation to confirm your rights, and click <strong>Process file</strong>. Once it finishes, compare the before and after, then download the result. Read our step-by-step guide on <a href=\"/how-to-remove-synthid/\">how to remove SynthID watermarks</a> for more detail."
    },
    {
      "h2": "Which AI tools add SynthID?",
      "html": "Google adds SynthID to media generated across its AI products, including the Gemini app, Imagen and Veo."
    },
    {
      "h2": "Why editing doesn’t remove SynthID",
      "html": "SynthID isn’t a logo or a metadata tag. It’s woven into the pixels themselves, and Google designed it specifically to survive cropping, resizing, filters, compression and screenshots. Stripping metadata doesn’t touch it either. That’s why you need a dedicated tool to <a href=\"/remove-synthid/\">remove SynthID</a>."
    }
  ],
  "faqHeading": "Frequently asked questions",
  "faqs": [
    { "q": "What is a SynthID remover?", "a": "A SynthID remover is a tool that processes AI-generated images and videos carrying Google’s SynthID watermark. RemoveSynth is a free online tool: you upload a file and download a processed version." },
    { "q": "Is this SynthID remover free?", "a": "Yes. While in early access, RemoveSynth is completely free to use. Paid plans with higher limits and batch processing will be added later." },
    { "q": "What file types can I upload?", "a": "You can upload PNG, JPG and WebP images, and MP4, WebM and MOV videos up to the file size listed below the uploader." },
    { "q": "Do you keep my files?", "a": "No. Files are held in a temporary directory while being processed and deleted as soon as your download is ready. We never store them, use them for training, or share them." },
    { "q": "Does cropping or taking a screenshot remove SynthID?", "a": "No, not reliably. SynthID is embedded in the pixel data across the image and is designed to survive standard edits, screenshots and re-saving." },
    { "q": "Is RemoveSynth affiliated with Google?", "a": "No. RemoveSynth is an independent tool. SynthID is a technology and trademark of Google LLC." }
  ],
  "cta": { "h2": "Try the SynthID remover", "p": "Free, no sign-up, works on images and video.", "button": "Remove SynthID now" }
})

# 2. DE
save("de", "de", {
  "lang": "de",
  "title": "SynthID entfernen online: Kostenlos für KI-Bilder und Videos",
  "description": "Kostenloses Online-Tool zum Entfernen von SynthID aus KI-Bildern und Videos. Entfernen Sie SynthID und C2PA-Metadaten verlustfrei direkt im Browser.",
  "hero": {
    "eyebrow": "Ohne Anmeldung · Kostenlos · Bilder, Video & Audio",
    "h1Before": "Kostenlos ",
    "h1Accent": "SynthID entfernen",
    "h1After": " online",
    "lead": "Entfernen Sie SynthID aus KI-generierten Bildern und Videos. Datei hochladen, mit einem Klick verarbeiten und in Originalqualität herunterladen.",
    "checks": ["Bilder, Video & Audio", "Jedes Video-Frame", "Dateien sofort gelöscht"],
    "worksWith": "Funktioniert mit Dateien von"
  },
  "features": [
    { "title": "Bilder und Videos", "text": "Ein SynthID-Entferner für PNG-, JPG- und WebP-Bilder sowie MP4-, WebM- und MOV-Clips." },
    { "title": "Jedes Frame", "text": "Bei Videos wird der gesamte Clip verarbeitet, nicht nur Stichproben." },
    { "title": "Originalqualität", "text": "Auflösung, Format und Bildrate Ihrer Datei bleiben unverändert erhalten." },
    { "title": "Ohne Registrierung", "text": "Datei ablegen und loslegen. Keine Kontoerstellung erforderlich." },
    { "title": "Keine Speicherung", "text": "Uploads werden nach Abschluss sofort gelöscht. Es verbleiben keine Daten." },
    { "title": "Läuft überall", "text": "Funktioniert in jedem modernen Browser auf Desktop, Tablet oder Smartphone." }
  ],
  "inside": {
    "kicker": "Was in einer KI-Datei steckt",
    "h2": "Zwei Arten von KI-Kennzeichnungen",
    "p": "Die meisten KI-Werkzeuge markieren generierte Inhalte. Keine der beiden Markierungen ist sichtbar.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Ein unsichtbares Signal in den Pixeln",
        "html": "SynthID ist tief in die Bilddaten und jedes Video-Frame eingewoben. Es ist unsichtbar und übersteht Zuschnitt, Filter und Kompression. <a href=\"/de/was-ist-synthid/\">Was ist SynthID?</a>"
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Ein signierter Datensatz in den Metadaten",
        "html": "Viele Generatoren binden zudem C2PA-Zertifikate ein – digitale Herkunftsnachweise in den Metadaten."
      }
    ]
  },
  "how": {
    "kicker": "So funktioniert es",
    "h2": "SynthID in vier einfachen Schritten entfernen",
    "steps": [
      { "title": "Datei auswählen", "text": "Wählen Sie ein Bild oder Video von Gemini, Imagen oder Veo." },
      { "title": "Rechte bestätigen", "text": "Bestätigen Sie per Häkchen, dass Sie zur Verarbeitung berechtigt sind." },
      { "title": "Automatische Verarbeitung", "text": "Ihre Datei wird Frame für Frame geprüft und bereinigt." },
      { "title": "Herunterladen", "text": "Vergleichen Sie Vorher/Nachher und laden Sie die bereinigte Datei herunter." }
    ]
  },
  "plans": {
    "kicker": "Tarife",
    "h2": "Kostenlos während der Early-Access-Phase",
    "p": "Alle Funktionen sind derzeit uneingeschränkt kostenlos nutzbar.",
    "free": {
      "name": "Kostenlos",
      "note": "Keine Kreditkarte nötig",
      "items": ["Bilder und Videos", "Bis zu 50 MB pro Datei", "Originalqualität", "Ohne Benutzerkonto"],
      "cta": "Datei verarbeiten"
    },
    "pro": {
      "badge": "Demnächst",
      "price": "Credits",
      "note": "Monatlich oder jährlich",
      "items": ["Größere Dateien & lange Videos", "Stapelverarbeitung", "Priorisierte Warteschlange", "API-Zugriff"]
    }
  },
  "hood": {
    "kicker": "Technologie & Datenschutz",
    "h2": "Auf Qualität und Privatsphäre ausgelegt",
    "cards": [
      { "title": "Jedes Einzelbild verarbeitet", "text": "Videos werden lückenlos über alle Frames bereinigt.", "tag": "Frame 1 → 240 · fertig" },
      { "title": "Null Speicherung", "text": "Dateien verbleiben nur während der Verarbeitung kurz im Speicher.", "tag": "0 Dateien gespeichert" },
      { "title": "Verlustfreie Qualität", "text": "Auflösung und Framerate bleiben exakt wie beim Original.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Zielgruppen",
    "h2": "Für Kreative, die mit eigener KI arbeiten",
    "cards": [
      { "title": "Content Creators", "text": "Sie haben die Datei generiert und möchten eine saubere Version behalten." },
      { "title": "Forscher & Journalisten", "text": "Sie testen die Robustheit von Wasserzeichen auf verschiedenen Medien." },
      { "title": "Entwickler", "text": "Sie integrieren automatisierte Bereinigungspipelines per API." }
    ],
    "note": "Verarbeiten Sie nur Inhalte, an denen Sie die Rechte besitzen."
  },
  "seo": [
    {
      "h2": "Anleitung: SynthID online entfernen",
      "html": "Legen Sie Ihre Datei im Upload-Bereich ab und klicken Sie auf <strong>Datei verarbeiten</strong>. Details in unserer Anleitung: <a href=\"/de/synthid-entfernen-anleitung/\">SynthID Wasserzeichen entfernen</a>."
    },
    { "h2": "Welche KI-Tools nutzen SynthID?", "html": "Google nutzt SynthID in Gemini, Imagen und Veo." },
    {
      "h2": "Warum herkömmliches Bearbeiten nicht hilft",
      "html": "SynthID ist kein sichtbares Logo, sondern ein mathematisches Signal in den Farbwerten. Daher benötigt man ein spezialisiertes Werkzeug zum <a href=\"/de/synthid-entfernen/\">SynthID entfernen</a>."
    }
  ],
  "faqHeading": "Häufig gestellte Fragen",
  "faqs": [
    { "q": "Was ist ein SynthID-Entferner?", "a": "Ein Werkzeug zum Neutralisieren des unsichtbaren SynthID-Wasserzeichens von Google aus KI-Inhalten." },
    { "q": "Ist RemoveSynth kostenlos?", "a": "Ja, während der Early-Access-Phase ist die Nutzung komplett kostenfrei." },
    { "q": "Welche Dateiformate werden unterstützt?", "a": "PNG, JPG, WebP sowie MP4, WebM und MOV." },
    { "q": "Werden meine Dateien gespeichert?", "a": "Nein, alle Dateien werden unmittelbar nach der Verarbeitung gelöscht." },
    { "q": "Reicht Zuschneiden oder ein Screenshot?", "a": "Nein, SynthID übersteht normale Bildbearbeitung und Zuschnitte." },
    { "q": "Gehört RemoveSynth zu Google?", "a": "Nein, RemoveSynth ist ein unabhängiges Open-Source-Projekt." }
  ],
  "cta": { "h2": "Jetzt SynthID entfernen", "p": "Kostenlos, ohne Registrierung für Bilder und Videos.", "button": "Jetzt starten" }
})

# 3. ES
save("es", "es", {
  "lang": "es",
  "title": "Eliminar SynthID Online Gratis: Imágenes y Vídeos con IA",
  "description": "Herramienta online gratuita para eliminar la marca de agua invisible SynthID y metadatos C2PA en imágenes y vídeos de IA sin pérdida de calidad.",
  "hero": {
    "eyebrow": "Sin registro · Gratis · Imágenes, vídeo y audio",
    "h1Before": "Gratis ",
    "h1Accent": "eliminar SynthID",
    "h1After": " online",
    "lead": "Elimina la marca de agua SynthID de imágenes y vídeos generados por IA. Sube tu archivo, procésalo en un clic y descárgalo en calidad original.",
    "checks": ["Imágenes, vídeo y audio", "Cada fotograma", "Archivos borrados tras procesar"],
    "worksWith": "Funciona con archivos de"
  },
  "features": [
    { "title": "Imágenes y vídeos", "text": "Una sola herramienta para imágenes PNG, JPG y WebP y vídeos MP4, WebM y MOV." },
    { "title": "Cada fotograma", "text": "En los vídeos se procesa el clip entero, no solo unos cuantos fotogramas." },
    { "title": "Calidad original", "text": "Tu archivo conserva su resolución, formato y frecuencia de fotogramas." },
    { "title": "Sin registro", "text": "Suelta un archivo y listo. No necesitas cuenta durante el acceso anticipado." },
    { "title": "Archivos borrados", "text": "Lo que subes se borra en cuanto te devolvemos el resultado." },
    { "title": "Funciona en todas partes", "text": "En cualquier navegador moderno, en ordenador, tableta o móvil." }
  ],
  "inside": {
    "kicker": "Qué hay dentro de un archivo de IA",
    "h2": "Dos formas de marcar el contenido de IA",
    "p": "La mayoría de las herramientas de IA marcan lo que generan. Ninguna de las dos marcas se ve.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Una señal invisible en los píxeles",
        "html": "SynthID va integrado en los datos de la imagen y en cada fotograma de un vídeo. No se ve, y está pensado para resistir recortes, filtros, compresión y capturas de pantalla. <a href=\"/es/que-es-synthid/\">¿Qué es SynthID?</a>"
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Un registro firmado en los metadatos",
        "html": "Muchos generadores también añaden C2PA Content Credentials: una nota firmada en los metadatos que indica cómo se creó el archivo."
      }
    ]
  },
  "how": {
    "kicker": "Cómo funciona",
    "h2": "Elimina SynthID en cuatro pasos",
    "steps": [
      { "title": "Suelta tu archivo", "text": "Elige una imagen o un vídeo de una herramienta que use SynthID, como Gemini, Imagen o Veo." },
      { "title": "Confirma tus derechos", "text": "Marca la casilla para confirmar que el archivo es tuyo o que puedes procesarlo." },
      { "title": "Lo procesamos", "text": "Tu archivo se revisa y se procesa en nuestro servidor, fotograma a fotograma si es un vídeo." },
      { "title": "Descarga", "text": "Compara el antes y el después y descarga el resultado en su formato original." }
    ]
  },
  "plans": {
    "kicker": "Planes",
    "h2": "Gratis durante el acceso anticipado",
    "p": "Todas las funciones son gratis durante el acceso anticipado. Los planes de pago añadirán límites más altos.",
    "free": {
      "name": "Gratis",
      "note": "sin tarjeta",
      "items": ["Imágenes y vídeos", "Hasta 50 MB por archivo", "Calidad original", "Sin cuenta"],
      "cta": "Procesar un archivo"
    },
    "pro": {
      "badge": "Próximamente",
      "price": "Créditos",
      "note": "mensual o anual",
      "items": ["Archivos más grandes y vídeos más largos", "Procesamiento por lotes", "Procesamiento prioritario", "Acceso a la API"]
    }
  },
  "hood": {
    "kicker": "Por dentro",
    "h2": "Pensado para la calidad y la privacidad",
    "cards": [
      { "title": "Cada fotograma", "text": "Los vídeos se procesan de principio a fin, sin saltarse fotogramas.", "tag": "fotograma 1 → 240 · listo" },
      { "title": "No guardamos nada", "text": "Los archivos están en una carpeta temporal solo mientras se procesan y después se borran.", "tag": "0 archivos guardados" },
      { "title": "Calidad original", "text": "La resolución, el formato y los fotogramas por segundo no cambian.", "tag": "1080×1920 · 30fps → 1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Para quién",
    "h2": "Para quien trabaja con sus propios contenidos de IA",
    "cards": [
      { "title": "Creadores", "text": "Creaste tú la imagen o el vídeo y quieres quedarte con el archivo tal como lo descargas." },
      { "title": "Investigación y periodismo", "text": "Estudias cómo resisten las marcas de agua de IA y necesitas una forma rápida de probar archivos." },
      { "title": "Desarrolladores", "text": "Creas flujos de trabajo con medios y necesitas una API para procesar por lotes. Está en camino." }
    ],
    "note": "Procesa solo archivos que sean tuyos o sobre los que tengas derechos, y sé transparente sobre cómo se creó tu contenido."
  },
  "seo": [
    {
      "h2": "Cómo usar el SynthID remover",
      "html": "Suelta tu archivo en el recuadro de arriba, marca la casilla para confirmar tus derechos y haz clic en <strong>Procesar archivo</strong>. Consulta la guía <a href=\"/es/como-eliminar-synthid/\">cómo eliminar las marcas de agua de SynthID</a>."
    },
    { "h2": "¿Qué herramientas de IA añaden SynthID?", "html": "Google añade SynthID al contenido de sus productos de IA generativa como Gemini, Imagen y Veo." },
    {
      "h2": "Por qué editar no elimina SynthID",
      "html": "SynthID está repartido por los propios píxeles. Por eso, para <a href=\"/es/eliminar-synthid/\">eliminar SynthID</a> hace falta una herramienta específica."
    }
  ],
  "faqHeading": "Preguntas frecuentes",
  "faqs": [
    { "q": "¿Qué es un SynthID remover?", "a": "Es una herramienta que procesa imágenes y vídeos generados con IA que llevan la marca SynthID de Google." },
    { "q": "¿Es gratis?", "a": "Sí, durante el acceso anticipado RemoveSynth es totalmente gratis." },
    { "q": "¿Qué archivos puedo subir?", "a": "Imágenes PNG, JPG, WebP y vídeos MP4, WebM o MOV." },
    { "q": "¿Guardáis mis archivos?", "a": "No, se borran inmediatamente tras procesarse." },
    { "q": "¿Recortar elimina SynthID?", "a": "No de forma fiable, ya que la señal está en los píxeles." },
    { "q": "¿RemoveSynth pertenece a Google?", "a": "No, es una herramienta independiente." }
  ],
  "cta": { "h2": "Prueba el SynthID remover", "p": "Gratis, sin registro, para imágenes y vídeos.", "button": "Eliminar SynthID ahora" }
})

# 4. FR
save("fr", "fr", {
  "lang": "fr",
  "title": "Supprimer SynthID en ligne gratuit : Images et vidéos IA",
  "description": "Outil gratuit de suppression de SynthID pour images et vidéos générées par IA. Supprimez les filigranes invisibles SynthID et métadonnées C2PA sans perte de qualité directement dans votre navigateur.",
  "hero": {
    "eyebrow": "Sans inscription · Gratuit · Images, vidéos et audio",
    "h1Before": "Gratuit ",
    "h1Accent": "supprimer SynthID",
    "h1After": " en ligne",
    "lead": "Supprimez le filigrane invisible SynthID de vos images et vidéos d'IA. Téléversez votre fichier, traitez-le en un clic et téléchargez-le dans sa qualité d'origine.",
    "checks": ["Images, vidéo et audio", "Chaque image vidéo", "Fichiers supprimés après traitement"],
    "worksWith": "Compatible avec les fichiers de"
  },
  "features": [
    { "title": "Images et vidéos", "text": "Un seul outil pour photos PNG, JPG, WebP et vidéos MP4, WebM, MOV." },
    { "title": "Chaque image", "text": "Sur les vidéos, l'intégralité du clip est traitée image par image." },
    { "title": "Qualité d'origine", "text": "Résolution, format et fréquence d'images restent parfaitement intacts." },
    { "title": "Sans inscription", "text": "Glissez votre fichier et téléchargez sans créer de compte." },
    { "title": "Confidentialité totale", "text": "Vos fichiers sont immédiatement supprimés dès la fin du traitement." },
    { "title": "Accessible partout", "text": "Fonctionne sur tous les navigateurs modernes sur ordinateur, tablette et mobile." }
  ],
  "inside": {
    "kicker": "Contenu des fichiers IA",
    "h2": "Deux méthodes de marquage des créations IA",
    "p": "La plupart des générateurs IA intègrent des marqueurs invisibles à l'œil nu.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Un signal invisible au cœur des pixels",
        "html": "SynthID est directement tissé dans les données de l'image et dans chaque trame vidéo. Il résiste aux recadrages et compressions."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Un certificat cryptographique dans les métadonnées",
        "html": "De nombreux outils ajoutent des métadonnées C2PA certifiées précisant l'origine IA de l'image."
      }
    ]
  },
  "how": {
    "kicker": "Comment ça marche",
    "h2": "Supprimer SynthID en quatre étapes",
    "steps": [
      { "title": "Déposez votre fichier", "text": "Sélectionnez une image ou une vidéo issue de Gemini, Imagen ou Veo." },
      { "title": "Confirmez vos droits", "text": "Cochez la case certifiant que vous êtes autorisé à traiter le contenu." },
      { "title": "Traitement instantané", "text": "Notre moteur neutralise le filigrane frame par frame." },
      { "title": "Téléchargement", "text": "Comparez le résultat et téléchargez votre fichier nettoyé." }
    ]
  },
  "plans": {
    "kicker": "Tarifs",
    "h2": "100% gratuit pendant l'accès anticipé",
    "p": "Toutes les fonctionnalités sont actuellement accessibles sans frais.",
    "free": {
      "name": "Gratuit",
      "note": "Sans carte bancaire",
      "items": ["Images et vidéos", "Jusqu'à 50 Mo par fichier", "Qualité originale", "Sans inscription"],
      "cta": "Traiter un fichier"
    },
    "pro": {
      "badge": "Bientôt",
      "price": "Crédits",
      "note": "Mensuel ou annuel",
      "items": ["Fichiers plus lourds & vidéos longues", "Traitement par lot", "File prioritaire", "Accès API"]
    }
  },
  "hood": {
    "kicker": "Technologie & Confidentialité",
    "h2": "Excellence de traitement et respect de la vie privée",
    "cards": [
      { "title": "Traitement trame par trame", "text": "Les clips vidéo sont traités dans leur intégralité sans omission.", "tag": "Frame 1 → 240 · terminé" },
      { "title": "Aucune rétention", "text": "Les fichiers temporaires sont purgés immédiatement après restitution.", "tag": "0 fichier conservé" },
      { "title": "Fidélité absolue", "text": "Les dimensions et le framerate d'origine sont strictement préservés.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Pour qui ?",
    "h2": "Conçu pour les créateurs gérant leurs propres médias IA",
    "cards": [
      { "title": "Créateurs de contenu", "text": "Vous avez généré l'image et souhaitez un fichier brut sans marquage additionnel." },
      { "title": "Chercheurs & Journalistes", "text": "Vous évaluez la robustesse des filigranes numériques face aux manipulations." },
      { "title": "Développeurs", "text": "Vous intégrez des pipelines multimédias automatisés via API." }
    ],
    "note": "Ne traitez que les fichiers dont vous possédez les droits et respectez l'honnêteté intellectuelle."
  },
  "seo": [
    {
      "h2": "Comment enlever le filigrane SynthID en ligne ?",
      "html": "Déposez votre fichier dans la zone d'import, validez vos droits puis cliquez sur <strong>Traiter le fichier</strong> pour récupérer un média sans filigrane."
    },
    { "h2": "Quels outils intègrent SynthID ?", "html": "Google applique SynthID aux contenus de Gemini, Imagen et Veo." },
    {
      "h2": "Pourquoi le recadrage ne suffit pas",
      "html": "SynthID est un motif stéganographique réparti sur tous les pixels. Seul un algorithme de neutralisation dédié permet de le supprimer."
    }
  ],
  "faqHeading": "Foire aux questions",
  "faqs": [
    { "q": "Qu'est-ce qu'un suppresseur de SynthID ?", "a": "C'est un outil spécialisé conçu pour neutraliser le filigrane stéganographique SynthID développé par Google." },
    { "q": "RemoveSynth est-il gratuit ?", "a": "Oui, le service est totalement gratuit durant la période d'accès anticipé." },
    { "q": "Quels formats sont acceptés ?", "a": "Images PNG, JPG, WebP et vidéos MP4, WebM, MOV." },
    { "q": "Conservez-vous une copie de mes créations ?", "a": "Non, aucun fichier n'est sauvegardé après la livraison du téléchargement." },
    { "q": "Une capture d'écran efface-t-elle SynthID ?", "a": "Non, le motif est conçu pour persister même lors de captures d'écran." },
    { "q": "Êtes-vous affilié à Google ?", "a": "Non, RemoveSynth est un outil tiers totalement indépendant." }
  ],
  "cta": { "h2": "Supprimer le filigrane SynthID maintenant", "p": "Gratuit, instantané, sans création de compte.", "button": "Nettoyer un fichier" }
})

# 5. PT-BR
save("pt-br", "ptBr", {
  "lang": "pt-br",
  "title": "Remover SynthID Online Grátis: Imagens e Vídeos com IA",
  "description": "Removedor de SynthID online grátis para imagens e vídeos de IA. Remova marcas d'água invisíveis SynthID e metadados C2PA sem perda de qualidade direto no navegador.",
  "hero": {
    "eyebrow": "Sem cadastro · Grátis · Imagens, vídeos e áudio",
    "h1Before": "Grátis ",
    "h1Accent": "remover SynthID",
    "h1After": " online",
    "lead": "Remova a marca d'água invisível SynthID de imagens e vídeos gerados por IA. Envie seu arquivo, processe em um clique e baixe na qualidade original.",
    "checks": ["Imagens, vídeo e áudio", "Todos os quadros de vídeo", "Arquivos excluídos após o processamento"],
    "worksWith": "Compatível com arquivos de"
  },
  "features": [
    { "title": "Imagens e vídeos", "text": "Uma única ferramenta para PNG, JPG, WebP, MP4, WebM e MOV." },
    { "title": "Todos os quadros", "text": "Em vídeos, o arquivo completo é processado quadro a quadro." },
    { "title": "Qualidade original", "text": "Resolução, taxa de quadros e formato são rigorosamente mantidos." },
    { "title": "Sem cadastro", "text": "Basta arrastar o arquivo e usar. Sem necessidade de conta." },
    { "title": "Privacidade total", "text": "Seus arquivos são deletados permanentemente assim que o download é liberado." },
    { "title": "Funciona em qualquer lugar", "text": "Compatível com qualquer navegador moderno no celular ou PC." }
  ],
  "inside": {
    "kicker": "O que há dentro de arquivos de IA",
    "h2": "Duas formas como conteúdos de IA são marcados",
    "p": "A maioria dos geradores insere marcas invisíveis nos arquivos exportados.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Um sinal imperceptível nos pixels",
        "html": "O SynthID fica integrado aos dados da imagem e a cada quadro de vídeo, resistindo a filtros e cortes."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Registro criptográfico nos metadados",
        "html": "Muitas ferramentas gravam dados de procedência C2PA informando a origem da IA."
      }
    ]
  },
  "how": {
    "kicker": "Como funciona",
    "h2": "Remova o SynthID em quatro etapas",
    "steps": [
      { "title": "Envie o arquivo", "text": "Selecione uma imagem ou vídeo gerado no Gemini, Imagen ou Veo." },
      { "title": "Confirme os direitos", "text": "Marque a caixa confirmando autorização para processar o arquivo." },
      { "title": "Processamento", "text": "O arquivo é limpo quadro a quadro de forma automatizada." },
      { "title": "Baixe o resultado", "text": "Compare o antes e depois e salve o arquivo pronto." }
    ]
  },
  "plans": {
    "kicker": "Planos",
    "h2": "Gratuito durante o acesso antecipado",
    "p": "Aproveite todos os recursos sem custo durante o lançamento.",
    "free": {
      "name": "Gratuito",
      "note": "Sem cartão de crédito",
      "items": ["Imagens e vídeos", "Até 50 MB por arquivo", "Qualidade original", "Sem cadastro"],
      "cta": "Processar arquivo"
    },
    "pro": {
      "badge": "Em breve",
      "price": "Créditos",
      "note": "Mensal ou anual",
      "items": ["Arquivos maiores & vídeos longos", "Processamento em lote", "Fila prioritária", "Acesso à API"]
    }
  },
  "hood": {
    "kicker": "Tecnologia & Privacidade",
    "h2": "Construído com foco em qualidade e sigilo",
    "cards": [
      { "title": "Quadro a quadro", "text": "Vídeos inteiros são processados sem pular quadros intermediários.", "tag": "quadro 1 → 240 · pronto" },
      { "title": "Zero retenção", "text": "Arquivos temporários são excluídos imediatamente.", "tag": "0 arquivos salvos" },
      { "title": "Qualidade intacta", "text": "Resolução e taxa de quadros permanecem inalteradas.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Público-alvo",
    "h2": "Para quem produz seus próprios conteúdos com IA",
    "cards": [
      { "title": "Criadores de conteúdo", "text": "Você criou o material e precisa do arquivo sem marcações ocultas." },
      { "title": "Pesquisadores", "text": "Testando a persistência e eficácia de marcas d'água invisíveis." },
      { "title": "Desenvolvedores", "text": "Integrando pipelines de mídia com automação via API." }
    ],
    "note": "Processe apenas conteúdos que você tem permissão legal para utilizar."
  },
  "seo": [
    {
      "h2": "Como remover a marca d'água SynthID?",
      "html": "Solte o arquivo na área indicada, confirme a permissão e clique em <strong>Processar arquivo</strong> para fazer o download limpo."
    },
    { "h2": "Quais IAs utilizam SynthID?", "html": "O Google aplica SynthID nas ferramentas Gemini, Imagen e Veo." },
    {
      "h2": "Por que recortar a imagem não resolve?",
      "html": "O SynthID está presente em toda a malha de pixels, sobrevivendo a cortes e capturas de tela."
    }
  ],
  "faqHeading": "Perguntas frequentes",
  "faqs": [
    { "q": "O que é um removedor de SynthID?", "a": "É uma ferramenta que neutraliza marcas d'água imperceptíveis SynthID em imagens e vídeos." },
    { "q": "O RemoveSynth é gratuito?", "a": "Sim, totalmente grátis durante a fase de acesso antecipado." },
    { "q": "Quais formatos são aceitos?", "a": "PNG, JPG, WebP e vídeos em MP4, WebM e MOV." },
    { "q": "Vocês armazenam meus arquivos?", "a": "Não, todos os arquivos são excluídos imediatamente após a entrega." },
    { "q": "Print de tela remove o SynthID?", "a": "Não, o sinal sobrevive a capturas de tela normais." },
    { "q": "O RemoveSynth tem ligação com o Google?", "a": "Não, somos uma ferramenta independente." }
  ],
  "cta": { "h2": "Experimente o removedor de SynthID", "p": "Grátis, rápido e sem cadastro.", "button": "Remover SynthID agora" }
})

# 6. JA
save("ja", "ja", {
  "lang": "ja",
  "title": "SynthID 削除 オンライン無料 : AI画像・動画の不可視透かし除去",
  "description": "AI画像・動画からGoogle SynthID透かしとC2PAメタデータを完全ブラウザ内処理で無劣化削除。PNG, JPG, WebP, MP4, MOV対応の無料オンラインツール。",
  "hero": {
    "eyebrow": "登録不要 · 無料 · 画像・動画・音声対応",
    "h1Before": "無料 ",
    "h1Accent": "SynthID 削除",
    "h1After": " ツール",
    "lead": "AI生成画像や動画に埋め込まれたGoogle SynthIDの不可視透かしを除去します。1クリックで処理し、元の品質と解像度のまま保存できます。",
    "checks": ["画像・動画・音声対応", "全フレーム処理", "処理後即座にデータ削除"],
    "worksWith": "対応AIツール"
  },
  "features": [
    { "title": "画像・動画に対応", "text": "PNG, JPG, WebP画像およびMP4, WebM, MOV動画を一括サポート。" },
    { "title": "全フレーム完全処理", "text": "動画は最初から最後まですべてのフレームを丁寧に処理します。" },
    { "title": "元画質を完全維持", "text": "解像度、フレームレート、色空間を劣化させずに保ちます。" },
    { "title": "アカウント登録不要", "text": "面倒な会員登録なしで、ドラッグ＆ドロップしてすぐ使えます。" },
    { "title": "プライバシー安心", "text": "処理完了後、アップロードされたファイルは即時に消去されます。" },
    { "title": "マルチデバイス対応", "text": "PC、タブレット、スマートフォンの主要ブラウザで動作します。" }
  ],
  "inside": {
    "kicker": "AIファイルの内部構造",
    "h2": "AIコンテンツに付与される2つの識別情報",
    "p": "多くのAIツールは肉眼では見えない方法で生成物を識別しています。",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "ピクセルデータに織り込まれた不可視信号",
        "html": "SynthIDは画像データや動画の全フレームに直接埋め込まれ、トリミングや圧縮に耐えるよう設計されています。"
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "メタデータ内の電子署名レコード",
        "html": "生成日時やAIモデルの情報をメタデータ領域に記録する業界標準の証明情報です。"
      }
    ]
  },
  "how": {
    "kicker": "利用手順",
    "h2": "4つのステップでSynthIDを除去",
    "steps": [
      { "title": "ファイルをアップロード", "text": "GeminiやImagen、Veoなどで生成したファイルを選択します。" },
      { "title": "利用権の確認", "text": "ファイルの処理権限を保持していることを確認してチェックします。" },
      { "title": "自動クレンジング", "text": "独自のアルゴリズムで透かし信号を中和・除去します。" },
      { "title": "ダウンロード", "text": "前後のプレビューを確認し、元の形式のままダウンロードします。" }
    ]
  },
  "plans": {
    "kicker": "料金プラン",
    "h2": "早期アクセス期間中は完全無料",
    "p": "現在すべての基本機能を無料でご自由にご利用いただけます。",
    "free": {
      "name": "無料プラン",
      "note": "クレジットカード不要",
      "items": ["画像・動画対応", "1ファイル最大50MB", "オリジナル画質維持", "アカウント登録不要"],
      "cta": "ファイルを処理する"
    },
    "pro": {
      "badge": "近日公開",
      "price": "クレジット制",
      "note": "月額または年額",
      "items": ["大容量ファイル＆長尺動画", "一括バッチ処理", "高速優先処理", "APIアクセス"]
    }
  },
  "hood": {
    "kicker": "テクノロジー & セキュリティ",
    "h2": "徹底した品質維持とプライバシー保護",
    "cards": [
      { "title": "全フレーム精密処理", "text": "動画の各フレームをスキップすることなく全域スキャン。", "tag": "Frame 1 → 240 完了" },
      { "title": "データ保持ゼロ", "text": "処理用のテンポラリ領域はダウンロード完了とともに破棄。", "tag": "保持ファイル 0件" },
      { "title": "劣化なしの出力", "text": "解像度とフレームレートをそのまま保持。", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "対象ユーザー",
    "h2": "自作のAIメディアを扱うクリエイターのために",
    "cards": [
      { "title": "コンテンツクリエイター", "text": "自身で作成した画像や動画を余計な不可視マーカーなしで保管したい方。" },
      { "title": "研究者・検証者", "text": "電子透かしの耐性検証やデジタルフォレンジック研究に。" },
      { "title": "エンジニア", "text": "自動化パイプラインへの組み込みを検討されている開発者。" }
    ],
    "note": "ご自身に権利があるファイルのみを処理し、透明性をもってご活用ください。"
  },
  "seo": [
    {
      "h2": "SynthID透かしを消す方法",
      "html": "ファイルをドロップエリアにドラッグし、<strong>ファイルを処理</strong>をクリックするだけで透かしのないデータをダウンロードできます。"
    },
    { "h2": "SynthIDを採用しているツールは？", "html": "GoogleのGemini、Imagen、Veoなどの生成AIモデルで採用されています。" },
    {
      "h2": "トリミングや再保存で消えない理由",
      "html": "SynthIDはピクセル全体に統計的パターンとして埋め込まれているため、通常の編集ソフトでは削除できません。"
    }
  ],
  "faqHeading": "よくある質問",
  "faqs": [
    { "q": "SynthIDリムーバーとは何ですか？", "a": "GoogleのSynthIDによって埋め込まれた不可視ウォーターマークを安全に除去するツールです。" },
    { "q": "無料で利用できますか？", "a": "はい、早期アクセス期間中はどなたでも完全無料でご利用いただけます。" },
    { "q": "対応しているファイル形式は？", "a": "画像はPNG, JPG, WebP、動画はMP4, WebM, MOVに対応しています。" },
    { "q": "ファイルはサーバーに保存されますか？", "a": "いいえ、処理直後にすべて自動消去され、AIの学習等に使用されることもありません。" },
    { "q": "スクリーンショットを撮れば透かしは消えますか？", "a": "いいえ、SynthIDはスクリーンショットやリサイズにも耐える設計になっています。" },
    { "q": "Googleと提携していますか？", "a": "いいえ、RemoveSynthは独自に開発された独立したツールです。" }
  ],
  "cta": { "h2": "SynthIDを今すぐ削除する", "p": "登録不要・無料・ブラウザですぐに実行できます。", "button": "今すぐ透かしを除去" }
})

# 7. TR
save("tr", "tr", {
  "lang": "tr",
  "title": "SynthID Kaldırıcı Çevrimiçi Ücretsiz: Yapay Zeka Resim ve Video",
  "description": "Yapay zeka resim ve videolarından SynthID görünmez filigranını ve C2PA meta verilerini kayıpsız temizleyin. Tarayıcıda çalışan ücretsiz SynthID kaldırıcı.",
  "hero": {
    "eyebrow": "Kayıt yok · Ücretsiz · Resim, video ve ses",
    "h1Before": "Ücretsiz ",
    "h1Accent": "SynthID kaldırıcı",
    "h1After": " çevrimiçi",
    "lead": "Yapay zeka ile üretilmiş resim ve videolardaki görünmez SynthID filigranını kaldırın. Dosyanızı yükleyin, tek tıkla orijinal kalitede indirin.",
    "checks": ["Resim, video ve ses", "Tüm video kareleri", "İşlemden sonra silinen dosyalar"],
    "worksWith": "Şu araçlardan dosyalarla çalışır:"
  },
  "features": [
    { "title": "Resim ve video", "text": "PNG, JPG, WebP resimler ile MP4, WebM, MOV videolar için tek araç." },
    { "title": "Tüm kareler", "text": "Videolarda sadece birkaç örnek değil, tüm klip baştan sona işlenir." },
    { "title": "Orijinal kalite", "text": "Çözünürlük, format ve kare hızı kaliteden ödün vermeden korunur." },
    { "title": "Kayıt gerektirmez", "text": "Hesap açmaya gerek kalmadan dosyanızı bırakıp hemen başlayın." },
    { "title": "Dosyalar silinir", "text": "İşlem biter bitmez yüklenen içerikler kalıcı olarak silinir." },
    { "title": "Her yerde çalışır", "text": "Masaüstü, tablet veya mobildeki tüm modern tarayıcılarda aktiftir." }
  ],
  "inside": {
    "kicker": "Yapay Zeka Dosyalarının İçeriği",
    "h2": "Yapay zeka içeriklerinin işaretlenme yolları",
    "p": "Çoğu yapay zeka aracı ürettiği medyaya görünmeyen işaretler ekler.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Piksellerin içindeki görünmez sinyal",
        "html": "SynthID piksellere işlenir; kırpma, filtre ve sıkıştırmaya karşı dayanıklıdır."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Meta verilerdeki dijital imza",
        "html": "Üretim detaylarını belirten kriptografik meta veri kaydıdır."
      }
    ]
  },
  "how": {
    "kicker": "Nasıl Çalışır?",
    "h2": "Dört adımda SynthID filigranını temizleyin",
    "steps": [
      { "title": "Dosyayı bırakın", "text": "Gemini, Imagen veya Veo ile oluşturulmuş dosyanızı seçin." },
      { "title": "Haklarınızı onaylayın", "text": "Dosyayı işleme hakkınız olduğunu onaylayan kutuyu işaretleyin." },
      { "title": "Otomatik temizleme", "text": "Dosyanız sunucuda kare kare analiz edilerek temizlenir." },
      { "title": "İndirin", "text": "Sonucu önizleyin ve orijinal formatında güvenle indirin." }
    ]
  },
  "plans": {
    "kicker": "Planlar",
    "h2": "Erken erişim sürecinde tamamen ücretsiz",
    "p": "Tüm özellikler şu an hiçbir ücret talep edilmeden sunulmaktadır.",
    "free": {
      "name": "Ücretsiz",
      "note": "Kart gerekmez",
      "items": ["Resim ve video", "Dosya başına 50 MB'a kadar", "Orijinal kalite", "Kayıt gereksiz"],
      "cta": "Dosya işle"
    },
    "pro": {
      "badge": "Yakında",
      "price": "Kredi",
      "note": "Aylık veya yıllık",
      "items": ["Daha büyük dosyalar ve uzun videolar", "Toplu işleme", "Öncelikli sıra", "API erişimi"]
    }
  },
  "hood": {
    "kicker": "Teknoloji ve Gizlilik",
    "h2": "Kalite ve veri gizliliği odaklı mimari",
    "cards": [
      { "title": "Her kare işlenir", "text": "Video boyunca hiçbir kare atlanmadan tüm akış temizlenir.", "tag": "Kare 1 → 240 · Tamamlandı" },
      { "title": "Veri saklanmaz", "text": "Geçici dosyalar indirme sonrasında anında imha edilir.", "tag": "0 dosya depolandı" },
      { "title": "Kayıpsız çıktı", "text": "Çözünürlük ve kare hızı birebir korunur.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Kimin İçin?",
    "h2": "Kendi yapay zeka içeriklerini üreten herkes için",
    "cards": [
      { "title": "İçerik üreticileri", "text": "Kendi ürettiğiniz görseli filigransız temiz haliyle kullanmak istediğinizde." },
      { "title": "Araştırmacılar", "text": "Görünmez filigran dirençlerini test eden akademisyen ve uzmanlar için." },
      { "title": "Geliştiriciler", "text": "Medya işleme süreçlerini API ile otomatikleştirmek isteyenler." }
    ],
    "note": "Yalnızca haklarına sahip olduğunuz içerikleri işleyin."
  },
  "seo": [
    {
      "h2": "SynthID filigranı nasıl kaldırılır?",
      "html": "Dosyayı yukarıdaki alana yükleyin ve <strong>Dosyayı İşle</strong> butonuna tıklayarak filigransız versiyonu indirin."
    },
    { "h2": "Hangi yapay zeka araçları SynthID kullanır?", "html": "Google'ın Gemini, Imagen ve Veo gibi modelleri SynthID içerir." },
    {
      "h2": "Kırpmak neden filigranı silmez?",
      "html": "SynthID resmin genel piksel dokusuna gömüldüğünden standart düzenlemelerle silinemez."
    }
  ],
  "faqHeading": "Sıkça Sorulan Sorular",
  "faqs": [
    { "q": "SynthID kaldırıcı nedir?", "a": "Google'ın yapay zeka içeriklerine eklediği gizli SynthID filigranını temizleyen özel bir araçtır." },
    { "q": "Kullanımı ücretsiz mi?", "a": "Evet, erken erişim süresince tamamen ücretsizdir." },
    { "q": "Hangi dosya türleri destekleniyor?", "a": "PNG, JPG, WebP resimler ve MP4, WebM, MOV videolar." },
    { "q": "Dosyalarım saklanıyor mu?", "a": "Hayır, işlem bittikten sonra derhal silinir." },
    { "q": "Ekran görüntüsü almak filigranı yok eder mi?", "a": "Hayır, SynthID ekran görüntülerinde de varlığını korur." },
    { "q": "RemoveSynth Google'a mı ait?", "a": "Hayır, RemoveSynth bağımsız bir açık araçtır." }
  ],
  "cta": { "h2": "SynthID filigranını hemen kaldırın", "p": "Ücretsiz, kayıtsız ve yüksek hızlı.", "button": "Şimdi Temizle" }
})

# 8. TL
save("tl", "tl", {
  "lang": "tl",
  "title": "Tanggalin ang SynthID Online Libre: AI Mga Larawan at Video",
  "description": "Libreng online SynthID remover para sa mga imahe at video ng AI. Alisin ang invisible SynthID watermark at C2PA metadata nang walang pagkawala ng kalidad sa browser.",
  "hero": {
    "eyebrow": "Walang sign-up · Libre · Larawan, video at audio",
    "h1Before": "Libreng ",
    "h1Accent": "SynthID remover",
    "h1After": " online",
    "lead": "Alisin ang invisible SynthID watermark mula sa mga larawan at video na gawa ng AI. I-upload ang file, iproseso sa isang click, at i-download sa orihinal na kalidad.",
    "checks": ["Larawan, video at audio", "Bawat frame ng video", "Binubura agad pagkatapos iproseso"],
    "worksWith": "Gumagana sa mga file mula sa"
  },
  "features": [
    { "title": "Mga larawan at video", "text": "Isang tool para sa PNG, JPG, WebP at MP4, WebM, MOV." },
    { "title": "Bawat frame", "text": "Sa video, buong clip ang pinoproseso nang walang nilalaktawan." },
    { "title": "Orihinal na kalidad", "text": "Nananatili ang resolution, format, at frame rate ng iyong file." },
    { "title": "Walang sign-up", "text": "I-drop lang ang file at magsimula nang hindi kailangan ng account." },
    { "title": "Ligtas at pribado", "text": "Agad na binubura ang mga file matapos maihatid ang download." },
    { "title": "Kahit saan pwede", "text": "Tumatakbo sa browser sa desktop, tablet, o mobile phone." }
  ],
  "inside": {
    "kicker": "Ano ang nasa loob ng AI file",
    "h2": "Dalawang paraan kung paano minamarkahan ang AI",
    "p": "Karamihan sa mga AI tool ay naglalagay ng mga markang hindi nakikita ng mata.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Invisible signal sa mga pixel",
        "html": "Nakahabi ang SynthID sa mismong pixel data at sa bawat frame ng video, kaya hindi ito basta natatanggal ng crop o filter."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Naka-sign na tala sa metadata",
        "html": "Cryptographic record na nakalagay sa metadata na nagsasabing gawa ito ng AI."
      }
    ]
  },
  "how": {
    "kicker": "Paano gamitin",
    "h2": "Tanggalin ang SynthID sa apat na hakbang",
    "steps": [
      { "title": "I-drop ang file", "text": "Pumili ng larawan o video mula sa Gemini, Imagen, o Veo." },
      { "title": "Kumpirmahin ang karapatan", "text": "Lagyan ng tsek upang kumpirmahing pagmamay-ari mo ang file." },
      { "title": "Ipoproseso namin", "text": "Sinusuri at nililinis ang file frame by frame sa server." },
      { "title": "I-download", "text": "Ihambing ang bago at pagkatapos, at i-save ang malinis na file." }
    ]
  },
  "plans": {
    "kicker": "Mga Plano",
    "h2": "Libre sa panahon ng early access",
    "p": "Lahat ng features ay libre habang nasa early access period.",
    "free": {
      "name": "Libre",
      "note": "Walang credit card",
      "items": ["Larawan at video", "Hanggang 50 MB bawat file", "Orihinal na kalidad", "Walang account"],
      "cta": "Magproseso ng file"
    },
    "pro": {
      "badge": "Malapit na",
      "price": "Credits",
      "note": "Buwanan o taunan",
      "items": ["Mas malalaking file & mahabang video", "Batch processing", "Priority queue", "API access"]
    }
  },
  "hood": {
    "kicker": "Teknolohiya at Privacy",
    "h2": "Gawa para sa mataas na kalidad at privacy",
    "cards": [
      { "title": "Bawat frame pinoproseso", "text": "Walang nalalaktawang frame sa buong haba ng video.", "tag": "Frame 1 → 240 tapos na" },
      { "title": "Walang itinatago", "text": "Agad na binubura ang temporary folder pagkatapos ng download.", "tag": "0 file na nakatago" },
      { "title": "Orihinal na linaw", "text": "Eksaktong pareho ang resolution at frame rate sa orihinal.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Para kanino ito",
    "h2": "Para sa mga taong gumagawa ng sarili nilang AI media",
    "cards": [
      { "title": "Mga Creator", "text": "Ikaw ang gumawa ng larawan o video at gusto mo ng malinis na kopya." },
      { "title": "Mga Mananaliksik", "text": "Sumusubok sa tibay ng invisible watermarks para sa pagsusuri." },
      { "title": "Mga Developer", "text": "Nais i-automate ang media pipeline gamit ang API." }
    ],
    "note": "Gamitin lamang sa mga file na pagmamay-ari mo o may pahintulot kang iproseso."
  },
  "seo": [
    {
      "h2": "Paano tanggalin ang SynthID watermark?",
      "html": "I-upload ang file sa itaas, kumpirmahin ang pahintulot, at i-click ang <strong>Iproseso ang file</strong> upang makuha ang malinis na bersyon."
    },
    { "h2": "Anong mga AI tool ang naglalagay ng SynthID?", "html": "Kasama rito ang Gemini, Imagen, at Veo ng Google." },
    {
      "h2": "Bakit hindi natatanggal ng crop ang SynthID?",
      "html": "Nakakalat ang SynthID sa mga pixel ng buong imahe, kaya nananatili ito kahit i-crop o i-screenshot."
    }
  ],
  "faqHeading": "Mga Madalas Itanong",
  "faqs": [
    { "q": "Ano ang SynthID remover?", "a": "Isang tool na nag-aalis ng invisible SynthID watermark mula sa Google AI media." },
    { "q": "Libre ba ito?", "a": "Oo, 100% libre sa panahon ng early access." },
    { "q": "Anong file types ang pwede?", "a": "PNG, JPG, WebP na larawan at MP4, WebM, MOV na video." },
    { "q": "Itinatabi ba ninyo ang mga file?", "a": "Hindi. Agad na binubura ang file pagkatapos ma-download." },
    { "q": "Natatanggal ba ng screenshot ang SynthID?", "a": "Hindi, dinisenyo ang SynthID para manatili kahit i-screenshot." },
    { "q": "Konektado ba ang RemoveSynth sa Google?", "a": "Hindi, ito ay isang independent tool." }
  ],
  "cta": { "h2": "Subukan ang SynthID remover", "p": "Libre, walang sign-up, para sa larawan at video.", "button": "Tanggalin ang SynthID ngayon" }
})

print("Batch 1 (Tier 1: en, de, es, fr, pt-br, ja, tr, tl) completed.")
