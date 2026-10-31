# -*- coding: utf-8 -*-
import os, json

LOCALES_DIR = r"d:\Nitin\removesynth\apps\removesynth\src\content\locales"

def save(code, var_name, data):
    with open(os.path.join(LOCALES_DIR, f"{code}.ts"), "w", encoding="utf-8") as f:
        f.write(f"import type {{ HomeContent }} from '../types';\n\nexport const {var_name}: HomeContent = {json.dumps(data, ensure_ascii=False, indent=2)};\n")
    print(f"Saved {code}.ts")

# 28. HI (Hindi)
save("hi", "hi", {
  "lang": "hi",
  "title": "हटाएं SynthID ऑनलाइन मुफ्त: AI इमेज और वीडियो के लिए",
  "description": "AI से बनी इमेज और वीडियो से अदृश्य SynthID वॉटरमार्क और C2PA मेटाडेटा हटाने का मुफ्त ऑनलाइन टूल। बिना क्वालिटी खोए सीधे ब्राउज़र में प्रोसेस करें।",
  "hero": {
    "eyebrow": "बिना साइन-अप · 100% मुफ्त · इमेज, वीडियो और ऑडियो",
    "h1Before": "मुफ्त ऑनलाइन ",
    "h1Accent": "SynthID हटाएं",
    "h1After": " टूल",
    "lead": "AI जनरेटेड इमेज और वीडियो से Google SynthID का अदृश्य वॉटरमार्क हटाएं। अपनी फाइल अपलोड करें, एक क्लिक में प्रोसेस करें और ओरिजिनल क्वालिटी में डाउनलोड करें।",
    "checks": ["इमेज, वीडियो और ऑडियो", "वीडियो का हर एक फ्रेम", "प्रोसेसिंग के तुरंत बाद फाइल डिलीट"],
    "worksWith": "इन AI टूल्स की फाइलों के साथ संगत:"
  },
  "features": [
    { "title": "इमेज और वीडियो दोनों", "text": "PNG, JPG, WebP इमेज और MP4, WebM, MOV वीडियो के लिए एकल समाधान।" },
    { "title": "प्रत्येक फ्रेम प्रोसेस", "text": "वीडियो में पूरे क्लिप को फ्रेम-दर-फ्रेम बिना कुछ छोड़े प्रोसेस किया जाता है।" },
    { "title": "मूल गुणवत्ता सुरक्षित", "text": "रेजोल्यूशन, फॉर्मेट और फ्रेम रेट में कोई कमी नहीं आती है।" },
    { "title": "कोई साइन-अप नहीं", "text": "फाइल ड्रैग करें और बिना अकाउंट बनाए तुरंत उपयोग शुरू करें।" },
    { "title": "पूर्ण गोपनीयता", "text": "डाउनलोड तैयार होते ही फाइलें सर्वर से हमेशा के लिए मिटा दी जाती हैं।" },
    { "title": "कहीं भी उपयोग करें", "text": "कंप्यूटर, टैबलेट या मोबाइल के किसी भी मॉडर्न ब्राउज़र में तुरंत चलता है।" }
  ],
  "inside": {
    "kicker": "AI फाइल के अंदर क्या होता है",
    "h2": "AI कंटेंट को मार्क करने के दो तरीके",
    "p": "अधिकांश AI टूल्स अपने द्वारा बनाई गई सामग्री में अदृश्य निशान छोड़ते हैं।",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "पिक्सल में बुना हुआ अदृश्य संकेत",
        "html": "SynthID पिक्सल डेटा और वीडियो के हर फ्रेम में गहराई से एम्बेडेड होता है, जो क्रॉपिंग और कंप्रेशन से भी नहीं मिटता।"
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "मेटाडेटा में डिजिटल हस्ताक्षर",
        "html": "मेटाडेटा में एक डिजिटल रिकॉर्ड जो यह प्रमाणित करता है कि सामग्री AI द्वारा तैयार की गई है।"
      }
    ]
  },
  "how": {
    "kicker": "यह कैसे काम करता है",
    "h2": "चार आसान चरणों में SynthID हटाएं",
    "steps": [
      { "title": "फाइल अपलोड करें", "text": "Gemini, Imagen या Veo द्वारा बनाई गई इमेज या वीडियो चुनें।" },
      { "title": "अधिकारों की पुष्टि करें", "text": "चेकबॉक्स पर टिक करके पुष्टि करें कि आप फाइल प्रोसेस करने के लिए अधिकृत हैं।" },
      { "title": "स्वचालित प्रोसेसिंग", "text": "हमारा एल्गोरिदम फ्रेम-दर-फ्रेम वॉटरमार्क को निष्प्रभावी करता है।" },
      { "title": "डाउनलोड करें", "text": "पहले और बाद की तुलना करें और अपनी क्लीन फाइल डाउनलोड करें।" }
    ]
  },
  "plans": {
    "kicker": "प्लान",
    "h2": "अर्ली एक्सेस के दौरान पूरी तरह मुफ्त",
    "p": "सभी मुख्य सुविधाएं वर्तमान में बिना किसी शुल्क के उपलब्ध हैं।",
    "free": {
      "name": "मुफ्त",
      "note": "क्रेडिट कार्ड की जरूरत नहीं",
      "items": ["इमेज और वीडियो", "50 MB प्रति फाइल तक", "ओरिजिनल क्वालिटी", "बिना अकाउंट"],
      "cta": "फाइल प्रोसेस करें"
    },
    "pro": {
      "badge": "जल्द आ रहा है",
      "price": "क्रेडिट्स",
      "note": "मासिक या वार्षिक",
      "items": ["बड़ी फाइलें और लंबे वीडियो", "बैच प्रोसेसिंग", "प्राथमिकता कतार", "API एक्सेस"]
    }
  },
  "hood": {
    "kicker": "तकनीक और गोपनीयता",
    "h2": "सर्वोच्च गुणवत्ता और सुरक्षा के लिए निर्मित",
    "cards": [
      { "title": "प्रत्येक फ्रेम की सफाई", "text": "बिना किसी रुकावट के पूरे वीडियो का निर्बाध विश्लेषण।", "tag": "फ्रेम 1 → 240 · संपन्न" },
      { "title": "जीरो डेटा स्टोरेज", "text": "डाउनलोड के बाद अस्थायी फाइलें तुरंत नष्ट कर दी जाती हैं।", "tag": "0 फाइलें संग्रहीत" },
      { "title": "सटीक रेजोल्यूशन", "text": "मूल रेजोल्यूशन और फ्रेम दर पूरी तरह बरकरार रहती है।", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "यह किसके लिए है",
    "h2": "अपने स्वयं के AI मीडिया पर काम करने वाले क्रिएटर्स के लिए",
    "cards": [
      { "title": "कंटेंट क्रिएटर्स", "text": "आपने सामग्री बनाई है और आप बिना छिपे वॉटरमार्क वाली मूल फाइल चाहते हैं।" },
      { "title": "शोधकर्ता", "text": "डिजिटल वॉटरमार्क और स्टेग्नोग्राफी की मजबूती का परीक्षण करने के लिए।" },
      { "title": "डेवलपर्स", "text": "API के जरिए मीडिया प्रोसेसिंग पाइपलाइन को स्वचालित करने के लिए।" }
    ],
    "note": "केवल उन्हीं फाइलों को प्रोसेस करें जिन पर आपका कानूनी अधिकार है।"
  },
  "seo": [
    {
      "h2": "ऑनलाइन SynthID वॉटरमार्क कैसे हटाएं?",
      "html": "ऊपर दिए गए बॉक्स में अपनी फाइल ड्रॉप करें, अधिकारों की पुष्टि करें और वॉटरमार्क रहित फाइल पाने के लिए <strong>फाइल प्रोसेस करें</strong> पर क्लिक करें।"
    },
    { "h2": "कौन से AI टूल्स SynthID जोड़ते हैं?", "html": "Google अपने Gemini, Imagen और Veo जैसे उत्पादों में SynthID एम्बेड करता है।" },
    {
      "h2": "क्रॉप करने से SynthID क्यों नहीं हटता?",
      "html": "SynthID पिक्सल पैटर्न में व्यापक रूप से फैला होता है, इसलिए केवल क्रॉप करने या स्क्रीनशॉट लेने से यह नहीं हटता।"
    }
  ],
  "faqHeading": "अक्सर पूछे जाने वाले सवाल",
  "faqs": [
    { "q": "SynthID रिमूवर क्या है?", "a": "यह एक विशेष टूल है जो Google द्वारा AI फाइलों में जोड़े गए अदृश्य SynthID वॉटरमार्क को हटाता है।" },
    { "q": "क्या यह मुफ्त है?", "a": "हाँ, अर्ली एक्सेस के दौरान RemoveSynth पूरी तरह से मुफ्त है।" },
    { "q": "कौन से फाइल फॉर्मेट सपोर्टेड हैं?", "a": "PNG, JPG, WebP इमेज और MP4, WebM, MOV वीडियो।" },
    { "q": "क्या आप मेरी फाइलें स्टोर करते हैं?", "a": "नहीं, डाउनलोड पूरा होते ही फाइलें तुरंत हटा दी जाती हैं।" },
    { "q": "क्या स्क्रीनशॉट लेने से वॉटरमार्क हट जाता है?", "a": "नहीं, SynthID स्क्रीनशॉट के बाद भी मौजूद रहता है।" },
    { "q": "क्या RemoveSynth Google से संबंधित है?", "a": "नहीं, RemoveSynth एक स्वतंत्र थर्ड-पार्टी टूल है।" }
  ],
  "cta": { "h2": "SynthID रिमूवर अभी आज़माएं", "p": "मुफ्त, बिना साइन-अप, इमेज और वीडियो दोनों के लिए।", "button": "अभी SynthID हटाएं" }
})

