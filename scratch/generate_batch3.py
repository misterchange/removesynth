# -*- coding: utf-8 -*-
import os, json

LOCALES_DIR = r"d:\Nitin\removesynth\apps\removesynth\src\content\locales"

def save(code, var_name, data):
    with open(os.path.join(LOCALES_DIR, f"{code}.ts"), "w", encoding="utf-8") as f:
        f.write(f"import type {{ HomeContent }} from '../types';\n\nexport const {var_name}: HomeContent = {json.dumps(data, ensure_ascii=False, indent=2)};\n")
    print(f"Saved {code}.ts")

# 15. PT (European Portuguese)
save("pt", "pt", {
  "lang": "pt",
  "title": "Remover SynthID Online Grátis: Imagens e Vídeos de IA",
  "description": "Ferramenta online gratuita para remover a marca d'água invisível SynthID e metadados C2PA de imagens e vídeos de IA diretamente no navegador sem perda de resolução.",
  "hero": {
    "eyebrow": "Sem registo · Gratuito · Imagens, vídeos e áudio",
    "h1Before": "Gratuito ",
    "h1Accent": "remover SynthID",
    "h1After": " online",
    "lead": "Elimine a marca d'água invisível SynthID de imagens e vídeos gerados por IA. Envie o ficheiro, processe com um clique e descarregue na qualidade original.",
    "checks": ["Imagens, vídeo e áudio", "Todos os fotogramas de vídeo", "Ficheiros eliminados após processamento"],
    "worksWith": "Compatível com ficheiros de"
  },
  "features": [
    { "title": "Imagens e vídeos", "text": "Uma única ferramenta para PNG, JPG, WebP, MP4, WebM e MOV." },
    { "title": "Todos os fotogramas", "text": "Nos vídeos, o ficheiro completo é processado fotograma a fotograma." },
    { "title": "Qualidade original", "text": "Resolução, taxa de fotogramas e formato são mantidos intactos." },
    { "title": "Sem registo", "text": "Basta arrastar o ficheiro e começar. Sem necessidade de conta." },
    { "title": "Privacidade absoluta", "text": "Os seus ficheiros são apagados logo que o download fica disponível." },
    { "title": "Universal", "text": "Compatível com qualquer navegador moderno no computador ou telemóvel." }
  ],
  "inside": {
    "kicker": "O que existe num ficheiro de IA",
    "h2": "Duas formas de etiquetagem de conteúdos IA",
    "p": "A maioria dos geradores insere marcas invisíveis nos ficheiros produzidos.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Um sinal impercetível nos píxeis",
        "html": "O SynthID está integrado nos dados dos píxeis e em cada fotograma, sobrevivendo a cortes e filtros."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Registo criptográfico nos metadados",
        "html": "Registo assinado indicando a proveniência do modelo de inteligência artificial."
      }
    ]
  },
  "how": {
    "kicker": "Como funciona",
    "h2": "Remova o SynthID em quatro passos simples",
    "steps": [
      { "title": "Envie o ficheiro", "text": "Selecione uma imagem ou vídeo do Gemini, Imagen ou Veo." },
      { "title": "Confirme os direitos", "text": "Assinale a caixa confirmando que pode processar o ficheiro." },
      { "title": "Processamento", "text": "O ficheiro é limpo fotograma a fotograma nos nossos servidores." },
      { "title": "Descarregue", "text": "Compare o antes e o depois e guarde a versão sem marcas." }
    ]
  },
  "plans": {
    "kicker": "Planos",
    "h2": "Gratuito durante o acesso antecipado",
    "p": "Todas as funcionalidades estão gratuitas durante a fase de lançamento.",
    "free": {
      "name": "Gratuito",
      "note": "Sem cartão",
      "items": ["Imagens e vídeos", "Até 50 MB por ficheiro", "Qualidade original", "Sem conta"],
      "cta": "Processar ficheiro"
    },
    "pro": {
      "badge": "Em breve",
      "price": "Créditos",
      "note": "Mensal ou anual",
      "items": ["Ficheiros maiores e vídeos longos", "Processamento em lote", "Fila prioritária", "Acesso à API"]
    }
  },
  "hood": {
    "kicker": "Engenharia e Privacidade",
    "h2": "Concebido para a máxima fidelidade e sigilo",
    "cards": [
      { "title": "Fotograma a fotograma", "text": "O vídeo inteiro é processado sem omissão de fotogramas.", "tag": "Fotograma 1 → 240 · concluído" },
      { "title": "Zero retenção", "text": "Os ficheiros temporários são destruídos de imediato.", "tag": "0 ficheiros guardados" },
      { "title": "Qualidade intacta", "text": "A resolução e os fps mantêm-se exatamente iguais.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Destinatários",
    "h2": "Para quem cria e trabalha com os seus próprios conteúdos de IA",
    "cards": [
      { "title": "Criadores", "text": "Produziu a imagem ou vídeo e quer o ficheiro sem identificadores ocultos." },
      { "title": "Investigação", "text": "Testes de robustez de marcas d'água digitais e esteganografia." },
      { "title": "Programadores", "text": "Automatização de pipelines de multimédia através de API." }
    ],
    "note": "Processe apenas ficheiros dos quais possui direitos legais."
  },
  "seo": [
    {
      "h2": "Como eliminar a marca d'água SynthID?",
      "html": "Arraste o ficheiro para a área acima, aceite os termos e clique em <strong>Processar ficheiro</strong> para descarregar a versão limpa."
    },
    { "h2": "Que ferramentas usam SynthID?", "html": "A Google utiliza SynthID no Gemini, Imagen e Veo." },
    {
      "h2": "Porque é que recortar não remove o SynthID?",
      "html": "O SynthID está presente em toda a matriz de píxeis, pelo que recortes ou capturas de ecrã não o eliminam."
    }
  ],
  "faqHeading": "Perguntas Frequentes",
  "faqs": [
    { "q": "O que é um removedor de SynthID?", "a": "É uma ferramenta para neutralizar a marca invisível SynthID da Google em ficheiros de IA." },
    { "q": "É gratuito?", "a": "Sim, totalmente gratuito no período de acesso inicial." },
    { "q": "Que ficheiros são suportados?", "a": "Imagens PNG, JPG, WebP e vídeos MP4, WebM, MOV." },
    { "q": "Guardam os meus dados?", "a": "Não, todos os ficheiros são destruídos logo após o download." },
    { "q": "Um screenshot retira o SynthID?", "a": "Não, a marca foi desenhada para resistir a capturas de ecrã." },
    { "q": "A RemoveSynth pertence à Google?", "a": "Não, é uma aplicação independente." }
  ],
  "cta": { "h2": "Experimente o removedor de SynthID", "p": "Gratuito, rápido e sem registo.", "button": "Remover SynthID agora" }
})

# 16. IT (Italian)
save("it", "it", {
  "lang": "it",
  "title": "Rimuovi SynthID Online Gratis: Immagini e Video IA",
  "description": "Strumento gratuito online per rimuovere il watermark invisibile SynthID e i metadati C2PA da immagini e video generati con IA direttamente nel browser senza perdita di qualità.",
  "hero": {
    "eyebrow": "Nessuna registrazione · Gratis · Immagini, video e audio",
    "h1Before": "Gratis ",
    "h1Accent": "rimuovi SynthID",
    "h1After": " online",
    "lead": "Rimuovi la filigrana invisibile SynthID da immagini e video generati con IA. Carica il file, elaboralo con un clic e scaricalo nella risoluzione originale.",
    "checks": ["Immagini, video e audio", "Ogni singolo fotogramma", "File cancellati subito dopo l'elaborazione"],
    "worksWith": "Compatibile con i file generati da"
  },
  "features": [
    { "title": "Immagini e video", "text": "Un unico strumento per immagini PNG, JPG, WebP e video MP4, WebM, MOV." },
    { "title": "Ogni fotogramma", "text": "Nei video l'intero clip viene ripulito frame dopo frame." },
    { "title": "Qualità invariata", "text": "Risoluzione, formato e framerate rimangono identici all'originale." },
    { "title": "Senza account", "text": "Trascina il file e inizia subito senza dover creare un profilo." },
    { "title": "Massima privacy", "text": "I file caricati vengono cancellati subito dopo la disponibilità del download." },
    { "title": "Sempre accessibile", "text": "Funziona su qualsiasi browser moderno su computer, tablet o smartphone." }
  ],
  "inside": {
    "kicker": "Cosa c'è in un file AI",
    "h2": "Due modalità di marcatura dei contenuti IA",
    "p": "La maggior parte dei generatori IA inserisce marcatori invisibili all'occhio umano.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Un segnale impercettibile nei pixel",
        "html": "SynthID è intessuto nei dati dei pixel e in ogni frame video, resistendo a ritagli e compressioni."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Firma crittografica nei metadati",
        "html": "Una nota crittografata inserita nei metadati che attesta la creazione mediante intelligenza artificiale."
      }
    ]
  },
  "how": {
    "kicker": "Come procedere",
    "h2": "Elimina SynthID in quattro semplici passaggi",
    "steps": [
      { "title": "Trascina il file", "text": "Seleziona un'immagine o un video creato con Gemini, Imagen o Veo." },
      { "title": "Conferma i diritti", "text": "Spunta la casella per confermare che sei autorizzato a elaborare il file." },
      { "title": "Elaborazione automatica", "text": "Il nostro algoritmo neutralizza il watermark frame per frame." },
      { "title": "Download immediato", "text": "Confronta il risultato e scarica il file pulito nel formato originale." }
    ]
  },
  "plans": {
    "kicker": "Tariffe",
    "h2": "Completamente gratuito durante l'accesso anticipato",
    "p": "Tutte le funzioni sono attualmente fruibili a costo zero.",
    "free": {
      "name": "Gratuito",
      "note": "Nessuna carta richiesta",
      "items": ["Immagini e video", "Fino a 50 MB per file", "Qualità originale", "Nessun account richiesto"],
      "cta": "Elabora file"
    },
    "pro": {
      "badge": "In arrivo",
      "price": "Crediti",
      "note": "Mensile o annuale",
      "items": ["File più grandi e video lunghi", "Elaborazione in batch", "Coda prioritaria", "Accesso alle API"]
    }
  },
  "hood": {
    "kicker": "Tecnologia & Riservatezza",
    "h2": "Progettato per la massima fedeltà e tutela della privacy",
    "cards": [
      { "title": "Frame per frame", "text": "Tutti i fotogrammi del video vengono esaminati e ripuliti.", "tag": "Frame 1 → 240 · completato" },
      { "title": "Nessun dato conservato", "text": "Le cartelle temporanee vengono distrutte subito dopo l'uso.", "tag": "0 file salvati" },
      { "title": "Zero perdite", "text": "Risoluzione e framerate rimangono invariati.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "A chi è rivolto",
    "h2": "Creato per chi gestisce i propri contenuti multimediali IA",
    "cards": [
      { "title": "Creator", "text": "Hai generato l'immagine o il video e vuoi una versione pulita del tuo file." },
      { "title": "Ricercatori", "text": "Test della robustezza delle filigrane e analisi di steganografia digitale." },
      { "title": "Sviluppatori", "text": "Integrazione di pipeline di pulizia multimediale tramite API." }
    ],
    "note": "Elabora unicamente file di cui possiedi i diritti d'autore o l'autorizzazione."
  },
  "seo": [
    {
      "h2": "Come rimuovere la filigrana SynthID online?",
      "html": "Trascina il file nell'area di upload, conferma i diritti e clicca su <strong>Elabora file</strong> per scaricare la copia senza watermark."
    },
    { "h2": "Quali strumenti AI inseriscono SynthID?", "html": "Google include SynthID in Gemini, Imagen e Veo." },
    {
      "h2": "Perché ritagliare non elimina SynthID?",
      "html": "SynthID è distribuito su tutti i pixel del file, quindi ritagli o screenshot non riescono a eliminarlo."
    }
  ],
  "faqHeading": "Domande Frequenti",
  "faqs": [
    { "q": "Cos'è un programma di rimozione SynthID?", "a": "Uno strumento capace di neutralizzare la filigrana invisibile SynthID di Google nei contenuti generati con IA." },
    { "q": "Il servizio è gratuito?", "a": "Sì, attualmente è gratuito al 100% per tutti gli utenti." },
    { "q": "Quali formati sono supportati?", "a": "PNG, JPG, WebP e video MP4, WebM, MOV." },
    { "q": "I miei file vengono archiviati?", "a": "No, tutti i file vengono eliminati definitivamente dopo il download." },
    { "q": "Uno screenshot elimina SynthID?", "a": "No, SynthID è studiato per resistere a screenshot e conversioni." },
    { "q": "RemoveSynth è legato a Google?", "a": "No, RemoveSynth è un'applicazione indipendente." }
  ],
  "cta": { "h2": "Prova il nostro strumento di rimozione SynthID", "p": "Gratuito, veloce e senza iscrizione.", "button": "Rimuovi SynthID adesso" }
})

