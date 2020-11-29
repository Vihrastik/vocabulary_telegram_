TOKEN = ''
END_MESSAGE = 'закончить'
HINT_MESSAGE = 'подсказка'
NEXT_MESSAGE = 'дальше'
RUS_ENG = '1. русский -> иностранный'
ENG_RUS = '2. иностранный -> русский'


class Language:
    eng = 'английский'
    fr = 'французский'
    ger = 'немецкий'


HAPPY_STICKERS = ['CAACAgIAAxkBAAJDnV6SICCQXNaN3Xf5SjlywNau6hahAAIkAAM7YCQU-9kChEBH5QEYBA',
                  'CAACAgIAAxkBAAJDoV6SIHPXIeyICGhNHS7hV7yWZ6GPAAKOIgAC4KOCB47m6cCnsW59GAQ',
                  'CAACAgIAAxkBAAJDp16SISYtAV5w99zkWghGPhs2pZT7AALcBQACNuwbBVGkm7UiKH0zGAQ',
                  'CAACAgQAAxkBAAJDr16SIWGrtbAhsuYL6-L9DYBsgWvQAAJkAAOodxIAAQT5BNcd-V0GGAQ',
                  'CAACAgIAAxkBAAJDs16SIc2u3cVeXIrXE4CyjHDJYOC-AAIwAAM_VJkIKsOCY7aldowYBA',
                  'CAACAgIAAxkBAAJDt16SIf7R3GuzmcC6Pr-vzFQxFgKBAAIvAAM_VJkIL_VMMBYmWosYBA',
                  'CAACAgIAAxkBAAJDuV6SIhwn-lWMzTHhknqKURuVI13RAALjIgAC4KOCBwjvGzGM_mqoGAQ',
                  'CAACAgIAAxkBAAJDwV6SInNgL1AVAQq7Mj9_hhIlh5QEAAJWJgACS2oDAAFOyVXYVNPR_hgE',
                  'CAACAgIAAxkBAAJDw16SIoPHdjcWYyrAilNTSAdqBqZoAAI7JgACS2oDAAFTcQldJoocJBgE',
                  'CAACAgIAAxkBAAJDy16SIrobnAw0A4X-ItBVtlx2y2vdAALEKwACS2oDAAGH2TjdEwZDlhgE',
                  'CAACAgIAAxkBAAJD1V6SIxT93w4iT3AOkR7d2L-JC2I3AAIxCAACIyEFAAF_DBHbfweT7xgE',
                  'CAACAgIAAxkBAAJD116SIy3iKP_7hzWewWNAxFlK1_qLAAJ4CAACIyEFAAE3KyN2vuoQ7BgE',
                  'CAACAgIAAxkBAAJD2V6SIzprlvfCKUGtzHpeQZlHV88-AAJsCAACIyEFAAEsN95Q6eqvbBgE',
                  'CAACAgIAAxkBAAJD216SI1_eA-Jm9IOc7CbI0q8K6bGiAALmAAN53aITqtmgLp-XPxcYBA',
                  'CAACAgIAAxkBAAJD3V6SI3Fsy1VkR7aL2RKjzz-rvgLaAALxAAN53aITR1Pci2mqAZMYBA',
                  'CAACAgIAAxkBAAJD316SI388DsLXvXuD6-y6KdiL5mt-AAL3AQACMdPJAf6xXydJPoJjGAQ',
                  'CAACAgQAAxkBAAJD416SI5rGVFtXBL9h9Y53EiNNTZ7pAAJYAQAC4nLZAAH878ddecC1ExgE',
                  'CAACAgQAAxkBAAJD5V6SI6OK3hgVgBuyOdLWiYV7kKe7AAJcAQAC4nLZAAFLNMxa2IZ1gxgE',
                  'CAACAgQAAxkBAAJD516SI68Y9FXzxx-8fzMGLQGT-2XlAAKJAQAC4nLZAAFIgirO8qEJZRgE',
                  'CAACAgQAAxkBAAJD6V6SI7sAAWT0XWnAKJGr4mqw29ynUwACiAEAAuJy2QAB0nVpxobPyTMYBA',
                  'CAACAgIAAxkBAAJD-V6SJBi48AzzCFbpj-Mntn6GXusIAAImCQACN4QwAAFby0megyEzahgE',
                  'CAACAgIAAxkBAAJECF6SJHyxqISHpWdxbcmES5qgC1lYAAJ4FQACQq9pAAGEtLbtC8QRdBgE',
                  'CAACAgIAAxkBAAJECl6SJI25-xPHWi1DhTWk7tWjoTqRAAJ2FQACQq9pAAHMQNBi_VXedhgE',
                  'CAACAgIAAxkBAAJEDF6SJJzQRyGIyJJZ9RlNYJHDxp-hAAJSAANgiW0MGnbfz9ckcHAYBA',
                  'CAACAgQAAxkBAAJEJF6SJRzAJW2ULMVVfXCjk2kdi7LkAAJeAANdK6kBi5oDtC-_pbsYBA',
                  'CAACAgQAAxkBAAJEJl6SJTPSYESVD7zMpk51hBeLjAoNAAJiAANdK6kBXejHu289q88YBA',
                  'CAACAgQAAxkBAAJEKl6SJUhyK8elOl_gVZgXT8amTNmEAAJqAANdK6kBCxsbu8mv41QYBA',
                  'CAACAgQAAxkBAAJELF6SJU_2ydIUewlHhSNCmeGnUl-pAAJsAANdK6kBKK5sjhmmXb4YBA',
                  'CAACAgUAAxkBAAJEMl6SJXvQygSN3atuxvdkIDo1cS1nAAKDAwAC6QrIA3LDp_J9s7MAARgE',
                  'CAACAgUAAxkBAAJENF6SJYzXO35cuynCHMakBsF18nMCAAKHAwAC6QrIAypdTyYxR1EwGAQ',
                  'CAACAgUAAxkBAAJEPF6SJbooj2ohGtDpigAB0Km62xHn4gACdQMAAukKyAPh87nO7IZtBBgE',
                  'CAACAgUAAxkBAAJESF6SJf8DbSw8JnBkTfciEclQrT11AAKmAwAC6QrIA3mzkAhrhbH0GAQ'
                 ]