# 29. BN (Bengali)
save("bn", "bn", {
  "lang": "bn",
  "title": "SynthID রিমুভার অনলাইন বিনামূল্যে: AI ছবি ও ভিডিও",
  "description": "AI দ্বারা তৈরি ছবি এবং ভিডিও থেকে অদৃশ্য SynthID জলছাপ এবং C2PA মেটাডেটা মুছে ফেলার জন্য বিনামূল্যে অনলাইন টুল। মূল কোয়ালিটি বজায় রেখে ব্রাউজারে ব্যবহার করুন।",
  "hero": {
    "eyebrow": "নিবন্ধনহীন · সম্পূর্ণ বিনামূল্যে · ছবি, ভিডিও ও অডিও",
    "h1Before": "বিনামূল্যে অনলাইন ",
    "h1Accent": "SynthID মুছুন",
    "h1After": " টুল",
    "lead": "AI-উত্পন্ন ছবি ও ভিডিও থেকে Google SynthID অদৃশ্য জলছাপ সরিয়ে ফেলুন। ফাইল আপলোড করুন, এক ক্লিকে প্রসেস করুন এবং মূল রেজোলিউশনে ডাউনলোড করুন।",
    "checks": ["ছবি, ভিডিও এবং অডিও", "ভিডিওর প্রতিটি ফ্রেম প্রসেস", "ডাউনলোডের সাথে সাথে ফাইল মুছে ফেলা হয়"],
    "worksWith": "যেসব প্ল্যাটফর্মের ফাইলের সাথে কাজ করে:"
  },
  "features": [
    { "title": "ছবি ও ভিডিও সাপোর্ট", "text": "PNG, JPG, WebP ছবি এবং MP4, WebM, MOV ভিডিওর জন্য একটিই সমাধান।" },
    { "title": "প্রতিটি ফ্রেম নিখুঁতভাবে পরিষ্কার", "text": "ভিডিওর ক্ষেত্রে কোনো অংশ বাদ না দিয়ে প্রতিটি ফ্রেম আলাদাভাবে প্রসেস করা হয়।" },
    { "title": "অরিজিনাল কোয়ালিটি", "text": "রেজোলিউশন, ফরম্যাট এবং ফ্রেম রেট সম্পূর্ণ অক্ষুণ্ণ থাকে।" },
    { "title": "অ্যাকাউন্টের প্রয়োজন নেই", "text": "ফাইলটি ড্রপ করুন এবং সরাসরি ব্যবহার শুরু করুন, কোনো সাইন-আপ দরকার নেই।" },
    { "title": "নিরাপদ ও ব্যক্তিগত", "text": "ডাউনলোড শেষ হওয়ার সাথে সাথে ফাইলগুলি স্থায়ীভাবে মুছে ফেলা হয়।" },
    { "title": "সব ডিভাইসে কার্যকর", "text": "কম্পিউটার, ট্যাবলেট বা ফোনের যেকোনো আধুনিক ব্রাউজারে চলে।" }
  ],
  "inside": {
    "kicker": "AI ফাইলের ভেতরে কী থাকে",
    "h2": "AI কনটেন্ট চিহ্নিত করার দুটি প্রধান মাধ্যম",
    "p": "বেশিরভাগ AI মডেল তাদের তৈরি মিডিয়াতে অদৃশ্য ট্রেসিং সংকেত যুক্ত করে।",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "পিক্সেলের ভেতরে বোনা অদৃশ্য সিগন্যাল",
        "html": "SynthID পিক্সেল ডেটা এবং ভিডিওর প্রতিটি ফ্রেমে প্রোথিত থাকে, যা ক্রপ বা কম্প্রেশনেও নষ্ট হয় না।"
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "মেটাডেটাতে ডিজিটাল ক্রিপ্টোগ্রাফিক রেকর্ড",
        "html": "মেটাডেটাতে সংরক্ষিত একটি ডিজিটাল প্রমাণপত্র যা নির্দেশ করে যে এটি AI দ্বারা তৈরি।"
      }
    ]
  },
  "how": {
    "kicker": "ব্যবহারের নিয়ম",
    "h2": "চারটি সহজ ধাপে SynthID দূর করুন",
    "steps": [
      { "title": "ফাইল আপলোড করুন", "text": "Gemini, Imagen বা Veo দ্বারা তৈরি যেকোনো ছবি বা ভিডিও নির্বাচন করুন।" },
      { "title": "স্বত্ব নিশ্চিত করুন", "text": "ফাইলটি ব্যবহারের আইনি অধিকার আছে তা নিশ্চিত করতে বক্সে টিক দিন।" },
      { "title": "স্বয়ংক্রিয় প্রসেসিং", "text": "আমাদের প্রযুক্তি ফ্রেম-বাই-ফ্রেম জলছাপ নিষ্ক্রিয় করে।" },
      { "title": "ডাউনলোড", "text": "আগের ও পরের অবস্থা তুলনা করুন এবং পরিষ্কার ফাইলটি ডাউনলোড করুন।" }
    ]
  },
  "plans": {
    "kicker": "পরিকল্পনা ও মূল্য",
    "h2": "আর্লি অ্যাক্সেস পর্বে সম্পূর্ণ বিনামূল্যে",
    "p": "বর্তমানে সমস্ত ফিচার কোনো চার্জ ছাড়াই উন্মুক্ত রয়েছে।",
    "free": {
      "name": "বিনামূল্যে",
      "note": "কার্ডের প্রয়োজন নেই",
      "items": ["ছবি এবং ভিডিও", "প্রতি ফাইলে ৫০ MB পর্যন্ত", "মূল গুণমান বজায় থাকে", "কোনো অ্যাকাউন্ট দরকার নেই"],
      "cta": "ফাইল প্রসেস করুন"
    },
    "pro": {
      "badge": "শীঘ্রই আসছে",
      "price": "ক্রেডিট",
      "note": "মাসিক বা বার্ষিক",
      "items": ["বৃহত্তর ফাইল এবং দীর্ঘ ভিডিও", "ব্যাচ প্রসেসিং", "অগ্রাধিকার কিউ", "API অ্যাক্সেস"]
    }
  },
  "hood": {
    "kicker": "প্রযুক্তি ও গোপনীয়তা",
    "h2": "সর্বোচ্চ মান ও সুরক্ষার নিশ্চয়তা",
    "cards": [
      { "title": "ফ্রেম-বাই-ফ্রেম ক্লিনিং", "text": "ভিডিওর প্রথম থেকে শেষ পর্যন্ত সম্পূর্ণ অংশ পরিষ্কার করা হয়।", "tag": "ফ্রেম ১ → ২৪০ · সম্পন্ন" },
      { "title": "শূন্য তথ্য সংরক্ষণ", "text": "ডাউনলোড প্রস্তুত হওয়ার পর ফাইলগুলি সার্ভার থেকে মুছে ফেলা হয়।", "tag": "সংরক্ষিত ফাইল ০" },
      { "title": "গুণগত মান অপরিবর্তিত", "text": "রেজোলিউশন এবং এফপিএস অক্ষুণ্ণ থাকে।", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "ব্যবহারকারী",
    "h2": "যারা নিজেদের তৈরি AI মিডিয়া নিয়ে কাজ করেন",
    "cards": [
      { "title": "কনটেন্ট ক্রিয়েটর", "text": "আপনি নিজেই ছবি বা ভিডিও তৈরি করেছেন এবং একটি পরিষ্কার ফাইল চান।" },
      { "title": "গবেষক", "text": "ডিজিটাল ওয়াটারমার্কের স্থায়িত্ব ও নিরাপত্তা বিশ্লেষণের জন্য।" },
      { "title": "ডেভেলপার", "text": "API-এর মাধ্যমে স্বয়ংক্রিয় মিডিয়া প্রসেসিং পাইপলাইন তৈরি করতে।" }
    ],
    "note": "কেবলমাত্র এমন ফাইল প্রসেস করুন যার বৈধ অধিকার আপনার রয়েছে।"
  },
  "seo": [
    {
      "h2": "কীভাবে অনলাইনে SynthID জলছাপ মুছবেন?",
      "html": "উপরের বক্সে ফাইলটি ড্রপ করুন, অনুমতির ঘরে টিক দিন এবং পরিষ্কার ফাইল ডাউনলোড করতে <strong>ফাইল প্রসেস করুন</strong>-এ ক্লিক করুন।"
    },
    { "h2": "কোন AI টুলগুলোতে SynthID থাকে?", "html": "Google-এর Gemini, Imagen এবং Veo-তে SynthID অন্তর্ভুক্ত থাকে।" },
    {
      "h2": "ক্রপ করলে কেন SynthID মোছে না?",
      "html": "SynthID পুরো পিক্সেল জুড়েই বিন্যস্ত থাকে, তাই ক্রপ বা স্ক্রিনশট নিলেও এটি থেকে যায়।"
    }
  ],
  "faqHeading": "সাধারণ জিজ্ঞাসা",
  "faqs": [
    { "q": "SynthID রিমুভার কী?", "a": "এটি একটি বিশেষ টুল যা AI ফাইলে থাকা Google-এর অদৃশ্য SynthID জলছাপ মুছে দেয়।" },
    { "q": "এটি কি সত্যিই বিনামূল্যে?", "a": "হ্যাঁ, আর্লি অ্যাক্সেস চলাকালীন এটি ১০০% বিনামূল্যে।" },
    { "q": "কোন ফরম্যাটগুলো সমর্থিত?", "a": "PNG, JPG, WebP ছবি এবং MP4, WebM, MOV ভিডিও।" },
    { "q": "আপনারা কি ফাইল জমা রাখেন?", "a": "না, কাজ শেষ হওয়ার সাথে সাথে ফাইল সম্পূর্ণরূপে মুছে ফেলা হয়।" },
    { "q": "স্ক্রিনশট নিলে কি জলছাপ চলে যায়?", "a": "না, স্ক্রিনশট নিলেও SynthID মুছে যায় না।" },
    { "q": "RemoveSynth কি Google-এর অংশ?", "a": "না, RemoveSynth সম্পূর্ণ স্বাধীন একটি টুল।" }
  ],
  "cta": { "h2": "SynthID রিমুভার এখনই ব্যবহার করে দেখুন", "p": "বিনামূল্যে, রেজিস্ট্রেশন ছাড়া, ছবি ও ভিডিওর জন্য।", "button": "SynthID এখনই মুছুন" }
})

