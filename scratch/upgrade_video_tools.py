import os
import re

pages_dir = r'd:\Nitin\removesynth\apps\removesynth\src\pages'

video_tools = {
    'dola-ai.astro': {
        'title': 'Remove Dola AI Watermark: Clean Dola Video Tags Free',
        'desc': 'Remove Dola AI video watermarks, C2PA manifests, and metadata tags from generated clips. Free in-browser video cleaner with no re-encoding or quality loss.',
        'app_name': 'Dola AI Watermark Remover',
        'url_slug': 'dola-ai',
    },
    'higgsfield.astro': {
        'title': 'Remove Higgsfield Watermark: Clean AI Video Free',
        'desc': 'Remove Higgsfield AI video watermarks, C2PA Content Credentials, and camera metadata tags. Free in-browser MP4 cleaner with zero re-encoding or quality loss.',
        'app_name': 'Higgsfield AI Watermark Remover',
        'url_slug': 'higgsfield',
    },
    'remove-higgsfield-watermark.astro': {
        'title': 'Remove Higgsfield Watermark Online: Clean Video Free',
        'desc': 'Clean Higgsfield AI video watermarks, C2PA manifests, and metadata tags from your MP4 clips. 100% in-browser video sanitizer with zero cloud server uploads.',
        'app_name': 'Higgsfield Video Sanitizer',
        'url_slug': 'remove-higgsfield-watermark',
    },
    'pika-ai.astro': {
        'title': 'Remove Pika AI Watermark: Clean Pika 2.0 & 2.1 Free',
        'desc': 'Remove Pika AI 2.0 and 2.1 video watermarks, C2PA provenance manifests, and user metadata. Free client-side MP4 cleaner with zero re-encoding and full privacy.',
        'app_name': 'Pika AI Watermark Remover',
        'url_slug': 'pika-ai',
    },
    'remove-pika-watermark.astro': {
        'title': 'Remove Pika Watermark Online: Pika Video Cleaner Free',
        'desc': 'Clean Pika AI video watermarks, C2PA manifests, and user metadata from generated MP4 files. 100% in-browser video sanitizer with zero cloud server uploads.',
        'app_name': 'Pika Video Sanitizer',
        'url_slug': 'remove-pika-watermark',
    },
    'pixverse-ai.astro': {
        'title': 'Remove PixVerse Watermark: Clean PixVerse Video Free',
        'desc': 'Remove PixVerse AI video watermarks, C2PA manifests, and QuickTime metadata tags. Free client-side video cleaner with zero re-encoding and zero server uploads.',
        'app_name': 'PixVerse AI Watermark Remover',
        'url_slug': 'pixverse-ai',
    },
    'remove-pixverse-watermark.astro': {
        'title': 'Remove PixVerse Watermark Online: Clean Video Free',
        'desc': 'Clean PixVerse AI video watermarks, C2PA manifests, and user metadata tags from MP4 clips. 100% in-browser video sanitizer with zero cloud server uploads.',
        'app_name': 'PixVerse Video Sanitizer',
        'url_slug': 'remove-pixverse-watermark',
    },
    'runway-ai.astro': {
        'title': 'Remove Runway Watermark: Clean Gen-3 & Gen-2 Video',
        'desc': 'Remove Runway Gen-3 and Gen-2 video watermarks, C2PA manifests, and camera metadata tags. Free in-browser MP4 cleaner with zero re-encoding and full privacy.',
        'app_name': 'Runway AI Watermark Remover',
        'url_slug': 'runway-ai',
    },
    'remove-runway-watermark.astro': {
        'title': 'Remove Runway Watermark Online: Gen-3 Video Cleaner',
        'desc': 'Clean Runway Gen-3 and Gen-2 video watermarks, C2PA manifests, and user metadata from MP4 clips. 100% in-browser sanitizer with zero cloud server uploads.',
        'app_name': 'Runway Video Sanitizer',
        'url_slug': 'remove-runway-watermark',
    },
    'sora-ai.astro': {
        'title': 'Remove Sora AI Watermark: Clean OpenAI Video Free',
        'desc': 'Remove OpenAI Sora video watermarks, C2PA Content Credentials, and provenance manifests. Free in-browser MP4 cleaner with zero re-encoding and full privacy.',
        'app_name': 'OpenAI Sora Watermark Remover',
        'url_slug': 'sora-ai',
    },
    'remove-sora-watermark.astro': {
        'title': 'Remove Sora Watermark Online: Sora Video Sanitizer',
        'desc': 'Clean OpenAI Sora video watermarks, C2PA manifests, and user metadata tags from MP4 clips. 100% in-browser video sanitizer with zero cloud server uploads.',
        'app_name': 'Sora Video Sanitizer',
        'url_slug': 'remove-sora-watermark',
    },
    'veo-ai.astro': {
        'title': 'Remove Google Veo Watermark: Clean Veo 2 Video Free',
        'desc': 'Remove Google Veo and Veo 2 video watermarks, SynthID signatures, and C2PA manifests. Free in-browser MP4 cleaner with zero re-encoding and full privacy.',
        'app_name': 'Google Veo Watermark Remover',
        'url_slug': 'veo-ai',
    },
    'remove-veo-watermark.astro': {
        'title': 'Remove Google Veo Watermark Online: Veo 2 Cleaner',
        'desc': 'Clean Google Veo and Veo 2 video SynthID signatures, C2PA manifests, and metadata tags from MP4 clips. 100% in-browser sanitizer with zero server uploads.',
        'app_name': 'Google Veo Sanitizer',
        'url_slug': 'remove-veo-watermark',
    },
    'kling-ai.astro': {
        'title': 'Remove Kling AI Watermark: Clean Kling Video Free',
        'desc': 'Remove Kling AI 1.0, 1.5, and 2.0 video watermarks, C2PA manifests, and camera metadata tags. Free in-browser MP4 cleaner with zero re-encoding loss.',
        'app_name': 'Kling AI Watermark Remover',
        'url_slug': 'kling-ai',
    },
    'hailuo-ai.astro': {
        'title': 'Remove Hailuo AI Watermark: Clean MiniMax Video Free',
        'desc': 'Remove MiniMax Hailuo AI video watermarks, C2PA manifests, and user metadata tags. Free in-browser MP4 video cleaner with zero re-encoding or quality loss.',
        'app_name': 'Hailuo AI Watermark Remover',
        'url_slug': 'hailuo-ai',
    },
    'luma-dream-machine.astro': {
        'title': 'Remove Luma Dream Machine Watermark: Clean Ray-2 Free',
        'desc': 'Remove Luma Dream Machine and Ray-2 video watermarks, C2PA manifests, and user metadata tags. Free in-browser video cleaner with zero re-encoding loss.',
        'app_name': 'Luma Dream Machine Watermark Remover',
        'url_slug': 'luma-dream-machine',
    },
    'viggle-ai.astro': {
        'title': 'Remove Viggle AI Watermark: Clean Character Dance Free',
        'desc': 'Remove Viggle AI video watermarks, character dance metadata, and C2PA manifests from MP4 clips. Free in-browser video cleaner with zero re-encoding loss.',
        'app_name': 'Viggle AI Watermark Remover',
        'url_slug': 'viggle-ai',
    },
    'wan-ai.astro': {
        'title': 'Remove Wan 2.1 Watermark: Clean Alibaba Wan Video Free',
        'desc': 'Remove Alibaba Wan 2.1 AI video watermarks, C2PA provenance manifests, and camera tags. Free in-browser MP4 video cleaner with zero re-encoding or quality loss.',
        'app_name': 'Alibaba Wan 2.1 Watermark Remover',
        'url_slug': 'wan-ai',
    },
    'seedance.astro': {
        'title': 'Remove Seedance Watermark: Clean 2.0, 2.1 & 2.2 Video',
        'desc': 'Remove Seedance 2.0, 2.1, and 2.2 video watermarks, C2PA manifests, and user metadata tags. Free in-browser MP4 cleaner with zero re-encoding or quality loss.',
        'app_name': 'Seedance Watermark Remover',
        'url_slug': 'seedance',
    },
    'seedance-2-0.astro': {
        'title': 'Remove Seedance 2.0 Watermark: Clean Video Free',
        'desc': 'Remove Seedance 2.0 video watermarks, C2PA manifests, and camera metadata tags from MP4 clips. Free in-browser video cleaner with zero re-encoding loss.',
        'app_name': 'Seedance 2.0 Watermark Remover',
        'url_slug': 'seedance-2-0',
    },
    'seedance-2-1.astro': {
        'title': 'Remove Seedance 2.1 Watermark: Clean Video Free',
        'desc': 'Remove Seedance 2.1 video watermarks, C2PA manifests, and camera metadata tags from MP4 clips. Free in-browser video cleaner with zero re-encoding loss.',
        'app_name': 'Seedance 2.1 Watermark Remover',
        'url_slug': 'seedance-2-1',
    },
    'seedance-2-2.astro': {
        'title': 'Remove Seedance 2.2 Watermark: Clean Video Free',
        'desc': 'Remove Seedance 2.2 video watermarks, C2PA manifests, and camera metadata tags from MP4 clips. Free in-browser video cleaner with zero re-encoding loss.',
        'app_name': 'Seedance 2.2 Watermark Remover',
        'url_slug': 'seedance-2-2',
    },
}

