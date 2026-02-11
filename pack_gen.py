import json
import random

# Load your nouns list
nouns_data = [
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca640"
    },
    "nameEn": "Deer",
    "nameHe": "אייל",
    "category": {
        "$oid": "69876de125b1a590af8ca603"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fdeer_1770581020104_1vyu9qz.png?alt=media&token=a276730b-3635-4151-881f-55ac60f11eac",
    "updatedAt": {
        "$date": "2026-02-08T20:03:42.992Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca641"
    },
    "nameEn": "Bear",
    "nameHe": "דוב",
    "category": {
        "$oid": "69876de125b1a590af8ca603"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fbear_1770580820920_u2av8z8.png?alt=media&token=00676f05-358a-46b6-bb23-f174e2e053f3",
    "updatedAt": {
        "$date": "2026-02-08T20:00:23.229Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca642"
    },
    "nameEn": "Dolphin",
    "nameHe": "דולפין",
    "category": {
        "$oid": "69876de125b1a590af8ca603"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fdolphin_1770581950141_p1oczx5.png?alt=media&token=5894a42b-692e-4177-bb38-ca528efcb5f0",
    "updatedAt": {
        "$date": "2026-02-08T20:19:12.648Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca649"
    },
    "nameEn": "Frog",
    "nameHe": "צפרדע",
    "category": {
        "$oid": "69876de125b1a590af8ca603"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Ffrog_1770582732349_27yysop.png?alt=media&token=60725e9f-e560-419c-9597-2babe2557482",
    "updatedAt": {
        "$date": "2026-02-08T20:32:14.452Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca64b"
    },
    "nameEn": "Bee",
    "nameHe": "דבורה",
    "category": {
        "$oid": "69876de125b1a590af8ca603"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fbee_1770580871756_536rge1.png?alt=media&token=f62bb2cd-e6d1-4a37-9651-753812d3a9ad",
    "updatedAt": {
        "$date": "2026-02-08T20:01:13.834Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca64d"
    },
    "nameEn": "Screwdriver",
    "nameHe": "מברג",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fscrewdriver_1770582641221_nlilcvg.png?alt=media&token=d639ce48-9b4c-4806-a65b-9c30a16b5d9f",
    "updatedAt": {
        "$date": "2026-02-08T20:30:43.229Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca64e"
    },
    "nameEn": "Computer",
    "nameHe": "מחשב",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fcomputer_1770582335857_ncbjr2z.png?alt=media&token=1482508a-2208-4a29-89ef-65d15df4de8b",
    "updatedAt": {
        "$date": "2026-02-08T20:25:37.848Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca64f"
    },
    "nameEn": "Keyboard",
    "nameHe": "מקלדת",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fkeyboard_1770582672139_6tfx7ts.png?alt=media&token=9f353e96-6865-49d6-9bfd-52beae96e18c",
    "updatedAt": {
        "$date": "2026-02-08T20:31:14.126Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca653"
    },
    "nameEn": "Camera",
    "nameHe": "מצלמה",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fcamera_1770582025037_ffw1t24.png?alt=media&token=cae201c0-d9e8-4e2d-9f88-2cb4a2f64830",
    "updatedAt": {
        "$date": "2026-02-08T20:20:27.479Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca654"
    },
    "nameEn": "Clock",
    "nameHe": "שעון",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fclock_1770582266177_lbpizz2.png?alt=media&token=855bbde5-8a8d-4a45-9c99-6c901af5f26e",
    "updatedAt": {
        "$date": "2026-02-08T20:24:28.295Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca655"
    },
    "nameEn": "Key",
    "nameHe": "מפתח",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fkey_1770582701477_iyf5e6u.png?alt=media&token=fb16cae9-254f-4b90-ad3a-1ee259a1e32c",
    "updatedAt": {
        "$date": "2026-02-08T20:31:43.316Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca656"
    },
    "nameEn": "Wallet",
    "nameHe": "ארנק",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fwallet_1770582582313_yjjdjzr.png?alt=media&token=a95bf1be-db37-4fa9-a30f-5dd3fbb0919b",
    "updatedAt": {
        "$date": "2026-02-08T20:29:44.292Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca738"
    },
    "nameEn": "Wall Clock",
    "nameHe": "שעון קיר",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "",
    "updatedAt": {
        "$date": "2026-02-08T20:25:17.334Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e825b1a590af8ca9d1"
    },
    "nameEn": "Hammer",
    "nameHe": "פטיש",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "https://firebasestorage.googleapis.com/v0/b/double-3153b.firebasestorage.app/o/nouns%2Fhammer_1770582422880_4n1fck2.png?alt=media&token=1b662a22-5daa-4d19-be2e-e42f1462a029",
    "updatedAt": {
        "$date": "2026-02-08T20:27:04.948Z"
    }
    },
    {
    "_id": {
        "$oid": "698772e925b1a590af8caa56"
    },
    "nameEn": "Ventilation",
    "nameHe": "אוורור",
    "category": {
        "$oid": "69876de125b1a590af8ca629"
    },
    "imageUrl": "",
    "updatedAt": {
        "$date": "2026-02-08T19:59:00.675Z"
    }
    },
    {
    "_id": {
        "$oid": "698a063d39c78395e72fc352"
    },
    "nameEn": "AAA",
    "nameHe": "אאא",
    "category": {
        "$oid": "69876de125b1a590af8ca629"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:07:25.212Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:07:25.212Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a079ef3deb3eb11b63e42"
    },
    "nameEn": "Squid",
    "nameHe": "דיונון",
    "category": {
        "$oid": "69876de125b1a590af8ca603"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:18.933Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:18.933Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a079ff3deb3eb11b63e46"
    },
    "nameEn": "Guitar pick",
    "nameHe": "מפרט",
    "category": {
        "$oid": "69876de125b1a590af8ca60a"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:19.149Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:19.149Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a079ff3deb3eb11b63e4a"
    },
    "nameEn": "Metronome",
    "nameHe": "מטרונום",
    "category": {
        "$oid": "69876de125b1a590af8ca60a"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:19.343Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:19.343Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a079ff3deb3eb11b63e4e"
    },
    "nameEn": "Music stand",
    "nameHe": "עמוד תווים",
    "category": {
        "$oid": "69876de125b1a590af8ca60a"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:19.537Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:19.537Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a079ff3deb3eb11b63e52"
    },
    "nameEn": "Tuning fork",
    "nameHe": "קולן",
    "category": {
        "$oid": "69876de125b1a590af8ca60a"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:19.727Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:19.727Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a079ff3deb3eb11b63e56"
    },
    "nameEn": "Drumstick",
    "nameHe": "מקל תיפוף",
    "category": {
        "$oid": "69876de125b1a590af8ca60a"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:19.918Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:19.918Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a0f3deb3eb11b63e5c"
    },
    "nameEn": "Mute",
    "nameHe": "עמעם",
    "category": {
        "$oid": "69876de125b1a590af8ca60a"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:20.237Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:20.237Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a0f3deb3eb11b63e60"
    },
    "nameEn": "Capo",
    "nameHe": "קאפו",
    "category": {
        "$oid": "69876de125b1a590af8ca60a"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:20.429Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:20.429Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a0f3deb3eb11b63e64"
    },
    "nameEn": "Amplifier",
    "nameHe": "מגבר",
    "category": {
        "$oid": "69876de125b1a590af8ca60a"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:20.623Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:20.623Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a0f3deb3eb11b63e68"
    },
    "nameEn": "Birdhouse",
    "nameHe": "תיבת קינון",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:20.814Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:20.814Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a1f3deb3eb11b63e6c"
    },
    "nameEn": "Wind chime",
    "nameHe": "פעמוני רוח",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:21.005Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:21.005Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a1f3deb3eb11b63e72"
    },
    "nameEn": "Sundial",
    "nameHe": "שעון שמש",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:21.325Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:21.325Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a1f3deb3eb11b63e7a"
    },
    "nameEn": "Hourglass",
    "nameHe": "שעון חול",
    "category": {
        "$oid": "69876de125b1a590af8ca604"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:21.774Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:21.774Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a2f3deb3eb11b63e7f"
    },
    "nameEn": "Mallet",
    "nameHe": "פטיש עץ",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:22.034Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:22.034Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a2f3deb3eb11b63e83"
    },
    "nameEn": "Plane",
    "nameHe": "מקצועה",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:22.227Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:22.227Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a2f3deb3eb11b63e88"
    },
    "nameEn": "Workbench",
    "nameHe": "שולחן עבודה",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:22.480Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:22.480Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a2f3deb3eb11b63e8c"
    },
    "nameEn": "Vise",
    "nameHe": "מלחציים",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:22.671Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:22.671Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a2f3deb3eb11b63e91"
    },
    "nameEn": "Plumb bob",
    "nameHe": "אנך",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:22.926Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:22.926Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a3f3deb3eb11b63e95"
    },
    "nameEn": "Trowel",
    "nameHe": "כף בנאים",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:23.120Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:23.120Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a3f3deb3eb11b63e99"
    },
    "nameEn": "Spade",
    "nameHe": "את",
    "category": {
        "$oid": "69876de125b1a590af8ca62c"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:23.312Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:23.312Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a4f3deb3eb11b63eb9"
    },
    "nameEn": "Avocado",
    "nameHe": "אבוקדו",
    "category": {
        "$oid": "69876de125b1a590af8ca607"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:24.972Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:24.972Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a5f3deb3eb11b63ebd"
    },
    "nameEn": "Papaya",
    "nameHe": "פאפאיה",
    "category": {
        "$oid": "69876de125b1a590af8ca607"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:25.163Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:25.163Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a5f3deb3eb11b63ec1"
    },
    "nameEn": "Kiwi",
    "nameHe": "קיווי",
    "category": {
        "$oid": "69876de125b1a590af8ca607"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:25.353Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:25.353Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a5f3deb3eb11b63ec6"
    },
    "nameEn": "Melon",
    "nameHe": "מלון",
    "category": {
        "$oid": "69876de125b1a590af8ca607"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:25.607Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:25.607Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a5f3deb3eb11b63eca"
    },
    "nameEn": "Grapefruit",
    "nameHe": "אשכולית",
    "category": {
        "$oid": "69876de125b1a590af8ca607"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:25.796Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:25.796Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a6f3deb3eb11b63ecf"
    },
    "nameEn": "Earmuffs",
    "nameHe": "מגיני אוזניים",
    "category": {
        "$oid": "69876de125b1a590af8ca60d"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:26.050Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:26.050Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a6f3deb3eb11b63ed3"
    },
    "nameEn": "Visor",
    "nameHe": "מצחייה",
    "category": {
        "$oid": "69876de125b1a590af8ca60d"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:26.240Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:26.240Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a6f3deb3eb11b63ed7"
    },
    "nameEn": "Lanyard",
    "nameHe": "שרוך לצוואר",
    "category": {
        "$oid": "69876de125b1a590af8ca60d"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:26.430Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:26.430Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a6f3deb3eb11b63edc"
    },
    "nameEn": "Bow tie",
    "nameHe": "עניבת פרפר",
    "category": {
        "$oid": "69876de125b1a590af8ca60d"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:26.683Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:26.683Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a6f3deb3eb11b63ee0"
    },
    "nameEn": "Pocket square",
    "nameHe": "מטפחת כיס",
    "category": {
        "$oid": "69876de125b1a590af8ca60d"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:26.878Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:26.878Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a7f3deb3eb11b63ee5"
    },
    "nameEn": "Brooch",
    "nameHe": "סיכת בגד",
    "category": {
        "$oid": "69876de125b1a590af8ca60d"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:27.132Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:27.132Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a7f3deb3eb11b63eed"
    },
    "nameEn": "Cabin",
    "nameHe": "בקתה",
    "category": {
        "$oid": "69876de125b1a590af8ca608"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:27.576Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:27.576Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a7f3deb3eb11b63ef1"
    },
    "nameEn": "Fortress",
    "nameHe": "מצודה",
    "category": {
        "$oid": "69876de125b1a590af8ca608"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:27.768Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:27.768Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a8f3deb3eb11b63ef7"
    },
    "nameEn": "Observatory",
    "nameHe": "מצפה כוכבים",
    "category": {
        "$oid": "69876de125b1a590af8ca608"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:28.086Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:28.086Z"
    },
    "__v": 0
    },
    {
    "_id": {
        "$oid": "698a07a8f3deb3eb11b63efc"
    },
    "nameEn": "Gallery",
    "nameHe": "גלריה",
    "category": {
        "$oid": "69876de125b1a590af8ca608"
    },
    "imageUrl": "",
    "createdAt": {
        "$date": "2026-02-09T16:13:28.341Z"
    },
    "updatedAt": {
        "$date": "2026-02-09T16:13:28.341Z"
    },
    "__v": 0
    }
]