# 17. NL (Dutch)
save("nl", "nl", {
  "lang": "nl",
  "title": "SynthID Verwijderen Online Gratis: AI Afbeeldingen en Video",
  "description": "Gratis online tool om het onzichtbare SynthID-watermerk en C2PA-metadata van AI-gegenereerde afbeeldingen en video's te verwijderen in uw browser met behoud van kwaliteit.",
  "hero": {
    "eyebrow": "Geen registratie · Gratis · Afbeeldingen, video & audio",
    "h1Before": "Gratis ",
    "h1Accent": "SynthID verwijderen",
    "h1After": " online",
    "lead": "Verwijder het onzichtbare SynthID-watermerk van door AI gegenereerde afbeeldingen en video's. Upload uw bestand, verwerk het in één klik en download in originele kwaliteit.",
    "checks": ["Afbeeldingen, video & audio", "Elk videoframe verwerkt", "Bestanden direct verwijderd na verwerking"],
    "worksWith": "Werkt met bestanden van"
  },
  "features": [
    { "title": "Afbeeldingen en video's", "text": "Eén tool voor PNG, JPG, WebP afbeeldingen en MP4, WebM, MOV video's." },
    { "title": "Elk afzonderlijk frame", "text": "Bij video's wordt de gehele clip frame voor frame verwerkt." },
    { "title": "Originele beeldkwaliteit", "text": "Resolutie, formaat en framerate blijven exact behouden." },
    { "title": "Geen registratie vereist", "text": "Sleep een bestand en ga direct aan de slag zonder account." },
    { "title": "Volledige privacy", "text": "Uploads worden direct permanent gewist zodra uw download klaar is." },
    { "title": "Overal beschikbaar", "text": "Werkt vlekkeloos in elke moderne webbrowser op pc, tablet of telefoon." }
  ],
  "inside": {
    "kicker": "Wat zit er in een AI-bestand",
    "h2": "Twee manieren waarop AI-content wordt gemarkeerd",
    "p": "De meeste AI-generatoren voegen onzichtbare markeringen toe aan de bestanden die ze maken.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Een onzichtbaar signaal in de pixels",
        "html": "SynthID is verweven in de pixeldata en elk videoframe en overleeft bijsnijden, filters en compressie."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Digitale handtekening in de metadata",
        "html": "Cryptografische metadata die registreert hoe en waarmee de AI-afbeelding is gegenereerd."
      }
    ]
  },
  "how": {
    "kicker": "Hoe het werkt",
    "h2": "Verwijder SynthID in vier eenvoudige stappen",
    "steps": [
      { "title": "Sleep uw bestand", "text": "Kies een afbeelding of video gemaakt met Gemini, Imagen of Veo." },
      { "title": "Bevestig uw rechten", "text": "Vink het vakje aan om te bevestigen dat u het bestand mag verwerken." },
      { "title": "Automatische verwerking", "text": "Het watermerk wordt frame voor frame geneutraliseerd." },
      { "title": "Downloaden", "text": "Bekijk het voor en na resultaat en download het schone bestand." }
    ]
  },
  "plans": {
    "kicker": "Tarieven",
    "h2": "Volledig gratis tijdens vroege toegang",
    "p": "Alle functies zijn momenteel zonder kosten beschikbaar.",
    "free": {
      "name": "Gratis",
      "note": "Geen creditcard nodig",
      "items": ["Afbeeldingen en video's", "Tot 50 MB per bestand", "Originele kwaliteit", "Geen account vereist"],
      "cta": "Bestand verwerken"
    },
    "pro": {
      "badge": "Binnenkort",
      "price": "Credits",
      "note": "Maandelijks of jaarlijks",
      "items": ["Grotere bestanden & lange video's", "Batchverwerking", "Voorrangswachtrij", "API-toegang"]
    }
  },
  "hood": {
    "kicker": "Technologie en Privacy",
    "h2": "Gebouwd voor compromisloze kwaliteit en privacy",
    "cards": [
      { "title": "Frame voor frame", "text": "Video's worden integraal zonder overgeslagen frames verwerkt.", "tag": "Frame 1 → 240 · voltooid" },
      { "title": "Geen data-opslag", "text": "Tijdelijke bestanden worden onmiddellijk vernietigd.", "tag": "0 bestanden opgeslagen" },
      { "title": "Kwaliteitsbehoud", "text": "Resolutie en framerate blijven ongewijzigd.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Voor wie",
    "h2": "Gemaakt voor makers die werken met eigen AI-content",
    "cards": [
      { "title": "Content Creators", "text": "U heeft de media zelf gecreëerd en wilt het zuivere origineel bewaren." },
      { "title": "Onderzoekers", "text": "Onderzoek naar de robuustheid en detectie van digitale watermerken." },
      { "title": "Ontwikkelaars", "text": "Integratie van mediaverwerking in geautomatiseerde workflows via API." }
    ],
    "note": "Verwerk uitsluitend bestanden waarover u de wettelijke rechten bezit."
  },
  "seo": [
    {
      "h2": "Hoe verwijdert u het SynthID-watermerk online?",
      "html": "Sleep uw bestand naar het uploadvak hierboven, bevestig uw rechten en klik op <strong>Bestand verwerken</strong> om uw schone bestand te downloaden."
    },
    { "h2": "Welke tools voegen SynthID toe?", "html": "Google voegt SynthID toe aan producten zoals Gemini, Imagen en Veo." },
    {
      "h2": "Waarom bijsnijden SynthID niet verwijdert",
      "html": "SynthID bevindt zich in de pixelpatronen over de gehele afbeelding; bijsnijden of screenshots verwijderen het watermerk niet."
    }
  ],
  "faqHeading": "Veelgestelde vragen",
  "faqs": [
    { "q": "Wat is een SynthID-remover?", "a": "Een programma dat het onzichtbare SynthID-watermerk van Google verwijdert uit AI-media." },
    { "q": "Is RemoveSynth gratis?", "a": "Ja, tijdens de vroege toegangsperiode is het gebruik 100% kosteloos." },
    { "q": "Welke bestandsindelingen kan ik uploaden?", "a": "PNG, JPG, WebP en video's in MP4, WebM en MOV." },
    { "q": "Worden mijn bestanden opgeslagen?", "a": "Nee, alle geüploade bestanden worden direct na afhandeling verwijderd." },
    { "q": "Verwijdert een screenshot SynthID?", "a": "Nee, SynthID is ontworpen om screenshots en lichte bewerkingen te overleven." },
    { "q": "Is RemoveSynth gelieerd aan Google?", "a": "Nee, RemoveSynth is een onafhankelijke applicatie van derden." }
  ],
  "cta": { "h2": "Probeer de SynthID-verwijderaar nu", "p": "Gratis, direct klaar en zonder account.", "button": "SynthID nu verwijderen" }
})

