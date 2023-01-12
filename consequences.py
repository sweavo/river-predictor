"""
https://flood-warning-information.service.gov.uk/station/8208

Riverside path on the Joseph Rowntree Park side of the river > 2.9m and < 3.3m Exact level not known at this time

"""

import sys

nodes = {
    'BWE': 'bridge west end',
    'BEE': 'bridge east end',
    'NEW': 'New Walk',
    'TAV': 'Terry Avenue',
    'HFR': 'Hospital Fields Road',
    'MAG': 'Maple Grove',
    'BTR': 'Butcher Terrace'
}

infos = {
    ('BEE', 'NEW'): { 2.4: 'Unsure',
                      2.9: 'No'},
    ('BEE', 'HFR'): { 3.5: 'Unsure',
                      3.6: 'Just passable on foot and bike',
                      3.7: 'Unsure',
                      4.0: 'Passable by bike, water nearly up to kerbstones.'},
    ('BWE', 'BTR'): { 3.8: 'Unsure',
                      4.0: 'Not recommended. Puddle across path deep enough to foul the crank. Possible for pedestrians to get round it on ,waterlogged grass.'},
    ('BEE', 'MAG'): { 4.3: 'Unsure. But the bridge is unusable on the other side'},
    ('BWE', 'TAV'): { 2.9: 'Unsure',
                      3.3: 'No' }
}

def generate_possible_routes( nodes ):
    for i, src in enumerate(node_names):
        for dst in node_names[i+1:]:
            yield( (src,dst) )

if __name__ == "__main__":
    depth = float(sys.argv[1])

    node_names = list(nodes.keys())
    possible_routes = list(generate_possible_routes(nodes.keys()))

    print(possible_routes)