# Function to generate a random MongoDB-style ObjectID string
def generate_id(i):
    return f"65c1f2e3d4e5f6a7b8c9d{str(i).zfill(3)}"

def generate_pack():
    cards = []
    
    for _ in range(57):
        symbols = []
        # Randomly select 8 unique indices from the nouns list for each card
        selected_indices = random.sample(range(len(nouns_data)), 8)
        
        for idx in selected_indices:
            symbol = {
                "noun": {"$oid": generate_id(idx)},
                "position": {
                    "x": round(random.uniform(0, 100), 2),
                    "y": round(random.uniform(0, 100), 2)
                },
                "zoomRatio": round(random.uniform(0.5, 2.0), 2),
                "rotation": random.randint(0, 359)
            }
            symbols.append(symbol)
        
        cards.append({"symbols": symbols})


    pack = {
        "name": "Educational Pack",
        "creator": { "$oid": "69879381e89775ac323b8e29" },
        "cards": cards,
        "createdAt": { "$date": "2026-02-10T12:00:00.000+00:00" },
        "updatedAt": { "$date": "2026-02-10T12:00:00.000+00:00" }
    }

    with open('generated_pack.json', 'w', encoding='utf-8') as f:
        json.dump(pack, f, ensure_ascii=False, indent=2)

generate_pack()