# 18. PL (Polish)
save("pl", "pl", {
  "lang": "pl",
  "title": "Usuń SynthID Online Za Darmo: Obrazy i Wideo AI",
  "description": "Darmowe narzędzie online do usuwania niewidzialnego znaku wodnego SynthID i metadanych C2PA z obrazów i filmów AI bezpośrednio w przeglądarce bez utraty jakości.",
  "hero": {
    "eyebrow": "Bez rejestracji · Za darmo · Obrazy, wideo i audio",
    "h1Before": "Darmowe narzędzie do ",
    "h1Accent": "usuwania SynthID",
    "h1After": " online",
    "lead": "Usuń niewidzialny znak wodny SynthID z obrazów i filmów wygenerowanych przez sztuczną inteligencję. Prześlij plik, przetwórz jednym kliknięciem i pobierz w oryginalnej jakości.",
    "checks": ["Obsługa obrazów, wideo i audio", "Przetwarzanie każdej klatki wideo", "Pliki usuwane natychmiast po pobraniu"],
    "worksWith": "Działa z plikami z"
  },
  "features": [
    { "title": "Obrazy i filmy", "text": "Jedno narzędzie dla formatów PNG, JPG, WebP oraz MP4, WebM, MOV." },
    { "title": "Każda klatka wideo", "text": "W przypadku wideo czyszczony jest cały klip klatka po klatce." },
    { "title": "Oryginalna jakość", "text": "Rozdzielczość, format i liczba klatek na sekundę pozostają nienaruszone." },
    { "title": "Bez rejestracji", "text": "Przeciągnij plik i zacznij natychmiast bez konieczności zakładania konta." },
    { "title": "Pełna prywatność", "text": "Pliki są trwale kasowane natychmiast po zakończeniu pobierania." },
    { "title": "Działa wszędzie", "text": "Dostępne na dowolnej nowoczesnej przeglądarce na komputerze i smartfonie." }
  ],
  "inside": {
    "kicker": "Co kryje plik generowany przez AI",
    "h2": "Dwa sposoby znakowania treści przez AI",
    "p": "Większość generatorów AI nanosi niewidoczne dla oka znaczniki pochodzenia.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Niewidzialny sygnał w pikselach",
        "html": "SynthID jest wpleciony bezpośrednio w strukturę pikseli i każdą klatkę wideo, zachowując odporność na kadrowanie i filtry."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Podpis cyfrowy w metadanych",
        "html": "Zaszyfrowany rekord w metadanych informujący o wygenerowaniu pliku przez model AI."
      }
    ]
  },
  "how": {
    "kicker": "Instrukcja krok po kroku",
    "h2": "Usuń SynthID w czterech prostych krokach",
    "steps": [
      { "title": "Upuść plik", "text": "Wybierz obraz lub film pochodzący z Gemini, Imagen lub Veo." },
      { "title": "Potwierdź uprawnienia", "text": "Zaznacz pole potwierdzające prawo do modyfikacji pliku." },
      { "title": "Automatyczne przetwarzanie", "text": "Algorytm wykrywa i neutralizuje niewidzialne oznaczenia." },
      { "title": "Pobierz plik", "text": "Porównaj wersję przed i po, a następnie pobierz czysty plik." }
    ]
  },
  "plans": {
    "kicker": "Plany cenowe",
    "h2": "Całkowicie za darmo we wczesnym dostępie",
    "p": "Wszystkie funkcjonalności są obecnie dostępne bez żadnych opłat.",
    "free": {
      "name": "Darmowy",
      "note": "Bez karty kredytowej",
      "items": ["Obrazy i wideo", "Do 50 MB na plik", "Oryginalna jakość", "Bez konieczności logowania"],
      "cta": "Przetwórz plik"
    },
    "pro": {
      "badge": "Wkrótce",
      "price": "Kredyty",
      "note": "Miesięcznie lub rocznie",
      "items": ["Większe pliki i długie wideo", "Przetwarzanie wsadowe", "Kolejka priorytetowa", "Dostęp do API"]
    }
  },
  "hood": {
    "kicker": "Technologia i Bezpieczeństwo",
    "h2": "Zaprojektowane z myślą o jakości i prywatności",
    "cards": [
      { "title": "Pełne przetwarzanie klatek", "text": "Pliki wideo są czyszczone w sposób ciągły bez pomijania klatek.", "tag": "Klatka 1 → 240 · gotowe" },
      { "title": "Brak retencji danych", "text": "Pliki tymczasowe są kasowane zaraz po zakończeniu sesji.", "tag": "0 zapisanych plików" },
      { "title": "Niezmienna jakość", "text": "Format i rozdzielczość nie ulegają pogorszeniu.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Dla kogo",
    "h2": "Dla twórców pracujących z własnymi mediami AI",
    "cards": [
      { "title": "Twórcy treści", "text": "Wygenerowałeś grafikę lub wideo i chcesz zachować wersję bez ukrytych sygnatur." },
      { "title": "Badacze", "text": "Testowanie odporności steganograficznych znaków wodnych." },
      { "title": "Programiści", "text": "Integracja czyszczenia mediów w automatycznych pipeline'ach przez API." }
    ],
    "note": "Przetwarzaj wyłącznie pliki, do których posiadasz prawa autorskie lub zgodę."
  },
  "seo": [
    {
      "h2": "Jak usunąć znak wodny SynthID online?",
      "html": "Przeciągnij plik w powyższe pole, potwierdź prawa i kliknij <strong>Przetwórz plik</strong>, aby pobrać wersję bez znaku wodnego."
    },
    { "h2": "Jakie narzędzia dodają SynthID?", "html": "Google dodaje SynthID do treści z modeli Gemini, Imagen oraz Veo." },
    {
      "h2": "Dlaczego przycięcie nie usuwa SynthID?",
      "html": "SynthID jest zintegrowany w całej siatce pikseli, więc kadrowanie ani zrzuty ekranu nie są w stanie go usunąć."
    }
  ],
  "faqHeading": "Często zadawane pytania",
  "faqs": [
    { "q": "Czym jest narzędzie do usuwania SynthID?", "a": "To specjalistyczny program usuwający niewidoczne znaki wodne SynthID od Google z grafik i filmów AI." },
    { "q": "Czy usługa jest bezpłatna?", "a": "Tak, we wczesnym dostępie narzędzie jest w 100% bezpłatne." },
    { "q": "Jakie formaty są obsługiwane?", "a": "Pliki graficzne PNG, JPG, WebP oraz wideo MP4, WebM i MOV." },
    { "q": "Czy moje pliki są przechowywane?", "a": "Nie, wszystkie pliki są bezpowrotnie niszczone po ich pobraniu." },
    { "q": "Czy zrzut ekranu usunie znak wodny?", "a": "Nie, SynthID jest zaprojektowany tak, by przetrwać wykonywanie zrzutów ekranu." },
    { "q": "Czy RemoveSynth należy do Google?", "a": "Nie, RemoveSynth to całkowicie niezależne narzędzie." }
  ],
  "cta": { "h2": "Wypróbuj narzędzie SynthID Remover", "p": "Za darmo, bez rejestracji, dla obrazów i wideo.", "button": "Usuń SynthID teraz" }
})

# 19. CS (Czech)
save("cs", "cs", {
  "lang": "cs",
  "title": "Odstranit SynthID Online Zdarma: AI Obrázky a Videa",
  "description": "Bezplatný online nástroj pro odstranění neviditelného vodoznaku SynthID a metadat C2PA z AI obrázků a videí přímo v prohlížeči v původní kvalitě.",
  "hero": {
    "eyebrow": "Bez registrace · Zdarma · Obrázky, videa a audio",
    "h1Before": "Zdarma ",
    "h1Accent": "odstranit SynthID",
    "h1After": " online",
    "lead": "Odstraňte neviditelný vodoznak SynthID z obrázků a videí vytvořených umělou inteligencí. Nahrajte soubor, zpracujte jedním kliknutím a stáhněte v původní kvalitě.",
    "checks": ["Obrázky, videa a audio", "Každý snímek videa", "Soubory smazány ihned po zpracování"],
    "worksWith": "Funguje se soubory z"
  },
  "features": [
    { "title": "Obrázky a videa", "text": "Jeden nástroj pro PNG, JPG, WebP a videa MP4, WebM, MOV." },
    { "title": "Každý snímek", "text": "U videa je kompletně zpracován celý klip bez přeskakování snímků." },
    { "title": "Původní kvalita", "text": "Rozlišení, formát i snímková frekvence zůstávají zachovány." },
    { "title": "Bez registrace", "text": "Stačí přetáhnout soubor a začít bez nutnosti vytvářet účet." },
    { "title": "Absolutní soukromí", "text": "Nahrané soubory jsou trvale smazány ihned po dokončení." },
    { "title": "Funguje kdekoli", "text": "Běží ve všech moderních prohlížečích na počítači i mobilu." }
  ],
  "inside": {
    "kicker": "Co je uvnitř AI souboru",
    "h2": "Dva způsoby označování obsahu AI",
    "p": "Většina nástrojů AI označuje své výstupy neviditelnými značkami.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Neviditelný signál v pixelech",
        "html": "SynthID je vpleten do dat pixelů i každého snímku videa a odolá ořezu i filtrům."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Kryptografický podpis v metadatech",
        "html": "Digitální záznam v metadatech osvědčující vytvoření pomocí AI modelu."
      }
    ]
  },
  "how": {
    "kicker": "Jak to funguje",
    "h2": "Odstraňte SynthID ve čtyřech krocích",
    "steps": [
      { "title": "Přetáhněte soubor", "text": "Vyberte obrázek nebo video z Gemini, Imagen nebo Veo." },
      { "title": "Potvrďte práva", "text": "Zaškrtněte políčko potvrzující oprávnění ke zpracování." },
      { "title": "Automatické vyčištění", "text": "Náš algoritmus neutralizuje vodoznak snímek po snímku." },
      { "title": "Stáhněte soubor", "text": "Porovnejte výsledek a stáhněte čistý soubor v původním formátu." }
    ]
  },
  "plans": {
    "kicker": "Tarify",
    "h2": "Během předběžného přístupu zcela zdarma",
    "p": "Všechny funkce jsou v současnosti dostupné bez poplatků.",
    "free": {
      "name": "Zdarma",
      "note": "Bez platební karty",
      "items": ["Obrázky a videa", "Až 50 MB na soubor", "Původní kvalita", "Bez nutnosti registrace"],
      "cta": "Zpracovat soubor"
    },
    "pro": {
      "badge": "Již brzy",
      "price": "Kredity",
      "note": "Měsíčně nebo ročně",
      "items": ["Větší soubory a dlouhá videa", "Dávkové zpracování", "Přednostní fronta", "Přístup k API"]
    }
  },
  "hood": {
    "kicker": "Technologie a Soukromí",
    "h2": "Postaveno na špičkové kvalitě a diskrétnosti",
    "cards": [
      { "title": "Zpracování každého snímku", "text": "Video je zpracováno souvisle bez vynechání jediného snímku.", "tag": "Snímek 1 → 240 · hotovo" },
      { "title": "Žádné ukládání dat", "text": "Dočasné soubory jsou smazány ihned po stažení.", "tag": "0 uložených souborů" },
      { "title": "Kvalita beze změny", "text": "Rozlišení i fps zůstávají zcela totožné.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Pro koho",
    "h2": "Pro tvůrce, kteří pracují s vlastním AI obsahem",
    "cards": [
      { "title": "Tvůrci obsahu", "text": "Vytvořili jste obrázek či video a chcete čistý originální soubor." },
      { "title": "Výzkumníci", "text": "Testování odolnosti digitálních vodoznaků a steganografie." },
      { "title": "Vývojáři", "text": "Automatizace zpracování médií v produkčních pipeline přes API." }
    ],
    "note": "Zpracovávejte pouze obsah, k němuž máte zákonná práva."
  },
  "seo": [
    {
      "h2": "Jak odstranit vodoznak SynthID online?",
      "html": "Přetáhněte soubor do pole výše, potvrďte práva a klikněte na <strong>Zpracovat soubor</strong> pro stažení verze bez vodoznaku."
    },
    { "h2": "Které nástroje obsahují SynthID?", "html": "Google integruje SynthID do systémů Gemini, Imagen a Veo." },
    {
      "h2": "Proč oříznutí neodstraní SynthID?",
      "html": "SynthID je zakomponován v celém spektru pixelů, takže ořez ani snímek obrazovky jej neodstraní."
    }
  ],
  "faqHeading": "Často kladené otázky",
  "faqs": [
    { "q": "Co je to SynthID remover?", "a": "Nástroj sloužící k neutralizaci neviditelného vodoznaku SynthID od společnosti Google z AI médií." },
    { "q": "Je služba zdarma?", "a": "Ano, během předběžného přístupu je zcela zdarma pro všechny." },
    { "q": "Jaké formáty jsou podporovány?", "a": "Obrázky PNG, JPG, WebP a videa MP4, WebM, MOV." },
    { "q": "Ukládáte mé soubory?", "a": "Ne, veškeré soubory jsou po stažení okamžitě smazány." },
    { "q": "Pomůže pořízení snímku obrazovky?", "a": "Ne, SynthID přežije i pořízení screenshotu." },
    { "q": "Je RemoveSynth součástí Google?", "a": "Ne, RemoveSynth je nezávislý nástroj." }
  ],
  "cta": { "h2": "Vyzkoušejte odstraňovač SynthID", "p": "Zdarma, bez registrace, pro obrázky i videa.", "button": "Odstranit SynthID nyní" }
})

