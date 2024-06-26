"""Enum class containing list of entities."""
from enum import Enum


class Entity(Enum):
    """
    List of entities
    ALL: all entities
    ONLY_COUNTRY: all countries
    NOT_COUNTRY: exclude countries
    POPULATION: the entities that have population value
    """
    ALL = ['Afghanistan',
           'Albania',
           'Algeria',
           'American Samoa',
           'Andorra',
           'Angola',
           'Antigua and Barbuda',
           'Argentina',
           'Armenia',
           'Australia',
           'Austria',
           'Azerbaijan',
           'Bahamas',
           'Bahrain',
           'Bangladesh',
           'Barbados',
           'Belarus',
           'Belgium',
           'Belize',
           'Benin',
           'Bhutan',
           'Bolivia',
           'Bosnia and Herzegovina',
           'Botswana',
           'Brazil',
           'Brunei',
           'Bulgaria',
           'Burkina Faso',
           'Burundi',
           'Cambodia',
           'Cameroon',
           'Canada',
           'Cape Verde',
           'Central African Republic',
           'Chad',
           'Chile',
           'China',
           'Colombia',
           'Comoros',
           'Congo',
           'Cook Islands',
           'Costa Rica',
           "Cote d'Ivoire",
           'Croatia',
           'Cuba',
           'Cyprus',
           'Czechia',
           'Democratic Republic of Congo',
           'Denmark',
           'Djibouti',
           'Dominica',
           'Dominican Republic',
           'East Timor',
           'Ecuador',
           'Egypt',
           'El Salvador',
           'Equatorial Guinea',
           'Eritrea',
           'Estonia',
           'Eswatini',
           'Ethiopia',
           'Fiji',
           'Finland',
           'France',
           'Gabon',
           'Gambia',
           'Georgia',
           'Germany',
           'Ghana',
           'Greece',
           'Grenada',
           'Guam',
           'Guatemala',
           'Guinea',
           'Guinea-Bissau',
           'Guyana',
           'Haiti',
           'Honduras',
           'Hungary',
           'Iceland',
           'India',
           'Indonesia',
           'Iran',
           'Iraq',
           'Ireland',
           'Israel',
           'Italy',
           'Jamaica',
           'Japan',
           'Jordan',
           'Kazakhstan',
           'Kenya',
           'Kiribati',
           'Kuwait',
           'Kyrgyzstan',
           'Laos',
           'Latvia',
           'Lebanon',
           'Lesotho',
           'Liberia',
           'Libya',
           'Lithuania',
           'Luxembourg',
           'Madagascar',
           'Malawi',
           'Malaysia',
           'Maldives',
           'Mali',
           'Malta',
           'Marshall Islands',
           'Mauritania',
           'Mauritius',
           'Mexico',
           'Micronesia (country)',
           'Moldova',
           'Monaco',
           'Mongolia',
           'Montenegro',
           'Morocco',
           'Mozambique',
           'Myanmar',
           'Namibia',
           'Nauru',
           'Nepal',
           'Netherlands',
           'New Zealand',
           'Nicaragua',
           'Niger',
           'Nigeria',
           'Niue',
           'North Korea',
           'North Macedonia',
           'Northern Mariana Islands',
           'Norway',
           'Oman',
           'Pakistan',
           'Palau',
           'Palestine',
           'Panama',
           'Papua New Guinea',
           'Paraguay',
           'Peru',
           'Philippines',
           'Poland',
           'Portugal',
           'Puerto Rico',
           'Qatar',
           'Romania',
           'Russia',
           'Rwanda',
           'Saint Kitts and Nevis',
           'Saint Lucia',
           'Saint Vincent and the Grenadines',
           'Samoa',
           'San Marino',
           'Sao Tome and Principe',
           'Saudi Arabia',
           'Senegal',
           'Serbia',
           'Seychelles',
           'Sierra Leone',
           'Singapore',
           'Slovakia',
           'Slovenia',
           'Solomon Islands',
           'Somalia',
           'South Africa',
           'South Korea',
           'South Sudan',
           'Spain',
           'Sri Lanka',
           'Sudan',
           'Suriname',
           'Sweden',
           'Switzerland',
           'Syria',
           'Taiwan',
           'Tajikistan',
           'Tanzania',
           'Thailand',
           'Togo',
           'Tokelau',
           'Tonga',
           'Trinidad and Tobago',
           'Tunisia',
           'Turkey',
           'Turkmenistan',
           'Tuvalu',
           'Uganda',
           'Ukraine',
           'United Arab Emirates',
           'United Kingdom',
           'United States',
           'Uruguay',
           'Uzbekistan',
           'Vanuatu',
           'Venezuela',
           'Vietnam',
           'Yemen',
           'Zambia',
           'Zimbabwe',
           'World',
           'England',
           'Wales',
           'Scotland',
           'Northern Ireland',
           'Bermuda',
           'Greenland',
           'United States Virgin Islands',
           'African Region (WHO)',
           'Eastern Mediterranean Region (WHO)',
           'European Region (WHO)',
           'Region of the Americas (WHO)',
           'South-East Asia Region (WHO)',
           'Western Pacific Region (WHO)',
           'East Asia & Pacific (WB)',
           'Europe & Central Asia (WB)',
           'Latin America & Caribbean (WB)',
           'Middle East & North Africa (WB)',
           'North America (WB)',
           'South Asia (WB)',
           'Sub-Saharan Africa (WB)',
           'G20',
           'OECD Countries',
           'World Bank High Income',
           'World Bank Low Income',
           'World Bank Lower Middle Income',
           'World Bank Upper Middle Income']
    COUNTRY = ['Afghanistan',
               'Albania',
               'Algeria',
               'American Samoa',
               'Andorra',
               'Angola',
               'Antigua and Barbuda',
               'Argentina',
               'Armenia',
               'Australia',
               'Austria',
               'Azerbaijan',
               'Bahamas',
               'Bahrain',
               'Bangladesh',
               'Barbados',
               'Belarus',
               'Belgium',
               'Belize',
               'Benin',
               'Bhutan',
               'Bolivia',
               'Bosnia and Herzegovina',
               'Botswana',
               'Brazil',
               'Brunei',
               'Bulgaria',
               'Burkina Faso',
               'Burundi',
               'Cambodia',
               'Cameroon',
               'Canada',
               'Cape Verde',
               'Central African Republic',
               'Chad',
               'Chile',
               'China',
               'Colombia',
               'Comoros',
               'Congo',
               'Cook Islands',
               'Costa Rica',
               "Cote d'Ivoire",
               'Croatia',
               'Cuba',
               'Cyprus',
               'Czechia',
               'Democratic Republic of Congo',
               'Denmark',
               'Djibouti',
               'Dominica',
               'Dominican Republic',
               'East Timor',
               'Ecuador',
               'Egypt',
               'El Salvador',
               'Equatorial Guinea',
               'Eritrea',
               'Estonia',
               'Eswatini',
               'Ethiopia',
               'Fiji',
               'Finland',
               'France',
               'Gabon',
               'Gambia',
               'Georgia',
               'Germany',
               'Ghana',
               'Greece',
               'Grenada',
               'Guam',
               'Guatemala',
               'Guinea',
               'Guinea-Bissau',
               'Guyana',
               'Haiti',
               'Honduras',
               'Hungary',
               'Iceland',
               'India',
               'Indonesia',
               'Iran',
               'Iraq',
               'Ireland',
               'Israel',
               'Italy',
               'Jamaica',
               'Japan',
               'Jordan',
               'Kazakhstan',
               'Kenya',
               'Kiribati',
               'Kuwait',
               'Kyrgyzstan',
               'Laos',
               'Latvia',
               'Lebanon',
               'Lesotho',
               'Liberia',
               'Libya',
               'Lithuania',
               'Luxembourg',
               'Madagascar',
               'Malawi',
               'Malaysia',
               'Maldives',
               'Mali',
               'Malta',
               'Marshall Islands',
               'Mauritania',
               'Mauritius',
               'Mexico',
               'Micronesia (country)',
               'Moldova',
               'Monaco',
               'Mongolia',
               'Montenegro',
               'Morocco',
               'Mozambique',
               'Myanmar',
               'Namibia',
               'Nauru',
               'Nepal',
               'Netherlands',
               'New Zealand',
               'Nicaragua',
               'Niger',
               'Nigeria',
               'Niue',
               'North Korea',
               'North Macedonia',
               'Northern Mariana Islands',
               'Norway',
               'Oman',
               'Pakistan',
               'Palau',
               'Palestine',
               'Panama',
               'Papua New Guinea',
               'Paraguay',
               'Peru',
               'Philippines',
               'Poland',
               'Portugal',
               'Puerto Rico',
               'Qatar',
               'Romania',
               'Russia',
               'Rwanda',
               'Saint Kitts and Nevis',
               'Saint Lucia',
               'Saint Vincent and the Grenadines',
               'Samoa',
               'San Marino',
               'Sao Tome and Principe',
               'Saudi Arabia',
               'Senegal',
               'Serbia',
               'Seychelles',
               'Sierra Leone',
               'Singapore',
               'Slovakia',
               'Slovenia',
               'Solomon Islands',
               'Somalia',
               'South Africa',
               'South Korea',
               'South Sudan',
               'Spain',
               'Sri Lanka',
               'Sudan',
               'Suriname',
               'Sweden',
               'Switzerland',
               'Syria',
               'Taiwan',
               'Tajikistan',
               'Tanzania',
               'Thailand',
               'Togo',
               'Tokelau',
               'Tonga',
               'Trinidad and Tobago',
               'Tunisia',
               'Turkey',
               'Turkmenistan',
               'Tuvalu',
               'Uganda',
               'Ukraine',
               'United Arab Emirates',
               'United Kingdom',
               'United States',
               'Uruguay',
               'Uzbekistan',
               'Vanuatu',
               'Venezuela',
               'Vietnam',
               'Yemen',
               'Zambia',
               'Zimbabwe']
    NOT_COUNTRY = ['World',
                   'England',
                   'Wales',
                   'Scotland',
                   'Northern Ireland',
                   'Bermuda',
                   'Greenland',
                   'United States Virgin Islands',
                   'African Region (WHO)',
                   'Eastern Mediterranean Region (WHO)',
                   'European Region (WHO)',
                   'Region of the Americas (WHO)',
                   'South-East Asia Region (WHO)',
                   'Western Pacific Region (WHO)',
                   'East Asia & Pacific (WB)',
                   'Europe & Central Asia (WB)',
                   'Latin America & Caribbean (WB)',
                   'Middle East & North Africa (WB)',
                   'North America (WB)',
                   'South Asia (WB)',
                   'Sub-Saharan Africa (WB)',
                   'G20',
                   'OECD Countries',
                   'World Bank High Income',
                   'World Bank Low Income',
                   'World Bank Lower Middle Income',
                   'World Bank Upper Middle Income']
    POPULATION = ['Afghanistan',
                  'Albania',
                  'Algeria',
                  'American Samoa',
                  'Andorra',
                  'Angola',
                  'Antigua and Barbuda',
                  'Argentina',
                  'Armenia',
                  'Australia',
                  'Austria',
                  'Azerbaijan',
                  'Bahamas',
                  'Bahrain',
                  'Bangladesh',
                  'Barbados',
                  'Belarus',
                  'Belgium',
                  'Belize',
                  'Benin',
                  'Bhutan',
                  'Bolivia',
                  'Bosnia and Herzegovina',
                  'Botswana',
                  'Brazil',
                  'Brunei',
                  'Bulgaria',
                  'Burkina Faso',
                  'Burundi',
                  'Cambodia',
                  'Cameroon',
                  'Canada',
                  'Cape Verde',
                  'Central African Republic',
                  'Chad',
                  'Chile',
                  'China',
                  'Colombia',
                  'Comoros',
                  'Congo',
                  'Cook Islands',
                  'Costa Rica',
                  "Cote d'Ivoire",
                  'Croatia',
                  'Cuba',
                  'Cyprus',
                  'Czechia',
                  'Democratic Republic of Congo',
                  'Denmark',
                  'Djibouti',
                  'Dominica',
                  'Dominican Republic',
                  'East Timor',
                  'Ecuador',
                  'Egypt',
                  'El Salvador',
                  'Equatorial Guinea',
                  'Eritrea',
                  'Estonia',
                  'Eswatini',
                  'Ethiopia',
                  'Fiji',
                  'Finland',
                  'France',
                  'Gabon',
                  'Gambia',
                  'Georgia',
                  'Germany',
                  'Ghana',
                  'Greece',
                  'Grenada',
                  'Guam',
                  'Guatemala',
                  'Guinea',
                  'Guinea-Bissau',
                  'Guyana',
                  'Haiti',
                  'Honduras',
                  'Hungary',
                  'Iceland',
                  'India',
                  'Indonesia',
                  'Iran',
                  'Iraq',
                  'Ireland',
                  'Israel',
                  'Italy',
                  'Jamaica',
                  'Japan',
                  'Jordan',
                  'Kazakhstan',
                  'Kenya',
                  'Kiribati',
                  'Kuwait',
                  'Kyrgyzstan',
                  'Laos',
                  'Latvia',
                  'Lebanon',
                  'Lesotho',
                  'Liberia',
                  'Libya',
                  'Lithuania',
                  'Luxembourg',
                  'Madagascar',
                  'Malawi',
                  'Malaysia',
                  'Maldives',
                  'Mali',
                  'Malta',
                  'Marshall Islands',
                  'Mauritania',
                  'Mauritius',
                  'Mexico',
                  'Micronesia (country)',
                  'Moldova',
                  'Monaco',
                  'Mongolia',
                  'Montenegro',
                  'Morocco',
                  'Mozambique',
                  'Myanmar',
                  'Namibia',
                  'Nauru',
                  'Nepal',
                  'Netherlands',
                  'New Zealand',
                  'Nicaragua',
                  'Niger',
                  'Nigeria',
                  'Niue',
                  'North Korea',
                  'North Macedonia',
                  'Northern Mariana Islands',
                  'Norway',
                  'Oman',
                  'Pakistan',
                  'Palau',
                  'Palestine',
                  'Panama',
                  'Papua New Guinea',
                  'Paraguay',
                  'Peru',
                  'Philippines',
                  'Poland',
                  'Portugal',
                  'Puerto Rico',
                  'Qatar',
                  'Romania',
                  'Russia',
                  'Rwanda',
                  'Saint Kitts and Nevis',
                  'Saint Lucia',
                  'Saint Vincent and the Grenadines',
                  'Samoa',
                  'San Marino',
                  'Sao Tome and Principe',
                  'Saudi Arabia',
                  'Senegal',
                  'Serbia',
                  'Seychelles',
                  'Sierra Leone',
                  'Singapore',
                  'Slovakia',
                  'Slovenia',
                  'Solomon Islands',
                  'Somalia',
                  'South Africa',
                  'South Korea',
                  'South Sudan',
                  'Spain',
                  'Sri Lanka',
                  'Sudan',
                  'Suriname',
                  'Sweden',
                  'Switzerland',
                  'Syria',
                  'Taiwan',
                  'Tajikistan',
                  'Tanzania',
                  'Thailand',
                  'Togo',
                  'Tokelau',
                  'Tonga',
                  'Trinidad and Tobago',
                  'Tunisia',
                  'Turkey',
                  'Turkmenistan',
                  'Tuvalu',
                  'Uganda',
                  'Ukraine',
                  'United Arab Emirates',
                  'United Kingdom',
                  'United States',
                  'Uruguay',
                  'Uzbekistan',
                  'Vanuatu',
                  'Venezuela',
                  'Vietnam',
                  'Yemen',
                  'Zambia',
                  'Zimbabwe',
                  'World']
