import re

path = r'd:\Nitin\removesynth\apps\removesynth\src\pages\social-media-safe-zones.astro'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = re.sub(
    r"const title\s*=\s*'[^']*';",
    "const title = 'Social Media Safe Zones: Reels, TikTok & Shorts Guide';",
    content
)

# Replace description
content = re.sub(
    r"const description\s*=\s*'[^']*';",
    "const description = 'Interactive safe zone simulator for Instagram Reels, TikTok, YouTube Shorts, and Stories. Preview overlays to prevent app UI from obstructing your text and titles.';",
    content
)

# Replace emojis with empty string or plain text
# Common emoji range
content = re.sub(r'[\U0001F300-\U0001FAFF]', '', content)

# Check for em/en dashes
content = content.replace('—', '-').replace('–', '-')

# Replace multiple schema with single schema graph
old_schema_pattern = r"const schema = \[.*?\];\n---"
new_schema = """const canonicalUrl = `${SITE.url}/social-media-safe-zones/`;

const singleSchemaGraph = {
  '@context': 'https://schema.org',
  '@graph': [
    {
      '@type': 'WebPage',
      '@id': canonicalUrl,
      url: canonicalUrl,
      name: title,
      description,
      inLanguage: 'en-US',
      isPartOf: {
        '@type': 'WebSite',
        '@id': `${SITE.url}/#website`,
        name: SITE.name,
        url: SITE.url,
      },
      breadcrumb: {
        '@type': 'BreadcrumbList',
        itemListElement: [
          { '@type': 'ListItem', position: 1, name: 'Home', item: `${SITE.url}/` },
          { '@type': 'ListItem', position: 2, name: 'Tools', item: `${SITE.url}/tools/` },
          { '@type': 'ListItem', position: 3, name: 'Social Media Safe Zones', item: canonicalUrl },
        ],
      },
    },
    {
      '@type': ['SoftwareApplication', 'WebApplication'],
      name: 'Social Media Safe Zones Simulator',
      url: canonicalUrl,
      applicationCategory: 'MultimediaApplication',
      operatingSystem: 'Any (web browser)',
      offers: {
        '@type': 'Offer',
        price: '0',
        priceCurrency: 'USD',
      },
      description,
      featureList: [
        'Instagram Reels 9:16, 4:5, and 1:1 safe zone overlays',
        'TikTok caption and engagement UI danger zone simulator',
        'YouTube Shorts subscribe and header overlay preview',
        'Downloadable transparent 1080x1920 PNG editing templates',
        '100 percent in-browser execution with zero video uploads',
      ],
    },
    {
      '@type': 'HowTo',
      name: 'How to Check Social Media Video Safe Zones for Reels and TikTok',
      description: 'Step-by-step instructions to test short-form 9:16 videos against mobile app UI obstructions.',
      step: [
        {
          '@type': 'HowToStep',
          position: 1,
          name: 'Upload video or image draft',
          text: 'Drag and drop your 9:16 short-form video or still frame into the simulator.',
        },
        {
          '@type': 'HowToStep',
          position: 2,
          name: 'Toggle platform UI overlays',
          text: 'Switch between Instagram Reels, TikTok, YouTube Shorts, and Snapchat overlays.',
        },
        {
          '@type': 'HowToStep',
          position: 3,
          name: 'Inspect text and graphics placement',
          text: 'Verify that captions, key visual subjects, and text calls-to-action remain inside green safe areas.',
        },
        {
          '@type': 'HowToStep',
          position: 4,
          name: 'Download PNG editing template',
          text: 'Export the 1080x1920 transparent overlay template to use as a guide track in Premiere Pro or CapCut.',
        },
      ],
    },
    {
      '@type': 'FAQPage',
      mainEntity: faqs.map((f) => ({
        '@type': 'Question',
        name: f.q,
        acceptedAnswer: {
          '@type': 'Answer',
          text: f.a,
        },
      })),
    },
  ],
};
---"""

content = re.sub(r"const schema = \[.*?\];\n---", new_schema, content, flags=re.DOTALL)
content = content.replace('<Base title={title} description={description} schema={schema}>', '<Base title={title} description={description} schema={singleSchemaGraph}>')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated social-media-safe-zones.astro successfully!')