# 20. HU (Hungarian)
save("hu", "hu", {
  "lang": "hu",
  "title": "SynthID Eltávolítása Online Ingyen: AI Képek és Videók",
  "description": "Ingyenes online eszköz a láthatatlan SynthID vízjel és C2PA metaadatok eltávolításához AI képekből és videókból közvetlenül a böngészőben minőségromlás nélkül.",
  "hero": {
    "eyebrow": "Regisztráció nélkül · Ingyenes · Kép, videó és hang",
    "h1Before": "Ingyenes ",
    "h1Accent": "SynthID eltávolítás",
    "h1After": " online",
    "lead": "Távolítsa el a láthatatlan SynthID vízjelet az AI által generált képekből és videókból. Töltse fel fájlját, dolgozza fel egyetlen kattintással, és töltse le eredeti minőségben.",
    "checks": ["Képek, videók és audió", "Minden egyes videókocka", "A fájlok azonnal törlődnek"],
    "worksWith": "Kompatibilis a következő eszközökkel:"
  },
  "features": [
    { "title": "Képek és videók", "text": "Egyetlen eszköz PNG, JPG, WebP és MP4, WebM, MOV formátumokhoz." },
    { "title": "Minden képkocka", "text": "Videók esetében a teljes klip kockáról kockára feldolgozásra kerül." },
    { "title": "Eredeti minőség", "text": "A felbontás, a formátum és a képkockasebesség változatlan marad." },
    { "title": "Regisztráció nélkül", "text": "Csak húzza be a fájlt, és kezdje el azonnal fiók létrehozása nélkül." },
    { "title": "Maximális adatvédelem", "text": "A feltöltött fájlok azonnal véglegesen törlődnek a letöltés után." },
    { "title": "Bárhol működik", "text": "Minden modern böngészőben fut számítógépen, táblagépen és mobilon." }
  ],
  "inside": {
    "kicker": "Mi van az AI fájlokban",
    "h2": "Az AI tartalmak megjelölésének két módja",
    "p": "A legtöbb AI eszköz szabad szemmel láthatatlan jelöléseket ágyaz be.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Láthatatlan digitális jel a pixelekben",
        "html": "A SynthID közvetlenül a képpontokba és minden videókockába beépül, így ellenáll a vágásnak és tömörítésnek."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Digitális aláírás a metaadatokban",
        "html": "Kriptográfiai tanúsítvány a metaadatokban, amely igazolja az AI eredetet."
      }
    ]
  },
  "how": {
    "kicker": "Hogyan működik",
    "h2": "Távolítsa el a SynthID-t négy egyszerű lépésben",
    "steps": [
      { "title": "Húzza be a fájlt", "text": "Válasszon ki egy Gemini, Imagen vagy Veo által készített képet vagy videót." },
      { "title": "Erősítse meg a jogokat", "text": "Jelölje be a négyzetet annak igazolására, hogy jogosult a fájl feldolgozására." },
      { "title": "Automatikus tisztítás", "text": "Algoritmusunk kockáról kockára semlegesíti a vízjelet." },
      { "title": "Letöltés", "text": "Hasonlítsa össze az előtte-utána állapotot, és töltse le a tiszta fájlt." }
    ]
  },
  "plans": {
    "kicker": "Csomagok",
    "h2": "Teljesen ingyenes a korai hozzáférés során",
    "p": "Jelenleg minden prémium funkció díjmentesen elérhető.",
    "free": {
      "name": "Ingyenes",
      "note": "Bankkártya nem szükséges",
      "items": ["Képek és videók", "Akár 50 MB fájlonként", "Eredeti felbontás", "Fiók nélkül használható"],
      "cta": "Fájl feldolgozása"
    },
    "pro": {
      "badge": "Hamarosan",
      "price": "Kreditek",
      "note": "Havi vagy éves elszámolás",
      "items": ["Nagyobb fájlok és hosszabb videók", "Kötegelt feldolgozás", "Prioritási sor", "API hozzáférés"]
    }
  },
  "hood": {
    "kicker": "Technológia és Adatbiztonság",
    "h2": "Minőségre és diszkrécióra tervezve",
    "cards": [
      { "title": "Minden képkocka tisztítva", "text": "A videó teljes időtartama kihagyás nélkül feldolgozásra kerül.", "tag": "Képkocka 1 → 240 · kész" },
      { "title": "Nulla adatmegőrzés", "text": "Az ideiglenes fájlok a letöltés után azonnal megsemmisülnek.", "tag": "0 tárolt fájl" },
      { "title": "Változatlan minőség", "text": "A felbontás és a képfrissítés teljesen megmarad.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Kiknek készült",
    "h2": "Alkotóknak, akik saját AI tartalmaikkal dolgoznak",
    "cards": [
      { "title": "Tartalomkészítők", "text": "Ön hozta létre a médiát, és a tiszta, eredeti fájlra van szüksége." },
      { "title": "Kutatók", "text": "A digitális vízjelek ellenállóságát és szteganográfiát vizsgálók számára." },
      { "title": "Fejlesztők", "text": "Médiafeldolgozási folyamatok automatizálása API-n keresztül." }
    ],
    "note": "Kizárólag olyan fájlokat dolgozzon fel, amelyekhez rendelkezik a megfelelő jogokkal."
  },
  "seo": [
    {
      "h2": "Hogyan távolítható el a SynthID vízjel online?",
      "html": "Húzza a fájlt a fenti mezőbe, igazolja jogosultságát, és kattintson a <strong>Fájl feldolgozása</strong> gombra a tiszta verzió letöltéséhez."
    },
    { "h2": "Mely eszközök alkalmazzák a SynthID-t?", "html": "A Google alkalmazza a Gemini, Imagen és Veo modelljeiben." },
    {
      "h2": "Miért nem tünteti el a kivágás a SynthID-t?",
      "html": "A SynthID a teljes képponthálózatban el van osztva, ezért egyszerű vágással vagy képernyőkép készítésével nem távolítható el."
    }
  ],
  "faqHeading": "Gyakori kérdések",
  "faqs": [
    { "q": "Mi az a SynthID eltávolító?", "a": "Egy speciális eszköz a Google láthatatlan SynthID vízjelének semlegesítésére AI képekből és videókból." },
    { "q": "Ingyenes a szolgáltatás?", "a": "Igen, a korai hozzáférési időszakban 100%-ban ingyenes." },
    { "q": "Milyen formátumok támogatottak?", "a": "PNG, JPG, WebP képek és MP4, WebM, MOV videók." },
    { "q": "Tárolják a feltöltött fájlokat?", "a": "Nem, minden fájl véglegesen törlődik a letöltést követően." },
    { "q": "Segít a képernyőkép készítése?", "a": "Nem, a SynthID-t úgy tervezték, hogy túlélje a képernyőfotózást is." },
    { "q": "A RemoveSynth a Google tulajdona?", "a": "Nem, a RemoveSynth független fejlesztésű harmadik féltől származó eszköz." }
  ],
  "cta": { "h2": "Próbálja ki a SynthID eltávolítót", "p": "Ingyenes, regisztráció nélkül, képekhez és videókhoz.", "button": "SynthID eltávolítása most" }
})

# 21. RO (Romanian)
save("ro", "ro", {
  "lang": "ro",
  "title": "Elimină SynthID Online Gratuit: Imagini și Videoclipuri AI",
  "description": "Instrument online gratuit pentru eliminarea filigranului invizibil SynthID și a metadatelor C2PA din imaginile și videoclipurile generate de AI direct în browser.",
  "hero": {
    "eyebrow": "Fără cont · Gratuit · Imagini, video și audio",
    "h1Before": "Gratuit ",
    "h1Accent": "elimină SynthID",
    "h1After": " online",
    "lead": "Elimină filigranul invizibil SynthID din imaginile și videoclipurile generate de AI. Încarcă fișierul, procesează-l cu un clic și descarcă-l în calitatea originală.",
    "checks": ["Imagini, video și audio", "Fiecare cadru video", "Fișiere șterse imediat după procesare"],
    "worksWith": "Compatibil cu fișiere din"
  },
  "features": [
    { "title": "Imagini și videoclipuri", "text": "Un singur instrument pentru PNG, JPG, WebP și MP4, WebM, MOV." },
    { "title": "Fiecare cadru", "text": "La videoclipuri, întregul fișier este procesat cadru cu cadru." },
    { "title": "Calitate originală", "text": "Rezoluția, formatul și rata de cadre rămân complet neschimbate." },
    { "title": "Fără înregistrare", "text": "Trage fișierul și începe imediat fără a fi nevoie de un cont." },
    { "title": "Confidențialitate absolută", "text": "Fișierele sunt șterse definitiv imediat ce descărcarea este gata." },
    { "title": "Accesibil oriunde", "text": "Funcționează pe orice browser modern pe calculator sau telefon." }
  ],
  "inside": {
    "kicker": "Ce conține un fișier AI",
    "h2": "Două moduri de marcare a conținutului AI",
    "p": "Majoritatea generatoarelor AI inserează marcaje invizibile în fișierele create.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Un semnal invizibil în pixeli",
        "html": "SynthID este integrat în datele pixelilor și în fiecare cadru video, rezistând la decupare și compresie."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Semnătură criptografică în metadate",
        "html": "Certificat digital inserat în metadate ce indică generarea cu ajutorul AI."
      }
    ]
  },
  "how": {
    "kicker": "Cum funcționează",
    "h2": "Elimină SynthID în patru pași simpli",
    "steps": [
      { "title": "Trage fișierul", "text": "Selectează o imagine sau un video din Gemini, Imagen sau Veo." },
      { "title": "Confirmă drepturile", "text": "Bifează căsuța pentru a confirma dreptul de a procesa fișierul." },
      { "title": "Curățare automată", "text": "Algoritmul nostru neutralizează filigranul cadru cu cadru." },
      { "title": "Descarcă", "text": "Compară rezultatul și descarcă fișierul curat în formatul original." }
    ]
  },
  "plans": {
    "kicker": "Abonamente",
    "h2": "Complet gratuit în perioada de acces timpuriu",
    "p": "Toate funcțiile sunt oferite gratuit în această etapă.",
    "free": {
      "name": "Gratuit",
      "note": "Fără card bancar",
      "items": ["Imagini și video", "Până la 50 MB per fișier", "Calitate originală", "Fără cont necesar"],
      "cta": "Procesează fișier"
    },
    "pro": {
      "badge": "În curând",
      "price": "Credite",
      "note": "Lunar sau anual",
      "items": ["Fișiere mari & videoclipuri lungi", "Procesare în lot", "Coadă prioritară", "Acces API"]
    }
  },
  "hood": {
    "kicker": "Tehnologie & Confidențialitate",
    "h2": "Construit pentru fidelitate maximă și securitate",
    "cards": [
      { "title": "Procesare cadru cu cadru", "text": "Clipul video este procesat fără a sări peste cadre intermediare.", "tag": "Cadru 1 → 240 · finalizat" },
      { "title": "Zero stocare", "text": "Fișierele temporare sunt eliminate instant după utilizare.", "tag": "0 fișiere stocate" },
      { "title": "Calitate păstrată", "text": "Rezoluția și fps-ul rămân identice cu cele originale.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Cui i se adresează",
    "h2": "Creat pentru cei care lucrează cu propriul conținut AI",
    "cards": [
      { "title": "Creatori de conținut", "text": "Ați generat imaginea sau videoclipul și doriți fișierul fără marcaje ascunse." },
      { "title": "Cercetători", "text": "Testarea robusteții filigranelor digitale și a tehnicilor de steganografie." },
      { "title": "Dezvoltatori", "text": "Automatizarea procesării fișierelor media prin intermediul API-ului." }
    ],
    "note": "Procesați numai fișiere pentru care dețineți drepturi legitime."
  },
  "seo": [
    {
      "h2": "Cum se elimină filigranul SynthID online?",
      "html": "Trageți fișierul în zona de încărcare de mai sus, confirmați drepturile și apăsați <strong>Procesează fișierul</strong> pentru a descărca versiunea curățată."
    },
    { "h2": "Ce unelte AI adaugă SynthID?", "html": "Google adaugă SynthID în Gemini, Imagen și Veo." },
    {
      "h2": "De ce decuparea nu elimină SynthID?",
      "html": "SynthID este inserat pe întreaga suprafață a pixelilor, astfel încât decuparea sau capturile de ecran nu îl pot șterge."
    }
  ],
  "faqHeading": "Întrebări frecvente",
  "faqs": [
    { "q": "Ce este un instrument de eliminare SynthID?", "a": "O aplicație dedicată neutralizării filigranului invizibil SynthID creat de Google în fișierele AI." },
    { "q": "Este gratuit?", "a": "Da, în perioada actuală de acces timpuriu este 100% gratuit." },
    { "q": "Ce formate sunt acceptate?", "a": "Imagini PNG, JPG, WebP și videoclipuri MP4, WebM, MOV." },
    { "q": "Păstrați fișierele mele?", "a": "Nu, toate fișierele sunt șterse definitiv imediat după descărcare." },
    { "q": "O captură de ecran elimină SynthID?", "a": "Nu, SynthID este proiectat să reziste chiar și la capturi de ecran." },
    { "q": "Aparține RemoveSynth companiei Google?", "a": "Nu, RemoveSynth este un instrument independent dezvoltat de o terță parte." }
  ],
  "cta": { "h2": "Încearcă instrumentul de eliminare SynthID", "p": "Gratuit, rapid și fără cont.", "button": "Elimină SynthID acum" }
})

