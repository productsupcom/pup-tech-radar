import csv
import json
import re
import datetime
import requests

# Publicly available
RINGS_CSV = 'https://docs.google.com/spreadsheets/u/1/d/1JKkdaeGJPrLhgtZ2jAPBjS8cpaJGL6PgK0SU28fgIJw/export?format=csv&id=1JKkdaeGJPrLhgtZ2jAPBjS8cpaJGL6PgK0SU28fgIJw&gid=0'
QUADRANTS_CSV = 'https://docs.google.com/spreadsheets/u/1/d/1YDRKVUGHRVREZ1gGUwRGffb7sQpVV3ztR4KTRSqwHds/export?format=csv&id=1YDRKVUGHRVREZ1gGUwRGffb7sQpVV3ztR4KTRSqwHds&gid=0'
ENTRIES_CSV = 'https://docs.google.com/spreadsheets/u/1/d/1Op2gILhJWK1YldR60xWBYMKxajSkHsy25DL_7y14HpU/export?format=csv&id=1Op2gILhJWK1YldR60xWBYMKxajSkHsy25DL_7y14HpU&gid=0'


def iter_csv(url):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    return csv.DictReader(response.iter_lines(decode_unicode=True))


TARGET_HTML = 'docs/index.html'
MARKER_START = '/* RADAR START */'
MARKER_END = '/* RADAR END */'


def main():
    # Quadrants
    quadrants = []
    quadrant_to_index = {}
    for row in iter_csv(QUADRANTS_CSV):
        quadrants.append({'name': row['Name']})
        quadrant_to_index[row['Name']] = len(quadrants) - 1

    # Rings
    rings = []
    ring_to_index = {}
    for row in iter_csv(RINGS_CSV):
        rings.append({'name': row['Name'].upper(), 'color': row['Colour']})
        ring_to_index[row['Name']] = len(rings) - 1

    # Entries
    entries = []
    for row in iter_csv(ENTRIES_CSV):

        # we will not import technologies with "Remove". These are old ones which we have removed from the chart
        if row['Ring'] == 'Remove':
            continue

        if not row['Link']:
            confluence_link = 'No Confluence page available. please check out: <a target="_blank" style="font-size:12pt" ' \
                              'href="https://productsup.atlassian.net/wiki/spaces/EN/pages/1930429957/Overview' \
                              '+Technologies">Tech Radar Technologies</a>'
        else:
            confluence_link = 'Learn more about: <a target="_blank" style="font-size:12pt" href="' + str(row['Link']) + '">' + str(row['Name']) + '</a> in our Documentation.'

        entries.append({
            'quadrant': quadrant_to_index[row['Quadrant']],
            'ring': ring_to_index[row['Ring']],
            'label': row['Name'],
            'explanation': confluence_link,
            'moved': row['Move']
        })

    dt = datetime.datetime.today()
    radar_config = {
        'svg_id': 'radar',
        'width': 1450,
        'height': 1000,
        'colors': {
            'background': "#fff",
            'grid': "#bbb",
            'inactive': "#ddd"
        },
        'title': "Productsup Tech Radar — as of " + str(dt.strftime("%Y.%m")),
        'print_layout': True,
        'quadrants': quadrants,
        'rings': rings,
        'entries': entries,
    }

    with open("JsonPrettyPrint.json", "w") as write_file:
        json.dump(radar_config, write_file, indent=4, separators=(", ", ": "), sort_keys=True)

    with open("JsonPrettyPrint.json", 'r') as f:
            radar_json_string = f.read()

    with open(TARGET_HTML, 'r') as f:
        html = f.read()

    html = re.sub(
        f'({re.escape(MARKER_START)}).*({re.escape(MARKER_END)})',
        r'\1' + radar_json_string.replace('\\', r'\\') + r'\2',
        html,
    )

    with open(TARGET_HTML, 'w') as f:
        f.write(html)


if __name__ == '__main__':
    main()