# 30. AR (Arabic - RTL)
save("ar", "ar", {
  "lang": "ar",
  "title": "مزيل SynthID عبر الإنترنت مجاناً: للصور والفيديو بالذكاء الاصطناعي",
  "description": "أداة مجانية عبر الإنترنت لإزالة العلامة المائية غير المرئية SynthID وبيانات C2PA الوصفية من الصور ومقاطع الفيديو المنشأة بالذكاء الاصطناعي مباشرة في المتصفح دون فقدان الجودة.",
  "hero": {
    "eyebrow": "بدون تسجيل · مجاني 100% · صور وفيديو وصوت",
    "h1Before": "أداة ",
    "h1Accent": "إزالة SynthID",
    "h1After": " المجانية عبر الإنترنت",
    "lead": "قم بإزالة العلامة المائية غير المرئية SynthID من الصور ومقاطع الفيديو المنشأة بواسطة الذكاء الاصطناعي. ارفع ملفك وعالجه بنقرة واحدة وحمله بجودته الأصلية.",
    "checks": ["يدعم الصور والفيديو والصوت", "معالجة شاملة لكل إطار فيديو", "حذف الملفات نهائياً بعد المعالجة"],
    "worksWith": "متوافق مع الملفات الناتجة عن:"
  },
  "features": [
    { "title": "الصور والفيديوهات", "text": "أداة موحدة لصور PNG وJPG وWebP ومقاطع MP4 وWebM وMOV." },
    { "title": "كل إطار بدقة", "text": "في الفيديو، يتم تنظيف المقطع بالكامل إطاراً تلو الآخر دون أي تخطي." },
    { "title": "جودة أصلية كاملة", "text": "الدقة ومعدل الإطارات والألوان تبقى مطابقة تماماً للأصل." },
    { "title": "بدون أي تسجيل", "text": "اسحب الملف وابدأ فوراً دون الحاجة لإنشاء أي حساب." },
    { "title": "خصوصية تامة ومطلقة", "text": "يتم تدمير الملفات المؤقتة فور إتمام عملية التنزيل." },
    { "title": "يعمل في كل مكان", "text": "يعمل بسلاسة على المتصفحات الحديثة في الحاسوب والأجهزة اللوحية والهواتف." }
  ],
  "inside": {
    "kicker": "ماذا يوجد داخل ملفات الذكاء الاصطناعي",
    "h2": "طريقتان لتتبع وتحديد وسائط الذكاء الاصطناعي",
    "p": "تدمج معظم منصات الذكاء الاصطناعي الحديثة علامات رقمية غير مرئية للعين المجردة.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "إشارة خفية مدمجة داخل البكسلات",
        "html": "تُدمج تقنية SynthID في بيانات البكسلات وإطارات الفيديو وتصمد أمام القص والفلاتر والضغط."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "سجل توثيق رقمي مشفر في البيانات الوصفية",
        "html": "شهادة رقمية مشفرة في الميتاداتا تشير إلى أن المحتوى تم إنشاؤه بواسطة نموذج ذكاء اصطناعي."
      }
    ]
  },
  "how": {
    "kicker": "طريقة الاستخدام",
    "h2": "تخلص من علامة SynthID في أربع خطوات",
    "steps": [
      { "title": "أفلت ملفك هنا", "text": "اختر صورة أو فيديو من Gemini أو Imagen أو Veo." },
      { "title": "تأكيد الحقوق", "text": "حدد المربع لتأكيد امتلاكك للحق القانوني لمعالجة الملف." },
      { "title": "معالجة ذكية وفورية", "text": "تقوم الخوارزمية بتحييد العلامة المائية إطاراً بإطار." },
      { "title": "تنزيل الملف", "text": "قارن النتيجة ونزّل نسختك النظيفة بالصيغة الأصلية." }
    ]
  },
  "plans": {
    "kicker": "الباقات",
    "h2": "مجاني تماماً خلال فترة الوصول المبكر",
    "p": "جميع الميزات والوظائف متاحة حالياً دون أي رسوم.",
    "free": {
      "name": "مجاني",
      "note": "لا يتطلب بطاقة ائتمان",
      "items": ["الصور والفيديوهات", "حتى 50 ميغابايت لكل ملف", "جودة أصلية بدون فقدان", "بدون حساب مستخدم"],
      "cta": "معالجة ملف الآن"
    },
    "pro": {
      "badge": "قريباً",
      "price": "نقاط رصيد",
      "note": "شهري أو سنوي",
      "items": ["ملفات أكبر وفيديوهات أطول", "معالجة دفعات متعددة", "أولوية في طابور المعالجة", "واجهة برمجية API"]
    }
  },
  "hood": {
    "kicker": "الهندسة والخصوصية",
    "h2": "مصمم لتحقيق أعلى دقة مع حماية الأمان الشخصي",
    "cards": [
      { "title": "معالجة شاملة للإطارات", "text": "يتم مسح وتنظيف الفيديو كاملاً دون استثناء أي لقطة.", "tag": "الإطار 1 ← 240 · تم بنجاح" },
      { "title": "انعدام التخزين", "text": "الملفات المؤقتة تُحذف نهائياً بمجرد إتمام التحميل.", "tag": "0 ملف مخزن" },
      { "title": "دقة مطابقة للأصل", "text": "تبقى الأبعاد ومعدل الإطارات كما هي تماماً.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "الفئات المستفيدة",
    "h2": "لكل من ينشئ ويتعامل مع محتوى الذكاء الاصطناعي الخاص به",
    "cards": [
      { "title": "صناع المحتوى", "text": "قمت بتوليد العمل الإبداعي بنفسك وتريد حفظ نسختك الأصلية دون علامات مخفية." },
      { "title": "الباحثون الرقميون", "text": "لاختبار متانة العلامات المائية وعلم إخفاء البيانات." },
      { "title": "المطورون", "text": "أتمتة مسارات معالجة الوسائط عبر واجهة برمجة التطبيقات." }
    ],
    "note": "يرجى معالجة المحتوى الذي تملكه أو لديك إذن صريح باستخدامه فقط."
  },
  "seo": [
    {
      "h2": "كيفية إزالة علامة SynthID المائية عبر الإنترنت؟",
      "html": "اسحب ملفك إلى المربع أعلاه، وافق على إقرار الملكية، ثم انقر على <strong>معالجة الملف</strong> لتحميل النسخة الخالية من العلامة المائية."
    },
    { "h2": "ما هي أدوات الذكاء الاصطناعي التي تضيف SynthID؟", "html": "تضيف Google علامة SynthID إلى مخرجات أدواتها مثل تطبيق Gemini وImagen وVeo." },
    {
      "h2": "لماذا لا يؤدي القص إلى إزالة SynthID؟",
      "html": "علامة SynthID منتشرة عبر شبكة البكسلات بأكملها، وبالتالي فإن القص أو التقاط الشاشة لا يمكنه إزالتها."
    }
  ],
  "faqHeading": "الأسئلة الشائعة",
  "faqs": [
    { "q": "ما هي أداة إزالة SynthID؟", "a": "هي أداة مخصصة لتحييد وإزالة العلامة المائية الرقمية غير المرئية SynthID التابعة لـ Google من الوسائط." },
    { "q": "هل الأداة مجانية؟", "a": "نعم، الأداة مجانية بنسبة 100% خلال مرحلة الوصول المبكر الحالية." },
    { "q": "ما هي صيغ الملفات المدعومة؟", "a": "الصور بصيغ PNG وJPG وWebP، ومقاطع الفيديو بصيغ MP4 وWebM وMOV." },
    { "q": "هل تحتفظون بملفاتي؟", "a": "كلا، يتم حذف جميع الملفات نهائياً وفورياً بعد اكتمال التنزيل." },
    { "q": "هل لقطة الشاشة تزيل العلامة؟", "a": "لا، تقنية SynthID مصممة لمقاومة لقطات الشاشة وإعادة الحفظ." },
    { "q": "هل يتبع RemoveSynth لشركة Google؟", "a": "لا، RemoveSynth هو مشروع مستقل تماماً ولا يتبع لأي جهة خارجية." }
  ],
  "cta": { "h2": "جرب مزيل SynthID الآن", "p": "مجاني، سريع، وبدون تسجيل للصور ومقاطع الفيديو.", "button": "إزالة SynthID الآن" }
})