# 22. UK (Ukrainian)
save("uk", "uk", {
  "lang": "uk",
  "title": "Видалити SynthID Онлайн Безкоштовно: AI Зображення та Відео",
  "description": "Безкоштовний онлайн-інструмент для видалення невидимого водяного знака SynthID та метаданих C2PA з AI зображень і відео прямо у браузері без втрати якості.",
  "hero": {
    "eyebrow": "Без реєстрації · Безкоштовно · Зображення, відео та аудіо",
    "h1Before": "Безкоштовно ",
    "h1Accent": "видалити SynthID",
    "h1After": " онлайн",
    "lead": "Видаліть невидимий водяний знак SynthID із зображень та відео, створених штучним інтелектом. Завантажте файл, обробіть в один клік та завантажте в оригінальній якості.",
    "checks": ["Зображення, відео та аудіо", "Обробка кожного кадру відео", "Файли видаляються відразу після завантаження"],
    "worksWith": "Працює з файлами від"
  },
  "features": [
    { "title": "Зображення та відео", "text": "Єдиний інструмент для PNG, JPG, WebP та відео MP4, WebM, MOV." },
    { "title": "Кожен кадр відео", "text": "У відеофайлах обробляється весь кліп без пропуску кадрів." },
    { "title": "Оригінальна якість", "text": "Роздільна здатність, колір та частота кадрів залишаються незмінними." },
    { "title": "Без реєстрації", "text": "Просто перетягніть файл та почніть без створення облікового запису." },
    { "title": "Повна конфіденційність", "text": "Файли безповоротно видаляються відразу після завершення завантаження." },
    { "title": "Працює скрізь", "text": "Працює в будь-якому сучасному браузері на комп'ютері чи смартфоні." }
  ],
  "inside": {
    "kicker": "Що містить AI-файл",
    "h2": "Два способи маркування контенту штучним інтелектом",
    "p": "Більшість сучасних AI-генераторів додають приховані від ока мітки.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Невидимий сигнал у структурі пікселів",
        "html": "SynthID вплітається у піксельні дані та кожен кадр відео, витримуючи кадрування та стиснення."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Криптографічний підпис у метаданих",
        "html": "Цифровий запис у метаданих, що підтверджує генерацію контенту моделлю AI."
      }
    ]
  },
  "how": {
    "kicker": "Як це працює",
    "h2": "Видаліть SynthID за чотири прості кроки",
    "steps": [
      { "title": "Перетягніть файл", "text": "Виберіть зображення або відео, згенероване в Gemini, Imagen чи Veo." },
      { "title": "Підтвердьте права", "text": "Поставте прапорець, підтверджуючи право на обробку файлу." },
      { "title": "Автоматична обробка", "text": "Алгоритм нейтралізує водяний знак покадрово." },
      { "title": "Завантажте результат", "text": "Порівняйте до і після та завантажте чистий файл у початковому форматі." }
    ]
  },
  "plans": {
    "kicker": "Тарифи",
    "h2": "Повністю безкоштовно у ранньому доступі",
    "p": "Усі функції наразі доступні без будь-яких прихованих платежів.",
    "free": {
      "name": "Безкоштовний",
      "note": "Банківська картка не потрібна",
      "items": ["Зображення та відео", "До 50 МБ на файл", "Оригінальна якість", "Без реєстрації"],
      "cta": "Обробити файл"
    },
    "pro": {
      "badge": "Незабаром",
      "price": "Кредити",
      "note": "Щомісяця або щороку",
      "items": ["Більші файли та тривалі відео", "Пакетна обробка", "Пріоритетна черга", "Доступ до API"]
    }
  },
  "hood": {
    "kicker": "Технології та Безпека",
    "h2": "Створено для безкомпромісної якості та конфіденційності",
    "cards": [
      { "title": "Обробка кожного кадру", "text": "Відео обробляється повністю без пропуску проміжних кадрів.", "tag": "Кадр 1 → 240 · виконано" },
      { "title": "Ніякого збереження", "text": "Тимчасові файли негайно знищуються після скачування.", "tag": "0 збережених файлів" },
      { "title": "Незмінна чіткість", "text": "Роздільна здатність і частота кадрів залишаються незмінними.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Для кого",
    "h2": "Для авторів, які створюють власний AI-контент",
    "cards": [
      { "title": "Контент-мейкери", "text": "Ви згенерували медіа та бажаєте мати чистий файл без сторонніх маркерів." },
      { "title": "Дослідники", "text": "Аналіз стійкості цифрових водяних знаків та стеганографії." },
      { "title": "Розробники", "text": "Автоматизація обробки медіапотоків через API." }
    ],
    "note": "Обробляйте виключно файли, на які маєте законні права."
  },
  "seo": [
    {
      "h2": "Як видалити водяний знак SynthID онлайн?",
      "html": "Перетягніть файл у поле вгорі, підтвердьте свої права та натисніть <strong>Обробити файл</strong>, щоб завантажити чисту версію."
    },
    { "h2": "Які інструменти AI додають SynthID?", "html": "Google інтегрує SynthID у Gemini, Imagen та Veo." },
    {
      "h2": "Чому обрізка зображення не видаляє SynthID?",
      "html": "SynthID нанесено по всій площині пікселів, тому обрізка або знімок екрана не здатні його позбутися."
    }
  ],
  "faqHeading": "Часті запитання",
  "faqs": [
    { "q": "Що таке інструмент видалення SynthID?", "a": "Спеціалізована програма для нейтралізації невидимого водяного знака SynthID від Google у контенті AI." },
    { "q": "Чи це безкоштовно?", "a": "Так, у період раннього доступу використання є повністю безкоштовним." },
    { "q": "Які формати файлів підтримуються?", "a": "Зображення PNG, JPG, WebP та відео MP4, WebM, MOV." },
    { "q": "Чи зберігаються мої файли?", "a": "Ні, всі файли видаляються негайно після передачі результату." },
    { "q": "Чи допоможе скріншот прибрати SynthID?", "a": "Ні, SynthID розроблено так, щоб зберігатися навіть на скріншотах." },
    { "q": "Чи пов'язаний RemoveSynth із Google?", "a": "Ні, RemoveSynth є незалежним стороннім сервісом." }
  ],
  "cta": { "h2": "Спробуйте засіб видалення SynthID", "p": "Безкоштовно, без реєстрації, для фото та відео.", "button": "Видалити SynthID зараз" }
})

