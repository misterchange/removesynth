import type { HomeContent } from './content/types';
import type { Locale } from './i18n';

export type { HomeContent } from './content/types';

export { en } from './content/locales/en';
export { de } from './content/locales/de';
export { es } from './content/locales/es';
export { fr } from './content/locales/fr';
export { ptBr as pt_br } from './content/locales/pt-br';
export { ja } from './content/locales/ja';
export { tr } from './content/locales/tr';
export { tl } from './content/locales/tl';
export { zh } from './content/locales/zh';
export { zhTw as zh_tw } from './content/locales/zh-tw';
export { ko } from './content/locales/ko';
export { th } from './content/locales/th';
export { vi } from './content/locales/vi';
export { id } from './content/locales/id';
export { pt } from './content/locales/pt';
export { it } from './content/locales/it';
export { nl } from './content/locales/nl';
export { pl } from './content/locales/pl';
export { cs } from './content/locales/cs';
export { hu } from './content/locales/hu';
export { ro } from './content/locales/ro';
export { uk } from './content/locales/uk';
export { el } from './content/locales/el';
export { sv } from './content/locales/sv';
export { no } from './content/locales/no';
export { da } from './content/locales/da';
export { fi } from './content/locales/fi';
export { hi } from './content/locales/hi';
export { bn } from './content/locales/bn';
export { ar } from './content/locales/ar';
export { he } from './content/locales/he';
export { sw } from './content/locales/sw';

import { en } from './content/locales/en';
import { de } from './content/locales/de';
import { es } from './content/locales/es';
import { fr } from './content/locales/fr';
import { ptBr } from './content/locales/pt-br';
import { ja } from './content/locales/ja';
import { tr } from './content/locales/tr';
import { tl } from './content/locales/tl';
import { zh } from './content/locales/zh';
import { zhTw } from './content/locales/zh-tw';
import { ko } from './content/locales/ko';
import { th } from './content/locales/th';
import { vi } from './content/locales/vi';
import { id } from './content/locales/id';
import { pt } from './content/locales/pt';
import { it } from './content/locales/it';
import { nl } from './content/locales/nl';
import { pl } from './content/locales/pl';
import { cs } from './content/locales/cs';
import { hu } from './content/locales/hu';
import { ro } from './content/locales/ro';
import { uk } from './content/locales/uk';
import { el } from './content/locales/el';
import { sv } from './content/locales/sv';
import { no } from './content/locales/no';
import { da } from './content/locales/da';
import { fi } from './content/locales/fi';
import { hi } from './content/locales/hi';
import { bn } from './content/locales/bn';
import { ar } from './content/locales/ar';
import { he } from './content/locales/he';
import { sw } from './content/locales/sw';

export const ALL_HOME_CONTENT: Record<Locale, HomeContent> = {
  en,
  es,
  de,
  fr,
  'pt-br': ptBr,
  ja,
  tr,
  tl,
  zh,
  'zh-tw': zhTw,
  ko,
  th,
  vi,
  id,
  pt,
  it,
  nl,
  pl,
  cs,
  hu,
  ro,
  uk,
  el,
  sv,
  no,
  da,
  fi,
  hi,
  bn,
  ar,
  he,
  sw,
};