# 31. HE (Hebrew - RTL)
save("he", "he", {
  "lang": "he",
  "title": "הסרת SynthID אונליין בחינם: תמונות ווידאו מבוססי AI",
  "description": "כלי מקוון חינמי להסרת סימן המים הבלתי נראה SynthID ומטא-נתוני C2PA מתמונות וסרטוני AI ישירות בדפדפן באיכות מקורית ללא העלאה לשרת.",
  "hero": {
    "eyebrow": "ללא הרשמה · חינם לחלוטין · תמונות, וידאו ואודיו",
    "h1Before": "כלי חינמי עבור ",
    "h1Accent": "הסרת SynthID",
    "h1After": " אונליין",
    "lead": "הסירו את סימן המים הבלתי נראה SynthID מתמונות וסרטונים שנוצרו על ידי בינה מלאכותית. העלו את הקובץ, עבדו בלחיצה אחת והורידו באיכות מקורית מלאה.",
    "checks": ["תמיכה בתמונות, וידאו ואודיו", "עיבוד של כל פריים בווידאו", "מחיקת קבצים מידית לאחר ההורדה"],
    "worksWith": "תואם קבצים שנוצרו באמצעות:"
  },
  "features": [
    { "title": "תמונות וסרטונים", "text": "כלי אחד עבור תמונות PNG, JPG, WebP וסרטוני MP4, WebM, MOV." },
    { "title": "כל פריים בנפרד", "text": "בווידאו כל הקליפ מעובד פריים אחר פריים ללא דילוג על אף תמונה." },
    { "title": "איכות מקורית מלאה", "text": "הרזולוציה, הפורמט וקצב הפריימים נשמרים ללא כל פגיעה באיכות." },
    { "title": "ללא צורך בהרשמה", "text": "גררו את הקובץ והתחילו מיד מבלי לפתוח חשבון." },
    { "title": "פרטיות מרבית", "text": "הקבצים נמחקים לצמיתות מיד עם סיום תהליך ההורדה." },
    { "title": "עובד בכל מכשיר", "text": "פועל בכל דפדפן מודרני במחשב, בטאבלט ובסמארטפון." }
  ],
  "inside": {
    "kicker": "מה נמצא בתוך קובץ AI",
    "h2": "שתי דרכים שבהן תכני AI מסומנים",
    "p": "רוב כלי הבינה המלאכותית מטמיעים חותמות שאינן נראות לעין האנושית.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "אות בלתי נראה המוטמע בפיקסלים",
        "html": "SynthID שזור בתוך נתוני הפיקסלים ובכל פריים של וידאו, ועמיד בפני חיתוך ודחיסה."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "חתימה מוצפנת במטא-דאטה",
        "html": "תעודה דיגיטלית מאובטחת במטא-נתונים המעידה כי הקובץ נוצר באמצעות AI."
      }
    ]
  },
  "how": {
    "kicker": "איך זה עובד",
    "h2": "הסירו את סימן המים SynthID בארבעה שלבים",
    "steps": [
      { "title": "גררו את הקובץ", "text": "בחרו תמונה או סרטון שנוצרו ב-Gemini, Imagen או Veo." },
      { "title": "אישור זכויות", "text": "סמנו את התיבה כדי לאשר שיש לכם הרשאה לעבד את הקובץ." },
      { "title": "עיבוד אוטומטי", "text": "האלגוריתם מנטרל את סימן המים פריים אחר פריים." },
      { "title": "הורדה", "text": "השוו בין לפני ואחרי והורידו את הקובץ הנקי בפורמט המקורי." }
    ]
  },
  "plans": {
    "kicker": "מסלולים",
    "h2": "חינם לחלוטין בתקופת ההשקה המוקדמת",
    "p": "כל התכונות זמינות כעת לשימוש חופשי ללא תשלום.",
    "free": {
      "name": "חינם",
      "note": "ללא כרטיס אשראי",
      "items": ["תמונות וסרטונים", "עד 50 מגה-בייט לקובץ", "איכות מקורית", "ללא צורך בחשבון"],
      "cta": "עיבוד קובץ"
    },
    "pro": {
      "badge": "בקרוב",
      "price": "קרדיטים",
      "note": "חודשי או שנתי",
      "items": ["קבצים גדולים וסרטונים ארוכים", "עיבוד אצווה מרובה", "תור עדיפות מהיר", "גישת API"]
    }
  },
  "hood": {
    "kicker": "טכנולוגיה ופרטיות",
    "h2": "נבנה עבור איכות בלתי מתפשרת וסודיות מלאה",
    "cards": [
      { "title": "עיבוד כל פריים", "text": "כל הסרטון מעובד בצורה רציפה מבלי לדלג על אף רגע.", "tag": "פריים 1 ← 240 · הושלם" },
      { "title": "אפס שמירת מידע", "text": "הקבצים הזמניים מושמדים מיד לאחר ההורדה.", "tag": "0 קבצים שמורים" },
      { "title": "שמירה על האיכות", "text": "הרזולוציה וקצב הפריימים נשארים ללא שינוי.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "קהל יעד",
    "h2": "עבור יוצרים שעובדים עם מדיה שנוצרה על ידם ב-AI",
    "cards": [
      { "title": "יוצרי תוכן", "text": "יצרתם את היצירה ואתם מעוניינים בקובץ נקי ללא סמנים נסתרים." },
      { "title": "חוקרים", "text": "בדיקת שרידות של סימני מים דיגיטליים וסטגנוגרפיה." },
      { "title": "מפתחים", "text": "אוטומציה של צינורות עיבוד מדיה באמצעות API." }
    ],
    "note": "עבדו אך ורק קבצים שיש לכם זכויות חוקיות עליהם."
  },
  "seo": [
    {
      "h2": "כיצד להסיר את סימן המים SynthID אונליין?",
      "html": "גררו את הקובץ לתיבה שלמעלה, אשרו את ההרשאה ולחצו על <strong>עיבוד קובץ</strong> כדי להוריד את הגרסה הנקייה."
    },
    { "h2": "אילו כלי בינה מלאכותית מוסיפים SynthID?", "html": "חברת Google מטמיעה את SynthID במוצרים כמו Gemini, Imagen ו-Veo." },
    {
      "h2": "מדוע חיתוך תמונה לא מסיר את SynthID?",
      "html": "הסימן SynthID מפוזר על פני כל רשת הפיקסלים, ולכן חיתוך או צילום מסך אינם מסירים אותו."
    }
  ],
  "faqHeading": "שאלות נפוצות",
  "faqs": [
    { "q": "מהו כלי להסרת SynthID?", "a": "תוכנה ייעודית לנטרול סימן המים הבלתי נראה SynthID של Google מקבצי מדיה מבוססי AI." },
    { "q": "האם הכלי חינמי?", "a": "כן, במהלך תקופת הגישה המוקדמת השימוש הוא 100% בחינם." },
    { "q": "באילו פורמטים יש תמיכה?", "a": "תמונות PNG, JPG, WebP וסרטוני MP4, WebM, MOV." },
    { "q": "האם הקבצים שלי נשמרים?", "a": "לא, כל הקבצים נמחקים באופן בלתי הפיך מיד לאחר סיום ההורדה." },
    { "q": "האם צילום מסך מסיר את הסימן?", "a": "לא, SynthID תוכנן לשרוד גם צילומי מסך והמרות." },
    { "q": "האם RemoveSynth שייך ל-Google?", "a": "לא, RemoveSynth הוא כלי עצמאי לחלוטין של צד שלישי." }
  ],
  "cta": { "h2": "נסו את מסיר ה-SynthID עכשיו", "p": "בחינם, במהירות וללא צורך בהרשמה.", "button": "הסרת SynthID כעת" }
})