# 23. EL (Greek)
save("el", "el", {
  "lang": "el",
  "title": "Αφαίρεση SynthID Online Δωρεάν: Εικόνες και Βίντεο AI",
  "description": "Δωρεάν online εργαλείο αφαίρεσης του αόρατου υδατογραφήματος SynthID και μεταδεδομένων C2PA από εικόνες και βίντεο AI απευθείας στο πρόγραμμα περιήγησης.",
  "hero": {
    "eyebrow": "Χωρίς εγγραφή · Δωρεάν · Εικόνες, βίντεο και ήχος",
    "h1Before": "Δωρεάν ",
    "h1Accent": "αφαίρεση SynthID",
    "h1After": " online",
    "lead": "Αφαιρέστε το αόρατο υδατογράφημα SynthID από εικόνες και βίντεο τεχνητής νοημοσύνης. Ανεβάστε το αρχείο σας, επεξεργαστείτε με ένα κλικ και κατεβάστε στην αρχική ποιότητα.",
    "checks": ["Εικόνες, βίντεο & ήχος", "Κάθε καρέ του βίντεο", "Άμεση διαγραφή αρχείων μετά τη λήψη"],
    "worksWith": "Συμβατό με αρχεία από"
  },
  "features": [
    { "title": "Εικόνες και βίντεο", "text": "Ένα εργαλείο για εικόνες PNG, JPG, WebP και βίντεο MP4, WebM, MOV." },
    { "title": "Κάθε καρέ", "text": "Στα βίντεο, ολόκληρο το κλιπ καθαρίζεται καρέ προς καρέ." },
    { "title": "Αρχική ποιότητα", "text": "Ανάλυση, φορμά και ρυθμός καρέ διατηρούνται πλήρως αναλλοίωτα." },
    { "title": "Χωρίς εγγραφή", "text": "Σύρετε το αρχείο και ξεκινήστε χωρίς απαίτηση λογαριασμού." },
    { "title": "Απόλυτο απόρρητο", "text": "Τα αρχεία διαγράφονται μόνιμα αμέσως μόλις ολοκληρωθεί η λήψη." },
    { "title": "Παντού προσβάσιμο", "text": "Λειτουργεί σε κάθε σύγχρονο πρόγραμμα περιήγησης σε υπολογιστή και κινητό." }
  ],
  "inside": {
    "kicker": "Τι περιέχει ένα αρχείο AI",
    "h2": "Δύο τρόποι σήμανσης περιεχομένου AI",
    "p": "Τα περισσότερα εργαλεία AI ενσωματώνουν μη ορατές ενδείξεις.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Αόρατο ψηφιακό σήμα στα εικονοστοιχεία",
        "html": "Το SynthID ενσωματώνεται στα δεδομένα των πίξελ και σε κάθε καρέ, αντέχοντας σε περικοπές και φίλτρα."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Κρυπτογραφημένη υπογραφή στα μεταδεδομένα",
        "html": "Ψηφιακό πιστοποιητικό που καταγράφει τη δημιουργία του αρχείου από μοντέλο AI."
      }
    ]
  },
  "how": {
    "kicker": "Πώς λειτουργεί",
    "h2": "Αφαιρέστε το SynthID σε τέσσερα απλά βήματα",
    "steps": [
      { "title": "Σύρετε το αρχείο", "text": "Επιλέξτε εικόνα ή βίντεο από Gemini, Imagen ή Veo." },
      { "title": "Επιβεβαιώστε δικαιώματα", "text": "Επιλέξτε το πλαίσιο ότι έχετε το δικαίωμα επεξεργασίας." },
      { "title": "Αυτόματη εκκαθάριση", "text": "Ο αλγόριθμός μας εξουδετερώνει το υδατογράφημα καρέ-καρέ." },
      { "title": "Λήψη αρχείου", "text": "Συγκρίνετε το αποτέλεσμα και κατεβάστε το καθαρό αρχείο." }
    ]
  },
  "plans": {
    "kicker": "Συνδρομές",
    "h2": "Εντελώς δωρεάν κατά την περίοδο πρώιμης πρόσβασης",
    "p": "Όλες οι λειτουργίες προσφέρονται χωρίς καμία χρέωση.",
    "free": {
      "name": "Δωρεάν",
      "note": "Χωρίς πιστωτική κάρτα",
      "items": ["Εικόνες και βίντεο", "Έως 50 MB ανά αρχείο", "Αρχική ποιότητα", "Χωρίς λογαριασμό"],
      "cta": "Επεξεργασία αρχείου"
    },
    "pro": {
      "badge": "Σύντομα",
      "price": "Μονάδες (Credits)",
      "note": "Μηνιαία ή ετήσια",
      "items": ["Μεγαλύτερα αρχεία & μακρά βίντεο", "Μαζική επεξεργασία", "Ουρά προτεραιότητας", "Πρόσβαση σε API"]
    }
  },
  "hood": {
    "kicker": "Τεχνολογία & Ιδιωτικότητα",
    "h2": "Σχεδιασμένο για κορυφαία ποιότητα και ασφάλεια",
    "cards": [
      { "title": "Πλήρης επεξεργασία καρέ", "text": "Το βίντεο επεξεργάζεται αδιάλειπτα χωρίς παράλειψη καρέ.", "tag": "Καρέ 1 → 240 · ολοκληρώθηκε" },
      { "title": "Καμία αποθήκευση", "text": "Τα προσωρινά αρχεία καταστρέφονται αμέσως μετά τη λήψη.", "tag": "0 αποθηκευμένα αρχεία" },
      { "title": "Απαράμιλλη ποιότητα", "text": "Ανάλυση και framerate παραμένουν αναλλοίωτα.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Σε ποιους απευθύνεται",
    "h2": "Για δημιουργούς που εργάζονται με δικό τους AI περιεχόμενο",
    "cards": [
      { "title": "Δημιουργοί περιεχομένου", "text": "Δημιουργήσατε το υλικό και θέλετε το αρχικό καθαρό αντίγραφο." },
      { "title": "Ερευνητές", "text": "Δοκιμές ανθεκτικότητας ψηφιακών υδατογραφημάτων και στεγανογραφίας." },
      { "title": "Προγραμματιστές", "text": "Αυτοματοποίηση ροών επεξεργασίας πολυμέσων μέσω API." }
    ],
    "note": "Επεξεργαστείτε μόνο αρχεία για τα οποία έχετε νόμιμο δικαίωμα."
  },
  "seo": [
    {
      "h2": "Πώς να αφαιρέσετε το SynthID online;",
      "html": "Σύρετε το αρχείο σας στην παραπάνω περιοχή, επιβεβαιώστε τα δικαιώματα και πατήστε <strong>Επεξεργασία αρχείου</strong> για να κατεβάσετε την καθαρή έκδοση."
    },
    { "h2": "Ποια εργαλεία AI εισάγουν SynthID;", "html": "Η Google προσθέτει SynthID σε Gemini, Imagen και Veo." },
    {
      "h2": "Γιατί η περικοπή δεν αφαιρεί το SynthID;",
      "html": "Το SynthID διαχέεται σε ολόκληρο το πλέγμα των πίξελ, επομένως το κροπάρισμα ή τα screenshots δεν μπορούν να το αφαιρέσουν."
    }
  ],
  "faqHeading": "Συχνές Ερωτήσεις",
  "faqs": [
    { "q": "Τι είναι το εργαλείο αφαίρεσης SynthID;", "a": "Ένα εξειδικευμένο πρόγραμμα για την εξουδετέρωση του αόρατου υδατογραφήματος SynthID της Google από αρχεία AI." },
    { "q": "Είναι δωρεάν;", "a": "Ναι, κατά την περίοδο πρώιμης πρόσβασης είναι 100% δωρεάν." },
    { "q": "Ποιες μορφές αρχείων υποστηρίζονται;", "a": "Εικόνες PNG, JPG, WebP και βίντεο MP4, WebM, MOV." },
    { "q": "Αποθηκεύονται τα αρχεία μου;", "a": "Όχι, όλα τα αρχεία διαγράφονται οριστικά αμέσως μετά την παράδοση." },
    { "q": "Αφαιρεί το screenshot το SynthID;", "a": "Όχι, το SynthID είναι σχεδιασμένο να αντέχει και σε στιγμιότυπα οθόνης." },
    { "q": "Σχετίζεται το RemoveSynth με την Google;", "a": "Όχι, το RemoveSynth είναι ανεξάρτητο εργαλείο τρίτου μέρους." }
  ],
  "cta": { "h2": "Δοκιμάστε το εργαλείο αφαίρεσης SynthID", "p": "Δωρεάν, γρήγορο και χωρίς εγγραφή.", "button": "Αφαίρεση SynthID τώρα" }
})

# 24. SV (Swedish)
save("sv", "sv", {
  "lang": "sv",
  "title": "Ta bort SynthID Online Gratis: AI Bilder och Video",
  "description": "Gratis onlineverktyg för att ta bort den osynliga SynthID-vattenstämpeln och C2PA-metadata från AI-bilder och videor direkt i webbläsaren utan kvalitetsförlust.",
  "hero": {
    "eyebrow": "Ingen registrering · Gratis · Bilder, video och ljud",
    "h1Before": "Gratis ",
    "h1Accent": "ta bort SynthID",
    "h1After": " online",
    "lead": "Ta bort den osynliga SynthID-vattenstämpeln från AI-genererade bilder och videor. Ladda upp din fil, bearbeta med ett klick och ladda ner i originalkvalitet.",
    "checks": ["Bilder, video och ljud", "Varje videobildruta bearbetas", "Filer raderas direkt efter bearbetning"],
    "worksWith": "Fungerar med filer från"
  },
  "features": [
    { "title": "Bilder och videor", "text": "Ett verktyg för PNG, JPG, WebP samt MP4, WebM, MOV." },
    { "title": "Varje bildruta", "text": "I videor bearbetas hela klippet bildruta för bildruta utan undantag." },
    { "title": "Bevarad kvalitet", "text": "Upplösning, format och bildfrekvens förblir helt oförändrade." },
    { "title": "Ingen registrering", "text": "Släpp en fil och kör igång direkt utan konto." },
    { "title": "Fullständig sekretess", "text": "Filer raderas permanent direkt efter att nedladdningen är klar." },
    { "title": "Fungerar överallt", "text": "Körs i alla moderna webbläsare på dator, surfplatta och mobil." }
  ],
  "inside": {
    "kicker": "Inuti en AI-fil",
    "h2": "Två sätt som AI-innehåll märks på",
    "p": "De flesta AI-verktyg bäddar in osynliga digitala spår i sina genereringar.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "En osynlig signal i pixlarna",
        "html": "SynthID är invävt i pixeldatan och varje videoram och tål beskärning och komprimering."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Kryptografisk signatur i metadata",
        "html": "En digital signatur i metadatan som intygar att filen skapats med en AI-modell."
      }
    ]
  },
  "how": {
    "kicker": "Så fungerar det",
    "h2": "Ta bort SynthID i fyra enkla steg",
    "steps": [
      { "title": "Släpp din fil", "text": "Välj en bild eller video från Gemini, Imagen eller Veo." },
      { "title": "Bekräfta rättigheter", "text": "Markera rutan för att bekräfta att du har rätt att bearbeta filen." },
      { "title": "Automatisk rensning", "text": "Vår algoritm neutraliserar vattenstämpeln bildruta för bildruta." },
      { "title": "Ladda ner", "text": "Jämför före och efter och ladda ner den rena filen i originalformat." }
    ]
  },
  "plans": {
    "kicker": "Prisplaner",
    "h2": "Helt gratis under tidig åtkomst",
    "p": "Alla funktioner är för närvarande kostnadsfria att använda.",
    "free": {
      "name": "Gratis",
      "note": "Inget betalkort krävs",
      "items": ["Bilder och video", "Upp till 50 MB per fil", "Originalkvalitet", "Inget konto krävs"],
      "cta": "Bearbeta fil"
    },
    "pro": {
      "badge": "Kommer snart",
      "price": "Krediter",
      "note": "Månadsvis eller årsvis",
      "items": ["Större filer och långa videor", "Batchbearbetning", "Prioriterad kö", "API-åtkomst"]
    }
  },
  "hood": {
    "kicker": "Teknik & Integritet",
    "h2": "Byggt för kompromisslös kvalitet och sekretess",
    "cards": [
      { "title": "Alla bildrutor behandlas", "text": "Hela videon bearbetas utan att några mellanliggande rutor hoppas över.", "tag": "Bildruta 1 → 240 · klart" },
      { "title": "Ingen datalagring", "text": "Temporära filer raderas omedelbart efter leverans.", "tag": "0 lagrade filer" },
      { "title": "Kvalitetsbevarande", "text": "Upplösning och bildhastighet förblir exakt desamma.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "För vem",
    "h2": "Skapat för kreatörer som arbetar med egengenererat AI-material",
    "cards": [
      { "title": "Kreatörer", "text": "Du har skapat bilden eller videon och vill ha den rena filen utan dolda märkningar." },
      { "title": "Forskare", "text": "Testar robustheten hos digitala vattenstämplar och steganografi." },
      { "title": "Utvecklare", "text": "Automatiserar medieflöden via API." }
    ],
    "note": "Bearbeta endast filer du äger eller har tillstånd att använda."
  },
  "seo": [
    {
      "h2": "Hur tar man bort SynthID-vattenstämpel online?",
      "html": "Släpp filen i rutan ovan, bekräfta dina rättigheter och klicka på <strong>Bearbeta fil</strong> för att ladda ner en ren version."
    },
    { "h2": "Vilka AI-verktyg använder SynthID?", "html": "Google använder SynthID i Gemini, Imagen och Veo." },
    {
      "h2": "Varför tar beskärning inte bort SynthID?",
      "html": "SynthID är inbäddat i hela pixelmatrisen, vilket gör att beskärning eller skärmdumpar inte kan avlägsna märket."
    }
  ],
  "faqHeading": "Vanliga frågor",
  "faqs": [
    { "q": "Vad är en SynthID-remover?", "a": "Ett specialverktyg för att neutralisera Googles osynliga SynthID-vattenstämpel i AI-genererade filer." },
    { "q": "Är tjänsten gratis?", "a": "Ja, under vår tidiga åtkomstfas är den 100 % kostnadsfri." },
    { "q": "Vilka filformat stöds?", "a": "PNG, JPG, WebP-bilder samt MP4, WebM, MOV-videor." },
    { "q": "Sparar ni mina filer?", "a": "Nej, alla filer raderas omedelbart efter avslutad nedladdning." },
    { "q": "Försvinner SynthID om man tar en skärmdump?", "a": "Nej, SynthID är konstruerat för att tåla skärmdumpar och omkomprimering." },
    { "q": "Är RemoveSynth kopplat till Google?", "a": "Nej, RemoveSynth är ett helt oberoende verktyg." }
  ],
  "cta": { "h2": "Prova SynthID-borttagaren nu", "p": "Gratis, snabbt och utan registrering.", "button": "Ta bort SynthID nu" }
})

