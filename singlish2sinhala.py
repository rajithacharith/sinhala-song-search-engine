consonants = []
consonantsUni = []
vowels = []
vowelsUni = []
vowelModifiersUni = []
specialConsonants = []
specialConsonantsUni = []
specialCharUni = []
specialChar = []

vowelsUni.extend(['ඌ', 'ඕ', 'ඕ', 'ආ', 'ආ', 'ඈ', 'ඈ', 'ඈ', 'ඊ', 'ඊ', 'ඊ', 'ඊ', 'ඒ', 'ඒ', 'ඒ', 'ඌ', 'ඌ', 'ඖ', 'ඇ'])

vowels.extend(
    ['oo', 'o\\)', 'oe', 'aa', 'a\\)', 'Aa', 'A\\)', 'ae', 'ii', 'i\\)', 'ie', 'ee', 'ea', 'e\\)', 'ei', 'uu', 'u\\)',
     'au', '/\a'])

vowelModifiersUni.extend(
    ['ූ', 'ෝ', 'ෝ', 'ා', 'ා', 'ෑ', 'ෑ', 'ෑ', 'ී', 'ී', 'ී', 'ී', 'ේ', 'ේ', 'ේ', 'ූ', 'ූ', 'ෞ', 'ැ'])

vowelsUni.extend(['අ', 'ඇ', 'ඉ', 'එ', 'උ', 'ඔ', 'ඓ'])

vowels.extend(['a', 'A', 'i', 'e', 'u', 'o', 'I'])

vowelModifiersUni.extend(['', 'ැ', 'ි', 'ෙ', 'ු', 'ො', 'ෛ'])

nVowels = 26;

specialConsonantsUni.extend(['ං', 'ඃ', 'ඞ', 'ඍ'])

specialConsonants.extend(["\n", "\h", "\R"])
# special characher Repaya
specialConsonantsUni.append('ර්' + '\u200D')
specialConsonantsUni.append('ර්' + '\u200D')

specialConsonants.append("/R")
specialConsonants.append("\r")

consonantsUni.extend(['ඬ', 'ඳ', 'ඟ', 'ථ', 'ධ', 'ඝ', 'ඡ', 'ඵ', 'භ', 'ශ', 'ෂ', 'ඥ', 'ඤ', 'ළු', 'ද', 'ච', 'ඛ', 'ත'])

consonants.extend(
    ['nnd', 'nndh', 'nng', 'Th', 'Dh', 'gh', 'Ch', 'ph', 'bh', 'sh', 'Sh', 'GN', 'KN', 'Lu', 'dh', 'ch', 'kh', 'th'])

consonantsUni.extend(
    ['ට', 'ක', 'ඩ', 'න', 'ප', 'බ', 'ම', '‍ය', '‍ය', 'ය', 'ජ', 'ල', 'ව', 'ව', 'ස', 'හ', 'ණ', 'ළ', 'ඛ', 'ඝ', 'ඨ', 'ඪ',
     'ඵ', 'ඹ', 'ෆ', 'ඣ', 'ග'])

consonants.extend(
    ['t', 'k', 'd', 'n', 'p', 'b', 'm', '\\u005C' + 'y', 'Y', 'y', 'j', 'l', 'v', 'w', 's', 'h', 'N', 'L', 'K', 'G',
     'T', 'D', 'P', 'B', 'f', 'q', 'g'])

consonantsUni.append('ර')
consonants.append('r')

specialCharUni.append('ෲ')
specialChar.append('ruu')
specialCharUni.append('ෘ')
specialChar.append('ru')


# specialCharUni.append('්‍ර')
# specialChar.append('ra')

def Translate(text):
    # special consonents
    for i in range(0, len(specialConsonants)):
        text = text.replace(specialConsonants[i], specialConsonantsUni[i])

    # consonents + special
    for i in range(0, len(specialCharUni)):
        for j in range(0, len(consonants)):
            s = consonants[j] + specialChar[i]
            v = consonantsUni[j] + specialCharUni[i]
            r = s
            text = text.replace(r, v)

    # consonants + Rakaransha + vowel modifiers
    for j in range(0, len(consonants)):
        for i in range(0, len(vowels)):
            s = consonants[j] + "r" + vowels[i]
            v = consonantsUni[j] + "්‍ර" + vowelModifiersUni[i]
            r = s
            # r = new RegExp(s, "g")
            text = text.replace(r, v)

        s = consonants[j] + "r"
        v = consonantsUni[j] + "්‍ර"
        r = v
        text = text.replace(r, v)

    # constants with vowels modifiers
    for i in range(0, len(consonants)):
        for j in range(0, nVowels):
            s = consonants[i] + vowels[j]
            v = consonantsUni[i] + vowelModifiersUni[j]
            r = s
            text = text.replace(r, v)

    # Hal kirima
    for i in range(0, len(consonants)):
        r = consonants[i]
        text = text.replace(r, consonantsUni[i] + "්")

    # adding vowels
    for i in range(0, len(vowels)):
        r = vowels[i]
        text = text.replace(r, vowelsUni[i])

    return text

