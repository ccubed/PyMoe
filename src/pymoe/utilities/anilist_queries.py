# SHARED ENDPOINTS
GET_CHARACTER_QUERY = """
query ($id: Int){
    Character (id: $id){
        name{
            first
            last
        }
        image {
            large
            medium
        }
        description
        gender
        age
        siteUrl
        media{
            nodes{
                id
                idMal
                title {
                    romaji
                    english
                    native
                }
                coverImage {
                    extraLarge
                    large
                    medium
                    color
                }
                siteUrl
            }
        }
    }
}
"""

GET_STAFF_QUERY = """
query ($id: Int){
    Staff (id: $id){
        name{
            first
            last
        }
        languageV2
        image {
            large
            medium
        }
        description
        primaryOccupations
        gender
        siteUrl
        dateOfBirth {
            year
            month
            day
        }
        dateOfDeath {
            year
            month
            day
        }
        age
        homeTown
        yearsActive
        staffMedia{
            nodes{
                id
                idMal
                title {
                    romaji
                    english
                    native
                }
                coverImage {
                    extraLarge
                    large
                    medium
                    color
                }
                siteUrl
            }
        }
        characters {
            nodes {
                id
                name {
                    first
                    last
                }
                image {
                    large
                    medium
                }
                age
                siteUrl
                media {
                    nodes {
                        id
                        idMal
                        title {
                            romaji
                            english
                            native
                        }
                        coverImage {
                            extraLarge
                            large
                            medium
                            color
                        }
                        siteUrl
                    }
                }
            }
        }
    }
}
"""

GET_STUDIO_QUERY = """
query ($id: Int){
    Studio (id: $id){
        name
        siteUrl
        media{
            nodes{
                id
                idMal
                title {
                    romaji
                    english
                    native
                }
                coverImage {
                    extraLarge
                    large
                    medium
                    color
                }
                siteUrl
            }
        }
    }
}
"""

SEARCH_CHARACTER_QUERY = """
query ($query: String, $page: Int, $perPage: Int) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            currentPage
            hasNextPage
        }
        characters(search: $query) {
            id
            name {
                first
                last
            }
            image {
                large
                medium
            }
            description
            gender
            age
            siteUrl
            media {
                nodes {
                    id
                    idMal
                    title {
                        romaji
                        english
                        native
                    }
                    coverImage {
                        extraLarge
                        large
                        medium
                        color
                    }
                    siteUrl
                }
            }
        }
    }
}
"""

SEARCH_STAFF_QUERY = """
query ($query: String, $page: Int, $perPage: Int) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            currentPage
            hasNextPage
        }
        staff(search: $query) {
            id
            name {
                first
                last
            }
            languageV2
            image {
                large
                medium
            }
            description
            primaryOccupations
            gender
            dateOfBirth {
                year
                month
                day
            }
            dateOfDeath {
                year
                month
                day
            }
            age
            homeTown
            yearsActive
            siteUrl
            staffMedia {
                nodes {
                    id
                    idMal
                    title {
                        romaji
                        english
                        native
                    }
                    coverImage {
                        extraLarge
                        large
                        medium
                        color
                    }
                    siteUrl
                }
            }
            characters {
                nodes {
                    name {
                        first
                        last
                    }
                    image {
                        large
                        medium
                    }
                    age
                    siteUrl
                    media {
                        nodes {
                            id
                            idMal
                            title {
                                romaji
                                english
                                native
                            }
                            coverImage {
                                extraLarge
                                large
                                medium
                                color
                            }
                            siteUrl
                        }
                    }
                }
            }
        }
    }
}
"""

SEARCH_STUDIO_QUERY = """
query ($query: String, $page: Int, $perPage: Int) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            currentPage
            hasNextPage
        }
        studios(search: $query) {
            id
            name
            siteUrl
            media {
                nodes {
                    id
                    idMal
                    title {
                        romaji
                        english
                        native
                    }
                    coverImage {
                        extraLarge
                        large
                        medium
                        color
                    }
                    siteUrl
                }
            }
        }
    }
}
"""