# 25. NO (Norwegian)
save("no", "no", {
  "lang": "no",
  "title": "Fjern SynthID Online Gratis: AI Bilder og Video",
  "description": "Gratis onlineverktøy for å fjerne det usynlige SynthID-vannmerket og C2PA-metadata fra AI-bilder og videoer direkte i nettleseren med original kvalitet.",
  "hero": {
    "eyebrow": "Ingen registrering · Gratis · Bilder, video og lyd",
    "h1Before": "Gratis ",
    "h1Accent": "fjern SynthID",
    "h1After": " online",
    "lead": "Fjern det usynlige SynthID-vannmerket fra AI-genererte bilder og videoer. Last opp filen din, behandle med ett klikk og last ned i original kvalitet.",
    "checks": ["Bilder, video og lyd", "Hver videobilderamme", "Filer slettes umiddelbart etter behandling"],
    "worksWith": "Fungerer med filer fra"
  },
  "features": [
    { "title": "Bilder og videoer", "text": "Ett verktøy for PNG, JPG, WebP og MP4, WebM, MOV." },
    { "title": "Hver bilderamme", "text": "I videoer behandles hele klippet ramme for ramme." },
    { "title": "Opprinnelig kvalitet", "text": "Oppløsning, format og bildefrekvens forblir fullstendig uberørt." },
    { "title": "Uten registrering", "text": "Slipp filen og start umiddelbart uten konto." },
    { "title": "Fullt personvern", "text": "Filer slettes permanent så snart nedlastingen er fullført." },
    { "title": "Virker overalt", "text": "Kjører i alle moderne nettlesere på pc, nettbrett og mobil." }
  ],
  "inside": {
    "kicker": "Innhold i en AI-fil",
    "h2": "To måter AI-innhold blir merket på",
    "p": "De fleste AI-verktøy legger inn usynlige markeringer i det de genererer.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Et usynlig signal i pikslene",
        "html": "SynthID er vevd inn i pikseldataene og hver videorammme, og overlever beskjæring og filtre."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Kryptografisk signatur i metadata",
        "html": "En digital signatur i metadataene som bekrefter at filen er laget av en AI-modell."
      }
    ]
  },
  "how": {
    "kicker": "Slik fungerer det",
    "h2": "Fjern SynthID i fire enkle steg",
    "steps": [
      { "title": "Slipp filen din", "text": "Velg et bilde eller en video fra Gemini, Imagen eller Veo." },
      { "title": "Bekreft rettigheter", "text": "Kryss av i boksen for å bekrefte at du har rett til å behandle filen." },
      { "title": "Automatisk rensing", "text": "Algoritmen vår fjerner vannmerket ramme for ramme." },
      { "title": "Last ned", "text": "Sammenlign før og etter og last ned den rene filen." }
    ]
  },
  "plans": {
    "kicker": "Priser",
    "h2": "Helt gratis under tidlig tilgang",
    "p": "Alle funksjoner er for tiden kostnadsfrie.",
    "free": {
      "name": "Gratis",
      "note": "Ingen kort kreves",
      "items": ["Bilder og video", "Opptil 50 MB per fil", "Original kvalitet", "Ingen konto nødvendig"],
      "cta": "Behandle fil"
    },
    "pro": {
      "badge": "Kommer snart",
      "price": "Kreditter",
      "note": "Månedlig eller årlig",
      "items": ["Større filer og lange videoer", "Batch-behandling", "Prioritert kø", "API-tilgang"]
    }
  },
  "hood": {
    "kicker": "Teknologi og Personvern",
    "h2": "Laget for maksimal kvalitet og diskresjon",
    "cards": [
      { "title": "Hver ramme behandles", "text": "Hele videon renses kontinuerlig uten at rammer hoppes over.", "tag": "Ramme 1 → 240 · ferdig" },
      { "title": "Null lagring", "text": "Midlertidige filer slettes automatisk etter nedlasting.", "tag": "0 lagrede filer" },
      { "title": "Bevaring av kvalitet", "text": "Oppløsning og fps forblir nøyaktig like.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Hvem det er for",
    "h2": "For skapere som jobber med eget AI-materiale",
    "cards": [
      { "title": "Skapere", "text": "Du har generert bildet eller videoen og ønsker den rene filen." },
      { "title": "Forskere", "text": "Tester robustheten til digitale vannmerker og steganografi." },
      { "title": "Utviklere", "text": "Integrerer mediebehandling via API i automatiserte rørledninger." }
    ],
    "note": "Behandle kun innhold du har rettigheter til."
  },
  "seo": [
    {
      "h2": "Hvordan fjerne SynthID-vannmerke på nettet?",
      "html": "Slipp filen i feltet over, bekreft rettighetene og klikk på <strong>Behandle fil</strong> for å laste ned den rene versjonen."
    },
    { "h2": "Hvilke verktøy bruker SynthID?", "html": "Google benytter SynthID i Gemini, Imagen og Veo." },
    {
      "h2": "Hvorfor fjerner ikke beskjæring SynthID?",
      "html": "SynthID er spredt over hele pikselmatrisen, og beskjæring eller skjermbilde fjerner det ikke."
    }
  ],
  "faqHeading": "Ofte stilte spørsmål",
  "faqs": [
    { "q": "Hva er en SynthID-fjerner?", "a": "Et verktøy som nøytraliserer det usynlige SynthID-vannmerket fra Google i AI-filer." },
    { "q": "Er tjenesten gratis?", "a": "Ja, under tidlig tilgang er den 100 % gratis." },
    { "q": "Hvilke filtyper støttes?", "a": "PNG, JPG, WebP samt MP4, WebM, MOV." },
    { "q": "Lagres filene mine?", "a": "Nei, filene slettes umiddelbart etter nedlasting." },
    { "q": "Hjelper det å ta et skjermbilde?", "a": "Nei, SynthID overlever skjermbilder." },
    { "q": "Er RemoveSynth knyttet til Google?", "a": "Nei, RemoveSynth er et uavhengig verktøy." }
  ],
  "cta": { "h2": "Prøv SynthID-fjerneren nå", "p": "Gratis, raskt og uten registrering.", "button": "Fjern SynthID nå" }
})