p = {}
p['අ'] = 'a'
p['ආ'] = 'aa'
p['ඇ'] = 'A'
p['ඈ'] = 'Aa'
p['ඉ'] = 'i'
p['ඊ'] = 'ie'
p['උ'] = 'u'
p['ඌ'] = 'uu'
p['එ'] = 'e'
p['ඒ'] = 'ea'
p['ඓ'] = 'I'
p['ඔ'] = 'o'

p['ැ'] = '-A'
p['ි'] = '-i'
p['ෙ'] = '-e'
p['ු'] = '-u'
p['ො'] = '-o'
p['ෛ'] = '-I'

# Vowel sounds - long
p['ා'] = '-aa'
p['ෑ'] = '-Aa'
p['ී'] = '-ie'
p['ේ'] = '-ei'
p['ෝ'] = '-oe'
p['ූ'] = '-uu'
p['ෞ'] = '-au'
p['ං'] = '\\n'
p['ඃ'] = '\h'
# p['ඞ'] = '\N'

# special (* = \u200d) - if * -> check char after it. if it's ය -> Ya, if it's ර -> ra, else -> -R
p['ර ්‍'] = '-R'  # repaya මර්‍ගය මර්*ගය
p['්‍ ය'] = 'Ya'  # yansaya මධ්‍යම මධ්*යම
p['්‍ ර'] = 'ra'  # rakaranshaya ක්‍රමය ක්*රමය    රත‍්‍රන්  රත‍්*රන්

p['්'] = '-'
# p['‍'] = '‍'

p['ෘ'] = '-ru'
p['ඖ'] = 'au'

# Consonants - Nasal
p['ඬ'] = 'nnda'
p['ඳ'] = 'nndha'
p['ඟ'] = 'nnga'

# Consonants - Common
p['ක'] = 'ka'
p['බ'] = 'ba'
p['ග'] = 'ga'
p['ම'] = 'ma'
p['ච'] = 'ca'
p['ය'] = 'ya'
p['ජ'] = 'ja'
p['ර'] = 'ra'
p['ට'] = 'Ta'
p['ල'] = 'la'
p['ඩ'] = 'Da'
p['ව'] = 'wa'
p['ත'] = 'ta'
p['ස'] = 'sa'
p['ද'] = 'da'
p['හ'] = 'ha'
p['න'] = 'na'
p['ණ'] = 'Na'
p['ප'] = 'pa'
p['ළ'] = 'La'

# Consonants - Aspirated
p['ඛ'] = 'Ka'
p['ඝ'] = 'Ga'
p['ඡ'] = 'cha'
p['ඨ'] = 'Tha'
p['ඪ'] = 'Da'
p['ථ'] = 'tha'
p['ධ'] = 'dha'
p['ඵ'] = 'Pa'
p['භ'] = 'bha'

# Consonants - Special
p['ඹ'] = 'Ba'
p['ශ'] = 'Sa'
p['ෂ'] = 'sha'
p['ෆ'] = 'fa'
p['ඥ'] = 'GNa'
p['ඤ'] = 'KNa'
p['ඣ'] = 'jha'
p['ළු'] = 'Lu'  # can't write 'luyanna'
p['ළූ'] = 'Luu'  # can't write 'deerga luyanna'


def transliterate(word):
    word = word.strip()

    # Ignore non sinhala words
    isSinhala = False
    for i in word:
        c = i
        if (c <= 'ෳ' and c >= 'ං'):
            isSinhala = True
    if not (isSinhala):
        return word

    src = word
    tgt = ''
    i = 0
    while i < len(src):
        if (src[i] == u'\u200d' and i < len(src) - 1):  # ZWJ
            if (src[i + 1] == u'\u0D9C'):  # ග  currently only set for මාර්‍ගය
                tgt = tgt[:-3]  # remove  'ra-'
                tgt += 'R'
                i += 1
                continue
            elif (src[i + 1] == u'\u0DBA'):  # ය
                tgt += 'Ya'
                i += 2  # jump over 'ය'
                continue
            elif (src[i + 1] == u'\u0DBB'):  # ර
                tgt += 'ra'
                i += 2  # jump over 'ර'
                continue

        t = src[i]
        if (t in p):
            tgt += p[t]
        else:
            tgt += t  # all non Sinhala unicode characters
        i += 1

    # remove each char before '-'
    outw = ''
    arr = tgt.split('-')
    for i in range(0, len(arr) - 1):
        if len(arr[i]) == 0:
            continue
        if (arr[i][-1] != 'a'):
            outw += arr[i][:-4] + arr[i][-3:]
        else:
            outw += arr[i][:-1]

    outw += arr[-1]
    return outw