# 32. SW (Swahili)
save("sw", "sw", {
  "lang": "sw",
  "title": "Ondoa SynthID Mtandaoni Bure: Picha na Video za AI",
  "description": "Zana ya bure ya mtandaoni ya kuondoa alama isiyoonekana ya SynthID na metadata ya C2PA kutoka kwa picha na video za AI moja kwa moja kwenye kivinjari bila kupoteza ubora.",
  "hero": {
    "eyebrow": "Bila kujisajili · Bure 100% · Picha, video na sauti",
    "h1Before": "Bure mtandaoni ",
    "h1Accent": "ondoa SynthID",
    "h1After": " zana",
    "lead": "Ondoa alama isiyoonekana ya SynthID kutoka kwa picha na video zilizotengenezwa na AI. Pakia faili yako, kamilisha kwa kubofya mara moja na upakue katika ubora asilia.",
    "checks": ["Picha, video na sauti", "Kila fremu ya video", "Faili hufutwa mara moja baada ya kuchakatwa"],
    "worksWith": "Inafanya kazi na faili kutoka"
  },
  "features": [
    { "title": "Picha na video", "text": "Zana moja kwa PNG, JPG, WebP na video za MP4, WebM, MOV." },
    { "title": "Kila fremu", "text": "Kwenye video, klipu nzima inasafishwa fremu kwa fremu bila kuruka." },
    { "title": "Ubora asilia", "text": "Azimio, muundo na kiwango cha fremu vinabaki vile vile." },
    { "title": "Bila kujiandikisha", "text": "Weka faili na uanze mara moja bila kuhitaji kufungua akaunti." },
    { "title": "Faragha kamili", "text": "Faili zilizopakiwa hufutwa kabisa mara tu upakuaji unapokamilika." },
    { "title": "Inafanya kazi popote", "text": "Inafanya kazi kwenye kivinjari chochote cha kisasa kwenye kompyuta au simu." }
  ],
  "inside": {
    "kicker": "Kilicho ndani ya faili ya AI",
    "h2": "Njia mbili ambazo maudhui ya AI huwekewa alama",
    "p": "Zana nyingi za AI huweka alama zisizoonekana kwa macho kwenye kazi wanazounda.",
    "cards": [
      {
        "kicker": "Google · SynthID",
        "title": "Ishara isiyoonekana ndani ya pikseli",
        "html": "SynthID imefumwa kwenye data ya pikseli na kila fremu ya video, na inahimili kukatwa na kubanwa."
      },
      {
        "kicker": "C2PA · Content Credentials",
        "title": "Sahihi ya kidijitali katika metadata",
        "html": "Rekodi iliyosimbwa kwenye metadata inayothibitisha kuwa faili ilitengenezwa na AI."
      }
    ]
  },
  "how": {
    "kicker": "Jinsi inavyofanya kazi",
    "h2": "Ondoa SynthID kwa hatua nne rahisi",
    "steps": [
      { "title": "Weka faili yako", "text": "Chagua picha au video kutoka kwa Gemini, Imagen au Veo." },
      { "title": "Thibitisha haki zako", "text": "Weka alama kwenye kisanduku kuthibitisha una ruhusa ya kuchakata faili." },
      { "title": "Usafishaji wa kiotomatiki", "text": "Kanuni zetu hupunguza na kuondoa alama fremu kwa fremu." },
      { "title": "Pakua", "text": "Linganisha kabla na baada kisha pakua faili safi katika umbizo asili." }
    ]
  },
  "plans": {
    "kicker": "Mipango",
    "h2": "Bure kabisa wakati wa ufikiaji wa mapema",
    "p": "Vipengele vyote vinapatikana bila malipo yoyote kwa sasa.",
    "free": {
      "name": "Bure",
      "note": "Hakuna kadi inayohitajika",
      "items": ["Picha na video", "Hadi MB 50 kwa faili", "Ubora asilia", "Hakuna akaunti inayohitajika"],
      "cta": "Chakata faili"
    },
    "pro": {
      "badge": "Inakuja hivi karibuni",
      "price": "Mikopo",
      "note": "Kila mwezi au mwaka",
      "items": ["Faili kubwa na video ndefu", "Uchakataji wa kundi", "Foleni ya kipaumbele", "Ufikiaji wa API"]
    }
  },
  "hood": {
    "kicker": "Teknolojia na Faragha",
    "h2": "Imejengwa kwa ubora wa juu na usiri kamili",
    "cards": [
      { "title": "Kila fremu inachakatwa", "text": "Video inashughulikiwa mfululizo bila kuruka fremu yoyote.", "tag": "Fremu 1 → 240 · imekamilika" },
      { "title": "Hakuna data inayohifadhiwa", "text": "Faili za muda zinafutwa mara tu baada ya kupakua.", "tag": "Faili 0 zilizohifadhiwa" },
      { "title": "Ubora thabiti", "text": "Azimio na fremu kwa sekunde hubaki sawa na asili.", "tag": "1080×1920 · 30fps" }
    ]
  },
  "who": {
    "kicker": "Inafaa nani",
    "h2": "Kwa waundaji wanaofanya kazi na maudhui yao ya AI",
    "cards": [
      { "title": "Waundaji wa maudhui", "text": "Umeunda picha au video na unataka faili asilia bila alama zilizofichwa." },
      { "title": "Watafiti", "text": "Kupima uimara wa alama za kidijitali na steganografia." },
      { "title": "Wasanidi programu", "text": "Kuunganisha mifumo ya kuchakata vyombo vya habari kupitia API." }
    ],
    "note": "Tafadhali chakata tu faili unazomiliki au una idhini nazo."
  },
  "seo": [
    {
      "h2": "Jinsi ya kuondoa alama ya SynthID mtandaoni?",
      "html": "Weka faili yako kwenye eneo hapo juu, thibitisha haki zako, na ubofye <strong>Chakata faili</strong> ili kupakua toleo safi."
    },
    { "h2": "Ni zana zipi za AI zinazoongeza SynthID?", "html": "Google inaongeza SynthID kwenye Gemini, Imagen na Veo." },
    {
      "h2": "Kwa nini kukata picha hakutoi SynthID?",
      "html": "SynthID imetawanyika kwenye pikseli zote, kwa hivyo kukata picha au picha ya skrini haiwezi kuiondoa."
    }
  ],
  "faqHeading": "Maswali Yanayoulizwa Mara kwa Mara",
  "faqs": [
    { "q": "Kiondoa SynthID ni nini?", "a": "Ni zana maalum ya kuondoa alama isiyoonekana ya SynthID ya Google kwenye picha na video za AI." },
    { "q": "Je, ni bure?", "a": "Ndiyo, katika kipindi hiki cha ufikiaji wa mapema ni bure 100%." },
    { "q": "Ni miundo gani inayoungwa mkono?", "a": "Picha za PNG, JPG, WebP na video za MP4, WebM, MOV." },
    { "q": "Je, mnahifadhi faili zangu?", "a": "Hapana, faili zote hufutwa kabisa mara tu baada ya upakuaji." },
    { "q": "Je, picha ya skrini inaondoa SynthID?", "a": "Hapana, SynthID imeundwa kudumu hata kwenye picha ya skrini." },
    { "q": "Je, RemoveSynth inamilikiwa na Google?", "a": "Hapana, RemoveSynth ni zana huru ya mtu mwingine." }
  ],
  "cta": { "h2": "Jaribu kiondoa SynthID sasa", "p": "Bure, haraka na bila kujiandikisha.", "button": "Ondoa SynthID sasa" }
})

print("Batch 4 (South Asia & Middle East/Africa: hi, bn, ar, he, sw) completed.")