BAD_STICKERS = ['CAACAgQAAxkBAAJDn16SIFSIvnyw0Z_L-QFH_zj7nHzeAALmAAOodxIAAWCGQcoWODi8GAQ',
                'CAACAgIAAxkBAAJDo16SIN88DoUGTDSbccjRCYWCSKhVAAJuAQACNuwbBV8eRYhKr0OJGAQ',
                'CAACAgIAAxkBAAJDpV6SIPNx4RfJ8i1d7VJg2L48bZG4AAJpAQACNuwbBQJGrl5U-BVaGAQ',
                'CAACAgIAAxkBAAJDqV6SIT9pZcK-3hFNERsJ_3oTJbZZAAI2AAM7YCQU691CcPqiFNEYBA',
                'CAACAgIAAxkBAAJDq16SIUoZ7Qfg50ym9Wdo6K43SKEKAAI9AAM7YCQUGcjeOT1GotMYBA',
                'CAACAgQAAxkBAAJDrV6SIVW7TTfgFHZOVNN9xPP_uKpKAAJyAAOodxIAAQE_-GdiBhsPGAQ',
                'CAACAgQAAxkBAAJDsV6SIbYqOJjuhOWtxUE0ikOhgMfrAAKVAAOodxIAAXHOFe9VGh4NGAQ',
                'CAACAgIAAxkBAAJDtV6SIdgXmWtEUC1mi_veIA7tnNOvAAIrAAM_VJkIpc__wQclmNEYBA',
                'CAACAgIAAxkBAAJDvV6SIljUxE6WeFKnhSl_mc0EMKE3AALmBwAClvoSBWB2oOUXBn3fGAQ',
                'CAACAgIAAxkBAAJDv16SImbqba6IBaysNdpn-E7Fsu45AAI9JgACS2oDAAGohRfizw0SfhgE',
                'CAACAgIAAxkBAAJDxV6SIo5R3wvd6w6rdo1oyy6cJpSBAAL5JgACS2oDAAEkpYGRNaWnOhgE',
                'CAACAgIAAxkBAAJDx16SIqCz1rQ4gcpGfPP17mTH6MlFAAJKJgACS2oDAAEF7ldzqeO67xgE',
                'CAACAgIAAxkBAAJDzV6SIs9dyX4BXQf0GHuHpG8GAarBAALxAgACXAJlAzwxPBDDth0RGAQ',
                'CAACAgIAAxkBAAJDz16SIub2SUbOHVWUmxr4z9DU9BoGAAIpBwACXAJlAzc6iZDu3H9PGAQ',
                'CAACAgIAAxkBAAJD0V6SIvIMJSBZm4mok0su164zg0yyAAInBwACXAJlA38iSmGhxypWGAQ',
                'CAACAgIAAxkBAAJD4V6SI49kgOWXPyhQzYuyv1FEVb3QAAL0AQACMdPJAeMUb-FuGC6IGAQ',
                'CAACAgIAAxkBAAJD8V6SI-VWiSjhoa-YvzRG3X26Ti9NAAKmAQACN4QwAAEUNCYrQEBreBgE',
                'CAACAgIAAxkBAAJD916SJAFG8hdSo7IiNsGMIH5KBhWxAALBCAACN4QwAAHv_SoV9dznEhgE',
                'CAACAgIAAxkBAAJEFF6SJMSFw4HUg1GyiATyH77PJpv4AAI1AAOVyB4LkaN2SWnuVs8YBA',
                'CAACAgIAAxkBAAJEFl6SJNr_ns9lEFWc6UC08fRk7IxmAAIrAAOVyB4LK4Y80FUZAAFNGAQ',
                'CAACAgIAAxkBAAJEGF6SJOLIi1wZybKCwOc-gRHXXfR0AAItAAOVyB4LBgpdx4HYgNkYBA',
                'CAACAgIAAxkBAAJEGl6SJOu4XNwPzl-hsKpiupiW94veAAIkAAOVyB4L_OMVV1DWnZoYBA',
                'CAACAgIAAxkBAAJEHF6SJP5XEyxGoisslH9H6KtY7m7GAAIlAAOVyB4LnuzoJKOkOXoYBA',
                'CAACAgIAAxkBAAJEHl6SJQbxWqlO9HOnJ06VuQYwWtnsAAImAAOVyB4LMKH4PrQAAbmuGAQ',
                'CAACAgIAAxkBAAJEIl6SJRI1PRNrkQYEQMOsY8JNVwABvAACKQADlcgeC6_vYJ_fVzAtGAQ',
                'CAACAgUAAxkBAAJEMF6SJXHipWP4jTOBjeGNOY47pSY-AAJzAwAC6QrIA2CbLBqZqhtHGAQ',
                'CAACAgUAAxkBAAJENl6SJZsV_M02YbfWwu49Ov5GhzvpAAJ5AwAC6QrIA5Hag_iV9NWgGAQ',
                'CAACAgUAAxkBAAJEOl6SJazY2oiMXJLNX8KF8Zvp9Xe0AAKWAwAC6QrIA5PWsYyB1_zxGAQ',
                'CAACAgUAAxkBAAJEPl6SJcWmPtIieqGa5oX8_OO20TQDAAKVAwAC6QrIAxPjuNsqJjnAGAQ',
                'CAACAgUAAxkBAAJEQl6SJdcv8qLXbtVutNF_JDVDEb-bAAKbAwAC6QrIA-yGSeNHm55zGAQ',
                'CAACAgUAAxkBAAJERF6SJeB0GRFb783pGoU7MbUKWGnCAAKfAwAC6QrIAxdH4pIj2R5sGAQ',
                'CAACAgUAAxkBAAJERl6SJfNsfPXLjmOKNn6mgRqkYrtjAAKeAwAC6QrIA-OY8_Qj7byAGAQ',
                'CAACAgUAAxkBAAJESl6SJgoUdPQ9ObI7JFTE8XqqFiOmAAKSAwAC6QrIA2slAq95gBxzGAQ',
                'CAACAgUAAxkBAAJETF6SJhbq3Dil6QTD7Q9yYrdVYpIWAAKTAwAC6QrIA-Q3DTE5nTkmGAQ',
                'CAACAgUAAxkBAAJETl6SJiRgVzwMQgK1EY0xBsAOT9DBAAK2AwAC6QrIA38gZjMEOh5nGAQ',
               ]