for fname, data in video_tools.items():
    fpath = os.path.join(pages_dir, fname)
    if not os.path.exists(fpath):
        continue
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update title
    content = re.sub(r"const title\s*=\s*['\"`].*?['\"`];", f"const title = '{data['title']}';", content)

    # Update description
    content = re.sub(r"const description\s*=\s*['\"`].*?['\"`];", f"const description =\n  '{data['desc']}';", content, flags=re.DOTALL)

    # Clean dashes and emojis
    content = content.replace('—', '-').replace('–', '-')
    content = re.sub(r'[\U0001F300-\U0001FAFF]', '', content)

    # If schema is disconnected arrays, convert to single JSON-LD @graph
    if '@graph' not in content and 'const schema =' in content:
        single_graph = f"""const canonicalUrl = `${{SITE.url}}/{data['url_slug']}/`;

const singleSchemaGraph = {{
  '@context': 'https://schema.org',
  '@graph': [
    {{
      '@type': 'WebPage',
      '@id': canonicalUrl,
      url: canonicalUrl,
      name: title,
      description,
      inLanguage: 'en-US',
      isPartOf: {{
        '@type': 'WebSite',
        '@id': `${{SITE.url}}/#website`,
        name: SITE.name,
        url: SITE.url,
      }},
      breadcrumb: {{
        '@type': 'BreadcrumbList',
        itemListElement: [
          {{ '@type': 'ListItem', position: 1, name: 'Home', item: `${{SITE.url}}/` }},
          {{ '@type': 'ListItem', position: 2, name: 'Tools', item: `${{SITE.url}}/tools/` }},
          {{ '@type': 'ListItem', position: 3, name: '{data['app_name']}', item: canonicalUrl }},
        ],
      }},
    }},
    {{
      '@type': ['SoftwareApplication', 'WebApplication'],
      name: '{data['app_name']}',
      url: canonicalUrl,
      applicationCategory: 'MultimediaApplication',
      operatingSystem: 'Any (web browser)',
      offers: {{
        '@type': 'Offer',
        price: '0',
        priceCurrency: 'USD',
      }},
      description,
    }},
    {{
      '@type': 'FAQPage',
      mainEntity: faqs.map((f) => ({{
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: {{
          '@type': 'Answer',
          text: f.a,
        }},
      }})),
    }},
  ],
}};
---"""
        content = re.sub(r"const schema = \[.*?\];\n---", single_graph, content, flags=re.DOTALL)
        content = content.replace('<Base title={title} description={description} schema={schema}>', '<Base title={title} description={description} schema={singleSchemaGraph}>')

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Successfully upgraded {fname}: Title len {len(data["title"])}, Desc len {len(data["desc"])}')

print('All video tool pages upgraded successfully!')
