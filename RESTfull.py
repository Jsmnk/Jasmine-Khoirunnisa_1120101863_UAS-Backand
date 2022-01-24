from dataclasses import dataclass
from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

null = None


class beranda(Resource):
    def get(self):
        return {
            "data": [
                {
                    "header": [
                        {
                            "kiriheader": {
                                "logo": {
                                    "gambar": "https://cdn-1.tstatic.net/img/logo/tribun/svg/tribunnews.svg",
                                    "url": "https://www.tribunnews.com/"
                                }
                            },
                            "kananheader": [
                                {
                                    "tanggal": {
                                        "text": "Sabtu, 15 Januari 2022"
                                    },
                                    "pencarian": [
                                        {
                                            "icon": "search",
                                            "text": "cari",
                                            "placeholder": "cari berita"
                                        }
                                    ]
                                },
                                {
                                    "network": [
                                        {
                                            "icon": "network",
                                            "text": "network",
                                            "url": "https://www.tribunnews.com/",
                                            "menu": [
                                                {
                                                    "atas": [
                                                        {
                                                            "text": "tribunnews.com",
                                                            "url": "https://www.tribunnews.com/"
                                                        },
                                                        {
                                                            "text": "Tribun-video.com",
                                                            "url": "https://video.tribunnews.com/?_ga=2.161208568.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunnewsWiki.com",
                                                            "url": "https://www.tribunnewswiki.com/"
                                                        },
                                                        {
                                                            "text": "TribunJualBeli.com",
                                                            "url": "https://www.tribunjualbeli.com/"
                                                        },
                                                        {
                                                            "text": "TribunStyle.com",
                                                            "url": "https://style.tribunnews.com/?_ga=2.135934964.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunHealth.com",
                                                            "url": "https://health.tribunnews.com/?_ga=2.73545687.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunTravel.com",
                                                            "url": "https://travel.tribunnews.com/?_ga=2.92934232.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunTrends.com",
                                                            "url": "https://trends.tribunnews.com/?_ga=2.160649336.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunWow.com",
                                                            "url": "https://wow.tribunnews.com/?_ga=2.159989752.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunNewsMaker.com",
                                                            "url": "https://newsmaker.tribunnews.com/?_ga=2.64044906.475167733.1642144590-1004112812.1642144589"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "tengah": [
                                                        {
                                                            "text": "TribunJakarta.com",
                                                            "url": "https://jakarta.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunJabar.com",
                                                            "url": "https://jabar.tribunnews.com/?_ga=2.132282443.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunMataram.com",
                                                            "url": "https://mataram.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunMataraman.com",
                                                            "url": "https://matarama.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunMedan.com",
                                                            "url": "https://medan.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunPadang.com",
                                                            "url": "https://padang.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunFlores.com",
                                                            "url": "https://flores.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunSulbar.com",
                                                            "url": "https://sulbar.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunAmbon.com",
                                                            "url": "https://ambon.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "WartaKotalive.com",
                                                            "url": "https://wartakota.tribunnews.com/?_ga=2.137040117.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunNewsBogor.com",
                                                            "url": "https://bogor.tribunnews.com/?_ga=2.65853547.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "Tribun-Pantura.com",
                                                            "url": "https://pantura.tribunnews.com/?_ga=2.65853547.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunMadura.com",
                                                            "url": "https://madura.tribunnews.com/?_ga=2.93468632.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "Sripoku.com",
                                                            "url": "https://palembang.tribunnews.com/?_ga=2.131674186.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunPekanbaru.com",
                                                            "url": "https://pekanbaru.tribunnews.com/?_ga=2.165944699.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "BanjarmasinPost.com",
                                                            "url": "https://jakarta.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunPontianak.com",
                                                            "url": "https://jakarta.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunPapua.com",
                                                            "url": "https://papua.tribunnews.com/?_ga=2.69350357.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunBekasi.com",
                                                            "url": "https://bekasi.tribunnews.com/?_ga=2.162217977.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunCirebon.com",
                                                            "url": "https://cirebon.tribunnews.com/?_ga=2.137115893.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunJogja.com",
                                                            "url": "https://jogja.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "Tribun-Bali.com",
                                                            "url": "https://bali.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "BangkaPos.com",
                                                            "url": "https://bangka.tribunnews.com/?_ga=2.165427578.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunJambi.com",
                                                            "url": "https://jakarta.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunKaltim.com",
                                                            "url": "https://kaltim.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunPalu.com",
                                                            "url": "https://palu.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunPapuaBarat.com",
                                                            "url": "https://papuabarat.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunBanten.com",
                                                            "url": "https://banten.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunJateng.com",
                                                            "url": "https://jateng.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "tribunJatim.com",
                                                            "url": "https://jatim.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "SerambiNews.com",
                                                            "url": "https://aceh.tribunnews.com/?_ga=2.131734602.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunBatam.com",
                                                            "url": "https://batam.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunSumsel.com",
                                                            "url": "https://sumsel.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunKalteng.com",
                                                            "url": "https://kalteng.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "Tribun-Timur.com",
                                                            "url": "https://makassar.tribunnews.com/?_ga=2.105468998.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunTangerang.com",
                                                            "url": "https://tangerang.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunSolo.com",
                                                            "url": "https://solo.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "Surya.co.id",
                                                            "url": "https://surabaya.tribunnews.com/?_ga=2.174291047.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "Prohaba.co",
                                                            "url": "https://prohaba.tribunnews.com/?_ga=2.174291047.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "PosBelitung.co",
                                                            "url": "https://belitung.tribunnews.com/?_ga=2.98647131.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunLampung.com",
                                                            "url": "https://lampung.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunKaltara.com",
                                                            "url": "https://kaltara.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunLombok.com",
                                                            "url": "https://lombok.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunnewsDepok.com",
                                                            "url": "https://depok.tribunnews.com/?_ga=2.94508121.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunBanyumas.com",
                                                            "url": "https://banyumas.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "SuryaMalang.com",
                                                            "url": "https://suryamalang.tribunnews.com/?_ga=2.61544681.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunnewsSultra.com",
                                                            "url": "https://sultra.tribunnews.com/?_ga=2.61546473.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "`BebelNews.id`",
                                                            "url": "https://babel.tribunnews.com/?_ga=2.61546473.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "Pos-Kupang.com",
                                                            "url": "https://kupang.tribunnews.com/?_ga=2.98794587.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunManado.com",
                                                            "url": "https://manado.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        },
                                                        {
                                                            "text": "TribunTernate.com",
                                                            "url": "https://ternate.tribunnews.com/?_ga=2.174281703.475167733.1642144590-1004112812.1642144589"
                                                        }
                                                    ]
                                                },
                                                {
                                                    "bawah": [
                                                        {
                                                            "text": "Karir",
                                                            "url": "https://www.tribunnetwork.com/career/"
                                                        },
                                                        {
                                                            "text": "Trubun Epaper",
                                                            "url": "https://www.tribunnews.com/epaper"
                                                        },
                                                        {
                                                            "text": "Gramedia.com",
                                                            "url": "https://www.gramedia.com/"
                                                        },
                                                        {
                                                            "text": "Gramedia Digital",
                                                            "url": "https://ebooks.gramedia.com/"
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "ikuti kami": {
                                        "text": "ikuti kami",
                                        "sosmed": [
                                            {
                                                "icon": "fa fa rss",
                                                "text": "RSS",
                                                "url": "https://www.tribunnews.com/rss"
                                            },
                                            {
                                                "icon": "fa fa facebook",
                                                "text": "Facebook",
                                                "url": "https://www.facebook.com/tribunnews/"
                                            },
                                            {
                                                "icon": "fa fa instagram",
                                                "text": "Instagram",
                                                "url": "https://instagram.com/tribunnews/"
                                            },
                                            {
                                                "icon": "fa fa twitter",
                                                "text": "Twitter",
                                                "url": "https://twitter.com/tribunnews"
                                            },
                                            {
                                                "icon": "fa fa google",
                                                "text": "Google",
                                                "url": "https://news.google.com/publications/CAAqBwgKMOaOjgswxOWgAw?hl=id&gl=ID&ceid=ID%3Aid"
                                            }
                                        ]
                                    }
                                },
                                {
                                    "login": [
                                        {
                                            "text": "login",
                                            "url": "https://account.tribunnews.com/login/dHJpYnVubmV3cw==/aHR0cHM6Ly93d3cudHJpYnVubmV3cy5jb20v?_ga=2.169009124.475167733.1642144590-1004112812.1642144589",
                                            "login2": [
                                                {
                                                    "text": "Belum mendaftar?"
                                                },
                                                {
                                                    "text": "Mendaftar",
                                                    "url": "https://account.tribunnews.com/register/dHJpYnVubmV3cw==?_ga=2.101987140.475167733.1642144590-1004112812.1642144589"
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                },
                {
                    "menu": [
                        {
                            "text": "News",
                            "url": "https://www.tribunnews.com/news"
                        },
                        {
                            "text": "Bisnis",
                            "url": "https://www.tribunnews.com/bisnis"
                        },
                        {
                            "text": "Superskor",
                            "url": "https://www.tribunnews.com/superskor"
                        },
                        {
                            "text": "Sport",
                            "url": "https://www.tribunnews.com/sport"
                        },
                        {
                            "text": "Seleb",
                            "url": "https://www.tribunnews.com/seleb"
                        },
                        {
                            "text": "Lifestyle",
                            "url": "https://www.tribunnews.com/lifestyle"
                        },
                        {
                            "text": "New Economy",
                            "url": "https://www.tribunnews.com/new-economy"
                        },
                        {
                            "text": "PARAPUAN",
                            "url": "https://www.tribunnews.com/parapuan"
                        },
                        {
                            "text": "Otomotif",
                            "url": "https://www.tribunnews.com/otomotif"
                        },
                        {
                            "text": "Techno",
                            "url": "https://www.tribunnews.com/techno"
                        },
                        {
                            "text": "Video",
                            "url": "https://www.tribunnews.com/video"
                        },
                        {
                            "text": "Images",
                            "url": "https://www.tribunnews.com/images"
                        },
                        {
                            "text": "Lainnya",
                            "icon": "fa fa-caret-down",
                            "url": "https://www.tribunnews.com/#",
                            "dropdown": [
                                {
                                    "text": "Kesehatan",
                                    "url": "https://www.tribunnews.com/kesehatan"
                                },
                                {
                                    "text": "Tribunners",
                                    "url": "https://www.tribunnews.com/tribunners"
                                },
                                {
                                    "text": "Tribun Epaper",
                                    "url": "https://www.tribunnews.com/epaper"
                                },
                                {
                                    "text": "Travel",
                                    "url": "https://www.tribunnews.com/travel"
                                },
                                {
                                    "text": "Karir",
                                    "url": "https://www.tribunnetwork.com/career/"
                                },
                                {
                                    "text": "Longform",
                                    "url": "https://longform.tribunnews.com/?_ga=2.139558006.475167733.1642144590-1004112812.1642144589"
                                },
                                {
                                    "text": "Indeks Tag",
                                    "url": "https://www.tribunnews.com/tag"
                                },
                                {
                                    "text": "Indeks Berita",
                                    "url": "https://www.tribunnews.com/indeks"
                                }
                            ]
                        }
                    ]
                },
                {
                    "submenu": [
                        {
                            "text": "KILAS",
                            "URL": "https://www.tribunnews.com/kilas-kementerian"
                        },
                        {
                            "text": "Jakarta",
                            "URL": "https://wartakota.tribunnews.com/?_ga=2.94666713.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Bandung",
                            "URL": "https://jabar.tribunnews.com/?_ga=2.94666713.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Bogor",
                            "URL": "https://bogor.tribunnews.com/?_ga=2.94666713.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Jogja",
                            "URL": "https://jogja.tribunnews.com/?_ga=2.102830149.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Solo",
                            "URL": "https://solo.tribunnews.com/?_ga=2.102830149.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Semarang",
                            "URL": "https://jateng.tribunnews.com/?_ga=2.102830149.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Surabaya",
                            "URL": "https://surabaya.tribunnews.com/?_ga=2.102830149.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Malang",
                            "URL": "https://suryamalang.tribunnews.com/?_ga=2.102830149.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Bali",
                            "URL": "https://bali.tribunnews.com/?_ga=2.160643448.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Aceh",
                            "URL": "https://aceh.tribunnews.com/?_ga=2.160643448.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Medan",
                            "URL": "https://medan.tribunnews.com/?_ga=2.160643448.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Pekanbaru",
                            "URL": "https://pekanbaru.tribunnews.com/?_ga=2.68302676.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Batam",
                            "URL": "https://batam.tribunnews.com/?_ga=2.68302676.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Jambi",
                            "URL": "https://jambi.tribunnews.com/?_ga=2.68302676.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Palembang",
                            "URL": "https://palembang.tribunnews.com/?_ga=2.72448086.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Bangka",
                            "URL": "https://bangka.tribunnews.com/?_ga=2.72448086.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Lampung",
                            "URL": "https://lampung.tribunnews.com/?_ga=2.72448086.475167733.1642144590-1004112812.1642144589"
                        },
                        {
                            "text": "Kota lain",
                            "icon": "fa fa-caret-down",
                            "url": "https://www.tribunnews.com/#",
                            "dropdown2": [
                                {
                                    "text": "Pontianak",
                                    "url": "https://pontianak.tribunnews.com/?_ga=2.103576389.475167733.1642144590-1004112812.1642144589"
                                },
                                {
                                    "text": "Banjarmasin",
                                    "url": "https://banjarmasin.tribunnews.com/?_ga=2.68956244.475167733.1642144590-1004112812.1642144589"
                                },
                                {
                                    "text": "Balikpapan",
                                    "url": "https://kaltim.tribunnews.com/?_ga=2.68956244.475167733.1642144590-1004112812.1642144589"
                                },
                                {
                                    "text": "Makassar",
                                    "url": "https://makassar.tribunnews.com/?_ga=2.94008408.475167733.1642144590-1004112812.1642144589"
                                },
                                {
                                    "text": "Manado",
                                    "url": "https://manado.tribunnews.com/?_ga=2.94008408.475167733.1642144590-1004112812.1642144589"
                                },
                                {
                                    "text": "Kupang",
                                    "url": "https://kupang.tribunnews.com/?_ga=2.94008408.475167733.1642144590-1004112812.1642144589"
                                },
                                {
                                    "text": "Sumsel",
                                    "url": "https://sumsel.tribunnews.com/?_ga=2.94008408.475167733.1642144590-1004112812.1642144589"
                                }
                            ]
                        }
                    ]
                },
                {
                    "body": [
                        {
                            "slider": [
                                {
                                    "text": "Gempa di Banten",
                                    "url": "https://www.tribunnews.com/topic/gempa-di-banten",
                                    "berita": [
                                        {
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/irjen-pol-rudy-heriyanto-yuhu.jpg",
                                            "text": "Kapolda Banten Tinju Posko Pengungsian Gempa di Pandeglang",
                                            "url": "https://www.tribunnews.com/regional/2022/01/15/kapolda-banten-tinjau-posko-pengungsian-gempa-di-pandeglang"
                                        },
                                        {
                                            "gambar": "https://www.tribunnews.com/regional/2022/01/15/1100-rumah-di-pandeglang-rusak-akibat-gempa-banten",
                                            "text": "1100 Rumah di Pandeglang Rusak Akibat Gempa Banten",
                                            "url": "https://www.tribunnews.com/regional/2022/01/15/1100-rumah-di-pandeglang-rusak-akibat-gempa-banten"
                                        }
                                    ]
                                },
                                {
                                    "text": "Pemindahan Ibu Kota Negara",
                                    "url": "https://www.tribunnews.com/topic/pemindahan-ibu-kota-negara",
                                    "berita": [
                                        {
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/desain-istana-di-ibu-kota-negara-yang-baru-di-kaltim.jpg",
                                            "text": "Presiden Jokowi Sudah Mengantongi Nama Ibu Kota Negara",
                                            "url": "https://www.tribunnews.com/nasional/2022/01/15/presiden-jokowi-disebut-sudah-mengantongi-nama-ibu-kota-negara"
                                        },
                                        {
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/wakil-ketua-komisi-ii-dpr-ri-saan-mustopa-1811.jpg",
                                            "text": "Pimpinan Pansus: Kepala Daerah IKN Baru Setingkat Menteri dan Dipilih Langsung Presiden",
                                            "url": "https://www.tribunnews.com/nasional/2022/01/14/pimpinan-pansus-kepala-daerah-ikn-baru-setingkat-menteri-dan-dipilih-langsung-presiden"
                                        }
                                    ]
                                },
                                {
                                    "text": "Liga Inggris",
                                    "url": "https://www.tribunnews.com/topic/liga-inggris",
                                    "berita": [
                                        {
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/keseruan-duel-aston-villa-vs-manchester-united-dapat-disaksikan-secara-gratis-melalui-sctv.jpg",
                                            "text": "Live Streaming TV Online SCTV, Aston Villa vs Manchester United Liga Inggris, Akses di Sini Gratis",
                                            "url": "https://www.tribunnews.com/superskor/2022/01/15/live-streaming-tv-online-sctv-aston-villa-vs-manchester-united-liga-inggris-akses-di-sini-gratis"
                                        },
                                        {
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/kevin-de-bruyne-setelah-mencetak-gol-ke-gawang-chelsea.jpg",
                                            "text": "Hasil Liga Inggris: Gol Sarat Makna Kevin De Bruyne Bawa Manchester City Libas Chelsea",
                                            "url": "https://www.tribunnews.com/superskor/2022/01/15/hasil-liga-inggris-gol-sarat-makna-kevin-de-bruyne-bawa-manchester-city-libas-chelsea"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "section-berita1": [
                                {
                                    "text judul": "OTT KPK di Langkat",
                                    "url judul": "https://www.tribunnews.com/topic/ott-kpk-di-langkat",
                                    "text subjudul": "Perluas Pasar, Traveloka dan Bluebird Operasikan Layanan Pemesanan Taksi QuickRide di 16 Kota",
                                    "url": "https://www.tribunnews.com/bisnis/2022/01/19/perluas-pasar-traveloka-dan-bluebird-operasikan-layanan-pemesanan-taksi-quickride-di-16-kota",
                                    "text isi": "Layanan ini tersedia di 16 kota besar dan destinasi pariwisata di mana terdapat jaringan taksi Bluebird dan bisa diakses melalui aplikasi Traveloka.",
                                    "kategori": "https://www.tribunnews.com/nasional",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "2 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ati-kabupaten-langkat-terbit-rencana-peranginangin-vv.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Harga Minyak Goreng",
                                    "url judul": "https://www.tribunnews.com/topic/harga-minyak-goreng",
                                    "text subjudul": "Harga Minyak Goreng Resmi Jadi Rp 14 Ribu per Liter, Ibu-ibu di Gowa Ramai Kunjungi Ritel",
                                    "url subjudul": "https://www.tribunnews.com/bisnis/2022/01/19/harga-minyak-goreng-resmi-jadi-rp-14-ribu-per-liter-ibu-ibu-di-gowa-ramai-kunjungi-ritel-modern",
                                    "text isi": "Pemerintah telah menetapkan kebijakan satu harga minyak goreng menjadi Rp 14 ribu di ritel modern seluruh Indonesia, Rabu(19/1/2022)",
                                    "kategori": "https://www.tribunnews.com/bisnis",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": " 34 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/salah-satu-toko-modern-di-kabupaten-bulukumba-sulsel-rabu-1912022.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Diperiksa Penyidik, Jokowi Mania Klaim Dosen UNJ Sebar Fitnah Kepada Anak Jokowi",
                                    "url": "https://www.tribunnews.com/nasional/2022/01/19/diperiksa-penyidik-jokowi-mania-klaim-dosen-unj-sebar-fitnah-kepada-anak-jokowi",
                                    "text isi": "Tim kuasa hukum Jokowi Mania kembali menyambangi Polda Metro Jaya terkait laporan terhadap dosen Universitas Negeri Jakarta, Ubedilah Badrun.",
                                    "kategori": "https://www.tribunnews.com/nasional",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "5 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/kuasa-hukum-relawan-jokowi-mania-bambang-sri-11.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Pemindahan Ibu Kota Negara",
                                    "url judul": "https://www.tribunnews.com/topic/pemindahan-ibu-kota-negara",
                                    "text subjudul": "Jokowi Sebut Kemungkinan Istana akan Pindah ke Ibu Kota Negara yang Baru pada 2024",
                                    "url": "https://www.tribunnews.com/nasional/2022/01/19/jokowi-sebut-kemungkinan-istana-akan-pindah-ke-ibu-kota-negara-yang-baru-pada-2024",
                                    "text isi": "Jokowi memperkirakan, proses perpindahan ke ibu kota negara baru tersebut akan memakan waktu hingga 20 tahun.",
                                    "kategori": "https://www.tribunnews.com/nasional",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": " 11 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/jkw-jangan-panik.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Chord Gitar",
                                    "url judul": "https://www.tribunnews.com/topic/chord-gitar",
                                    "text subjudul": "Chord Gitar Rungokno Aku - Ndarboy Genk feat Denny Caknan, Lengkap dengan Lirik Lagunya",
                                    "url subjudul": "https://www.tribunnews.com/seleb/2022/01/19/chord-gitar-rungokno-aku-ndarboy-genk-feat-denny-caknan-lengkap-dengan-lirik-lagunya",
                                    "text isi": "Lagu berjudul Rungokno Aku dinyanyikan dan dipopulerkan oleh Ndarboy Genk feat Denny Caknan, simak chord gitar dan lirik lagunya berikut ini.",
                                    "kategori": "https://www.tribunnews.com/seleb",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "12 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/lagu-rungokno-aku.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Sekjen Kemnaker: Kemnaker Corpu Alat Stratgis Cetak SDM ASN yang Kompeten",
                                    "url judul": "https://www.tribunnews.com/kilas-kementerian/2022/01/19/sekjen-kemnaker-kemnaker-corpu-alat-stratgis-cetak-sdm-asn-yang-kompeten",
                                    "text isi": "Kemnaker Corpu dalam penerapannya akan dilaksanakan oleh Pusat Pengembangan SDM (PPSDM) Ketenagakerjaan dengan pelibatan seluruh",
                                    "kategori": "https://www.tribunnews.com/kilas-kementerian",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "2 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/kemnaker-corpu-alat-stratgis-cetak-sdm-asn-yang-kompeten.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Kasus Gaga Muhammad dan Laura Anna",
                                    "url judul": "https://www.tribunnews.com/topic/kasus-gaga-muhammad-dan-laura-anna",
                                    "text subjudul": "Menangis Baca Percakapan Laura Anna dan Gaga Muhammad di HP, Greta: Ternyata Sejahat Itu",
                                    "url subjudul": "https://www.tribunnews.com/seleb/2022/01/19/menangis-baca-percakapan-laura-anna-dan-gaga-muhammad-di-hp-greta-ternyata-sejahat-itu",
                                    "text isi": "Inti percakapan yang diunggah Greta Irene, menunjukkan Gaga Muhammad memang tak memiliki itikad untuk bertanggung jawab atas yang dialami",
                                    "kategori": "https://www.tribunnews.com/seleb",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "4 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/gaga-muhammad-ingin-lihat-jenazah-laura-anna.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "MotoGP",
                                    "url judul": "https://www.tribunnews.com/topic/motogp",
                                    "text subjudul": "Jadwal Tayang MotoGP 2022 Live Trans7 - Quartararo Was-was Lihat Rider Ducati yang Kian",
                                    "url subjudul": "https://www.tribunnews.com/sport/2022/01/19/jadwal-tayang-motogp-2022-live-trans7-quartararo-was-was-lihat-rider-ducati-yang-kian-mengancam",
                                    "text isi": ".Pembalap Yamaha, Fabio Quartararo mewaspadai delapan rider Ducati untuk perburuan gelar juara dunia MotoGP 2022",
                                    "kategori": "https://www.tribunnews.com/sport",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "4 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/jorge-martin-kedua-dari-kiri-berlomba-untuk-balapan-pertama.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Buku Tematik",
                                    "url judul": "https://www.tribunnews.com/topic/buku-tematik",
                                    "text subjudul": "Kunci Jawaban Tema 7 Kelas 6 Halaman 16 17 19 20 Pembelajaran 2 Subtema 1",
                                    "url subjudul": "https://www.tribunnews.com/pendidikan/2022/01/19/kunci-jawaban-tema-7-kelas-6-halaman-16-17-19-20-pembelajaran-2-subtema-1",
                                    "text isi": "Kunci Jawaban Tema 7 Kelas 6 Halaman 16 17 19 20 Buku Tematik SD, Apa perbedaan fisik perempuan sebelum dan setelah masa pubertas?",
                                    "kategori": "https://www.tribunnews.com/pendidikan",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "4 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/tangkap-gambar-buku-tematik-kelas-6-tema-7-halaman-13.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "top stories": [
                                {
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/gedung-baru-kpk_20160222_231400.jpg",
                                    "text": "Dalam 2 Pekan, 2 Kepala Daerah dari Golkar Ditangkap KPK, Berikut Kronologisnya Dalam 2 Pekan, 2 Kepala Daerah dari Golkar Ditangkap KPK, Berikut",
                                    "url": "https://www.tribunnews.com/nasional/2022/01/19/dalam-2-pekan-2-kepala-daerah-dari-golkar-ditangkap-kpk-berikut-kronologisnya"
                                },
                                {
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/drama-korea-ghost-doctor-1.jpg",
                                    "text": "6 Dokter Keren dalam Drama Korea Ghost Doctor, Siapa Favoritmu?",
                                    "url": "https://www.tribunnews.com/seleb/2022/01/18/6-dokter-keren-dalam-drama-korea-ghost-doctor-siapa-favoritmu"
                                },
                                {
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/cuplikan-video-yang-diunggah-mia-di-akun-tiktoknya2.jpg",
                                    "text": "Viral Suami Rela Pakai Daster agar sang Anak Tenang dan Tertidur, Sikapnya Tuai",
                                    "url": "https://www.tribunnews.com/regional/2022/01/18/viral-suami-rela-pakai-daster-agar-sang-anak-tenang-dan-tertidur-sikapnya-tuai-pujian"
                                }
                            ]
                        }
                    ]
                },
                {
                    "aside": [
                        {
                            "text": "berita POPULER",
                            "isi": [
                                {
                                    "text": "Bupati Langkat yang Terjaring OTT KPK Termasuk Kepala Daerah",
                                    "url": "https://www.tribunnews.com/nasional/2022/01/19/bupati-langkat-yang-terjaring-ott-kpk-termasuk-kepala-daerah-terkaya-versi-lhkpn-hartanya-rp-85-m",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/bupati-langkat-terbit-rencana-peranginangin-19122.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "5 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "Ditetapkan Tersangka karena Laporan Anak Ahok, Ini Respons Ayu Thalia Saat Diminta Klarifikasi",
                                    "url": "https://www.tribunnews.com/seleb/2022/01/19/ditetapkan-tersangka-karena-laporan-anak-ahok-ini-respons-ayu-thalia-saat-diminta-klarifikasi",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/selebgram-ayu-thalia-atau-thata-anma-akhirnya-bu.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "5 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "Persija Jakarta Tak Kuasa Lawan Ketatnya Persaingan BRI Liga 1,",
                                    "url": "https://www.tribunnews.com/superskor/2022/01/19/persija-jakarta-tak-kuasa-lawan-ketatnya-persaingan-bri-liga-1-persib-bandung-ngekor-ganti-pelatih",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/persija-jakarta-taklukan-persib-bandung-dengan-1-0_20211121_190217.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "5 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "Tanda-tanda Arema FC Bisa Juara BRI Liga 1 2021: Depan dan Belakang Sing",
                                    "url": "https://www.tribunnews.com/superskor/2022/01/19/tanda-tanda-arema-fc-bisa-juara-bri-liga-1-2021-depan-dan-belakang-singo-edan-makin-oke",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/arema-fc-bungkap-pss-sleman-2-0-tanpa-balas_20220116_182934.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "4 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "Striker Persib Disemprit Wasit di Lapangan Sendiri, Aturan Offside Liga 1 Jadi",
                                    "url": "https://www.tribunnews.com/superskor/2022/01/19/striker-persib-disemprit-wasit-di-lapangan-sendiri-aturan-offside-liga-1-jadi-sorotan",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/david-da-silva-saat-menerima-umpan-bruno-cantanhede.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "3 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "Ditangkap KPK, Bupati Langkat Pakai Celana Pendek Saat Digelandang",
                                    "url": "https://www.tribunnews.com/nasional/2022/01/19/ditangkap-kpk-bupati-langkat-pakai-celana-pendek-saat-digelandang-ke-kantor-polisi",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ati-kabupaten-langkat-terbit-rencana-peranginangin-vv.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "4 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "Ramai-ramai Maskapai Penerbangan Batalkan Tujuan ke AS, Usai Dapat",
                                    "url": "https://www.tribunnews.com/internasional/2022/01/19/ramai-ramai-maskapai-penerbangan-batalkan-tujuan-ke-as-usai-dapat-peringatan-faa-soal-menara-5g",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ilustrasi-penerbangan-tersibuk_20180704_190355.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "4 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "RAMALAN ZODIAK CINTA Kamis, 20 Januari 2022: Virgo Romantis pada",
                                    "url": "https://www.tribunnews.com/lifestyle/2022/01/19/ramalan-zodiak-cinta-kamis-20-januari-2022-virgo-romantis-pada-kekasih-capricorn-sibuk-menyendiri",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ramalan-zodiak-cinta-1762019.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "4 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "Ramalan Zodiak Kamis 20 Januari 2022: Scorpio Sangat Ambisius, Aquarius",
                                    "url": "https://www.tribunnews.com/lifestyle/2022/01/19/ramalan-zodiak-kamis-20-januari-2022-scorpio-sangat-ambisius-aquarius-berkomitmen-tinggi",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ramalan-zodiak-2022.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "5 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text": "Bareskrim Bongkar Aplikasi Robot Trading Ilegal Pakai Sistem Ponzi, ",
                                    "url": "https://www.tribunnews.com/nasional/2022/01/19/bareskrim-bongkar-aplikasi-robot-trading-ilegal-pakai-sistem-ponzi-6-orang-jadi-tersangka",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ilustrasi-trading-forex1.jpg",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "4 jam lalu",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "text": "topik POPULER",
                            "isi": [
                                {
                                    "text": "01. Liga 1",
                                    "url": "https://www.tribunnews.com/topics/liga-1"
                                },
                                {
                                    "text": "02. OTT KPK di Langkat",
                                    "url": "https://www.tribunnews.com/topics/ott-kpk-di-langkat"
                                },
                                {
                                    "text": "03. Pemindahan Ibu Kota Negara",
                                    "url": "https://www.tribunnews.com/topics/pemindahan-ibu-kota-negara"
                                },
                                {
                                    "text": "04. Kasus Gaga Muhammad dan Laura Anna",
                                    "url": "https://www.tribunnews.com/topics/kasus-gaga-muhammad-dan-laura-anna"
                                },
                                {
                                    "text": "05. Jabatan Pangkostrad",
                                    "url": "https://www.tribunnews.com/topics/jabatan-pangkostrad"
                                },
                                {
                                    "text": "06. Virus Corona",
                                    "url": "https://www.tribunnews.com/topics/virus-corona"
                                },
                                {
                                    "text": "07. Harga Minyak Goreng",
                                    "url": "https://www.tribunnews.com/topics/harga-minyak-goreng"
                                },
                                {
                                    "text": "08. Berita Populer Hari Ini",
                                    "url": "https://www.tribunnews.com/topics/berita-populer-hari-ini"
                                },
                                {
                                    "text": "09. Ramalan Zodiak",
                                    "url": "https://www.tribunnews.com/topics/ramalan-zodiak"
                                },
                                {
                                    "text": "10. Liga Inggris",
                                    "url": "https://www.tribunnews.com/topics/liga-inggris"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class beranda_body_slider(Resource):
    def get(self):
        return {
            "data": [
                {
                    "slider": [
                        {
                            "text": "Gempa di Banten",
                            "url": "https://www.tribunnews.com/topic/gempa-di-banten",
                            "berita": [
                                {
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/irjen-pol-rudy-heriyanto-yuhu.jpg",
                                    "text": "Kapolda Banten Tinju Posko Pengungsian Gempa di Pandeglang",
                                    "url": "https://www.tribunnews.com/regional/2022/01/15/kapolda-banten-tinjau-posko-pengungsian-gempa-di-pandeglang"
                                },
                                {
                                    "gambar": "https://www.tribunnews.com/regional/2022/01/15/1100-rumah-di-pandeglang-rusak-akibat-gempa-banten",
                                    "text": "1100 Rumah di Pandeglang Rusak Akibat Gempa Banten",
                                    "url": "https://www.tribunnews.com/regional/2022/01/15/1100-rumah-di-pandeglang-rusak-akibat-gempa-banten"
                                }
                            ]
                        },
                        {
                            "text": "Pemindahan Ibu Kota Negara",
                            "url": "https://www.tribunnews.com/topic/pemindahan-ibu-kota-negara",
                            "berita": [
                                {
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/desain-istana-di-ibu-kota-negara-yang-baru-di-kaltim.jpg",
                                    "text": "Presiden Jokowi Sudah Mengantongi Nama Ibu Kota Negara",
                                    "url": "https://www.tribunnews.com/nasional/2022/01/15/presiden-jokowi-disebut-sudah-mengantongi-nama-ibu-kota-negara"
                                },
                                {
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/wakil-ketua-komisi-ii-dpr-ri-saan-mustopa-1811.jpg",
                                    "text": "Pimpinan Pansus: Kepala Daerah IKN Baru Setingkat Menteri dan Dipilih Langsung Presiden",
                                    "url": "https://www.tribunnews.com/nasional/2022/01/14/pimpinan-pansus-kepala-daerah-ikn-baru-setingkat-menteri-dan-dipilih-langsung-presiden"
                                }
                            ]
                        },
                        {
                            "text": "Liga Inggris",
                            "url": "https://www.tribunnews.com/topic/liga-inggris",
                            "berita": [
                                {
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/keseruan-duel-aston-villa-vs-manchester-united-dapat-disaksikan-secara-gratis-melalui-sctv.jpg",
                                    "text": "Live Streaming TV Online SCTV, Aston Villa vs Manchester United Liga Inggris, Akses di Sini Gratis",
                                    "url": "https://www.tribunnews.com/superskor/2022/01/15/live-streaming-tv-online-sctv-aston-villa-vs-manchester-united-liga-inggris-akses-di-sini-gratis"
                                },
                                {
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/kevin-de-bruyne-setelah-mencetak-gol-ke-gawang-chelsea.jpg",
                                    "text": "Hasil Liga Inggris: Gol Sarat Makna Kevin De Bruyne Bawa Manchester City Libas Chelsea",
                                    "url": "https://www.tribunnews.com/superskor/2022/01/15/hasil-liga-inggris-gol-sarat-makna-kevin-de-bruyne-bawa-manchester-city-libas-chelsea"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class beranda_body_section_berita1(Resource):
    def get(self):
        return {
            "data": [
                {
                    "section berita1": [
                        {
                            "text judul": "OTT KPK di Langkat",
                            "url judul": "https://www.tribunnews.com/topic/ott-kpk-di-langkat",
                            "text subjudul": "Perluas Pasar, Traveloka dan Bluebird Operasikan Layanan Pemesanan Taksi QuickRide di 16 Kota",
                            "url": "https://www.tribunnews.com/bisnis/2022/01/19/perluas-pasar-traveloka-dan-bluebird-operasikan-layanan-pemesanan-taksi-quickride-di-16-kota",
                            "text isi": "Layanan ini tersedia di 16 kota besar dan destinasi pariwisata di mana terdapat jaringan taksi Bluebird dan bisa diakses melalui aplikasi Traveloka.",
                            "kategori": "https://www.tribunnews.com/nasional",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "2 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ati-kabupaten-langkat-terbit-rencana-peranginangin-vv.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Harga Minyak Goreng",
                            "url judul": "https://www.tribunnews.com/topic/harga-minyak-goreng",
                            "text subjudul": "Harga Minyak Goreng Resmi Jadi Rp 14 Ribu per Liter, Ibu-ibu di Gowa Ramai Kunjungi Ritel",
                            "url subjudul": "https://www.tribunnews.com/bisnis/2022/01/19/harga-minyak-goreng-resmi-jadi-rp-14-ribu-per-liter-ibu-ibu-di-gowa-ramai-kunjungi-ritel-modern",
                            "text isi": "Pemerintah telah menetapkan kebijakan satu harga minyak goreng menjadi Rp 14 ribu di ritel modern seluruh Indonesia, Rabu(19/1/2022)",
                            "kategori": "https://www.tribunnews.com/bisnis",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": " 34 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/salah-satu-toko-modern-di-kabupaten-bulukumba-sulsel-rabu-1912022.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Diperiksa Penyidik, Jokowi Mania Klaim Dosen UNJ Sebar Fitnah Kepada Anak Jokowi",
                            "url": "https://www.tribunnews.com/nasional/2022/01/19/diperiksa-penyidik-jokowi-mania-klaim-dosen-unj-sebar-fitnah-kepada-anak-jokowi",
                            "text isi": "Tim kuasa hukum Jokowi Mania kembali menyambangi Polda Metro Jaya terkait laporan terhadap dosen Universitas Negeri Jakarta, Ubedilah Badrun.",
                            "kategori": "https://www.tribunnews.com/nasional",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "5 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/kuasa-hukum-relawan-jokowi-mania-bambang-sri-11.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Pemindahan Ibu Kota Negara",
                            "url judul": "https://www.tribunnews.com/topic/pemindahan-ibu-kota-negara",
                            "text subjudul": "Jokowi Sebut Kemungkinan Istana akan Pindah ke Ibu Kota Negara yang Baru pada 2024",
                            "url": "https://www.tribunnews.com/nasional/2022/01/19/jokowi-sebut-kemungkinan-istana-akan-pindah-ke-ibu-kota-negara-yang-baru-pada-2024",
                            "text isi": "Jokowi memperkirakan, proses perpindahan ke ibu kota negara baru tersebut akan memakan waktu hingga 20 tahun.",
                            "kategori": "https://www.tribunnews.com/nasional",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": " 11 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/jkw-jangan-panik.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Chord Gitar",
                            "url judul": "https://www.tribunnews.com/topic/chord-gitar",
                            "text subjudul": "Chord Gitar Rungokno Aku - Ndarboy Genk feat Denny Caknan, Lengkap dengan Lirik Lagunya",
                            "url subjudul": "https://www.tribunnews.com/seleb/2022/01/19/chord-gitar-rungokno-aku-ndarboy-genk-feat-denny-caknan-lengkap-dengan-lirik-lagunya",
                            "text isi": "Lagu berjudul Rungokno Aku dinyanyikan dan dipopulerkan oleh Ndarboy Genk feat Denny Caknan, simak chord gitar dan lirik lagunya berikut ini.",
                            "kategori": "https://www.tribunnews.com/seleb",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "12 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/lagu-rungokno-aku.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Sekjen Kemnaker: Kemnaker Corpu Alat Stratgis Cetak SDM ASN yang Kompeten",
                            "url judul": "https://www.tribunnews.com/kilas-kementerian/2022/01/19/sekjen-kemnaker-kemnaker-corpu-alat-stratgis-cetak-sdm-asn-yang-kompeten",
                            "text isi": "Kemnaker Corpu dalam penerapannya akan dilaksanakan oleh Pusat Pengembangan SDM (PPSDM) Ketenagakerjaan dengan pelibatan seluruh",
                            "kategori": "https://www.tribunnews.com/kilas-kementerian",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "2 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/kemnaker-corpu-alat-stratgis-cetak-sdm-asn-yang-kompeten.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Kasus Gaga Muhammad dan Laura Anna",
                            "url judul": "https://www.tribunnews.com/topic/kasus-gaga-muhammad-dan-laura-anna",
                            "text subjudul": "Menangis Baca Percakapan Laura Anna dan Gaga Muhammad di HP, Greta: Ternyata Sejahat Itu",
                            "url subjudul": "https://www.tribunnews.com/seleb/2022/01/19/menangis-baca-percakapan-laura-anna-dan-gaga-muhammad-di-hp-greta-ternyata-sejahat-itu",
                            "text isi": "Inti percakapan yang diunggah Greta Irene, menunjukkan Gaga Muhammad memang tak memiliki itikad untuk bertanggung jawab atas yang dialami",
                            "kategori": "https://www.tribunnews.com/seleb",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "4 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/gaga-muhammad-ingin-lihat-jenazah-laura-anna.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "MotoGP",
                            "url judul": "https://www.tribunnews.com/topic/motogp",
                            "text subjudul": "Jadwal Tayang MotoGP 2022 Live Trans7 - Quartararo Was-was Lihat Rider Ducati yang Kian",
                            "url subjudul": "https://www.tribunnews.com/sport/2022/01/19/jadwal-tayang-motogp-2022-live-trans7-quartararo-was-was-lihat-rider-ducati-yang-kian-mengancam",
                            "text isi": ".Pembalap Yamaha, Fabio Quartararo mewaspadai delapan rider Ducati untuk perburuan gelar juara dunia MotoGP 2022",
                            "kategori": "https://www.tribunnews.com/sport",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "4 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/jorge-martin-kedua-dari-kiri-berlomba-untuk-balapan-pertama.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Buku Tematik",
                            "url judul": "https://www.tribunnews.com/topic/buku-tematik",
                            "text subjudul": "Kunci Jawaban Tema 7 Kelas 6 Halaman 16 17 19 20 Pembelajaran 2 Subtema 1",
                            "url subjudul": "https://www.tribunnews.com/pendidikan/2022/01/19/kunci-jawaban-tema-7-kelas-6-halaman-16-17-19-20-pembelajaran-2-subtema-1",
                            "text isi": "Kunci Jawaban Tema 7 Kelas 6 Halaman 16 17 19 20 Buku Tematik SD, Apa perbedaan fisik perempuan sebelum dan setelah masa pubertas?",
                            "kategori": "https://www.tribunnews.com/pendidikan",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "4 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/tangkap-gambar-buku-tematik-kelas-6-tema-7-halaman-13.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class beranda_body_top_stories(Resource):
    def get(self):
        return {
            "data": [
                {
                    "top stories": [
                        {
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/gedung-baru-kpk_20160222_231400.jpg",
                            "text": "Dalam 2 Pekan, 2 Kepala Daerah dari Golkar Ditangkap KPK, Berikut Kronologisnya Dalam 2 Pekan, 2 Kepala Daerah dari Golkar Ditangkap KPK, Berikut",
                            "url": "https://www.tribunnews.com/nasional/2022/01/19/dalam-2-pekan-2-kepala-daerah-dari-golkar-ditangkap-kpk-berikut-kronologisnya"
                        },
                        {
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/drama-korea-ghost-doctor-1.jpg",
                            "text": "6 Dokter Keren dalam Drama Korea Ghost Doctor, Siapa Favoritmu?",
                            "url": "https://www.tribunnews.com/seleb/2022/01/18/6-dokter-keren-dalam-drama-korea-ghost-doctor-siapa-favoritmu"
                        },
                        {
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/cuplikan-video-yang-diunggah-mia-di-akun-tiktoknya2.jpg",
                            "text": "Viral Suami Rela Pakai Daster agar sang Anak Tenang dan Tertidur, Sikapnya Tuai",
                            "url": "https://www.tribunnews.com/regional/2022/01/18/viral-suami-rela-pakai-daster-agar-sang-anak-tenang-dan-tertidur-sikapnya-tuai-pujian"
                        }
                    ]
                }
            ]
        }


class beranda_aside_beritaPOPULER(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "berita POPULER",
                    "isi": [
                        {
                            "text": "Bupati Langkat yang Terjaring OTT KPK Termasuk Kepala Daerah",
                            "url": "https://www.tribunnews.com/nasional/2022/01/19/bupati-langkat-yang-terjaring-ott-kpk-termasuk-kepala-daerah-terkaya-versi-lhkpn-hartanya-rp-85-m",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/bupati-langkat-terbit-rencana-peranginangin-19122.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "5 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "Ditetapkan Tersangka karena Laporan Anak Ahok, Ini Respons Ayu Thalia Saat Diminta Klarifikasi",
                            "url": "https://www.tribunnews.com/seleb/2022/01/19/ditetapkan-tersangka-karena-laporan-anak-ahok-ini-respons-ayu-thalia-saat-diminta-klarifikasi",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/selebgram-ayu-thalia-atau-thata-anma-akhirnya-bu.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "5 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "Persija Jakarta Tak Kuasa Lawan Ketatnya Persaingan BRI Liga 1,",
                            "url": "https://www.tribunnews.com/superskor/2022/01/19/persija-jakarta-tak-kuasa-lawan-ketatnya-persaingan-bri-liga-1-persib-bandung-ngekor-ganti-pelatih",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/persija-jakarta-taklukan-persib-bandung-dengan-1-0_20211121_190217.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "5 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "Tanda-tanda Arema FC Bisa Juara BRI Liga 1 2021: Depan dan Belakang Sing",
                            "url": "https://www.tribunnews.com/superskor/2022/01/19/tanda-tanda-arema-fc-bisa-juara-bri-liga-1-2021-depan-dan-belakang-singo-edan-makin-oke",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/arema-fc-bungkap-pss-sleman-2-0-tanpa-balas_20220116_182934.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "4 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "Striker Persib Disemprit Wasit di Lapangan Sendiri, Aturan Offside Liga 1 Jadi",
                            "url": "https://www.tribunnews.com/superskor/2022/01/19/striker-persib-disemprit-wasit-di-lapangan-sendiri-aturan-offside-liga-1-jadi-sorotan",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/david-da-silva-saat-menerima-umpan-bruno-cantanhede.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "3 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "Ditangkap KPK, Bupati Langkat Pakai Celana Pendek Saat Digelandang",
                            "url": "https://www.tribunnews.com/nasional/2022/01/19/ditangkap-kpk-bupati-langkat-pakai-celana-pendek-saat-digelandang-ke-kantor-polisi",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ati-kabupaten-langkat-terbit-rencana-peranginangin-vv.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "4 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "Ramai-ramai Maskapai Penerbangan Batalkan Tujuan ke AS, Usai Dapat",
                            "url": "https://www.tribunnews.com/internasional/2022/01/19/ramai-ramai-maskapai-penerbangan-batalkan-tujuan-ke-as-usai-dapat-peringatan-faa-soal-menara-5g",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ilustrasi-penerbangan-tersibuk_20180704_190355.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "4 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "RAMALAN ZODIAK CINTA Kamis, 20 Januari 2022: Virgo Romantis pada",
                            "url": "https://www.tribunnews.com/lifestyle/2022/01/19/ramalan-zodiak-cinta-kamis-20-januari-2022-virgo-romantis-pada-kekasih-capricorn-sibuk-menyendiri",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ramalan-zodiak-cinta-1762019.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "4 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "Ramalan Zodiak Kamis 20 Januari 2022: Scorpio Sangat Ambisius, Aquarius",
                            "url": "https://www.tribunnews.com/lifestyle/2022/01/19/ramalan-zodiak-kamis-20-januari-2022-scorpio-sangat-ambisius-aquarius-berkomitmen-tinggi",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ramalan-zodiak-2022.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "5 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text": "Bareskrim Bongkar Aplikasi Robot Trading Ilegal Pakai Sistem Ponzi, ",
                            "url": "https://www.tribunnews.com/nasional/2022/01/19/bareskrim-bongkar-aplikasi-robot-trading-ilegal-pakai-sistem-ponzi-6-orang-jadi-tersangka",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ilustrasi-trading-forex1.jpg",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "4 jam lalu",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class beranda_aside_topikPOPULER(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "topik POPULER",
                    "isi": [
                        {
                            "text": "01. Liga 1",
                            "url": "https://www.tribunnews.com/topics/liga-1"
                        },
                        {
                            "text": "02. OTT KPK di Langkat",
                            "url": "https://www.tribunnews.com/topics/ott-kpk-di-langkat"
                        },
                        {
                            "text": "03. Pemindahan Ibu Kota Negara",
                            "url": "https://www.tribunnews.com/topics/pemindahan-ibu-kota-negara"
                        },
                        {
                            "text": "04. Kasus Gaga Muhammad dan Laura Anna",
                            "url": "https://www.tribunnews.com/topics/kasus-gaga-muhammad-dan-laura-anna"
                        },
                        {
                            "text": "05. Jabatan Pangkostrad",
                            "url": "https://www.tribunnews.com/topics/jabatan-pangkostrad"
                        },
                        {
                            "text": "06. Virus Corona",
                            "url": "https://www.tribunnews.com/topics/virus-corona"
                        },
                        {
                            "text": "07. Harga Minyak Goreng",
                            "url": "https://www.tribunnews.com/topics/harga-minyak-goreng"
                        },
                        {
                            "text": "08. Berita Populer Hari Ini",
                            "url": "https://www.tribunnews.com/topics/berita-populer-hari-ini"
                        },
                        {
                            "text": "09. Ramalan Zodiak",
                            "url": "https://www.tribunnews.com/topics/ramalan-zodiak"
                        },
                        {
                            "text": "10. Liga Inggris",
                            "url": "https://www.tribunnews.com/topics/liga-inggris"
                        }
                    ]
                }
            ]
        }


class news(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "News",
                    "url": "https://www.tribunnews.com/news",
                    "content": [
                            {
                                "header": [
                                    {
                                        "icon": "lg lg-twhiteicon",
                                        "url": "https://www.tribunnews.com/",
                                        "hover": [
                                            {
                                                "text": "News",
                                                "url": "https://www.tribunnews.com/news"
                                            },
                                            {
                                                "text": "Bisnis",
                                                "url": "https://www.tribunnews.com/bisnis"
                                            },
                                            {
                                                "text": "Super Skor",
                                                "url": "https://www.tribunnews.com/superskor"
                                            },
                                            {
                                                "text": "Sport",
                                                "url": "https://www.tribunnews.com/sport"
                                            },
                                            {
                                                "text": "Seleb",
                                                "url": "https://www.tribunnews.com/seleb"
                                            },
                                            {
                                                "text": "Lifestyle",
                                                "url": "https://www.tribunnews.com/lifestyle"
                                            },
                                            {
                                                "text": "New Economy",
                                                "url": "https://www.tribunnews.com/new-economy"
                                            },
                                            {
                                                "text": "PARAPUAN",
                                                "url": "https://www.tribunnews.com/parapuan"
                                            },
                                            {
                                                "text": "Otomotif",
                                                "url": "https://www.tribunnews.com/otomotif"
                                            },
                                            {
                                                "text": "Techno",
                                                "url": "https://www.tribunnews.com/techno"
                                            },
                                            {
                                                "text": "Kesehatan",
                                                "url": "https://www.tribunnews.com/kesehatan"
                                            },
                                            {
                                                "text": "Video",
                                                "url": "https://www.tribunnews.com/video"
                                            },
                                            {
                                                "text": "Images",
                                                "url": "https://www.tribunnews.com/images"
                                            },
                                            {
                                                "text": "Tribunners",
                                                "url": "https://www.tribunnews.com/tribunners"
                                            },
                                            {
                                                "text": "Indeks Berita",
                                                "url": "https://www.tribunnews.com/indeks"
                                            }
                                        ]
                                    },
                                    {
                                        "text": "Home",
                                        "url": "https://www.tribunnews.com/news"
                                    },
                                    {
                                        "text": "Nasional",
                                        "url": "https://www.tribunnews.com/nasional"
                                    },
                                    {
                                        "text": "Internasional",
                                        "url": "https://www.tribunnews.com/internasional"
                                    },
                                    {
                                        "text": "Regional",
                                        "url": "https://www.tribunnews.com/regional"
                                    },
                                    {
                                        "text": "Metropolitan",
                                        "url": "https://www.tribunnews.com/metropolitan"
                                    },
                                    {
                                        "text": "Sains",
                                        "url": "https://www.tribunnews.com/sains"
                                    },
                                    {
                                        "text": "Pendidikan",
                                        "url": "https://www.tribunnews.com/pendidikan"
                                    }
                                ]
                            },
                        {
                                "body": [
                                    {
                                        "text": "News",
                                        "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images2/uid-bali-bakal-jadi-kampus-terpadu-nih3.jpg",
                                        "judul": "Universitas Ternama dari AS & China Pilih Dirikan Kampus Bersama di Indonesia, Eks PM Malaysia Iri",
                                        "url": "https://www.tribunnews.com/internasional/2022/01/20/universitas-ternama-dari-as-china-pilih-dirikan-kampus-bersama-di-indonesia-eks-pm-malaysia-iri"
                                    },
                                    {
                                        "text judul": "Polemik Ucapan Arteria Dahlan",
                                        "url judul": "https://www.tribunnews.com/topic/polemik-ucapan-arteria-dahlan",
                                        "text subjudul": "Momen Petinggi Sunda Empire Lord Rangga Datangi Gedung DPR RI Ingin Labrak Arteria",
                                        "url subjudul": "https://www.tribunnews.com/nasional/2022/01/20/momen-petinggi-sunda-empire-lord-rangga-datangi-gedung-dpr-ri-ingin-labrak-arteria-dahlan",
                                        "text isi": "Petinggi Sunda Empire Ki Ageng Rangga Sasana mendatangi Gedung DPR RI, Kompleks Perlemen Senayan, Jakarta, Kamis (20/1/2022).",
                                        "kategori": "https://www.tribunnews.com/nasional",
                                        "icon": "fa fa-clock-o mr7",
                                        "waktu": "1 menit lalu",
                                        "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/petinggi-sunda-empire-ki-ageng-rangga-sasana-nih3.jpg",
                                        "sosmed": [
                                            {
                                                "icon": "fa fa facebook",
                                                "text": "shere",
                                                "url": "javascript:void(0)"
                                            },
                                            {
                                                "icon": "twitter",
                                                "text": "tweet",
                                                "url": "javascript:void(0)"
                                            }
                                        ]
                                    },
                                    {
                                        "text judul": "Mahasiswi UI Tewas Ditabrak KRL di Perlintasan Stasiun Pondok Cina Kota Depok, Berikut",
                                        "url judul": "https://www.tribunnews.com/metropolitan/2022/01/20/mahasiswi-ui-ditabrak-krl-di-perlintasan-stasiun-pondok-cina-kota-depok-berikut-kronologisnya",
                                        "text isi": "Saat ini, jasad korban sudah dibawa menggunakan mobil ambulans dan kasusnya ditangani Kepolisian Sektor Beji, Kota Depok.",
                                        "kategori": "https://www.tribunnews.com/metropolitan",
                                        "icon": "fa fa-clock-o mr7",
                                        "waktu": "10 menit lalu",
                                        "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/seorang-wanita-diduga-mahasiswi-tewas-mengenaskan-usa.jpg",
                                        "sosmed": [
                                            {
                                                "icon": "fa fa facebook",
                                                "text": "shere",
                                                "url": "javascript:void(0)"
                                            },
                                            {
                                                "icon": "twitter",
                                                "text": "tweet",
                                                "url": "javascript:void(0)"
                                            }
                                        ]
                                    },
                                    {
                                        "text judul": "Remaja Semarang Meninggal Usai Tertimbun Longsor, Korban Tengah Beristirahat dalam",
                                        "url judul": "https://www.tribunnews.com/regional/2022/01/20/remaja-semarang-meninggal-usai-tertimbun-longsor-korban-tengah-beristirahat-dalam-kamar",
                                        "text isi": "Saat itu korban yang bekerja sebagai tukang tambal ban itu sedang beristirahat di kamarnya",
                                        "kategori": "https://www.tribunnews.com/regional",
                                        "icon": "fa fa-clock-o mr7",
                                        "waktu": "12 menit lalu",
                                        "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ilustrasi-mayat_20180826_182838.jpg",
                                        "sosmed": [
                                            {
                                                "icon": "fa fa facebook",
                                                "text": "shere",
                                                "url": "javascript:void(0)"
                                            },
                                            {
                                                "icon": "twitter",
                                                "text": "tweet",
                                                "url": "javascript:void(0)"
                                            }
                                        ]
                                    },
                                    {
                                        "text judul": "Aparat Polsek Duren Sawit Tangkap Suami Bunuh Istri Usai Berhubungan Badan di Sebuah Salon",
                                        "url judul": "https://www.tribunnews.com/metropolitan/2022/01/20/aparat-polsek-duren-sawit-tangkap-suami-bunuh-istri-usai-berhubungan-badan-di-sebuah-salon",
                                        "text isi": "W (41) pelaku pembunuhan istrinya sendiri SS (29) diringkus aparat Polsek Duren Sawit, Jakarta Timur di sebuah salon.",
                                        "kategori": "https://www.tribunnews.com/metropolitan",
                                        "icon": "fa fa-clock-o mr7",
                                        "waktu": "16 menit lalu",
                                        "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/kontrakan-lokasi-istri-dibunuh.jpg",
                                        "sosmed": [
                                            {
                                                "icon": "fa fa facebook",
                                                "text": "shere",
                                                "url": "javascript:void(0)"
                                            },
                                            {
                                                "icon": "twitter",
                                                "text": "tweet",
                                                "url": "javascript:void(0)"
                                            }
                                        ]
                                    }
                                ]
                            },
                        {
                                "aside": [
                                    {
                                        "text": "berita POPULER",
                                        "isi": [
                                            {
                                                "text": "Perbandingan Harta 4 Mayjen TNI yang Berpeluang Jadi",
                                                "url": "https://www.tribunnews.com/nasional/2022/01/20/perbandingan-harta-4-mayjen-tni-yang-berpeluang-jadi-pangkostrad-maruli-simanjuntak-paling-kaya",
                                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/4-mayjen-tni-berpeluang-jadi-pangkostrad.jpg",
                                                "icon": "fa fa-clock-o mr7",
                                                "waktu": "11 jam lalu",
                                                "sosmed": [
                                                    {
                                                        "icon": "fa fa facebook",
                                                        "text": "shere",
                                                        "url": "javascript:void(0)"
                                                    },
                                                    {
                                                        "icon": "twitter",
                                                        "text": "tweet",
                                                        "url": "javascript:void(0)"
                                                    }
                                                ]
                                            },
                                            {
                                                "text": "Ridwan Kamil Unggah Video Arteria Dahlan Ngomong Sunda, Singgun",
                                                "url": "https://www.tribunnews.com/nasional/2022/01/20/ridwan-kamil-unggah-video-arteria-dahlan-ngomong-sunda-singgung-cara-komunikasi-jokowi-bung-karno",
                                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/arteria-dahlan-dan-ridwan-kamil-20122.jpg",
                                                "icon": "fa fa-clock-o mr7",
                                                "waktu": "3 jam lalu",
                                                "sosmed": [
                                                    {
                                                        "icon": "fa fa facebook",
                                                        "text": "shere",
                                                        "url": "javascript:void(0)"
                                                    },
                                                    {
                                                        "icon": "twitter",
                                                        "text": "tweet",
                                                        "url": "javascript:void(0)"
                                                    }
                                                ]
                                            },
                                            {
                                                "text": "OTT KPK di Jawa Timur Terkait Suap Penanganan Perkara di PN Surabaya",
                                                "url": "https://www.tribunnews.com/nasional/2022/01/20/ott-kpk-di-jawa-timur-terkait-suap-penanganan-perkara-di-pn-surabaya",
                                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/gedung-baru-kpk-1.jpg",
                                                "icon": "fa fa-clock-o mr7",
                                                "waktu": "8 jam lalu",
                                                "sosmed": [
                                                    {
                                                        "icon": "fa fa facebook",
                                                        "text": "shere",
                                                        "url": "javascript:void(0)"
                                                    },
                                                    {
                                                        "icon": "twitter",
                                                        "text": "tweet",
                                                        "url": "javascript:void(0)"
                                                    }
                                                ]
                                            },
                                            {
                                                "text": "Deretan OTT KPK di Awal Tahun 2022, Ada Bupati Langkat, Terbaru Hakim",
                                                "url": "https://www.tribunnews.com/nasional/2022/01/20/deretan-ott-kpk-di-awal-tahun-2022-ada-bupati-langkat-terbaru-hakim-pn-surabaya",
                                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/bupati-langkat-terbit-rencana-perangin-angin-resmi-ditahan-kpk_20220120_050651.jpg",
                                                "icon": "fa fa-clock-o mr7",
                                                "waktu": "5 jam lalu",
                                                "sosmed": [
                                                    {
                                                        "icon": "fa fa facebook",
                                                        "text": "shere",
                                                        "url": "javascript:void(0)"
                                                    },
                                                    {
                                                        "icon": "twitter",
                                                        "text": "tweet",
                                                        "url": "javascript:void(0)"
                                                    }
                                                ]
                                            },
                                            {
                                                "text": "BREAKING NEWS: KPK OTT Panitera dan Pengacara di Surabaya",
                                                "url": "https://www.tribunnews.com/nasional/2022/01/20/breaking-news-kpk-ott-panitera-dan-pengacara-di-surabaya",
                                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/logo-kpk-nih.jpg",
                                                "icon": "fa fa-clock-o mr7",
                                                "waktu": "8 jam lalu",
                                                "sosmed": [
                                                    {
                                                        "icon": "fa fa facebook",
                                                        "text": "shere",
                                                        "url": "javascript:void(0)"
                                                    },
                                                    {
                                                        "icon": "twitter",
                                                        "text": "tweet",
                                                        "url": "javascript:void(0)"
                                                    }
                                                ]
                                            }
                                        ]
                                    },
                                    {
                                        "text": "tag POPULER",
                                        "isi": [
                                            {
                                                "text": "DKI Jakarta",
                                                "url": "https://www.tribunnews.com/tag/dki-jakarta"
                                            },
                                            {
                                                "text": "Bupati Langkat",
                                                "url": "https://www.tribunnews.com/tag/bupati-langkat"
                                            },
                                            {
                                                "text": "vaksin Covid-19",
                                                "url": "https://www.tribunnews.com/tag/vaksin-covid-19"
                                            },
                                            {
                                                "text": "Swiss",
                                                "url": "https://www.tribunnews.com/tag/swiss"
                                            },
                                            {
                                                "text": "Arteria Dahlan",
                                                "url": "https://www.tribunnews.com/tag/arteria-dahlan"
                                            },
                                            {
                                                "text": "Pembelajaran Tatap Muka (PTM)",
                                                "url": "https://www.tribunnews.com/tag/pembelajaran-tatap-muka-ptm"
                                            },
                                            {
                                                "text": "Polda Sumut",
                                                "url": "https://www.tribunnews.com/tag/polda-sumut"
                                            },
                                            {
                                                "text": "OTT KPK di Langkat",
                                                "url": "https://www.tribunnews.com/tag/ott-kpk-di-langkat"
                                            },
                                            {
                                                "text": "PTM",
                                                "url": "https://www.tribunnews.com/tag/ptm"
                                            },
                                            {
                                                "text": "Sumatera Utara",
                                                "url": "https://www.tribunnews.com/tag/sumatera-utara"
                                            },
                                            {
                                                "text": "virus corona",
                                                "url": "https://www.tribunnews.com/tag/virus-corona"
                                            },
                                            {
                                                "text": "OTT KPK",
                                                "url": "https://www.tribunnews.com/tag/ott-kpk"
                                            },
                                            {
                                                "text": "Covid-19",
                                                "url": "https://www.tribunnews.com/tag/covid-19"
                                            },
                                            {
                                                "text": "Lockdown di China",
                                                "url": "https://www.tribunnews.com/tag/lockdown-di-china"
                                            },
                                            {
                                                "text": "Langkat",
                                                "url": "https://www.tribunnews.com/tag/langkat"
                                            }
                                        ]
                                    }
                                ]
                            }
                    ]
                }
            ]
        }


class news_header(Resource):
    def get(self):
        return {
            "data": [
                {
                    "header": [
                        {
                            "icon": "lg lg-twhiteicon",
                            "url": "https://www.tribunnews.com/",
                            "hover": [
                                {
                                    "text": "News",
                                    "url": "https://www.tribunnews.com/news"
                                },
                                {
                                    "text": "Bisnis",
                                    "url": "https://www.tribunnews.com/bisnis"
                                },
                                {
                                    "text": "Super Skor",
                                    "url": "https://www.tribunnews.com/superskor"
                                },
                                {
                                    "text": "Sport",
                                    "url": "https://www.tribunnews.com/sport"
                                },
                                {
                                    "text": "Seleb",
                                    "url": "https://www.tribunnews.com/seleb"
                                },
                                {
                                    "text": "Lifestyle",
                                    "url": "https://www.tribunnews.com/lifestyle"
                                },
                                {
                                    "text": "New Economy",
                                    "url": "https://www.tribunnews.com/new-economy"
                                },
                                {
                                    "text": "PARAPUAN",
                                    "url": "https://www.tribunnews.com/parapuan"
                                },
                                {
                                    "text": "Otomotif",
                                    "url": "https://www.tribunnews.com/otomotif"
                                },
                                {
                                    "text": "Techno",
                                    "url": "https://www.tribunnews.com/techno"
                                },
                                {
                                    "text": "Kesehatan",
                                    "url": "https://www.tribunnews.com/kesehatan"
                                },
                                {
                                    "text": "Video",
                                    "url": "https://www.tribunnews.com/video"
                                },
                                {
                                    "text": "Images",
                                    "url": "https://www.tribunnews.com/images"
                                },
                                {
                                    "text": "Tribunners",
                                    "url": "https://www.tribunnews.com/tribunners"
                                },
                                {
                                    "text": "Indeks Berita",
                                    "url": "https://www.tribunnews.com/indeks"
                                }
                            ]
                        },
                        {
                            "text": "Home",
                            "url": "https://www.tribunnews.com/news"
                        },
                        {
                            "text": "Nasional",
                            "url": "https://www.tribunnews.com/nasional"
                        },
                        {
                            "text": "Internasional",
                            "url": "https://www.tribunnews.com/internasional"
                        },
                        {
                            "text": "Regional",
                            "url": "https://www.tribunnews.com/regional"
                        },
                        {
                            "text": "Metropolitan",
                            "url": "https://www.tribunnews.com/metropolitan"
                        },
                        {
                            "text": "Sains",
                            "url": "https://www.tribunnews.com/sains"
                        },
                        {
                            "text": "Pendidikan",
                            "url": "https://www.tribunnews.com/pendidikan"
                        }
                    ]
                }
            ]
        }


class news_body(Resource):
    def get(self):
        return {
            "data": [
                {
                    "body": [
                        {
                            "text": "News",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images2/uid-bali-bakal-jadi-kampus-terpadu-nih3.jpg",
                            "judul": "Universitas Ternama dari AS & China Pilih Dirikan Kampus Bersama di Indonesia, Eks PM Malaysia Iri",
                            "url": "https://www.tribunnews.com/internasional/2022/01/20/universitas-ternama-dari-as-china-pilih-dirikan-kampus-bersama-di-indonesia-eks-pm-malaysia-iri"
                        },
                        {
                            "text judul": "Polemik Ucapan Arteria Dahlan",
                            "url judul": "https://www.tribunnews.com/topic/polemik-ucapan-arteria-dahlan",
                            "text subjudul": "Momen Petinggi Sunda Empire Lord Rangga Datangi Gedung DPR RI Ingin Labrak Arteria",
                            "url subjudul": "https://www.tribunnews.com/nasional/2022/01/20/momen-petinggi-sunda-empire-lord-rangga-datangi-gedung-dpr-ri-ingin-labrak-arteria-dahlan",
                            "text isi": "Petinggi Sunda Empire Ki Ageng Rangga Sasana mendatangi Gedung DPR RI, Kompleks Perlemen Senayan, Jakarta, Kamis (20/1/2022).",
                            "kategori": "https://www.tribunnews.com/nasional",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "1 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/petinggi-sunda-empire-ki-ageng-rangga-sasana-nih3.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Mahasiswi UI Tewas Ditabrak KRL di Perlintasan Stasiun Pondok Cina Kota Depok, Berikut",
                            "url judul": "https://www.tribunnews.com/metropolitan/2022/01/20/mahasiswi-ui-ditabrak-krl-di-perlintasan-stasiun-pondok-cina-kota-depok-berikut-kronologisnya",
                            "text isi": "Saat ini, jasad korban sudah dibawa menggunakan mobil ambulans dan kasusnya ditangani Kepolisian Sektor Beji, Kota Depok.",
                            "kategori": "https://www.tribunnews.com/metropolitan",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "10 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/seorang-wanita-diduga-mahasiswi-tewas-mengenaskan-usa.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Remaja Semarang Meninggal Usai Tertimbun Longsor, Korban Tengah Beristirahat dalam",
                            "url judul": "https://www.tribunnews.com/regional/2022/01/20/remaja-semarang-meninggal-usai-tertimbun-longsor-korban-tengah-beristirahat-dalam-kamar",
                            "text isi": "Saat itu korban yang bekerja sebagai tukang tambal ban itu sedang beristirahat di kamarnya",
                            "kategori": "https://www.tribunnews.com/regional",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "12 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ilustrasi-mayat_20180826_182838.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Aparat Polsek Duren Sawit Tangkap Suami Bunuh Istri Usai Berhubungan Badan di Sebuah Salon",
                            "url judul": "https://www.tribunnews.com/metropolitan/2022/01/20/aparat-polsek-duren-sawit-tangkap-suami-bunuh-istri-usai-berhubungan-badan-di-sebuah-salon",
                            "text isi": "W (41) pelaku pembunuhan istrinya sendiri SS (29) diringkus aparat Polsek Duren Sawit, Jakarta Timur di sebuah salon.",
                            "kategori": "https://www.tribunnews.com/metropolitan",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "16 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/kontrakan-lokasi-istri-dibunuh.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class news_aside_beritaPOPULER(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "berita POPULER",
                    "isi": [
                            {
                                "text": "Perbandingan Harta 4 Mayjen TNI yang Berpeluang Jadi",
                                "url": "https://www.tribunnews.com/nasional/2022/01/20/perbandingan-harta-4-mayjen-tni-yang-berpeluang-jadi-pangkostrad-maruli-simanjuntak-paling-kaya",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/4-mayjen-tni-berpeluang-jadi-pangkostrad.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "11 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Ridwan Kamil Unggah Video Arteria Dahlan Ngomong Sunda, Singgun",
                                "url": "https://www.tribunnews.com/nasional/2022/01/20/ridwan-kamil-unggah-video-arteria-dahlan-ngomong-sunda-singgung-cara-komunikasi-jokowi-bung-karno",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/arteria-dahlan-dan-ridwan-kamil-20122.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "3 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "OTT KPK di Jawa Timur Terkait Suap Penanganan Perkara di PN Surabaya",
                                "url": "https://www.tribunnews.com/nasional/2022/01/20/ott-kpk-di-jawa-timur-terkait-suap-penanganan-perkara-di-pn-surabaya",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/gedung-baru-kpk-1.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "8 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Deretan OTT KPK di Awal Tahun 2022, Ada Bupati Langkat, Terbaru Hakim",
                                "url": "https://www.tribunnews.com/nasional/2022/01/20/deretan-ott-kpk-di-awal-tahun-2022-ada-bupati-langkat-terbaru-hakim-pn-surabaya",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/bupati-langkat-terbit-rencana-perangin-angin-resmi-ditahan-kpk_20220120_050651.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "5 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "BREAKING NEWS: KPK OTT Panitera dan Pengacara di Surabaya",
                                "url": "https://www.tribunnews.com/nasional/2022/01/20/breaking-news-kpk-ott-panitera-dan-pengacara-di-surabaya",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/logo-kpk-nih.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "8 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            }
                    ]
                }
            ]
        }


class news_aside_tagPOPULER(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "tag POPULER",
                    "isi": [
                            {
                                "text": "DKI Jakarta",
                                "url": "https://www.tribunnews.com/tag/dki-jakarta"
                            },
                        {
                                "text": "Bupati Langkat",
                                "url": "https://www.tribunnews.com/tag/bupati-langkat"
                            },
                        {
                                "text": "vaksin Covid-19",
                                "url": "https://www.tribunnews.com/tag/vaksin-covid-19"
                            },
                        {
                                "text": "Swiss",
                                "url": "https://www.tribunnews.com/tag/swiss"
                            },
                        {
                                "text": "Arteria Dahlan",
                                "url": "https://www.tribunnews.com/tag/arteria-dahlan"
                            },
                        {
                                "text": "Pembelajaran Tatap Muka (PTM)",
                                "url": "https://www.tribunnews.com/tag/pembelajaran-tatap-muka-ptm"
                            },
                        {
                                "text": "Polda Sumut",
                                "url": "https://www.tribunnews.com/tag/polda-sumut"
                            },
                        {
                                "text": "OTT KPK di Langkat",
                                "url": "https://www.tribunnews.com/tag/ott-kpk-di-langkat"
                            },
                        {
                                "text": "PTM",
                                "url": "https://www.tribunnews.com/tag/ptm"
                            },
                        {
                                "text": "Sumatera Utara",
                                "url": "https://www.tribunnews.com/tag/sumatera-utara"
                            },
                        {
                                "text": "virus corona",
                                "url": "https://www.tribunnews.com/tag/virus-corona"
                            },
                        {
                                "text": "OTT KPK",
                                "url": "https://www.tribunnews.com/tag/ott-kpk"
                            },
                        {
                                "text": "Covid-19",
                                "url": "https://www.tribunnews.com/tag/covid-19"
                            },
                        {
                                "text": "Lockdown di China",
                                "url": "https://www.tribunnews.com/tag/lockdown-di-china"
                            },
                        {
                                "text": "Langkat",
                                "url": "https://www.tribunnews.com/tag/langkat"
                            }
                    ]
                }
            ]
        }


class bisnis(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "Bisnis",
                    "url": "https://www.tribunnews.com/bisnis",
                    "content": [
                        {
                            "header": [
                                {
                                    "icon": "lg lg-twhiteicon",
                                    "url": "https://www.tribunnews.com/",
                                    "hover": [
                                        {
                                            "text": "News",
                                            "url": "https://www.tribunnews.com/news"
                                        },
                                        {
                                            "text": "Bisnis",
                                            "url": "https://www.tribunnews.com/bisnis"
                                        },
                                        {
                                            "text": "Super Skor",
                                            "url": "https://www.tribunnews.com/superskor"
                                        },
                                        {
                                            "text": "Sport",
                                            "url": "https://www.tribunnews.com/sport"
                                        },
                                        {
                                            "text": "Seleb",
                                            "url": "https://www.tribunnews.com/seleb"
                                        },
                                        {
                                            "text": "Lifestyle",
                                            "url": "https://www.tribunnews.com/lifestyle"
                                        },
                                        {
                                            "text": "New Economy",
                                            "url": "https://www.tribunnews.com/new-economy"
                                        },
                                        {
                                            "text": "PARAPUAN",
                                            "url": "https://www.tribunnews.com/parapuan"
                                        },
                                        {
                                            "text": "Otomotif",
                                            "url": "https://www.tribunnews.com/otomotif"
                                        },
                                        {
                                            "text": "Techno",
                                            "url": "https://www.tribunnews.com/techno"
                                        },
                                        {
                                            "text": "Kesehatan",
                                            "url": "https://www.tribunnews.com/kesehatan"
                                        },
                                        {
                                            "text": "Video",
                                            "url": "https://www.tribunnews.com/video"
                                        },
                                        {
                                            "text": "Images",
                                            "url": "https://www.tribunnews.com/images"
                                        },
                                        {
                                            "text": "Tribunners",
                                            "url": "https://www.tribunnews.com/tribunners"
                                        },
                                        {
                                            "text": "Indeks Berita",
                                            "url": "https://www.tribunnews.com/indeks"
                                        }
                                    ]
                                },
                                {
                                    "text": "Home",
                                    "url": "https://www.tribunnews.com/bisnis"
                                },
                                {
                                    "text": "Makro",
                                    "url": "https://www.tribunnews.com/bisnis/makro"
                                },
                                {
                                    "text": "Energi",
                                    "url": "https://www.tribunnews.com/bisnis/energi"
                                },
                                {
                                    "text": "Finansial",
                                    "url": "https://www.tribunnews.com/bisnis/finansial"
                                },
                                {
                                    "text": "Mikro",
                                    "url": "https://www.tribunnews.com/bisnis/mikro"
                                },
                                {
                                    "text": "Investasi",
                                    "url": "https://www.tribunnews.com/bisnis/investasi"
                                },
                                {
                                    "text": "Transportasi",
                                    "url": "https://www.tribunnews.com/bisnis/transportasi"
                                },
                                {
                                    "text": "Infrastruktur",
                                    "url": "https://www.tribunnews.com/bisnis/infrastruktur"
                                },
                                {
                                    "text": "Insight",
                                    "url": "https://www.tribunnews.com/bisnis/insight"
                                },
                                {
                                    "text": "Properti",
                                    "url": "https://www.tribunnews.com/bisnis/properti"
                                }
                            ]
                        },
                        {
                            "body": [
                                {
                                    "text": "Bisnis",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images2/wabah-corona-tak-berpengaruh-pada-harga-emas-batangan_20200320_205512.jpg",
                                    "judul": "Harga Emas Antam Melonjak Rp 12.000, Kini Jadi Rp 948.000/Gram",
                                    "url": "https://www.tribunnews.com/bisnis/2022/01/20/harga-emas-antam-melonjak-rp-12000-kini-jadi-rp-948000gram"
                                },
                                {
                                    "text judul": "Tips dan Trik",
                                    "url judul": "https://www.tribunnews.com/topic/tips-dan-trik",
                                    "text subjudul": "Tips Atur Keuangan Bulanan, Pilih Hiburan Murah hingga Sisihkan Uang di Awal Bulan",
                                    "url subjudul": "https://www.tribunnews.com/bisnis/2022/01/20/tips-atur-keuangan-bulanan-pilih-hiburan-murah-hingga-sisihkan-uang-di-awal-bulan",
                                    "text isi": "Berikut tips mengatur keuangan bulanan diantaranya bisa memilih hiburan murah hingga menyisihkan uang di awal bulan.",
                                    "kategori": "https://www.tribunnews.com/bisnis/finansial",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "34 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/menabung_20180731_123451.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Ketua APPBI Nilai Pusat Perbelanjaan Diperlukan di Ibu Kota Baru",
                                    "url judul": "https://www.tribunnews.com/bisnis/2022/01/20/ketua-appbi-nilai-pusat-perbelanjaan-diperlukan-di-ibu-kota-baru",
                                    "text isi": "Keberadaan pusat perbelanjaan untuk melayani masyarakat yang tinggal IKN tentu sangat dibutuhkan. Ketum APPBI Alphonzus Widjaja mengamini harapan itu",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "1 jam lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/menabung_20180731_123451.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Meski Masih Dihantui Pandemi, BI Sebut Ekonomi Nasional Bakal Tumbuh 5,5 Persen di 2022",
                                    "url judul": "https://www.tribunnews.com/bisnis/2022/01/20/meski-masih-dihantui-pandemi-bi-sebut-ekonomi-nasional-bakal-tumbuh-55-persen-di-2022",
                                    "text isi": "Bank Indonesia memprediksi perekonomian nasional bakal tumbuh di angka 3,2 persen hingga 4 persen pada 2021.",
                                    "kategori": "https://www.tribunnews.com/bisnis/finansial",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "3 jam lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/perry-warjiyo___.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Genjot Kinerja, PT PP Akan Lepas Empat Perusahaan Patungan Hingga 19 Aset Properti",
                                    "url judul": "https://www.tribunnews.com/bisnis/2022/01/20/genjot-kinerja-pt-pp-akan-lepas-empat-perusahaan-patungan-hingga-19-aset-properti",
                                    "text isi": "PT PP (Persero) pada tahun ini akan melakukan divestasi sejumlah asetnya atau asset recycling di sektor properti dan non properti",
                                    "kategori": "https://www.tribunnews.com/bisnis/properti",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "3 jam lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ilustrasi-proyek-konstruksi-pt-pp-persero-tbk.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "aside": [
                                {
                                    "text": "berita POPULER",
                                    "isi": [
                                        {
                                            "text": "Minyak Goreng Rp 14 Ribu, Pedagang Pasar: Kami Hanya Penonton,",
                                            "url": "https://www.tribunnews.com/bisnis/2022/01/19/minyak-goreng-rp-14-ribu-pedagang-pasar-kami-hanya-penonton-diperhatikan-saat-akan-pilpres-saja",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/harga-minyak-goreng-di-ritel-modern.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "1 hari lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Harga Minyak Goreng Jadi Rp 14 Ribu per Liter Mulai Hari Ini, Mendag Imbau",
                                            "url": "https://www.tribunnews.com/bisnis/2022/01/19/harga-minyak-goreng-jadi-rp-14-ribu-per-liter-mulai-hari-ini-mendag-imbau-warga-tidak-panic-buying",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images/ridwan-kamil-dan-yana-mulyana-tunjau-operasi-pasar-minyak-goreng_20220113_235708.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "1 hari lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Harga Emas Antam Melonjak Rp 12.000, Kini Jadi Rp 948.000/Gram",
                                            "url": "https://www.tribunnews.com/bisnis/2022/01/20/harga-emas-antam-melonjak-rp-12000-kini-jadi-rp-948000gram",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images/wabah-corona-tak-berpengaruh-pada-harga-emas-batangan_20200320_205512.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "12 jam lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Pemerintah Kembangkan Industri Petrokimia untuk Tekan Defisit Neraca",
                                            "url": "https://www.tribunnews.com/bisnis/2022/01/20/pemerintah-kembangkan-industri-petrokimia-untuk-tekan-defisit-neraca-perdagangan",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images/pabrik-petrokimia1.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "14 jam lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Tutup Sejumlah Rute Domestik dan Internasional, Garuda Fokus ke Layanan Kargo",
                                            "url": "https://www.tribunnews.com/bisnis/2022/01/19/tutup-sejumlah-rute-domestik-dan-internasional-garuda-fokus-ke-layanan-kargo",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images/penerbangan-kargo.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "1 jam lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "text": "tag POPULER",
                                    "isi": [
                                        {
                                            "text": "harga minyak goreng",
                                            "url": "https://www.tribunnews.com/tag/harga-minyak-goreng"
                                        },
                                        {
                                            "text": "minyak goreng",
                                            "url": "https://www.tribunnews.com/tag/minyak-goreng"
                                        },
                                        {
                                            "text": "Harga emas",
                                            "url": "https://www.tribunnews.com/tag/harga-emas"
                                        },
                                        {
                                            "text": "Kementerian Perdagangan (Kemendag)",
                                            "url": "https://www.tribunnews.com/tag/kementerian-perdagangan-kemendag"
                                        },
                                        {
                                            "text": "Minyak Goreng Harga Rp 14.000 per Liter",
                                            "url": "https://www.tribunnews.com/tag/minyak-goreng-harga-rp-14000-per-liter"
                                        },
                                        {
                                            "text": "minyak goreng kemasan",
                                            "url": "https://www.tribunnews.com/tag/minyak-goreng-kemasan"
                                        },
                                        {
                                            "text": "Harga Emas Antam Kamis 20 Januari 2022",
                                            "url": "https://www.tribunnews.com/tag/harga-emas-antam-kamis-20-januari-2022"
                                        },
                                        {
                                            "text": "Harga Emas Antam hari ini",
                                            "url": "https://www.tribunnews.com/tag/harga-emas-antam-hari-ini"
                                        },
                                        {
                                            "text": "ritel",
                                            "url": "https://www.tribunnews.com/tag/ritel"
                                        },
                                        {
                                            "text": "Menteri Perdagangan Muhammad Lutfi",
                                            "url": "https://www.tribunnews.com/tag/menteri-perdagangan-muhammad-lutfi"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class bisnis_header(Resource):
    def get(self):
        return {
            "data": [
                {
                    "header": [
                        {
                            "icon": "lg lg-twhiteicon",
                            "url": "https://www.tribunnews.com/",
                            "hover": [
                                {
                                    "text": "News",
                                    "url": "https://www.tribunnews.com/news"
                                },
                                {
                                    "text": "Bisnis",
                                    "url": "https://www.tribunnews.com/bisnis"
                                },
                                {
                                    "text": "Super Skor",
                                    "url": "https://www.tribunnews.com/superskor"
                                },
                                {
                                    "text": "Sport",
                                    "url": "https://www.tribunnews.com/sport"
                                },
                                {
                                    "text": "Seleb",
                                    "url": "https://www.tribunnews.com/seleb"
                                },
                                {
                                    "text": "Lifestyle",
                                    "url": "https://www.tribunnews.com/lifestyle"
                                },
                                {
                                    "text": "New Economy",
                                    "url": "https://www.tribunnews.com/new-economy"
                                },
                                {
                                    "text": "PARAPUAN",
                                    "url": "https://www.tribunnews.com/parapuan"
                                },
                                {
                                    "text": "Otomotif",
                                    "url": "https://www.tribunnews.com/otomotif"
                                },
                                {
                                    "text": "Techno",
                                    "url": "https://www.tribunnews.com/techno"
                                },
                                {
                                    "text": "Kesehatan",
                                    "url": "https://www.tribunnews.com/kesehatan"
                                },
                                {
                                    "text": "Video",
                                    "url": "https://www.tribunnews.com/video"
                                },
                                {
                                    "text": "Images",
                                    "url": "https://www.tribunnews.com/images"
                                },
                                {
                                    "text": "Tribunners",
                                    "url": "https://www.tribunnews.com/tribunners"
                                },
                                {
                                    "text": "Indeks Berita",
                                    "url": "https://www.tribunnews.com/indeks"
                                }
                            ]
                        },
                        {
                            "text": "Home",
                            "url": "https://www.tribunnews.com/bisnis"
                        },
                        {
                            "text": "Makro",
                            "url": "https://www.tribunnews.com/bisnis/makro"
                        },
                        {
                            "text": "Energi",
                            "url": "https://www.tribunnews.com/bisnis/energi"
                        },
                        {
                            "text": "Finansial",
                            "url": "https://www.tribunnews.com/bisnis/finansial"
                        },
                        {
                            "text": "Mikro",
                            "url": "https://www.tribunnews.com/bisnis/mikro"
                        },
                        {
                            "text": "Investasi",
                            "url": "https://www.tribunnews.com/bisnis/investasi"
                        },
                        {
                            "text": "Transportasi",
                            "url": "https://www.tribunnews.com/bisnis/transportasi"
                        },
                        {
                            "text": "Infrastruktur",
                            "url": "https://www.tribunnews.com/bisnis/infrastruktur"
                        },
                        {
                            "text": "Insight",
                            "url": "https://www.tribunnews.com/bisnis/insight"
                        },
                        {
                            "text": "Properti",
                            "url": "https://www.tribunnews.com/bisnis/properti"
                        }
                    ]
                }
            ]
        }


class bisnis_body(Resource):
    def get(self):
        return {
            "data": [
                {
                    "body": [
                        {
                            "text": "Bisnis",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images2/wabah-corona-tak-berpengaruh-pada-harga-emas-batangan_20200320_205512.jpg",
                            "judul": "Harga Emas Antam Melonjak Rp 12.000, Kini Jadi Rp 948.000/Gram",
                            "url": "https://www.tribunnews.com/bisnis/2022/01/20/harga-emas-antam-melonjak-rp-12000-kini-jadi-rp-948000gram"
                        },
                        {
                            "text judul": "Tips dan Trik",
                            "url judul": "https://www.tribunnews.com/topic/tips-dan-trik",
                            "text subjudul": "Tips Atur Keuangan Bulanan, Pilih Hiburan Murah hingga Sisihkan Uang di Awal Bulan",
                            "url subjudul": "https://www.tribunnews.com/bisnis/2022/01/20/tips-atur-keuangan-bulanan-pilih-hiburan-murah-hingga-sisihkan-uang-di-awal-bulan",
                            "text isi": "Berikut tips mengatur keuangan bulanan diantaranya bisa memilih hiburan murah hingga menyisihkan uang di awal bulan.",
                            "kategori": "https://www.tribunnews.com/bisnis/finansial",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "34 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/menabung_20180731_123451.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Ketua APPBI Nilai Pusat Perbelanjaan Diperlukan di Ibu Kota Baru",
                            "url judul": "https://www.tribunnews.com/bisnis/2022/01/20/ketua-appbi-nilai-pusat-perbelanjaan-diperlukan-di-ibu-kota-baru",
                            "text isi": "Keberadaan pusat perbelanjaan untuk melayani masyarakat yang tinggal IKN tentu sangat dibutuhkan. Ketum APPBI Alphonzus Widjaja mengamini harapan itu",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "1 jam lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/menabung_20180731_123451.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Meski Masih Dihantui Pandemi, BI Sebut Ekonomi Nasional Bakal Tumbuh 5,5 Persen di 2022",
                            "url judul": "https://www.tribunnews.com/bisnis/2022/01/20/meski-masih-dihantui-pandemi-bi-sebut-ekonomi-nasional-bakal-tumbuh-55-persen-di-2022",
                            "text isi": "Bank Indonesia memprediksi perekonomian nasional bakal tumbuh di angka 3,2 persen hingga 4 persen pada 2021.",
                            "kategori": "https://www.tribunnews.com/bisnis/finansial",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "3 jam lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/perry-warjiyo___.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Genjot Kinerja, PT PP Akan Lepas Empat Perusahaan Patungan Hingga 19 Aset Properti",
                            "url judul": "https://www.tribunnews.com/bisnis/2022/01/20/genjot-kinerja-pt-pp-akan-lepas-empat-perusahaan-patungan-hingga-19-aset-properti",
                            "text isi": "PT PP (Persero) pada tahun ini akan melakukan divestasi sejumlah asetnya atau asset recycling di sektor properti dan non properti",
                            "kategori": "https://www.tribunnews.com/bisnis/properti",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "3 jam lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/ilustrasi-proyek-konstruksi-pt-pp-persero-tbk.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class bisnis_aside_beritaPOPULER(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "berita POPULER",
                    "isi": [
                            {
                                "text": "Minyak Goreng Rp 14 Ribu, Pedagang Pasar: Kami Hanya Penonton,",
                                "url": "https://www.tribunnews.com/bisnis/2022/01/19/minyak-goreng-rp-14-ribu-pedagang-pasar-kami-hanya-penonton-diperhatikan-saat-akan-pilpres-saja",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/harga-minyak-goreng-di-ritel-modern.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "1 hari lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Harga Minyak Goreng Jadi Rp 14 Ribu per Liter Mulai Hari Ini, Mendag Imbau",
                                "url": "https://www.tribunnews.com/bisnis/2022/01/19/harga-minyak-goreng-jadi-rp-14-ribu-per-liter-mulai-hari-ini-mendag-imbau-warga-tidak-panic-buying",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images/ridwan-kamil-dan-yana-mulyana-tunjau-operasi-pasar-minyak-goreng_20220113_235708.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "1 hari lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Harga Emas Antam Melonjak Rp 12.000, Kini Jadi Rp 948.000/Gram",
                                "url": "https://www.tribunnews.com/bisnis/2022/01/20/harga-emas-antam-melonjak-rp-12000-kini-jadi-rp-948000gram",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images/wabah-corona-tak-berpengaruh-pada-harga-emas-batangan_20200320_205512.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "12 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Pemerintah Kembangkan Industri Petrokimia untuk Tekan Defisit Neraca",
                                "url": "https://www.tribunnews.com/bisnis/2022/01/20/pemerintah-kembangkan-industri-petrokimia-untuk-tekan-defisit-neraca-perdagangan",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images/pabrik-petrokimia1.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "14 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Tutup Sejumlah Rute Domestik dan Internasional, Garuda Fokus ke Layanan Kargo",
                                "url": "https://www.tribunnews.com/bisnis/2022/01/19/tutup-sejumlah-rute-domestik-dan-internasional-garuda-fokus-ke-layanan-kargo",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images/penerbangan-kargo.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "1 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            }
                    ]
                }
            ]
        }


class bisnis_aside_tagPOPULER(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "tag POPULER",
                    "isi": [
                            {
                                "text": "harga minyak goreng",
                                "url": "https://www.tribunnews.com/tag/harga-minyak-goreng"
                            },
                        {
                                "text": "minyak goreng",
                                "url": "https://www.tribunnews.com/tag/minyak-goreng"
                            },
                        {
                                "text": "Harga emas",
                                "url": "https://www.tribunnews.com/tag/harga-emas"
                            },
                        {
                                "text": "Kementerian Perdagangan (Kemendag)",
                                "url": "https://www.tribunnews.com/tag/kementerian-perdagangan-kemendag"
                            },
                        {
                                "text": "Minyak Goreng Harga Rp 14.000 per Liter",
                                "url": "https://www.tribunnews.com/tag/minyak-goreng-harga-rp-14000-per-liter"
                            },
                        {
                                "text": "minyak goreng kemasan",
                                "url": "https://www.tribunnews.com/tag/minyak-goreng-kemasan"
                            },
                        {
                                "text": "Harga Emas Antam Kamis 20 Januari 2022",
                                "url": "https://www.tribunnews.com/tag/harga-emas-antam-kamis-20-januari-2022"
                            },
                        {
                                "text": "Harga Emas Antam hari ini",
                                "url": "https://www.tribunnews.com/tag/harga-emas-antam-hari-ini"
                            },
                        {
                                "text": "ritel",
                                "url": "https://www.tribunnews.com/tag/ritel"
                            },
                        {
                                "text": "Menteri Perdagangan Muhammad Lutfi",
                                "url": "https://www.tribunnews.com/tag/menteri-perdagangan-muhammad-lutfi"
                            }
                    ]
                }
            ]
        }


class superskor(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "Superskor",
                    "url": "https://www.tribunnews.com/superskor",
                    "content": [
                        {
                            "header": [
                                {
                                    "icon": "lg lg-twhiteicon",
                                    "url": "https://www.tribunnews.com/",
                                    "hover": [
                                        {
                                            "text": "News",
                                            "url": "https://www.tribunnews.com/news"
                                        },
                                        {
                                            "text": "Bisnis",
                                            "url": "https://www.tribunnews.com/bisnis"
                                        },
                                        {
                                            "text": "Super Skor",
                                            "url": "https://www.tribunnews.com/superskor"
                                        },
                                        {
                                            "text": "Sport",
                                            "url": "https://www.tribunnews.com/sport"
                                        },
                                        {
                                            "text": "Seleb",
                                            "url": "https://www.tribunnews.com/seleb"
                                        },
                                        {
                                            "text": "Lifestyle",
                                            "url": "https://www.tribunnews.com/lifestyle"
                                        },
                                        {
                                            "text": "New Economy",
                                            "url": "https://www.tribunnews.com/new-economy"
                                        },
                                        {
                                            "text": "PARAPUAN",
                                            "url": "https://www.tribunnews.com/parapuan"
                                        },
                                        {
                                            "text": "Otomotif",
                                            "url": "https://www.tribunnews.com/otomotif"
                                        },
                                        {
                                            "text": "Techno",
                                            "url": "https://www.tribunnews.com/techno"
                                        },
                                        {
                                            "text": "Kesehatan",
                                            "url": "https://www.tribunnews.com/kesehatan"
                                        },
                                        {
                                            "text": "Video",
                                            "url": "https://www.tribunnews.com/video"
                                        },
                                        {
                                            "text": "Images",
                                            "url": "https://www.tribunnews.com/images"
                                        },
                                        {
                                            "text": "Tribunners",
                                            "url": "https://www.tribunnews.com/tribunners"
                                        },
                                        {
                                            "text": "Indeks Berita",
                                            "url": "https://www.tribunnews.com/indeks"
                                        }
                                    ]
                                },
                                {
                                    "text": "Home",
                                    "url": "https://www.tribunnews.com/superskor"
                                },
                                {
                                    "text": "Indonesia",
                                    "url": "https://www.tribunnews.com/superskor/liga-indonesia"
                                },
                                {
                                    "text": "Inggris",
                                    "url": "https://www.tribunnews.com/superskor/liga-inggris"
                                },
                                {
                                    "text": "Spanyol",
                                    "url": "https://www.tribunnews.com/superskor/liga-spanyol"
                                },
                                {
                                    "text": "Italia",
                                    "url": "https://www.tribunnews.com/superskor/liga-italia"
                                },
                                {
                                    "text": "Champions",
                                    "url": "https://www.tribunnews.com/superskor/champions-eropa"
                                },
                                {
                                    "text": "Super Pandit",
                                    "url": "https://www.tribunnews.com/topic/super-pandit"
                                },
                                {
                                    "text": "Lainnya",
                                    "url": "https://www.tribunnews.com/superskor/lainnya"
                                }
                            ]
                        },
                        {
                            "body": [
                                {
                                    "text": "Super Skor",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images2/striker-liverpool-asal-portugal-diogo-jota-ke-3-dari-kanan.jpg",
                                    "judul": "Sudah Jatuh Tertimpa Tangga, Januari Kelabu Bagi Arsenal, Nihil Gelar & Label Raja Kartu Merah",
                                    "url": "https://www.tribunnews.com/superskor/2022/01/21/sudah-jatuh-tertimpa-tangga-januari-kelabu-bagi-arsenal-nihil-gelar-label-raja-kartu-merah"
                                },
                                {
                                    "text judul": "Piala Asia Wanita 2022",
                                    "url judul": "https://www.tribunnews.com/topic/piala-asia-wanita-2022",
                                    "text subjudul": "Jadwal Piala Asia Wanita 2022 Hari Ini, Live iNews TV: Timnas Indonesia vs Australia Pukul 17.00 WIB",
                                    "url subjudul": "https://www.tribunnews.com/superskor/2022/01/21/jadwal-piala-asia-wanita-2022-hari-ini-live-inews-tv-timnas-indonesia-vs-australia-pukul-1700-wib",
                                    "text isi": "Jadwal Piala Asia Wanita 2022 hari ini, Timnas Wanita Indonesia akan bertanding melawan Australia pukul 17.00 WIB, live di iNews TV.",
                                    "kategori": "https://www.tribunnews.com/superskor/liga-indonesia",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "6 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/latihan-perdana-timnas-wanita-indonesia_20210308_202908.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Liga Inggris",
                                    "url judul": "https://www.tribunnews.com/topic/super-pandit",
                                    "text subjudul": "Jadwal Liga Inggris Pekan 23: Balas Dendam Spurs Jumpa Chelsea, City Berburu Mangsa, Live Mola",
                                    "url subjudul": "https://www.tribunnews.com/superskor/2022/01/21/jadwal-liga-inggris-pekan-23-balas-dendam-spurs-jumpa-chelsea-city-berburu-mangsa-live-mola-tv",
                                    "text isi": "Terdapat berbagai laga seru yang akan mewarnai pertandingan matchday 23 Liga Inggris sebelum agenda jeda internasional, akhir pekan ini.",
                                    "kategori": "https://www.tribunnews.com/superskor/liga-inggris",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "2 jam lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/malang-sarr-sikut-kane.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Bongkar Pasang Kriteria Pelatih Baru Timnas Malaysia, Nahkoda Persib Ternyata Dijadikan",
                                    "url judul": "https://www.tribunnews.com/superskor/2022/01/21/bongkar-pasang-kriteria-pelatih-baru-timnas-malaysia-pelatih-persib-ternyata-dijadikan-teladan",
                                    "text isi": "Federasi Sepak Bola Malaysia (FAM) tengah sibuk mencari pelatih baru untuk menangani Timnas Harimau Malaya selepas memecat Tan Chong Hoe.",
                                    "kategori": "https://www.tribunnews.com/superskor/lainnya",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "5 menit lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/piala-aff-timnas-indonesia-bantai-malaysia-4-1_20211220_054309.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                },
                                {
                                    "text judul": "Copa Del Rey",
                                    "url judul": "https://www.tribunnews.com/topic/copa-del-rey",
                                    "text subjudul": "Berkah Kemenangan Comeback Real Madrid, Ancelotti Sanjung Duo Pahlawan Dadakan Los",
                                    "url subjudul": "https://www.tribunnews.com/superskor/2022/01/21/berkah-kemenangan-comeback-real-madrid-ancelotti-sanjung-duo-pahlawan-dadakan-los-blancos",
                                    "text isi": "Real Madrid berhasil menuai kemenangan berharga saat meladeni El Che pada babak 16 besar Copa Del Rey, Jumat (21/1/2022) dinihari tadi.",
                                    "kategori": "https://www.tribunnews.com/superskor/liga-spanyol",
                                    "icon": "fa fa-clock-o mr7",
                                    "waktu": "3 jam lalu",
                                    "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/hazard-dan-ancelotti.jpg",
                                    "sosmed": [
                                        {
                                            "icon": "fa fa facebook",
                                            "text": "shere",
                                            "url": "javascript:void(0)"
                                        },
                                        {
                                            "icon": "twitter",
                                            "text": "tweet",
                                            "url": "javascript:void(0)"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "aside": [
                                {
                                    "kotak skor": [
                                        {
                                            "atas": [
                                                {
                                                    "kiri": {
                                                        "text": "klub"
                                                    }
                                                },
                                                {
                                                    "kanan": [
                                                        {
                                                            "text 1": "D"
                                                        },
                                                        {
                                                            "text 2": "M"
                                                        },
                                                        {
                                                            "text 3": "S"
                                                        },
                                                        {
                                                            "text 4": "K"
                                                        },
                                                        {
                                                            "text 5": "GM"
                                                        },
                                                        {
                                                            "text 6": "GK"
                                                        },
                                                        {
                                                            "text 7": "-/+"
                                                        },
                                                        {
                                                            "text 8": "P"
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "tengah": [
                                                {
                                                    "id": "1",
                                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/man-city.png",
                                                    "text": "Manchest",
                                                    "nomer 1": "21",
                                                    "nomer 2": "17",
                                                    "nomer 3": "2",
                                                    "nomer 4": "2",
                                                    "nomer 5": "53",
                                                    "nomer 6": "13",
                                                    "nomer 7": "40",
                                                    "nomer 8": "53"
                                                },
                                                {
                                                    "id": "2",
                                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/chelsea.png",
                                                    "text": "Chelsea",
                                                    "nomer 1": "21",
                                                    "nomer 2": "12",
                                                    "nomer 3": "7",
                                                    "nomer 4": "2",
                                                    "nomer 5": "45",
                                                    "nomer 6": "16",
                                                    "nomer 7": "29",
                                                    "nomer 8": "43"
                                                },
                                                {
                                                    "id": "3",
                                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/liverpool.png",
                                                    "text": "Liverpool",
                                                    "nomer 1": "20",
                                                    "nomer 2": "12",
                                                    "nomer 3": "6",
                                                    "nomer 4": "2",
                                                    "nomer 5": "52",
                                                    "nomer 6": "18",
                                                    "nomer 7": "34",
                                                    "nomer 8": "42"
                                                },
                                                {
                                                    "id": "4",
                                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/west-ham.png",
                                                    "text": "West Ham",
                                                    "nomer 1": "21",
                                                    "nomer 2": "11",
                                                    "nomer 3": "4",
                                                    "nomer 4": "6",
                                                    "nomer 5": "39",
                                                    "nomer 6": "27",
                                                    "nomer 7": "12",
                                                    "nomer 8": "37"
                                                },
                                                {
                                                    "id": "5",
                                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/arsenal.png",
                                                    "text": "Arsenal",
                                                    "nomer 1": "20",
                                                    "nomer 2": "11",
                                                    "nomer 3": "2",
                                                    "nomer 4": "7",
                                                    "nomer 5": "33",
                                                    "nomer 6": "25",
                                                    "nomer 7": "8",
                                                    "nomer 8": "35"
                                                }
                                            ]
                                        },
                                        {
                                            "bawah": {
                                                "text": "Lihat selengkapnya",
                                                "url": "https://www.tribunnews.com/klasemen",
                                                "icon": "icon icon-angle-right"
                                            }
                                        }
                                    ]
                                },
                                {
                                    "text": "berita POPULER",
                                    "isi": [
                                        {
                                            "text": "Magis Diogo Jota di Liverpool, Kesabaran Klopp, Kematangan dari",
                                            "url": "https://www.tribunnews.com/superskor/2022/01/21/magis-diogo-jota-di-liverpool-kesabaran-klopp-kematangan-dari-simeone-tandem-salah-dan-mane",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/striker-liverpool-asal-portugal-diogo-jota-kanan-melewati-bek-arsenal.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "9 jam lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Hasil Arsenal vs Liverpool di Carabao Cup 2021, Menang 0-2, The Reds",
                                            "url": "https://www.tribunnews.com/superskor/2022/01/21/hasil-arsenal-vs-liverpool-di-carabao-cup-2021-menang-0-2-the-reds-tantang-chelsea-di-final",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/striker-liverpool-asal-portugal-diogo-jota-ke-3-dari-kanan.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "9 jam lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Kelolosan Dramatis Inter Milan Memakan Korban, Inzaghi Khawatirkan",
                                            "url": "https://www.tribunnews.com/superskor/2022/01/20/kelolosan-dramatis-inter-milan-memakan-korban-inzaghi-khawatirkan-cedera-hamstring-correa",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/joaquin-correa-mendapatkan-cedera-pinggul-setelah-membela-inter-milan-selama-28-menit.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "1 hari lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "Pragmatisme Manchester United di Bawah Ralf Rangnick, Ubah Peran",
                                            "url": "https://www.tribunnews.com/superskor/2022/01/21/pragmatisme-manchester-united-di-bawah-ralf-rangnick-ubah-peran-ronaldo-permudah-fred-dan-bruno",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/rangnick-dalam-laga-melawan-brentford.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "10 jam lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        },
                                        {
                                            "text": "7 Pemain Arsenal Dipastikan Absen Lawan Liverpool, 4 Pemain",
                                            "url": "https://www.tribunnews.com/superskor/2022/01/20/7-pemain-arsenal-dipastikan-absen-lawan-liverpool-4-pemain-lainnya-sedang-tidak-fit-ini-daftarnya",
                                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/wasit-inggris-michael-oliver-tengah-membantu-gelandang-arsenal-granit-xhaka-berdiri.jpg",
                                            "icon": "fa fa-clock-o mr7",
                                            "waktu": "21 jam lalu",
                                            "sosmed": [
                                                {
                                                    "icon": "fa fa facebook",
                                                    "text": "shere",
                                                    "url": "javascript:void(0)"
                                                },
                                                {
                                                    "icon": "twitter",
                                                    "text": "tweet",
                                                    "url": "javascript:void(0)"
                                                }
                                            ]
                                        }
                                    ]
                                },
                                {
                                    "text": "tag POPULER",
                                    "url": "https://www.tribunnews.com/tag/index/all",
                                    "isi": [
                                        {
                                            "text": "Liverpool",
                                            "url": "https://www.tribunnews.com/tag/liverpool"
                                        },
                                        {
                                            "text": "Diogo Jota",
                                            "url": "https://www.tribunnews.com/tag/diogo-jota"
                                        },
                                        {
                                            "text": "Arsenal",
                                            "url": "https://www.tribunnews.com/tag/arsenal"
                                        },
                                        {
                                            "text": "Manchester United",
                                            "url": "https://www.tribunnews.com/tag/manchester-united"
                                        },
                                        {
                                            "text": "Arsenal vs Liverpool",
                                            "url": "https://www.tribunnews.com/tag/arsenal-vs-liverpool"
                                        },
                                        {
                                            "text": "Ralf Rangnick",
                                            "url": "https://www.tribunnews.com/tag/ralf-rangnick"
                                        },
                                        {
                                            "text": "Anthony Elanga",
                                            "url": "https://www.tribunnews.com/tag/anthony-elanga"
                                        },
                                        {
                                            "text": "Barcelona",
                                            "url": "https://www.tribunnews.com/tag/barcelona"
                                        },
                                        {
                                            "text": "HASIL Arsenal vs Liverpool",
                                            "url": "https://www.tribunnews.com/tag/hasil-arsenal-vs-liverpool"
                                        },
                                        {
                                            "text": "Jurgen Klopp",
                                            "url": "https://www.tribunnews.com/tag/jurgen-klopp"
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class superskor_header(Resource):
    def get(self):
        return {
            "data": [
                {
                    "header": [
                        {
                            "icon": "lg lg-twhiteicon",
                            "url": "https://www.tribunnews.com/",
                            "hover": [
                                {
                                    "text": "News",
                                    "url": "https://www.tribunnews.com/news"
                                },
                                {
                                    "text": "Bisnis",
                                    "url": "https://www.tribunnews.com/bisnis"
                                },
                                {
                                    "text": "Super Skor",
                                    "url": "https://www.tribunnews.com/superskor"
                                },
                                {
                                    "text": "Sport",
                                    "url": "https://www.tribunnews.com/sport"
                                },
                                {
                                    "text": "Seleb",
                                    "url": "https://www.tribunnews.com/seleb"
                                },
                                {
                                    "text": "Lifestyle",
                                    "url": "https://www.tribunnews.com/lifestyle"
                                },
                                {
                                    "text": "New Economy",
                                    "url": "https://www.tribunnews.com/new-economy"
                                },
                                {
                                    "text": "PARAPUAN",
                                    "url": "https://www.tribunnews.com/parapuan"
                                },
                                {
                                    "text": "Otomotif",
                                    "url": "https://www.tribunnews.com/otomotif"
                                },
                                {
                                    "text": "Techno",
                                    "url": "https://www.tribunnews.com/techno"
                                },
                                {
                                    "text": "Kesehatan",
                                    "url": "https://www.tribunnews.com/kesehatan"
                                },
                                {
                                    "text": "Video",
                                    "url": "https://www.tribunnews.com/video"
                                },
                                {
                                    "text": "Images",
                                    "url": "https://www.tribunnews.com/images"
                                },
                                {
                                    "text": "Tribunners",
                                    "url": "https://www.tribunnews.com/tribunners"
                                },
                                {
                                    "text": "Indeks Berita",
                                    "url": "https://www.tribunnews.com/indeks"
                                }
                            ]
                        },
                        {
                            "text": "Home",
                            "url": "https://www.tribunnews.com/superskor"
                        },
                        {
                            "text": "Indonesia",
                            "url": "https://www.tribunnews.com/superskor/liga-indonesia"
                        },
                        {
                            "text": "Inggris",
                            "url": "https://www.tribunnews.com/superskor/liga-inggris"
                        },
                        {
                            "text": "Spanyol",
                            "url": "https://www.tribunnews.com/superskor/liga-spanyol"
                        },
                        {
                            "text": "Italia",
                            "url": "https://www.tribunnews.com/superskor/liga-italia"
                        },
                        {
                            "text": "Champions",
                            "url": "https://www.tribunnews.com/superskor/champions-eropa"
                        },
                        {
                            "text": "Super Pandit",
                            "url": "https://www.tribunnews.com/topic/super-pandit"
                        },
                        {
                            "text": "Lainnya",
                            "url": "https://www.tribunnews.com/superskor/lainnya"
                        }
                    ]
                }
            ]
        }


class superskor_body(Resource):
    def get(self):
        return {
            "data": [
                {
                    "body": [
                        {
                            "text": "Super Skor",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/images2/striker-liverpool-asal-portugal-diogo-jota-ke-3-dari-kanan.jpg",
                            "judul": "Sudah Jatuh Tertimpa Tangga, Januari Kelabu Bagi Arsenal, Nihil Gelar & Label Raja Kartu Merah",
                            "url": "https://www.tribunnews.com/superskor/2022/01/21/sudah-jatuh-tertimpa-tangga-januari-kelabu-bagi-arsenal-nihil-gelar-label-raja-kartu-merah"
                        },
                        {
                            "text judul": "Piala Asia Wanita 2022",
                            "url judul": "https://www.tribunnews.com/topic/piala-asia-wanita-2022",
                            "text subjudul": "Jadwal Piala Asia Wanita 2022 Hari Ini, Live iNews TV: Timnas Indonesia vs Australia Pukul 17.00 WIB",
                            "url subjudul": "https://www.tribunnews.com/superskor/2022/01/21/jadwal-piala-asia-wanita-2022-hari-ini-live-inews-tv-timnas-indonesia-vs-australia-pukul-1700-wib",
                            "text isi": "Jadwal Piala Asia Wanita 2022 hari ini, Timnas Wanita Indonesia akan bertanding melawan Australia pukul 17.00 WIB, live di iNews TV.",
                            "kategori": "https://www.tribunnews.com/superskor/liga-indonesia",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "6 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/latihan-perdana-timnas-wanita-indonesia_20210308_202908.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Liga Inggris",
                            "url judul": "https://www.tribunnews.com/topic/super-pandit",
                            "text subjudul": "Jadwal Liga Inggris Pekan 23: Balas Dendam Spurs Jumpa Chelsea, City Berburu Mangsa, Live Mola",
                            "url subjudul": "https://www.tribunnews.com/superskor/2022/01/21/jadwal-liga-inggris-pekan-23-balas-dendam-spurs-jumpa-chelsea-city-berburu-mangsa-live-mola-tv",
                            "text isi": "Terdapat berbagai laga seru yang akan mewarnai pertandingan matchday 23 Liga Inggris sebelum agenda jeda internasional, akhir pekan ini.",
                            "kategori": "https://www.tribunnews.com/superskor/liga-inggris",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "2 jam lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/malang-sarr-sikut-kane.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Bongkar Pasang Kriteria Pelatih Baru Timnas Malaysia, Nahkoda Persib Ternyata Dijadikan",
                            "url judul": "https://www.tribunnews.com/superskor/2022/01/21/bongkar-pasang-kriteria-pelatih-baru-timnas-malaysia-pelatih-persib-ternyata-dijadikan-teladan",
                            "text isi": "Federasi Sepak Bola Malaysia (FAM) tengah sibuk mencari pelatih baru untuk menangani Timnas Harimau Malaya selepas memecat Tan Chong Hoe.",
                            "kategori": "https://www.tribunnews.com/superskor/lainnya",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "5 menit lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/piala-aff-timnas-indonesia-bantai-malaysia-4-1_20211220_054309.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        },
                        {
                            "text judul": "Copa Del Rey",
                            "url judul": "https://www.tribunnews.com/topic/copa-del-rey",
                            "text subjudul": "Berkah Kemenangan Comeback Real Madrid, Ancelotti Sanjung Duo Pahlawan Dadakan Los",
                            "url subjudul": "https://www.tribunnews.com/superskor/2022/01/21/berkah-kemenangan-comeback-real-madrid-ancelotti-sanjung-duo-pahlawan-dadakan-los-blancos",
                            "text isi": "Real Madrid berhasil menuai kemenangan berharga saat meladeni El Che pada babak 16 besar Copa Del Rey, Jumat (21/1/2022) dinihari tadi.",
                            "kategori": "https://www.tribunnews.com/superskor/liga-spanyol",
                            "icon": "fa fa-clock-o mr7",
                            "waktu": "3 jam lalu",
                            "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/hazard-dan-ancelotti.jpg",
                            "sosmed": [
                                {
                                    "icon": "fa fa facebook",
                                    "text": "shere",
                                    "url": "javascript:void(0)"
                                },
                                {
                                    "icon": "twitter",
                                    "text": "tweet",
                                    "url": "javascript:void(0)"
                                }
                            ]
                        }
                    ]
                }
            ]
        }


class superskor_aside_kotakskor(Resource):
    def get(self):
        return {
            "data": [
                {
                    "kotak skor": [
                        {
                            "atas": [
                                {
                                    "kiri": {
                                        "text": "klub"
                                    }
                                },
                                {
                                    "kanan": [
                                        {
                                            "text 1": "D"
                                        },
                                        {
                                            "text 2": "M"
                                        },
                                        {
                                            "text 3": "S"
                                        },
                                        {
                                            "text 4": "K"
                                        },
                                        {
                                            "text 5": "GM"
                                        },
                                        {
                                            "text 6": "GK"
                                        },
                                        {
                                            "text 7": "-/+"
                                        },
                                        {
                                            "text 8": "P"
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "tengah": [
                                {
                                    "id": "1",
                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/man-city.png",
                                    "text": "Manchest",
                                    "nomer 1": "21",
                                    "nomer 2": "17",
                                    "nomer 3": "2",
                                    "nomer 4": "2",
                                    "nomer 5": "53",
                                    "nomer 6": "13",
                                    "nomer 7": "40",
                                    "nomer 8": "53"
                                },
                                {
                                    "id": "2",
                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/chelsea.png",
                                    "text": "Chelsea",
                                    "nomer 1": "21",
                                    "nomer 2": "12",
                                    "nomer 3": "7",
                                    "nomer 4": "2",
                                    "nomer 5": "45",
                                    "nomer 6": "16",
                                    "nomer 7": "29",
                                    "nomer 8": "43"
                                },
                                {
                                    "id": "3",
                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/liverpool.png",
                                    "text": "Liverpool",
                                    "nomer 1": "20",
                                    "nomer 2": "12",
                                    "nomer 3": "6",
                                    "nomer 4": "2",
                                    "nomer 5": "52",
                                    "nomer 6": "18",
                                    "nomer 7": "34",
                                    "nomer 8": "42"
                                },
                                {
                                    "id": "4",
                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/west-ham.png",
                                    "text": "West Ham",
                                    "nomer 1": "21",
                                    "nomer 2": "11",
                                    "nomer 3": "4",
                                    "nomer 4": "6",
                                    "nomer 5": "39",
                                    "nomer 6": "27",
                                    "nomer 7": "12",
                                    "nomer 8": "37"
                                },
                                {
                                    "id": "5",
                                    "gambar": "https://asset.kompas.com/data/2021/klasemenliga/ligainggris/arsenal.png",
                                    "text": "Arsenal",
                                    "nomer 1": "20",
                                    "nomer 2": "11",
                                    "nomer 3": "2",
                                    "nomer 4": "7",
                                    "nomer 5": "33",
                                    "nomer 6": "25",
                                    "nomer 7": "8",
                                    "nomer 8": "35"
                                }
                            ]
                        },
                        {
                            "bawah": {
                                "text": "Lihat selengkapnya",
                                "url": "https://www.tribunnews.com/klasemen",
                                "icon": "icon icon-angle-right"
                            }
                        }
                    ]
                }
            ]
        }


class superskor_aside_beritaPOPULER(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "berita POPULER",
                    "isi": [
                            {
                                "text": "Magis Diogo Jota di Liverpool, Kesabaran Klopp, Kematangan dari",
                                "url": "https://www.tribunnews.com/superskor/2022/01/21/magis-diogo-jota-di-liverpool-kesabaran-klopp-kematangan-dari-simeone-tandem-salah-dan-mane",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/striker-liverpool-asal-portugal-diogo-jota-kanan-melewati-bek-arsenal.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "9 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Hasil Arsenal vs Liverpool di Carabao Cup 2021, Menang 0-2, The Reds",
                                "url": "https://www.tribunnews.com/superskor/2022/01/21/hasil-arsenal-vs-liverpool-di-carabao-cup-2021-menang-0-2-the-reds-tantang-chelsea-di-final",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/striker-liverpool-asal-portugal-diogo-jota-ke-3-dari-kanan.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "9 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Kelolosan Dramatis Inter Milan Memakan Korban, Inzaghi Khawatirkan",
                                "url": "https://www.tribunnews.com/superskor/2022/01/20/kelolosan-dramatis-inter-milan-memakan-korban-inzaghi-khawatirkan-cedera-hamstring-correa",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/joaquin-correa-mendapatkan-cedera-pinggul-setelah-membela-inter-milan-selama-28-menit.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "1 hari lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "Pragmatisme Manchester United di Bawah Ralf Rangnick, Ubah Peran",
                                "url": "https://www.tribunnews.com/superskor/2022/01/21/pragmatisme-manchester-united-di-bawah-ralf-rangnick-ubah-peran-ronaldo-permudah-fred-dan-bruno",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/rangnick-dalam-laga-melawan-brentford.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "10 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            },
                        {
                                "text": "7 Pemain Arsenal Dipastikan Absen Lawan Liverpool, 4 Pemain",
                                "url": "https://www.tribunnews.com/superskor/2022/01/20/7-pemain-arsenal-dipastikan-absen-lawan-liverpool-4-pemain-lainnya-sedang-tidak-fit-ini-daftarnya",
                                "gambar": "https://cdn-2.tstatic.net/tribunnews/foto/bank/thumbnails2/wasit-inggris-michael-oliver-tengah-membantu-gelandang-arsenal-granit-xhaka-berdiri.jpg",
                                "icon": "fa fa-clock-o mr7",
                                "waktu": "21 jam lalu",
                                "sosmed": [
                                    {
                                        "icon": "fa fa facebook",
                                        "text": "shere",
                                        "url": "javascript:void(0)"
                                    },
                                    {
                                        "icon": "twitter",
                                        "text": "tweet",
                                        "url": "javascript:void(0)"
                                    }
                                ]
                            }
                    ]
                }
            ]
        }


class superskor_aside_tagPOPULER(Resource):
    def get(self):
        return {
            "data": [
                {
                    "text": "tag POPULER",
                    "url": "https://www.tribunnews.com/tag/index/all",
                    "isi": [
                            {
                                "text": "Liverpool",
                                "url": "https://www.tribunnews.com/tag/liverpool"
                            },
                        {
                                "text": "Diogo Jota",
                                "url": "https://www.tribunnews.com/tag/diogo-jota"
                                },
                        {
                                "text": "Arsenal",
                                "url": "https://www.tribunnews.com/tag/arsenal"
                                },
                        {
                                "text": "Manchester United",
                                "url": "https://www.tribunnews.com/tag/manchester-united"
                                },
                        {
                                "text": "Arsenal vs Liverpool",
                                "url": "https://www.tribunnews.com/tag/arsenal-vs-liverpool"
                                },
                        {
                                "text": "Ralf Rangnick",
                                "url": "https://www.tribunnews.com/tag/ralf-rangnick"
                                },
                        {
                                "text": "Anthony Elanga",
                                "url": "https://www.tribunnews.com/tag/anthony-elanga"
                                },
                        {
                                "text": "Barcelona",
                                "url": "https://www.tribunnews.com/tag/barcelona"
                                },
                        {
                                "text": "HASIL Arsenal vs Liverpool",
                                "url": "https://www.tribunnews.com/tag/hasil-arsenal-vs-liverpool"
                                },
                        {
                                "text": "Jurgen Klopp",
                                "url": "https://www.tribunnews.com/tag/jurgen-klopp"
                                }
                    ]
                }
            ]
        }




api.add_resource(beranda, '/beranda/')
api.add_resource(beranda_body_slider, '/beranda/body/slider/')
api.add_resource(beranda_body_section_berita1, '/beranda/body/section/berita1/')
api.add_resource(beranda_body_top_stories, '/beranda/body/top/stories/')
api.add_resource(beranda_aside_beritaPOPULER, '/beranda/aside/beritaPOPULER/')
api.add_resource(beranda_aside_topikPOPULER, '/beranda/aside/topikPOPULER/')
api.add_resource(news, '/news/')
api.add_resource(news_header, '/news/header/')
api.add_resource(news_body, '/news/body/')
api.add_resource(news_aside_beritaPOPULER, '/news/aside/beritaPOPULER/')
api.add_resource(news_aside_tagPOPULER, '/news/aside/tagPOPULER/')
api.add_resource(bisnis, '/bisnis/')
api.add_resource(bisnis_header, '/bisnis/header/')
api.add_resource(bisnis_body, '/bisnis/body/')
api.add_resource(bisnis_aside_beritaPOPULER, '/bisnis/aside/beritaPOPULER/')
api.add_resource(bisnis_aside_tagPOPULER, '/bisnis/aside/tagPOPULER/')
api.add_resource(superskor, '/superskor/')
api.add_resource(superskor_header, '/superskor/header/')
api.add_resource(superskor_body, '/superskor/body/')
api.add_resource(superskor_aside_kotakskor, '/superskor/aside/kotakskor/')
api.add_resource(superskor_aside_beritaPOPULER, '/superskor/aside/beritaPOPULER/')
api.add_resource(superskor_aside_tagPOPULER, '/superskor/aside/tagPOPULER/')


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "not found end point"}, 404


if __name__ == '__main__':
    app.run(debug=True)