# 26. DA (Danish)
save("da", "da", {
  "lang": "da",
  "title": "Fjern SynthID Online Gratis: AI Billeder og Video",
  "description": "Gratis online værktøj til at fjerne det usynlige SynthID-vandmærke og C2PA-metadata fra AI-genererede billeder og videoer direkte i browseren uden kvalitetstab.",
  "hero": {
    "eyebrow": "Ingen registrering · Gratis · Billeder, video og lyd",
    "h1Before": "Gratis ",
    "h1Accent": "fjern SynthID",
    "h1After": " online",
    "lead": "Fjern det usynlige SynthID-vandmærke fra AI-genererede billeder og videoer. Upload din fil, behandl med ét klik og download i original kvalitet.",
    "checks": ["Billeder, video og lyd", "Hver enkelt videobilledramme", "Filer slettes straks efter behandling"],
    "worksWith": "Fungerer med filer fra"
  },
  "features": [
    { "title": "Billeder og videoer", "text": "Ét samlet værktøj til PNG, JPG, WebP og MP4, WebM, MOV." },
    { "title": "Hvert enkelt frame", "text": "I videoer behandles hele klippet frame for frame." },
    { "title": "Original kvalitet", "text": "Opløsning, format og billedfrekvens forbliver uændret." },
    { "title": "Uden login", "text": "Træk en fil og kom i gang uden at oprette en konto." },
    { "title": "Streng privatlivspolitik", "text": "Filer slettes permanent så snart downloadet er klar." },
    { "title": "Kører overalt", "text": "Fungerer i alle moderne browsere på pc, tablet og mobil." }
  ],
  "inside": {
    "kicker": "Hvad findes i en AI-fil",
    "h2": "To måder AI-indhold bliver mærket på",
    "p": "De fleste AI-værktøjer integrerer usynlige digitale mærker i deres filer.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Et usynligt signal i pixels",
        "html": "SynthID er flettet ind i pixeldataene og hver videoramme og modstår beskæring og filtre."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Kryptografisk signatur i metadata",
        "html": "En digital signatur i metadataene der angiver, at mediet er genereret med AI."
      }
    ]
  },
  "how": {
    "kicker": "Sådan fungerer det",
    "h2": "Fjern SynthID i fire enkle trin",
    "steps": [
      { "title": "Træk filen hertil", "text": "Vælg et billede eller en video fra Gemini, Imagen eller Veo." },
      { "title": "Bekræft dine rettigheder", "text": "Afkryds boksen for at bekræfte tilladelse til behandling." },
      { "title": "Automatisk rensning", "text": "Vores algoritme neutraliserer vandmærket frame for frame." },
      { "title": "Download", "text": "Sammenlign før og efter og download den rene fil." }
    ]
  },
  "plans": {
    "kicker": "Priser",
    "h2": "Helt gratis under tidlig adgang",
    "p": "Alle funktioner er i øjeblikket tilgængelige uden omkostninger.",
    "free": {
      "name": "Gratis",
      "note": "Intet betalingskort påkrævet",
      "items": ["Billeder og video", "Op til 50 MB pr. fil", "Original kvalitet", "Ingen konto nødvendig"],
      "cta": "Behandl fil"
    },
    "pro": {
      "badge": "Kommer snart",
      "price": "Kreditter",
      "note": "Månedligt eller årligt",
      "items": ["Større filer og lange videoer", "Batch-behandling", "Prioriteret kø", "API-adgang"]
    }
  },
  "hood": {
    "kicker": "Teknologi og Fortrolighed",
    "h2": "Konstrueret til maksimal kvalitet og datasikkerhed",
    "cards": [
      { "title": "Hvert frame renses", "text": "Videoen behandles ubrudt uden at springe frames over.", "tag": "Frame 1 → 240 · udført" },
      { "title": "Ingen datalagring", "text": "Midlertidige filer destrueres automatisk efter download.", "tag": "0 gemte filer" },
      { "title": "Kvalitetsbevarelse", "text": "Opløsning og framerate forbliver helt intakte.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Målgruppe",
    "h2": "Til skabere der arbejder med egne AI-genererede medier",
    "cards": [
      { "title": "Indholdsskabere", "text": "Du har genereret værket og ønsker den rene originale fil." },
      { "title": "Forskere", "text": "Tester robustheden af digitale vandmærker og steganografi." },
      { "title": "Udviklere", "text": "Automatiserer mediebehandling via API i egne systemer." }
    ],
    "note": "Behandl kun filer du har de fornødne rettigheder til."
  },
  "seo": [
    {
      "h2": "Hvordan fjerner man SynthID-vandmærket online?",
      "html": "Træk filen til upload-feltet ovenfor, bekræft rettighederne og klik på <strong>Behandl fil</strong> for at hente den rensede version."
    },
    { "h2": "Hvilke AI-værktøjer tilføjer SynthID?", "html": "Google benytter SynthID i Gemini, Imagen og Veo." },
    {
      "h2": "Hvorfor fjerner beskæring ikke SynthID?",
      "html": "SynthID er fordelt over hele billedets pixelstruktur, så beskæring eller screenshots kan ikke fjerne det."
    }
  ],
  "faqHeading": "Ofte stillede spørgsmål",
  "faqs": [
    { "q": "Hvad er en SynthID-fjerner?", "a": "Et værktøj til at neutralisere Googles usynlige SynthID-vandmærke fra AI-medier." },
    { "q": "Er det gratis?", "a": "Ja, under den tidlige adgangsperiode er det 100 % gratis." },
    { "q": "Hvilke formater understøttes?", "a": "PNG, JPG, WebP samt MP4, WebM, MOV." },
    { "q": "Gemmer I mine filer?", "a": "Nej, alle filer slettes permanent straks efter download." },
    { "q": "Fjerner et screenshot SynthID?", "a": "Nej, SynthID overlever skærmbilleder." },
    { "q": "Er RemoveSynth ejet af Google?", "a": "Nej, RemoveSynth er et uafhængigt værktøj." }
  ],
  "cta": { "h2": "Prøv SynthID-fjerneren nu", "p": "Gratis, hurtigt og uden registrering.", "button": "Fjern SynthID nu" }
})

# 27. FI (Finnish)
save("fi", "fi", {
  "lang": "fi",
  "title": "Poista SynthID Verkossa Ilmaiseksi: AI Kuvat ja Videot",
  "description": "Ilmainen online-työkalu näkymättömän SynthID-vesileiman ja C2PA-metatietojen poistamiseen AI-kuvista ja videoista suoraan selaimessa ilman laadun heikkenemistä.",
  "hero": {
    "eyebrow": "Ei rekisteröitymistä · Ilmainen · Kuvat, videot ja ääni",
    "h1Before": "Ilmainen ",
    "h1Accent": "poista SynthID",
    "h1After": " verkossa",
    "lead": "Poista näkymätön SynthID-vesileima tekoälyn luomista kuvista ja videoista. Lataa tiedostosi, käsittele se yhdellä napsautuksella ja lataa alkuperäisessä laadussa.",
    "checks": ["Kuvat, videot ja ääni", "Jokainen videon ruutu käsitellään", "Tiedostot poistetaan heti käsittelyn jälkeen"],
    "worksWith": "Toimii tiedostoilla seuraavista:"
  },
  "features": [
    { "title": "Kuvat ja videot", "text": "Yksi työkalu PNG-, JPG- ja WebP-kuville sekä MP4-, WebM- ja MOV-videoille." },
    { "title": "Jokainen ruutu", "text": "Videoissa koko leike käsitellään tarkasti ruutu ruudulta." },
    { "title": "Alkuperäinen laatu", "text": "Tarkkuus, muoto ja kuvanopeus säilyvät täysin ennallaan." },
    { "title": "Ei rekisteröitymistä", "text": "Pudota tiedosto ja aloita heti ilman tilin luomista." },
    { "title": "Täysi yksityisyys", "text": "Tiedostot poistetaan pysyvästi heti latauksen valmistuttua." },
    { "title": "Toimii kaikkialla", "text": "Käytettävissä kaikissa nykyaikaisissa selaimissa pc:llä ja puhelimella." }
  ],
  "inside": {
    "kicker": "Mitä AI-tiedosto sisältää",
    "h2": "Kaksi tapaa, joilla tekoälysisältö merkitään",
    "p": "Useimmat tekoälytyökalut upottavat luomiinsa tiedostoihin näkymättömiä tunnisteita.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Näkymätön signaali pikseleissä",
        "html": "SynthID on kudottu pikselitietoihin ja jokaiseen videoruutuun, ja se kestää rajausta ja pakkausta."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Kryptografinen allekirjoitus metatiedoissa",
        "html": "Digitaalinen varmenne metatiedoissa, joka todistaa sisällön luodun tekoälyllä."
      }
    ]
  },
  "how": {
    "kicker": "Kuinka se toimii",
    "h2": "Poista SynthID neljässä helpossa vaiheessa",
    "steps": [
      { "title": "Pudota tiedostosi", "text": "Valitse kuva tai video Geministä, Imagenista tai Veosta." },
      { "title": "Vahvista oikeutesi", "text": "Merkitse valintaruutu vahvistaaksesi, että sinulla on oikeus käsitellä tiedostoa." },
      { "title": "Automaattinen puhdistus", "text": "Algoritmimme neutraloi vesileiman ruutu ruudulta." },
      { "title": "Lataa tiedosto", "text": "Vertaa ennen ja jälkeen -tilannetta ja lataa puhdas tiedosto." }
    ]
  },
  "plans": {
    "kicker": "Hinnoittelu",
    "h2": "Täysin ilmainen ennakkoversion aikana",
    "p": "Kaikki ominaisuudet ovat toistaiseksi käytettävissä maksutta.",
    "free": {
      "name": "Ilmainen",
      "note": "Luottokorttia ei tarvita",
      "items": ["Kuvat ja videot", "Jopa 50 Mt per tiedosto", "Alkuperäinen laatu", "Ei vaadi tiliä"],
      "cta": "Käsittele tiedosto"
    },
    "pro": {
      "badge": "Tulossa pian",
      "price": "Saldot",
      "note": "Kuukausi- tai vuosimaksu",
      "items": ["Suuremmat tiedostot ja pitkät videot", "Eräkäsittely", "Ensisijainen jono", "API-käyttöoikeus"]
    }
  },
  "hood": {
    "kicker": "Teknologia ja Yksityisyys",
    "h2": "Rakennettu tinkimättömään laatuun ja tietosuojaan",
    "cards": [
      { "title": "Kaikki ruudut käsitellään", "text": "Video käsitellään keskeytyksettä hyppäämättä minkään ruudun yli.", "tag": "Ruutu 1 → 240 · valmis" },
      { "title": "Ei tietojen tallennusta", "text": "Väliaikaistiedostot tuhotaan välittömästi latauksen jälkeen.", "tag": "0 tallennettua tiedostoa" },
      { "title": "Laadun säilyminen", "text": "Resoluutio ja kuvanopeus säilyvät identtisinä.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Kenelle",
    "h2": "Tekijöille, jotka työskentelevät oman AI-sisältönsä parissa",
    "cards": [
      { "title": "Sisällöntuottajat", "text": "Olet luonut teoksen itse ja haluat puhtaan tiedoston ilman piilomerkintöjä." },
      { "title": "Tutkijat", "text": "Digitaalisten vesileimojen ja steganografian kestävyystutkimukseen." },
      { "title": "Kehittäjät", "text": "Mediaprosessien automatisointiin API-rajapinnan kautta." }
    ],
    "note": "Käsittele vain tiedostoja, joihin sinulla on lailliset oikeudet."
  },
  "seo": [
    {
      "h2": "Miten SynthID-vesileima poistetaan verkossa?",
      "html": "Pudota tiedosto yllä olevaan kenttään, vahvista oikeutesi ja napsauta <strong>Käsittele tiedosto</strong> ladataksesi puhtaan version."
    },
    { "h2": "Mitkä AI-työkalut käyttävät SynthID:tä?", "html": "Google käyttää SynthID:tä Geminissä, Imagenissa ja Veossa." },
    {
      "h2": "Miksi rajaus ei poista SynthID-vesileimaa?",
      "html": "SynthID on jaettu kuvan koko pikselirakenteeseen, joten rajaus tai kuvakaappaus ei pysty poistamaan sitä."
    }
  ],
  "faqHeading": "Usein kysytyt kysymykset",
  "faqs": [
    { "q": "Mikä on SynthID-poistaja?", "a": "Työkalu Googlen näkymättömän SynthID-vesileiman neutraloimiseksi tekoälytiedostoista." },
    { "q": "Onko palvelu ilmainen?", "a": "Kyllä, ennakkoversion aikana se on 100 % ilmainen." },
    { "q": "Mitä tiedostomuotoja tuetaan?", "a": "PNG-, JPG-, WebP-kuvia sekä MP4-, WebM-, MOV-videoita." },
    { "q": "Tallennatteko tiedostojani?", "a": "Ei, kaikki tiedostot poistetaan pysyvästi heti latauksen jälkeen." },
    { "q": "Poistaako näyttökuva vesileiman?", "a": "Ei, SynthID kestää myös näyttökuvien ottamisen." },
    { "q": "Liittyykö RemoveSynth Googleen?", "a": "Ei, RemoveSynth on itsenäinen kolmannen osapuolen työkalu." }
  ],
  "cta": { "h2": "Kokeile SynthID-poistajaa nyt", "p": "Ilmainen, nopea ja ilman rekisteröitymistä.", "button": "Poista SynthID nyt" }
})

print("Batch 3 (Europe: pt, it, nl, pl, cs, hu, ro, uk, el, sv, no, da, fi) completed.")
