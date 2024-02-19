# Pymoe.Manga - Kitsu

This is the documentation for the Kitsu module of Pymoe.Manga.

## Overview

| Operation  | Endpoints                              |
| ---------- | -------------------------------------- |
| `GET`      | manga |
| `SEARCH`   | manga |

Since Kitsu only supports two methods, I won't write in depth documentation for this. You can get a manga by id or you can search for a manga by title. That's it. What you really have to worry about is the return formatting.

!!! note "A Note on Kitsu"

    I really don't recommend using Kitsu. It's here since some apps rely on it, but with searching going away and no promise these endpoints will continue to work you'd be much better off using Anilist or MangaUpdates.

## Return Formatting

Kitsu's return formatting is a lot. Let me show you an example.

```json
{
  "data": {
    "id": "14916",
    "type": "manga",
    "links": {
      "self": "https://kitsu.io/api/edge/manga/14916"
    },
    "attributes": {
      "createdAt": "2013-12-18T13:59:39.232Z",
      "updatedAt": "2024-02-15T20:05:44.395Z",
      "slug": "shingeki-no-kyojin",
      "synopsis": "A century ago, the grotesque giants known as Titans appeared and consumed all but a few thousand humans. The survivors took refuge behind giant walls. Today, the threat of the Titans is a distant memory, and a boy named Eren yearns to explore the world beyond Wall Maria. But what began as a childish dream will become an all-too-real nightmare when the Titans return and humanity is once again on the brink of extinction … Attack on Titan is the award-winning and New York Times-bestselling series that is the manga hit of the decade! Spawning the monster hit anime TV series of the same name, Attack on Titan has become a pop culture sensation. \n\n(Source: Kodansha Comics)\n\nVolume 3 contains the special story \"Rivai Heishichou\" (リヴァイ兵士長, Captain Levi).\nVolume 5 contains the side story \"Ilse no Techou\" (イルゼの手帳, Ilse's Notebook).",
      "description": "A century ago, the grotesque giants known as Titans appeared and consumed all but a few thousand humans. The survivors took refuge behind giant walls. Today, the threat of the Titans is a distant memory, and a boy named Eren yearns to explore the world beyond Wall Maria. But what began as a childish dream will become an all-too-real nightmare when the Titans return and humanity is once again on the brink of extinction … Attack on Titan is the award-winning and New York Times-bestselling series that is the manga hit of the decade! Spawning the monster hit anime TV series of the same name, Attack on Titan has become a pop culture sensation. \n\n(Source: Kodansha Comics)\n\nVolume 3 contains the special story \"Rivai Heishichou\" (リヴァイ兵士長, Captain Levi).\nVolume 5 contains the side story \"Ilse no Techou\" (イルゼの手帳, Ilse's Notebook).",
      "coverImageTopOffset": 112,
      "titles": {
        "ar": "العملاق المهاجم",
        "en": "Attack on Titan",
        "cs_cz": "Útok Titánů",
        "en_jp": "Shingeki no Kyojin",
        "es_es": "Ataque a los Titanes",
        "fa_ir": "حمله به تایتان",
        "fi_fi": "Titaanien sota",
        "fr_fr": "L'Attaque des Titans",
        "hr_hr": "Napad Titana",
        "it_it": "L'attacco dei Giganti",
        "ja_jp": "進撃の巨人",
        "ko_kr": "진격의 거인",
        "pt_br": "Ataque dos Titãs",
        "ru_ru": "Атака на титанов",
        "th_th": "ผ่าพิภพไททัน",
        "tr_tr": "Titana Saldırı",
        "vi_vn": "Đại Chiến Titan",
        "zh_cn": "进击的巨人"
      },
      "canonicalTitle": "Attack on Titan",
      "abbreviatedTitles": [
        "L'attaque sur les titans",
        "Атака титанов",
        "ھێرش بۆ سەر زەبەلاحەكان",
        "進擊的巨人",
        "SNK",
        "AOT",
        "Ilse no Techou",
        "Rivai Heishichou"
      ]
    }
  }
}
```

Kitsu returns data by following the Swagger API methodology exactly to the letter. You get self referential links, a ton of title information across several different headings, and even such things as the cover image offset. It returns average ratings, number of ratings per rating number, and even adjusted weighted rating. Kitsu returns *a lot* of data all at once, but the reality is that you don't need a lot of it. Lots of information you might want isn't even included. It's a separate call to get character data, a separate call to get episode data, a separate call to get staff and author data. So on and so forth. The benefits to using Kitsu would be the ease of creating a fluent application using the relationships data, the per language titles, and how many image options it has. It has images for covers, portraits and backgrounds in various sizes along with a definition of what each of those sizes actually is in pixels.

As an example, let's say I want the French title for Attack on Titans...
```python
import pymoe

# This is the manga Attack on Titan
result = pymoe.manga.get.kitsu.manga(14916)

# This prints L'Attaque des Titans
print(result['data']['titles']['fr_fr'])
```