# ANIME ENDPOINTS
GET_ANIME_QUERY = """
query($id: Int){
    Media(id: $id, type: ANIME) {
        title {
            romaji
            english
            native
        }
        startDate{
            year
            month
            day
        }
        endDate {
            year
            month
            day
        }
        coverImage {
            extraLarge
            large
            medium
            color
        }
        bannerImage
        description
        format
        status
        episodes
        season
        seasonYear
        averageScore
        meanScore
        genres
        synonyms
        isAdult
        siteUrl
        idMal
        popularity
        nextAiringEpisode {
            timeUntilAiring
            airingAt
        }
        streamingEpisodes {
            title
            thumbnail
            url
            site
        }
        externalLinks {
            site
            url
            language
        }
        characters {
            nodes {
                id
                name {
                    first
                    last
                }
                image {
                    large
                    medium
                }
                description
                gender
                age
                siteUrl
            }
        }
    }
}
"""

GET_ANIMESTREAMING_QUERY = """
query ($id: Int) {
    Media(id: $id) {
        streamingEpisodes {
            title
            thumbnail
            url
            site
        }
    }
}
"""

GET_ANIMEAIRINGSCHEDULE_QUERY = """
query( $id: Int, $page: Int, $perPage: Int) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            currentPage
            hasNextPage
        }
        airingSchedules(mediaId: $id) {
            id
            episode
            timeUntilAiring
        }
    }
}
"""

SEARCH_ANIMESEASON_QUERY = """
query ($season: MediaSeason, $seasonYear: Int, $page: Int, $perPage: Int) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            currentPage
            hasNextPage
        }
        media(season: $season, seasonYear: $seasonYear) {
            id
            idMal
            title {
                romaji
                english
                native
            }
            coverImage {
                extraLarge
                large
                medium
                color
            }
            nextAiringEpisode {
                timeUntilAiring
                airingAt
            }
            startDate {
                year
                month
                day
            }
            streamingEpisodes {
                title
                thumbnail
                url
                site
            }
            externalLinks {
                site
                url
                language
            }
            description
            genres
            isAdult
            siteUrl
        }
    }
}
"""

SEARCH_ANIME_QUERY = """
query ($query: String, $page: Int, $perPage: Int) {
    Page(page: $page, perPage: $perPage) {
        pageInfo {
            currentPage
            hasNextPage
        }
        media(search: $query, type: ANIME) {
            id
            idMal
            title {
                romaji
                english
                native
            }
            coverImage {
                extraLarge
                large
                medium
                color
            }
            averageScore
            popularity
            episodes
            season
            hashtag
            isAdult
            siteUrl
            characters {
                nodes {
                    id
                    name {
                        first
                        last
                    }
                    image {
                        large
                        medium
                    }
                    description
                    gender
                    age
                    siteUrl
                }
            }
        }
    }
}
"""

# MANGA ENDPOINTS
GET_MANGA_QUERY = """
query( $id: Int ) {
    Media( id: $id, type: MANGA ) {
        idMal
        title {
            romaji
            english
        }
        status
        description
        startDate {
            year
            month
            day
        }
        endDate {
            year
            month
            day
        }
        coverImage {
            extraLarge
            large
            medium
            color
        }
        chapters
        volumes
        genres
        synonyms
        averageScore
        isAdult
        siteUrl
        popularity
        characters {
            nodes {
                id
                name {
                    first
                    last
                }
                image {
                    large
                    medium
                }
                description
                gender
                age
                siteUrl
            }
        }
    }
}
"""

SEARCH_MANGA_QUERY = """
query( $query: String, $page: Int, $perPage: Int ){
    Page ( page: $page, perPage: $perPage ) {
        pageInfo {
            currentPage
            hasNextPage
        }
        media ( search: $query, type: MANGA ){
            id
            idMal
            title {
                romaji
                english
            }
            coverImage {
                extraLarge
                large
                medium
                color
            }
            status
            description
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            averageScore
            popularity
            chapters
            volumes
            genres
            hashtag
            isAdult
            averageScore
            synonyms
            siteUrl
        }
    }
}    
"""