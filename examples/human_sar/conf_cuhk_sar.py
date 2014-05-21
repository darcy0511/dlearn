# Datasets
datasets = [
    'CUHK_SAR'
]

# Attributes
attr_names = [
    'accessoryFaceMask',
    'accessoryHairBand',
    'accessoryHat',
    'accessoryHeadphone',
    'accessoryKerchief',
    'accessoryMuffler',
    'accessoryNothing',
    'accessorySunglasses',
    'carryingBabyBuggy',
    'carryingBackpack',
    'carryingFolder',
    'carryingLuggageCase',
    'carryingMessengerBag',
    'carryingNothing',
    'carryingOther',
    'carryingPlasticBags',
    'carryingSuitcase',
    'carryingUmbrella',
    'footwearBlack',
    'footwearBlue',
    'footwearBoots',
    'footwearBrown',
    'footwearGreen',
    'footwearGrey',
    'footwearLeatherShoes',
    'footwearOrange',
    'footwearPink',
    'footwearRed',
    'footwearSandals',
    'footwearShoes',
    'footwearSneakers',
    'lowerBodyStocking',
    'footwearWhite',
    'footwearYellow',
    'hairBald',
    'hairBlack',
    'hairBrown',
    'hairGrey',
    'hairLong',
    'hairOrange',
    'hairRed',
    'hairShort',
    'hairWhite',
    'hairYellow',
    'lowerBodyBlack',
    'lowerBodyBlue',
    'lowerBodyBrown',
    'lowerBodyCapri',
    'lowerBodyCasual',
    'lowerBodyFormal',
    'lowerBodyGreen',
    'lowerBodyGrey',
    'lowerBodyJeans',
    'lowerBodyLongSkirt',
    'lowerBodyOrange',
    'lowerBodyPink',
    'lowerBodyPlaid',
    'lowerBodyPurple',
    'lowerBodyRed',
    'lowerBodyShortSkirt',
    'lowerBodyShorts',
    'lowerBodySuits',
    'lowerBodyThickStripes',
    'lowerBodyTrousers',
    'lowerBodyWhite',
    'lowerBodyYellow',
    'personalFemale',
    'personalLarger60',
    'personalLess15',
    'personalLess30',
    'personalLess45',
    'personalLess60',
    'personalMale',
    'upperBodyBlack',
    'upperBodyBlue',
    'upperBodyBrown',
    'upperBodyCasual',
    'upperBodyFormal',
    'upperBodyGreen',
    'upperBodyGrey',
    'upperBodyJacket',
    'upperBodyLogo',
    'upperBodyLongSleeve',
    'upperBodyNoSleeve',
    'upperBodyOrange',
    'upperBodyOther',
    'upperBodyPink',
    'upperBodyPlaid',
    'upperBodyPurple',
    'upperBodyRed',
    'upperBodyShortSleeve',
    'upperBodySuit',
    'upperBodySweater',
    'upperBodyThickStripes',
    'upperBodyThinStripes',
    'upperBodyTshirt',
    'upperBodyVNeck',
    'upperBodyWhite',
    'upperBodyYellow'
]

attr_uni = [
]

attr_uni_titles = [
]

attr_mul = [
    [
        'hairBlack',
        'hairBrown',
        'hairGrey',
        'hairOrange',
        'hairRed',
        'hairWhite',
        'hairYellow'
    ],
    [
        'hairBald',
        'hairLong',
        'hairShort'
    ],
    [
        'footwearBlack',
        'footwearBlue',
        'footwearBrown',
        'footwearGreen',
        'footwearGrey',
        'footwearOrange',
        'footwearPink',
        'footwearRed',
        'footwearWhite',
        'footwearYellow'
    ],
    [
        'footwearBoots',
        'footwearLeatherShoes',
        'footwearSandals',
        'footwearShoes',
        'footwearSneakers'
    ],
    [
        'lowerBodyBlack',
        'lowerBodyBlue',
        'lowerBodyBrown',
        'lowerBodyGreen',
        'lowerBodyGrey',
        'lowerBodyOrange',
        'lowerBodyPink',
        'lowerBodyPurple',
        'lowerBodyRed',
        'lowerBodyWhite',
        'lowerBodyYellow'
    ],
    [
        'personalFemale',
        'personalMale'
    ],
    [
        'personalLess15',
        'personalLess30',
        'personalLess45',
        'personalLess60',
        'personalLarger60'
    ],
    [
        'accessoryFaceMask',
        'accessoryHairBand',
        'accessoryHat',
        'accessoryHeadphone',
        'accessoryKerchief',
        'accessoryMuffler',
        'accessoryNothing',
        'accessorySunglasses'
    ],
    [
        'carryingBabyBuggy',
        'carryingBackpack',
        'carryingFolder',
        'carryingLuggageCase',
        'carryingMessengerBag',
        'carryingNothing',
        'carryingOther',
        'carryingPlasticBags',
        'carryingSuitcase',
        'carryingUmbrella'
    ],
    [
        'lowerBodyCapri',
        'lowerBodyCasual',
        'lowerBodyFormal',
        'lowerBodyJeans',
        'lowerBodyLongSkirt',
        'lowerBodyPlaid',
        'lowerBodyShortSkirt',
        'lowerBodyShorts',
        'lowerBodySuits',
        'lowerBodyThickStripes',
        'lowerBodyTrousers',
        'lowerBodyStocking'
    ],
    [
        'upperBodyBlack',
        'upperBodyBlue',
        'upperBodyBrown',
        'upperBodyGreen',
        'upperBodyGrey',
        'upperBodyOrange',
        'upperBodyPink',
        'upperBodyPurple',
        'upperBodyRed',
        'upperBodyWhite',
        'upperBodyYellow'
    ],
    [
        'upperBodyCasual',
        'upperBodyFormal',
        'upperBodyJacket',
        'upperBodyLogo',
        'upperBodyLongSleeve',
        'upperBodyNoSleeve',
        'upperBodyOther',
        'upperBodyPlaid',
        'upperBodyShortSleeve',
        'upperBodySuit',
        'upperBodySweater',
        'upperBodyThickStripes',
        'upperBodyThinStripes',
        'upperBodyTshirt',
        'upperBodyVNeck'
    ]
]

attr_mul_titles = [
    'Hair Color',
    'Hair Style',
    'Footwear Color',
    'Footwear Style',
    'Lower Body Color',
    'Gender',
    'Age',
    'Accessories',
    'Carryings',
    'Lower Body Styles',
    'Upper Body Colors',
    'Upper Body Styles'
]


# Segmentations
seg_pix = {
    'Background': 0,
    'Hair': 9,
    'Head': 19,
    'Upper': 29,
    'Arms': 50,
    'Lower': 39,
    'Legs': 60,
    'Feet': 62
}